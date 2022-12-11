# https://i.ibb.co/KWSz3th/grreeny.png
# https://i.ibb.co/wS2b32z/grreeny.png

"""
  {
    "game_area": {
        "nb_tile_width": 8,
        "nb_tile_height": 8
    },
    "tile_size": 32,
    "img_coords": {
      "grreeny": [0, 0],
      "col_red": [32, 0],
      "col_grn": [64, 0],
      "col_blu": [96, 0],

      "void": [0, 0]
    }
  }
"""

import random

DIR_INT_FROM_STR = {
    "U": 0,
    "R": 2,
    "D": 4,
    "L": 6,
}

OFFSET_COORDS_FROM_STR = {
    "U": (0, -1),
    "R": (+1, 0),
    "D": (0, +1),
    "L": (-1, 0),
}


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.adjacencies = None
        self.has_grreeny = False
        self.col_red = 0
        self.col_grn = 0
        self.col_blu = 0

    def render(self):
        gamobjs = []
        gamobjs.extend(["col_red"] * self.col_red)
        gamobjs.extend(["col_grn"] * self.col_grn)
        gamobjs.extend(["col_blu"] * self.col_blu)
        if self.has_grreeny:
            gamobjs.append("grreeny")
        return gamobjs


class GameModel:
    def __init__(self):
        self.w = 8
        self.h = 8
        self.tiles = []
        for y in range(self.h):
            line = []
            for x in range(self.w):
                line.append(Tile(x, y))
            self.tiles.append(line)

        for y in range(self.h):
            for x in range(self.w):
                self.get_tile(x, y).adjacencies = self._make_adjacencies(x, y)

        self.grreeny_coords = (3, 4)
        self.get_tile(*self.grreeny_coords).has_grreeny = True

        # Juste pour tester :
        tiles_to_colorize = [
            self.get_tile(
                random.randrange(0, self.w),
                random.randrange(0, self.h),
            )
            for _ in range(4)
        ]

        tiles_to_colorize[0].col_red = 1
        tiles_to_colorize[1].col_red = 1
        tiles_to_colorize[2].col_grn = 1
        tiles_to_colorize[3].col_blu = 1

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

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def export_all_tiles(self):
        exported_tiles = []
        for line_tiles in self.tiles:
            exported_line = []
            for tile in line_tiles:
                exported_line.append(tile.render())
            exported_tiles.append(exported_line)

        return exported_tiles

    def get_moved_grreeny_coords(self, offset_coords):
        """
        Renvoie les nouvelles coordonnées de grreeny après
        son déplacement, si le déplacement est possible.
        Sinon renvoie None.
        """
        grreeny_x, grreeny_y = self.grreeny_coords
        offset_x, offset_y = offset_coords
        new_grreeny_x = grreeny_x + offset_x
        new_grreeny_y = grreeny_y + offset_y
        if not (0 <= new_grreeny_x < self.w):
            return None
        if not (0 <= new_grreeny_y < self.h):
            return None
        return (new_grreeny_x, new_grreeny_y)

    def on_game_event(self, event_name):

        offset_coords = OFFSET_COORDS_FROM_STR.get(event_name)
        if offset_coords is not None:
            move_result = self.get_moved_grreeny_coords(offset_coords)
            if move_result is not None:
                prev_tile = self.get_tile(*self.grreeny_coords)
                prev_tile.has_grreeny = False
                self.grreeny_coords = move_result
                cur_tile = self.get_tile(*self.grreeny_coords)
                cur_tile.has_grreeny = True
