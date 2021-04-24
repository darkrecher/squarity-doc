# https://i.postimg.cc/KjMBC4bz/snake-match-tileset.png
# https://i.postimg.cc/c4yJRSwJ/snake-match-tileset.png
# https://i.postimg.cc/K8WHBk2C/snake-match-tileset.png
# https://i.postimg.cc/4xwYHY3p/snake-match-tileset.png

# Note pour plus tard : imgbb c'est de la daube comme hébergeur d'images.
# Ça, ça marche mieux. Et ça retaille pas stupidement les images sans prévenir.
# https://postimages.org/

# https://tinyurl.com/f7bbky72

"""
{
    "game_area": {
        "nb_tile_width": 10,
        "nb_tile_height": 15
    },
    "tile_size": 32,
    "img_coords": {
        "fruit_00": [0, 0],
        "fruit_01": [32, 0],
        "fruit_02": [64, 0],
        "block_00": [96, 0],
        "backgrnd": [128, 0],

        "snake_neck_up": [64, 0],
        "snake_neck_right": [64, 0],
        "snake_neck_down": [64, 0],
        "snake_neck_left": [64, 0],
        "snake_head_up": [64, 35],
        "snake_head_right": [96, 35],
        "snake_head_down": [128, 35],
        "snake_head_left": [160, 35],

        "snake_horiz": [0, 35],
        "snake_vertic": [32, 35],
        "snake_turn_up_left": [0, 70],
        "snake_turn_up_right": [32, 70],
        "snake_turn_down_right": [64, 70],
        "snake_turn_down_left": [96, 70],

        "match_up": [0, 105],
        "match_right": [32, 105],
        "match_down": [64, 105],
        "match_left": [96, 105],
        "match_horiz": [128, 105],
        "match_vertic": [160, 105],

        "bla": [0, 0]
    }
}
"""

"""

Snake-Match

Déplacez votre serpent et mangez les fruits.

Ne vous étonnez pas, au début, les fruits ne tombent pas,
et dès qu'on fait le premier mouvement, ils tombent.

C'est parce que j'ai pas fini de tout coder.

Le bouton d'action "2" permet d'afficher les match-3 horizontaux.
Et pour l'instant, ça fait que ça. Mais c'est déjà pas mal.

"""

import random

NB_FRUITS = 3

DEBUG = False


DIR_UP = 0
DIR_RIGHT = 2
DIR_DOWN = 4
DIR_LEFT = 6

DIR_FROM_EVENT = {"U": DIR_UP, "R": DIR_RIGHT, "D": DIR_DOWN, "L": DIR_LEFT}

OPPOSITE_DIR = {
    DIR_UP: DIR_DOWN,
    DIR_RIGHT: DIR_LEFT,
    DIR_DOWN: DIR_UP,
    DIR_LEFT: DIR_RIGHT,
}

DELAY_GRAVITY_MS = 250
ACTION_GRAVITY = f""" {{ "delayed_actions": [ {{"name": "apply_gravity", "delay_ms": {DELAY_GRAVITY_MS}}} ] }} """


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fruit = None
        self.block_type = None
        # snake_part est une string, correspondant directement
        # au gamobj du snake. (Pas besoin de se prendre plus la tête
        # que ça, à priori)
        self.snake_part = None
        self.game_objects = []
        self.gamobj_matches = []
        self.has_horizontal_match = False
        self.has_vertical_match = False

    def set_random_content(self):
        self.fruit = None
        self.block_type = None
        choice = random.randrange(NB_FRUITS + 2)
        if choice == 0:
            # On met rien du tout.
            pass
        elif choice == 1:
            self.block_type = 0
        else:
            self.fruit = choice - 2
        self.render()

    def set_snake_part(self, snake_part):
        self.emptify()
        self.snake_part = snake_part
        self.render()

    def add_match(self, gamobj):
        # TODO : On fait un clear_match puis plusieurs add_match.
        # Et c'est que à la fin de ces traitements qu'on aurait besoin
        # de faire un render().
        # Mais là, on fait des render à chaque modif. C'est bourrin.
        self.gamobj_matches.append(gamobj)
        # TODO : c'est moche de gérer avec les gamobj,
        # on essaiera de faire mieux si on a le temps.
        if "right" in gamobj or "left" in gamobj or "horiz" in gamobj:
            self.has_horizontal_match = True
        else:
            self.has_vertical_match = True
        self.render()

    def clear_match(self):
        self.gamobj_matches = []
        self.has_horizontal_match = False
        self.has_vertical_match = False
        self.render()

    def render(self):
        self.game_objects[:] = ["backgrnd"]
        if self.fruit is not None:
            gamobj_fruit = f"fruit_{self.fruit:02}"
            self.game_objects.append(gamobj_fruit)
        elif self.block_type is not None:
            gamobj_block = f"block_{self.block_type:02}"
            self.game_objects.append(gamobj_block)
        elif self.snake_part is not None:
            self.game_objects.append(self.snake_part)

        self.game_objects += self.gamobj_matches

    def does_stop_gravity(self):
        # Plus tard, on aura peut-être des blocs qui tombent.
        # Donc je checke explicitement le numéro de type.
        if self.block_type == 0:
            return True
        if self.snake_part is not None:
            return True
        return False

    def is_empty(self):
        return all(
            (self.fruit is None, self.block_type is None, self.snake_part is None)
        )

    def get_content_from_other_tile(self, other):
        self.fruit = other.fruit
        self.block_type = other.block_type
        self.render()

    def emptify(self):
        self.fruit = None
        self.block_type = None
        self.snake_part = None
        self.render()


class Snake:

    GAMOBJ_FROM_HEAD_DIR = {
        DIR_UP: "snake_head_up",
        DIR_RIGHT: "snake_head_right",
        DIR_DOWN: "snake_head_down",
        DIR_LEFT: "snake_head_left",
    }

    # clé : tuple de 2 éléments.
    #  - la direction au début de la tile du body.
    #  - la direction à la fin de la tile du body.
    # Il y a des combinaisons impossibles (toutes celles où on
    # fait demi-tour, par exemple RIGHT, RIGHT). Osef, on met tout.
    GAMOBJ_BODY_FROM_DIRS = {
        (DIR_UP, DIR_UP): "snake_vertic",
        (DIR_UP, DIR_RIGHT): "snake_turn_up_right",
        (DIR_UP, DIR_DOWN): "snake_vertic",
        (DIR_UP, DIR_LEFT): "snake_turn_up_left",
        (DIR_RIGHT, DIR_UP): "snake_turn_up_right",
        (DIR_RIGHT, DIR_RIGHT): "snake_horiz",
        (DIR_RIGHT, DIR_DOWN): "snake_turn_down_right",
        (DIR_RIGHT, DIR_LEFT): "snake_horiz",
        (DIR_DOWN, DIR_UP): "snake_vertic",
        (DIR_DOWN, DIR_RIGHT): "snake_turn_down_right",
        (DIR_DOWN, DIR_DOWN): "snake_vertic",
        (DIR_DOWN, DIR_LEFT): "snake_turn_down_left",
        (DIR_LEFT, DIR_UP): "snake_turn_up_left",
        (DIR_LEFT, DIR_RIGHT): "snake_horiz",
        (DIR_LEFT, DIR_DOWN): "snake_turn_down_left",
        (DIR_LEFT, DIR_LEFT): "snake_horiz",
    }

    def __init__(self, game_model, x, y):
        self.game_model = game_model
        self.tile_snake_head = self.game_model.tiles[y][x]
        self.head_dir = DIR_DOWN
        gamobj_head = Snake.GAMOBJ_FROM_HEAD_DIR[self.head_dir]
        self.tile_snake_head.set_snake_part(gamobj_head)
        tile_snake_up = self.tile_snake_head.adjacencies[DIR_UP]
        tile_snake_up.set_snake_part("snake_vertic")
        # Liste de tuple de 3 elems :
        # - direction du serpent au début de la tile.
        # - la tile sur laquelle se trouve le morceau de corps du serpent.
        # - direction du serpent à la fin de la tile.
        self.bodies = [(DIR_UP, tile_snake_up, DIR_DOWN)]

    def on_event_direction(self, direction):
        if self._can_move(direction):
            tile_dest = self.tile_snake_head.adjacencies[direction]
            cancel_last_body = False
            tile_last_body_infos = None
            if self.bodies:
                tile_last_body_infos = self.bodies[-1]
                tile_last_body = tile_last_body_infos[1]
                if tile_last_body == tile_dest:
                    cancel_last_body = True

            if cancel_last_body:
                self.tile_snake_head.emptify()
                # Le serpent revient en arrière.
                self.bodies.pop()
                self.head_dir = OPPOSITE_DIR[tile_last_body_infos[0]]
            else:
                # Le serpent avance.
                tile_new_body = self.tile_snake_head
                if tile_last_body_infos is None:
                    # Il n'y a pas du tout de body. On prend une direction par défaut.
                    # Et comme le serpent arrive par le haut de l'écran, on prend up.
                    start_dir = DIR_UP
                else:
                    start_dir = OPPOSITE_DIR[tile_last_body_infos[2]]
                gamobj_body = Snake.GAMOBJ_BODY_FROM_DIRS[(start_dir, direction)]
                tile_new_body.set_snake_part(gamobj_body)
                new_body_part = (start_dir, tile_new_body, direction)
                self.bodies.append(new_body_part)
                self.head_dir = direction

            self.tile_snake_head = tile_dest
            gamobj_head = Snake.GAMOBJ_FROM_HEAD_DIR[self.head_dir]
            self.tile_snake_head.set_snake_part(gamobj_head)

    def _can_move(self, direction):
        tile_dest = self.tile_snake_head.adjacencies[direction]
        if tile_dest is None:
            return False
        if tile_dest.block_type is not None:
            return False
        if tile_dest.snake_part is not None:
            # Le snake peut revenir en arrière, uniquement sur la snake part précédente.
            if not self.bodies:
                print("No body, but body. Not supposed to happen")
                return False
            else:
                tile_last_body_infos = self.bodies[-1]
                tile_last_body = tile_last_body_infos[1]
                if tile_last_body == tile_dest:
                    return True
                else:
                    return False
        return True


class GameModel:
    def __init__(self):
        self.w = 10
        self.h = 15
        self.game_w = 9
        self.game_h = 13
        self.offset_interface_x = 1
        self.offset_interface_y = 2
        snake_x = self.w // 2
        snake_y = 1

        tiles = []
        for y in range(self.game_h):
            line = [Tile(x, y) for x in range(self.game_w)]
            line = tuple(line)
            tiles.append(line)
        self.tiles = tuple(tiles)

        for y, line in enumerate(self.tiles):
            for x, tile in enumerate(line):
                adj = self.make_adjacencies(x, y)
                tile.adjacencies = adj
                tile.set_random_content()

        self.snake = Snake(self, snake_x, snake_y)
        self.applying_gravity = False

    def make_adjacencies(self, x, y):
        """
        Renvoie les tiles adjacentes à la tile aux coordonnées x, y.
        On renvoie toujours une liste de 8 éléments (les 8 directions), mais certains éléments
        peuvent être None, si les coordonnées x, y sont sur un bord de l'aire de jeu.
        0 : haut, 1 diagonale haut-droite, 2 : droite, etc.
        """
        adjacencies = (
            self.tiles[y - 1][x] if 0 <= y - 1 else None,
            self.tiles[y - 1][x + 1] if 0 <= y - 1 and x + 1 < self.game_w else None,
            self.tiles[y][x + 1] if x + 1 < self.game_w else None,
            self.tiles[y + 1][x + 1]
            if y + 1 < self.game_h and x + 1 < self.game_w
            else None,
            self.tiles[y + 1][x] if y + 1 < self.game_h else None,
            self.tiles[y + 1][x - 1] if y + 1 < self.game_h and 0 <= x - 1 else None,
            self.tiles[y][x - 1] if 0 <= x - 1 else None,
            self.tiles[y - 1][x - 1] if 0 <= y - 1 and 0 <= x - 1 else None,
        )
        return adjacencies

    def export_all_tiles(self):
        exported_tiles = []

        for y in range(self.offset_interface_y):
            # Pas d'interface pour l'instant, mais ça va venir.
            line = [[] for x in range(self.w)]
            exported_tiles.append(line)

        for game_line in self.tiles:
            interface_line = []
            for x in range(self.offset_interface_x):
                # Toujours pas d'interface.
                interface_line.append([])
            for game_tile in game_line:
                interface_line.append(game_tile.game_objects)
            exported_tiles.append(interface_line)
        if DEBUG:
            print(exported_tiles)
        return exported_tiles

    def check_fall_column(self, x_column, fall_column):
        # print("fall_column", fall_column)
        if not fall_column:
            return False

        if not all((tile.is_empty() for tile in fall_column)):
            return True

        tile_top = fall_column[-1]
        tile_top_up = tile_top.adjacencies[DIR_UP]
        if not tile_top_up.is_empty():
            return True
        return False

    def compute_gravity_falls(self, x_column):
        """
        Renvoie une liste de liste.
        Chaque élément de la liste de liste est une tile,
        indiquant que cette tile doit prendre
        le contenu de la tile au-dessus d'elle, pour appliquer une gravité.
        Chaque sous-liste indique implicitement qu'il faut prendre la
        dernière tile au-dessus et la vider.
        """
        gravity_falls = []
        currently_falling = False
        current_fall_column = []
        current_tile = self.tiles[self.game_h - 1][x_column]

        for _ in range(self.game_h - 1):
            if currently_falling:
                if current_tile.does_stop_gravity():
                    # Faut annuler la chute de la tile d'avant.
                    current_fall_column.pop()
                    if self.check_fall_column(x_column, current_fall_column):
                        gravity_falls.append(current_fall_column)
                    current_fall_column = []
                    currently_falling = False
                else:
                    current_fall_column.append(current_tile)
            else:
                if current_tile.is_empty():
                    current_fall_column.append(current_tile)
                    currently_falling = True
            current_tile = current_tile.adjacencies[DIR_UP]

        if currently_falling:

            tile_top = current_fall_column[-1]
            tile_up_top = tile_top.adjacencies[DIR_UP]

            if tile_up_top.does_stop_gravity():
                # Faut aussi annuler la chute de la tile d'avant.
                # Ou quelque chose du genre. Bref, j'ai testé et faut faire comme ça.
                current_fall_column.pop()
            if self.check_fall_column(x_column, current_fall_column):
                gravity_falls.append(current_fall_column)
        # print(gravity_falls)
        return gravity_falls

    def apply_gravity(self, gravity_falls):
        # print("gravity_falls wtf", gravity_falls)
        for current_fall in gravity_falls:
            for tile_dst in current_fall:

                # Donc là ça va péter si tiles_src est la tile tout en haut.
                # Mais comme j'ai bien codé ma fonction compute_gravity_falls.
                # on va jamais jusqu'en haut.
                tile_src = tile_dst.adjacencies[DIR_UP]
                tile_dst.get_content_from_other_tile(tile_src)
            # À la fin du fall, on vide la dernière tile.
            tile_src.emptify()

    def check_gravity_all_area(self):
        gravities_to_apply = []
        must_apply_gravity = False
        for x in range(self.game_w):
            gravity_falls = self.compute_gravity_falls(x)
            gravities_to_apply.append(gravity_falls)
            if gravity_falls:
                must_apply_gravity = True
        if not must_apply_gravity:
            gravities_to_apply = None
        return gravities_to_apply

    def check_all_match(self):

        # clear des matches précédents.
        for line in self.tiles:
            for tile in line:
                tile.clear_match()

        # check horizontal.
        for line in self.tiles:
            for tile_start in line:
                # TODO : mettre ça dans une fonction parce que là c'est
                # trop de code imbriqué.
                current_matches = []
                current_fruit_type = tile_start.fruit
                if (
                    not tile_start.has_horizontal_match
                    and current_fruit_type is not None
                ):
                    tile_cur = tile_start
                    while tile_cur is not None and tile_cur.fruit == current_fruit_type:
                        current_matches.append(tile_cur)
                        tile_cur = tile_cur.adjacencies[DIR_RIGHT]
                    # print(tile_start.x, tile_start.y, len(current_matches))
                    if len(current_matches) >= 3:
                        print(
                            "first and length : ",
                            tile_start.x,
                            tile_start.y,
                            len(current_matches),
                        )
                        print("last", current_matches[-1].x, current_matches[-1].y)
                        current_matches[0].add_match("match_right")
                        for tile in current_matches[1:-1]:
                            tile.add_match("match_horiz")
                        current_matches[-1].add_match("match_left")

    def on_game_event(self, event_name):
        direction = DIR_FROM_EVENT.get(event_name)

        if direction is not None:
            self.snake.on_event_direction(direction)
            if not self.applying_gravity:
                # On est pas déjà en train d'appliquer de la gravité.
                # On en appliquera une (pas tout de suite, dans quelques ms).
                self.applying_gravity = True
                return ACTION_GRAVITY
            else:
                return None

        elif event_name == "action_1":
            if not self.applying_gravity:
                # On est pas déjà en train d'appliquer de la gravité.
                # On en appliquera une (pas tout de suite, dans quelques ms).
                self.applying_gravity = True
                return ACTION_GRAVITY
            else:
                return None

        elif event_name == "action_2":
            self.check_all_match()

        elif event_name == "apply_gravity":

            gravities_to_apply = self.check_gravity_all_area()
            if gravities_to_apply is not None:
                for gravity_falls in gravities_to_apply:
                    self.apply_gravity(gravity_falls)
                return ACTION_GRAVITY
            else:
                self.applying_gravity = False
                return None
