# https://i.postimg.cc/155hbHMf/unstable-isotope.png

"""
{
  "game_area": {
    "nb_tile_width": 10,
    "nb_tile_height": 10
  },
  "tile_size": 64,

  "img_coords": {
    "cursor_normal": [0, 0],
    "cursor_select_01": [64, 0],
    "background": [128, 0],
    "isot_01": [0, 64],
    "isot_02": [64, 64],
    "isot_03": [128, 64],
    "isot_04": [192, 64],
    "isot_05": [256, 64],
    "isot_06": [0, 128],

    "blorp": [0, 0]
  }
}
"""

"""
Le thème c'est "Unstable".
Qu'est-ce qu'on va bien pouvoir faire avec ça ?

un jeu genre Aqua Splash (sur KadoKado). Le truc avec les boules d'eau. Sauf que ce sera des isotopes instables.
"""

GAME_SIZE_W = 10
GAME_SIZE_H = 10


class Tile:
    def __init__(self, x, y, nb_isotope):
        self.x = x
        self.y = y
        self.nb_isotope = nb_isotope
        self.moving_isot = []

    def get_gamobjs(self):
        if self.nb_isotope > 6:
            raise Exception(f"Trop d'isotope. Tile : {self.x}, {self.y}")
        result_gamobjs = ["background"]
        if self.nb_isotope:
            result_gamobjs.append(f"isot_0{self.nb_isotope}")
        return result_gamobjs


class GameModel:
    def __init__(self):
        self.w = GAME_SIZE_W
        self.h = GAME_SIZE_H
        self.tiles = []
        for y in range(self.h):
            line = []
            for x in range(self.w):
                new_tile = Tile(x, y, 1)
                line.append(new_tile)
            self.tiles.append(line)

        self.x_cursor = 2
        self.y_cursor = 3

        self.tiles[4][0].nb_isotope = 3

    def export_all_tiles(self):
        tiles_to_export = []
        for y in range(self.h):
            line_to_export = [tile.get_gamobjs() for tile in self.tiles[y]]
            tiles_to_export.append(line_to_export)
        gamobjs_cursor = tiles_to_export[self.y_cursor][self.x_cursor]
        gamobjs_cursor.append("cursor_normal")
        return tiles_to_export
