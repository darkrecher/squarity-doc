# https://i.ibb.co/k3NBpGq/grreeny.png

"""
  {
    "game_area": {
        "nb_tile_width": 8,
        "nb_tile_height": 8
    },
    "tile_size": 32,
    "img_coords": {
      "grreeny": [0,  0],
      "col_red": [32, 0],
      "col_grn": [64, 0],
      "col_blu": [96, 0],

      "col_red_red_blu": [128, 0],
      "col_red_grn_grn": [0,  32],
      "col_red_red_grn": [32, 32],
      "col_grn_blu_blu": [64, 32],
      "col_grn_grn_blu": [96, 32],
      "col_red_blu_blu": [128, 32],

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

# TODO : useless ??
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

    def set_color(self, red, grn, blu):
        self.col_red = red
        self.col_grn = grn
        self.col_blu = blu

    def has_color(self):
        return bool(self.col_red) or bool(self.col_grn) or bool(self.col_blu)

    def is_mono_color(self):
        nb_distinct_colors = sum(
            (
                int(bool(self.col_red)),
                int(bool(self.col_grn)),
                int(bool(self.col_blu)),
            )
        )
        return nb_distinct_colors == 1

    def has_same_mono_color(self, other_tile):
        if not self.is_mono_color():
            return False
        if not other_tile.is_mono_color():
            return False
        return all(
            (
                bool(self.col_red) == bool(other_tile.col_red),
                bool(self.col_grn) == bool(other_tile.col_grn),
                bool(self.col_blu) == bool(other_tile.col_blu),
            )
        )

    def render(self):
        gamobjs = []

        if self.is_mono_color():
            # Le 0.7 est un peu arbitraire. Pouet.
            gamobjs.extend(["col_red"] * int(self.col_red**0.7))
            gamobjs.extend(["col_grn"] * int(self.col_grn**0.7))
            gamobjs.extend(["col_blu"] * int(self.col_blu**0.7))
        elif self.has_color():
            gamobj_name = (
                "col"
                + "_red" * self.col_red
                + "_grn" * self.col_grn
                + "_blu" * self.col_blu
            )
            gamobjs.append(gamobj_name)

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
            for _ in range(5)
        ]

        for tile in tiles_to_colorize:
            if not tile.has_color():
                red, grn, blu = self.random_choose_multicol()
                tile.set_color(red, grn, blu)

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

    def random_choose_multicol(self):
        colors = [2, 1, 0]
        random.shuffle(colors)
        return colors

    def move_colors(self, tile_src, tile_dst):
        tile_dst.col_red = tile_src.col_red
        tile_dst.col_grn = tile_src.col_grn
        tile_dst.col_blu = tile_src.col_blu
        tile_src.col_red = 0
        tile_src.col_grn = 0
        tile_src.col_blu = 0

    def merge_colors(self, tile_src, tile_dst):
        tile_dst.col_red += tile_src.col_red
        tile_dst.col_grn += tile_src.col_grn
        tile_dst.col_blu += tile_src.col_blu
        tile_src.col_red = 0
        tile_src.col_grn = 0
        tile_src.col_blu = 0

    def move_grreeny(self, move_dir):
        """
        Déplace greeny, ainsi que les couleurs.
        Renvoie un booléen, indiquant si un mouvement
        a pu être effectué, ou pas.
        """
        tile_grreeny_cur = self.get_tile(*self.grreeny_coords)
        tile_grreeny_next = tile_grreeny_cur.adjacencies[move_dir]
        if tile_grreeny_next is None:
            return False

        if tile_grreeny_next.has_color():
            tile_grreeny_next_next = tile_grreeny_next.adjacencies[move_dir]
            if tile_grreeny_next_next is None:
                return False
            if tile_grreeny_next_next.has_color():
                if tile_grreeny_next.has_same_mono_color(tile_grreeny_next_next):
                    self.merge_colors(tile_grreeny_next, tile_grreeny_next_next)
                else:
                    return False
            else:
                self.move_colors(tile_grreeny_next, tile_grreeny_next_next)

        tile_grreeny_cur.has_grreeny = False
        self.grreeny_coords = (tile_grreeny_next.x, tile_grreeny_next.y)
        tile_grreeny_next.has_grreeny = True
        return True

    def on_game_event(self, event_name):

        move_dir = DIR_INT_FROM_STR.get(event_name)
        if move_dir is not None:
            move_result = self.move_grreeny(move_dir)
