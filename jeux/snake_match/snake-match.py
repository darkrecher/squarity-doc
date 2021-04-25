# https://i.postimg.cc/pd7yS6bZ/snake-match-tileset.png
# https://i.postimg.cc/L6svkJDM/snake-match-tileset.png
# https://i.postimg.cc/KjMBC4bz/snake-match-tileset.png

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

DELAY_ANIM_MATCH = 100
ACTION_ANIM_MATCH = f""" {{ "delayed_actions": [ {{"name": "anim_match", "delay_ms": {DELAY_ANIM_MATCH}}} ] }} """


class Tile:
    def __init__(self, game_model, x, y):
        self.game_model = game_model
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
        """
        Place un élément au hasard, mais forcément quelque chose.
        On met pas un élément vide, parce que j'ai pas besoin de ça !
        """
        self.emptify()
        # TODO : ce sera pas comme ça du tout, car plus on va profondément
        # plus on a de chance de tomber sur des blocs.
        choice = random.randrange(NB_FRUITS + 1)
        if choice == 0:
            self.block_type = 0
        else:
            self.fruit = choice - 1
        self.render()

    def set_snake_part(self, snake_part):
        self.emptify()
        self.snake_part = snake_part
        self.render()

    def add_match(self, gamobj):
        self.gamobj_matches.append(gamobj)
        # TODO : c'est moche de gérer avec les gamobj,
        # on essaiera de faire mieux si on a le temps.
        if "right" in gamobj or "left" in gamobj or "horiz" in gamobj:
            self.has_horizontal_match = True
        else:
            self.has_vertical_match = True

    def clear_match(self):
        self.gamobj_matches = []
        self.has_horizontal_match = False
        self.has_vertical_match = False

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

        self.game_objects += self.gamobj_matches * self.game_model.match_show_gamobj

    def does_stop_gravity(self):
        # Plus tard, on aura peut-être des blocs qui tombent.
        # Donc je checke explicitement le numéro de type.
        if self.block_type == 0:
            return True
        if self.snake_part is not None:
            return True
        if self.gamobj_matches:
            # Les tiles en cours de match ne peuvent pas tomber.
            # Ça fait bizarre, car pendant quelques fractions de
            # secondes, on verra des fruits qui restent en l'air
            # pendant qu'ils se matchent. Mais ça simplifie beaucoup de choses.
            return True
        return False

    def is_empty(self):
        return all(
            (self.fruit is None, self.block_type is None, self.snake_part is None)
        )

    def get_content_from_other_tile(self, other):
        self.fruit = other.fruit
        self.block_type = other.block_type
        self.snake_part = other.snake_part
        self.gamobj_matches = other.gamobj_matches
        self.has_horizontal_match = other.has_horizontal_match
        self.has_vertical_match = other.has_vertical_match

        self.render()

    def emptify(self):
        self.fruit = None
        self.block_type = None
        self.snake_part = None
        self.gamobj_matches = []
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
        # Liste de liste de 3 elems :
        # - direction du serpent au début de la tile.
        # - la tile sur laquelle se trouve le morceau de corps du serpent.
        # - direction du serpent à la fin de la tile.
        self.bodies = [[DIR_UP, tile_snake_up, DIR_DOWN]]

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
                new_body_part = [start_dir, tile_new_body, direction]
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
        if tile_dest.gamobj_matches:
            # On ne peut pas manger des fruits en train d'être matchés.
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

    def update_scroll_to_deeper(self):
        self.tile_snake_head = self.tile_snake_head.adjacencies[DIR_UP]
        if self.tile_snake_head is None:
            # Not supposed to happen.
            raise Exception("On est allé plus profond jusqu'à supprimer le serpent")
        for body_infos in self.bodies:
            tile_body = body_infos[1]
            if tile_body is not None:
                tile_body = tile_body.adjacencies[DIR_UP]
                body_infos[1] = tile_body
        # TODO : Je sais pas comment gérer le serpent qui se découpe !!
        # if self.bodies[-1][1] is None:
        #     keep_last_body = self.bodies[-1]
        # else:
        #     keep_last_body = None
        self.bodies = [
            body_infos for body_infos in self.bodies if body_infos[1] is not None
        ]
        # if keep_last_body is not None:
        #     print("keep last body !!")
        #     # Sauf que maintenant j'ai un putain de None dans mes tiles de body...
        #     # Sur un malentendu, ça va passer.
        #     self.bodies.append(keep_last_body)
        # print(self.bodies)


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

        self.match_anim_time = 0
        self.match_show_gamobj = 0

        tiles = []
        for y in range(self.game_h):
            line = [Tile(self, x, y) for x in range(self.game_w)]
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
        self.must_check_match = False
        self.matched_tiles = []

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
        matched_tiles = set()
        for line in self.tiles:
            for tile in line:
                tile.clear_match()

        # --- check des matches horizontaux ---
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
                        # print(
                        #     "first and length : ",
                        #     tile_start.x,
                        #     tile_start.y,
                        #     len(current_matches),
                        # )
                        # print("last", current_matches[-1].x, current_matches[-1].y)
                        current_matches[0].add_match("match_right")
                        for tile in current_matches[1:-1]:
                            tile.add_match("match_horiz")
                        current_matches[-1].add_match("match_left")
                        matched_tiles = matched_tiles.union(set(current_matches))

        # --- check des matches verticaux. ---
        # TODO : copié-collé de gros bourrin avec le check horizontal.
        # À mon avis y'a moyen de faire mieux.
        # TODO : et ce serait tellement classe d'avoir les tiles
        # indexées par ligne ET par colonne. Comme ça j'aurais pas besoin
        # d'itérer sur x et y comme un pauvre.
        for x_start in range(self.game_w):
            for y_start in range(self.game_h):
                tile_start = self.tiles[y_start][x_start]
                # TODO : mettre ça dans une fonction parce que là c'est
                # trop de code imbriqué.
                current_matches = []
                current_fruit_type = tile_start.fruit
                if not tile_start.has_vertical_match and current_fruit_type is not None:
                    tile_cur = tile_start
                    while tile_cur is not None and tile_cur.fruit == current_fruit_type:
                        current_matches.append(tile_cur)
                        tile_cur = tile_cur.adjacencies[DIR_DOWN]
                    # print(tile_start.x, tile_start.y, len(current_matches))
                    if len(current_matches) >= 3:
                        current_matches[0].add_match("match_down")
                        for tile in current_matches[1:-1]:
                            tile.add_match("match_vertic")
                        current_matches[-1].add_match("match_up")
                        matched_tiles = matched_tiles.union(set(current_matches))

        # TODO : calculer les XP des matches.
        self.matched_tiles = list(matched_tiles)

    def destroy_matched_fruits(self):
        for tile in self.matched_tiles:
            tile.emptify()
            # On détruit les blocs adjacents aux matches.
            # J'aurais sûrement pas le temps de faire des blocs ayant
            # plusieurs points de vie (à détruire en plusieurs matchs)
            # Donc je pète le bloc direct.
            for adj_tile in tile.adjacencies[::2]:
                if adj_tile is not None and adj_tile.block_type == 0:
                    adj_tile.emptify()

    def go_deeper(self):
        # Les tiles doivent prendre ce qu'il y a en-dessous d'elles.
        # Encore des itérations stupides avec des x et y, car j'ai pas
        # indexé par colonne. C'est pas grave. On est des pauvres, on indexe pas, mais on n'a honte de rien.
        for x in range(self.game_w):
            tile_current = self.tiles[0][x]
            for _ in range(self.game_h - 1):
                tile_below = tile_current.adjacencies[DIR_DOWN]
                tile_current.get_content_from_other_tile(tile_below)
                tile_current = tile_below
            tile_below.set_random_content()
        # Il faut aussi déplacer les références de tiles du body du serpent.
        self.snake.update_scroll_to_deeper()
        # Et les références des tiles en cours de match.
        self.matched_tiles = [tile.adjacencies[DIR_UP] for tile in self.matched_tiles]
        self.matched_tiles = [tile for tile in self.matched_tiles if tile is not None]

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
            self.go_deeper()
            if not self.match_anim_time and not self.applying_gravity:
                self.check_all_match()
                if self.matched_tiles:
                    self.match_anim_time = 1
                    self.match_show_gamobj = 1
                    for tile in self.matched_tiles:
                        tile.render()
                    return ACTION_ANIM_MATCH
                else:
                    # Pas de match suite à un scroll plus profond.
                    # On peut s'arrêter. Pas besoin de checker la gravité,
                    # quand on va plus profond on tombe forcément sur des objets et pas du vide.
                    return None

        elif event_name == "action_2":
            return None

        elif event_name == "anim_match":
            # print("anim match", self.match_anim_time, self.match_show_gamobj)
            self.match_anim_time += 1
            self.match_show_gamobj = [0, 1, 2, 3, 2, 1, 0][self.match_anim_time]
            for tile in self.matched_tiles:
                tile.render()
            if self.match_anim_time == 6:
                self.match_anim_time = 0
                # Animation du match terminé. On détruit les fruits
                self.destroy_matched_fruits()
                # Et du coup, faut revérifier la gravité.
                self.applying_gravity = True
                return ACTION_GRAVITY
            else:
                return ACTION_ANIM_MATCH

        elif event_name == "apply_gravity":

            gravities_to_apply = self.check_gravity_all_area()
            if gravities_to_apply is not None:
                for gravity_falls in gravities_to_apply:
                    self.apply_gravity(gravity_falls)
                return ACTION_GRAVITY
            else:
                self.applying_gravity = False
                # La gravité est finie. Maintenant, il faut vérifier
                # si on doit faire des matches.
                if self.match_anim_time:
                    # Ah zut alors. La gravité est finie mais on a encore
                    # des matchs en cours. (Ça peut arriver si le serpent
                    # fait tomber des fruits pendant qu'il y a un autre
                    # match).
                    # Dans ce cas, on fait rien dans l'immédiat, mais
                    # on retient qu'il faudra quand même refaire un check
                    # de match. (TODO : je sais pas vraiment si j'ai besoin
                    # de ça en fait).
                    self.must_check_match = True
                    return None
                else:
                    self.check_all_match()
                    if self.matched_tiles:
                        self.match_anim_time = 1
                        self.match_show_gamobj = 1
                        for tile in self.matched_tiles:
                            tile.render()
                        return ACTION_ANIM_MATCH
                    else:
                        # On a fini la gravité, et on vient de vérifier
                        # qu'il n'y a plus de match à faire.
                        # on peut s'arrêter là.
                        return None

