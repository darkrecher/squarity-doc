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
        "bla": [0, 0]
    }
}
"""

import random

NB_FRUITS = 3

DEBUG = False


class Tile:
    def __init__(self):
        self.fruit = None
        self.block_type = None
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

    def render(self):
        if self.fruit is not None:
            gamobj_fruit = f"fruit_{self.fruit:02}"
            self.game_objects[:] = [gamobj_fruit]
        elif self.block_type is not None:
            gamobj_block = f"block_{self.block_type:02}"
            self.game_objects[:] = [gamobj_block]
        else:
            self.game_objects[:] = []

    def does_stop_gravity(self):
        # Plus tard, on aura peut-être des blocs qui tombent.
        # Donc je checke explicitement le numéro de type.
        return self.block_type == 0

    def is_empty(self):
        return self.fruit is None and self.block_type is None

    def get_content_from_other_tile(self, other):
        self.fruit = other.fruit
        self.block_type = other.block_type
        self.render()

    def emptify(self):
        self.fruit = None
        self.block_type = None
        self.render()


class GameModel:
    def __init__(self):
        self.w = 10
        self.h = 15
        self.game_w = 9
        self.game_h = 13
        self.offset_interface_x = 1
        self.offset_interface_y = 2
        tiles = []
        for y in range(self.game_h):
            line = [Tile() for x in range(self.game_w)]
            line = tuple(line)
            tiles.append(line)
        self.tiles = tuple(tiles)

        for line in self.tiles:
            for tile in line:
                tile.set_random_content()

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
        print("fall_column", fall_column)
        if not fall_column:
            return False

        # TODO : Ça va être dégueux ce truc. Il faudra vraiment
        # que je gère avec les tiles, et pas les coordonnées.
        if not all(
            (self.tiles[y_check][x_column].is_empty() for y_check in fall_column)
        ):
            return True
        y_check = fall_column[-1]
        if not self.tiles[y_check - 1][x_column].is_empty():
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
        for y in range(self.game_h - 1, 0, -1):
            current_tile = self.tiles[y][x_column]
            if currently_falling:
                if current_tile.does_stop_gravity():
                    # Faut annuler la chute de la tile d'avant.
                    current_fall_column.pop()
                    # if current_fall_column:
                    if self.check_fall_column(x_column, current_fall_column):
                        gravity_falls.append(current_fall_column)
                    current_fall_column = []
                    currently_falling = False
                else:
                    current_fall_column.append(y)
            else:
                if current_tile.is_empty():
                    current_fall_column.append(y)
                    currently_falling = True

        if currently_falling:

            y_up = current_fall_column[-1]
            if self.tiles[y_up - 1][x_column].does_stop_gravity():
                current_fall_column.pop()
            if self.check_fall_column(x_column, current_fall_column):
                gravity_falls.append(current_fall_column)
        print(gravity_falls)
        return gravity_falls

    def apply_gravity(self, x_column, gravity_falls):
        print("gravity_falls wtf", gravity_falls)
        for current_fall in gravity_falls:
            for y in current_fall:
                tile_dst = self.tiles[y][x_column]
                # Donc là ça va péter si y vaut 0.
                # Mais comme j'ai bien codé ma fonction compute_gravity_falls.
                # y ne vaut jamais 0. Ha !!!
                tile_src = self.tiles[y - 1][x_column]
                tile_dst.get_content_from_other_tile(tile_src)
            # Et à la fin du fall, on vide la dernière tile.
            tile_src.emptify()

    def on_game_event(self, event_name):
        print("pouet")
        applied_gravity = False
        for x in range(self.game_w):
            gravity_falls = self.compute_gravity_falls(x)
            if gravity_falls:
                applied_gravity = True
            self.apply_gravity(x, gravity_falls)
        if not applied_gravity:
            print("Plus besoin d'appliquer la gravité !!")

