# https://i.postimg.cc/4xwYHY3p/snake-match-tileset.png
# https://i.postimg.cc/pVJsMDxY/snake-match-tileset.png
# https://i.postimg.cc/gcQqQtbX/snake-match-tileset.png
# https://i.postimg.cc/XJdtF6nF/snake-match-tileset.png

# Note pour plus tard : imgbb c'est de la daube comme hébergeur d'images.
# Ça, ça marche mieux. Et ça retaille pas stupidement les images sans prévenir.
# https://postimages.org/

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

        "snake_horiz": [0, 35],
        "snake_vertic": [32, 35],
        "snake_head_up": [64, 35],
        "snake_head_right": [96, 35],
        "snake_head_down": [128, 35],
        "snake_head_left": [160, 35],

        "bla": [0, 0]
    }
}
"""

import random

NB_FRUITS = 3

DEBUG = False


DIR_UP = 0
DIR_RIGHT = 2
DIR_DOWN = 4
DIR_LEFT = 6

DIR_FROM_EVENT = {"U": DIR_UP, "R": DIR_RIGHT, "D": DIR_DOWN, "L": DIR_LEFT}


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

    def render(self):
        if self.fruit is not None:
            gamobj_fruit = f"fruit_{self.fruit:02}"
            self.game_objects[:] = [gamobj_fruit]
        elif self.block_type is not None:
            gamobj_block = f"block_{self.block_type:02}"
            self.game_objects[:] = [gamobj_block]
        elif self.snake_part is not None:
            self.game_objects[:] = [self.snake_part]
        else:
            self.game_objects[:] = []

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
        0: "snake_head_up",
        2: "snake_head_right",
        4: "snake_head_down",
        6: "snake_head_left",
    }

    def __init__(self, game_model, x, y):
        self.game_model = game_model
        self.tile_snake_head = self.game_model.tiles[y][x]
        self.head_dir = DIR_DOWN
        gamobj_head = Snake.GAMOBJ_FROM_HEAD_DIR[self.head_dir]
        self.tile_snake_head.set_snake_part(gamobj_head)
        tile_snake_up = self.tile_snake_head.adjacencies[DIR_UP]
        tile_snake_up.set_snake_part("snake_vertic")

    def on_event_direction(self, direction):
        if self.head_dir != direction:
            # TODO : C'est pas tout à fait comme ça. Mais on verra ça plus tard
            self.head_dir = direction
            gamobj_head = Snake.GAMOBJ_FROM_HEAD_DIR[self.head_dir]
            self.tile_snake_head.set_snake_part(gamobj_head)
        else:
            # La direction de l'event est pareil que la direction
            # de la tête. On peut faire avancer le serpent.
            if self._can_move(direction):
                self.tile_snake_head.emptify()
                self.tile_snake_head = self.tile_snake_head.adjacencies[direction]
                gamobj_head = Snake.GAMOBJ_FROM_HEAD_DIR[self.head_dir]
                self.tile_snake_head.set_snake_part(gamobj_head)

    def _can_move(self, direction):
        tile_dest = self.tile_snake_head.adjacencies[direction]
        if tile_dest is None:
            return False
        if tile_dest.block_type is not None:
            return False
        # C'est pas tout à fait ça. Le snake peut revenir en arrière
        # sur la snake part précédente. On verra ça après.
        if tile_dest.snake_part is not None:
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
        Chaque élément de la liste de liste est une ordonnée Y,
        indiquant que la tile à cette ordonnée doit prendre
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

    def on_game_event(self, event_name):
        direction = DIR_FROM_EVENT.get(event_name)
        if direction is not None:
            self.snake.on_event_direction(direction)
        else:
            applied_gravity = False
            for x in range(self.game_w):
                gravity_falls = self.compute_gravity_falls(x)
                if gravity_falls:
                    applied_gravity = True
                    self.apply_gravity(gravity_falls)
            if not applied_gravity:
                print("Plus besoin d'appliquer la gravité !!")

