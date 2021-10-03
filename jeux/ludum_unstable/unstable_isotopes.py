# https://i.postimg.cc/155hbHMf/unstable-isotope.png

"""
{
  "game_area": {
    "nb_tile_width": 7,
    "nb_tile_height": 7
  },
  "tile_size": 64,

  "img_coords": {
    "cursor_normal": [0, 0],
    "cursor_select_01": [64, 0],
    "cursor_select_02": [64, 0],
    "cursor_select_03": [64, 0],
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

import random

GAME_SIZE_W = 7
GAME_SIZE_H = 7

DIR_INT_FROM_STR = {
    "U": 0,
    "R": 2,
    "D": 4,
    "L": 6,
}


class Tile:
    def __init__(self, x, y, nb_isotope):
        self.x = x
        self.y = y
        self.nb_isotope = nb_isotope
        self.moving_isot = []
        self.adjacencies = None

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
                isot = random.randint(0, 3)
                new_tile = Tile(x, y, isot)
                line.append(new_tile)
            self.tiles.append(line)

        for y in range(self.h):
            for x in range(self.w):
                self.tiles[y][x].adjacencies = self._make_adjacencies(x, y)

        x_cursor = 0
        y_cursor = 0
        self.tile_cursor = self.tiles[y_cursor][x_cursor]
        self.taking_isotope = False
        self.gamobj_cursor = "cursor_normal"

        self.told_msg_no_iso = False

        # TODO : crap
        # self.tiles[4][0].nb_isotope = 4

    def _make_adjacencies(self, x, y):
        """
        Renvoie les tiles adjacentes à la tile située aux coordonnées x, y.
        On renvoie toujours une liste de 8 éléments (les 8 directions), mais certains éléments
        peuvent être None, si les coordonnées x, y sont sur un bord de l'aire de jeu.
        """
        adjacencies = (
            self.tiles[y - 1][x] if 0 <= y - 1 else None,
            self.tiles[y - 1][x + 1] if 0 <= y - 1 and x + 1 < self.w else None,
            self.tiles[y][x + 1] if x + 1 < self.w else None,
            self.tiles[y + 1][x + 1] if y + 1 < self.h and x + 1 < self.w else None,
            self.tiles[y + 1][x] if y + 1 < self.h else None,
            self.tiles[y + 1][x - 1] if y + 1 < self.h and 0 <= x - 1 else None,
            self.tiles[y][x - 1] if 0 <= x - 1 else None,
            self.tiles[y - 1][x - 1] if 0 <= y - 1 and 0 <= x - 1 else None,
        )
        return adjacencies

    def export_all_tiles(self):
        tiles_to_export = []
        for y in range(self.h):
            line_to_export = [tile.get_gamobjs() for tile in self.tiles[y]]
            tiles_to_export.append(line_to_export)

        x_cursor = self.tile_cursor.x
        y_cursor = self.tile_cursor.y
        gamobjs_cursor = tiles_to_export[y_cursor][x_cursor]
        gamobjs_cursor.append(self.gamobj_cursor)
        return tiles_to_export

    def on_game_event(self, event_name):

        move_dir = DIR_INT_FROM_STR.get(event_name)
        if move_dir is not None:
            new_tile_cursor = self.tile_cursor.adjacencies[move_dir]
            if new_tile_cursor is None:
                return
            if self.taking_isotope:
                if new_tile_cursor.nb_isotope:
                    if new_tile_cursor.nb_isotope > 3:
                        return
                    self.taking_isotope = False
                    self.gamobj_cursor = "cursor_normal"
                nb_iso_to_move = self.tile_cursor.nb_isotope
                self.tile_cursor.nb_isotope = 0
                new_tile_cursor.nb_isotope += nb_iso_to_move
            self.tile_cursor = new_tile_cursor

        if event_name == "action_1":
            if self.taking_isotope:
                self.taking_isotope = False
                self.gamobj_cursor = "cursor_normal"
            else:
                iso_on_cursor = self.tile_cursor.nb_isotope
                if 0 < iso_on_cursor <= 3:
                    self.taking_isotope = True
                    self.gamobj_cursor = f"cursor_select_0{iso_on_cursor}"
                else:
                    if not iso_on_cursor and not self.told_msg_no_iso:
                        print("You must be on a tile containing some isotopes.")
                        self.told_msg_no_iso = True
