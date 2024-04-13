# https://i.ibb.co/VjVQnxQ/koballd-tileset.png

"""

  {
    "version": "1.0.0",
    "game_area": {
        "nb_tile_width": 21,
        "nb_tile_height": 21
    },
    "tile_size": 32,
    "img_coords": {
        "dark": [0, 0],
        "kob_right_up": [32, 0],
        "kob_right_down": [32, 32],
        "kob_down_left": [64, 0],
        "kob_down_right": [96, 0],
        "kob_up_left": [64, 32],
        "kob_up_right": [96, 32],
        "kob_left_up": [128, 0],
        "kob_left_down": [128, 32],
        "selection": [64, 64],
        "wall": [0, 64],
        "ground": [0, 32],
        "cake": [32, 64],

        "osef": [0, 0]
    }
  }

"""


OFFSET_FROM_DIR_STR = {
    "up": (0, -1),
    "right": (+1, 0),
    "down": (0, +1),
    "left": (-1, 0),
}

OFFSET_SCREEN_TO_MAP = (2, 2)


class MapTile:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.adjacencies = None
        self.game_objects = []


    def render(self):
        return self.game_objects


class KoballdLauncher:

    def __init__(self, x, y, direction, subdirection, selected):
        self.x = x
        self.y = y
        self.direction = direction
        self.subdirection = subdirection
        self.selected = selected
        self.kob_game_object = "kob_" + self.direction + "_" + self.subdirection

    def set_neighbor_launcher(self, neighbor):
        self.neighbor = neighbor

    def select(self):
        self.selected = True
        self.neighbor.selected = False

    def render(self):
        if self.selected:
            return ["dark", self.kob_game_object, "selection"]
        else:
            return ["dark", self.kob_game_object]



class GameModel():

    def __init__(self):
        self.w = 21
        self.h = 21
        ofs_x, ofs_y = OFFSET_SCREEN_TO_MAP
        self.map_w = self.w - 2*ofs_x
        self.map_h = self.h - 2*ofs_y
        self.rendered_tiles = [
            [
                [] for x in range(self.w)
            ]
            for y in range(self.h)
        ]

        self.map_tiles = [
            [
                MapTile(x, y) for x in range(self.map_w)
            ]
            for y in range(self.map_h)
        ]
        for y in range(self.map_h):
            for x in range(self.map_w):
                self.get_map_tile(x, y).adjacencies = self._make_adjacencies(x, y)

        KOBALLD_LAUNCHER_DEFINITIONS = (
            (self.w // 2 - 2, 0, "down", "left", True),
            (self.w // 2 + 2, 0, "down", "right", False),
            (self.w // 2 - 2, self.h - 1, "up", "left", True),
            (self.w // 2 + 2, self.h - 1, "up", "right", False),
            (0, self.h // 2 - 2, "right", "up", True),
            (0, self.h // 2 + 2, "right", "down", False),
            (self.w - 1, self.h // 2 - 2, "left", "up", True),
            (self.w - 1, self.h // 2 + 2, "left", "down", False),
        )
        self.koblau = []
        self.koblau_from_coord = {}
        for x, y, direction, subdirection, selected in KOBALLD_LAUNCHER_DEFINITIONS:
            koballd_launcher = KoballdLauncher(x, y, direction, subdirection, selected)
            self.koblau.append(koballd_launcher)
            self.koblau_from_coord[(x, y)] = koballd_launcher
        for idx_kob in range(0, 8, 2):
            self.koblau[idx_kob].set_neighbor_launcher(self.koblau[idx_kob + 1])
            self.koblau[idx_kob + 1].set_neighbor_launcher(self.koblau[idx_kob])

        self.init_ihm()
        self.init_level()


    def _make_adjacencies(self, x, y):
        """
        Renvoie les tiles adjacentes à la tile située aux coordonnées x, y.
        On renvoie toujours une liste de 8 éléments (les 8 directions), mais certains éléments
        peuvent être None, si les coordonnées x, y sont sur un bord de l'aire de jeu.
        """
        adjacencies = (
            self.map_tiles[y - 1][x] if 0 <= y - 1 else None,
            self.map_tiles[y - 1][x + 1] if 0 <= y - 1 and x + 1 < self.map_w else None,
            self.map_tiles[y][x + 1] if x + 1 < self.map_w else None,
            self.map_tiles[y + 1][x + 1] if y + 1 < self.map_h and x + 1 < self.map_w else None,
            self.map_tiles[y + 1][x] if y + 1 < self.map_h else None,
            self.map_tiles[y + 1][x - 1] if y + 1 < self.map_h and 0 <= x - 1 else None,
            self.map_tiles[y][x - 1] if 0 <= x - 1 else None,
            self.map_tiles[y - 1][x - 1] if 0 <= y - 1 and 0 <= x - 1 else None,
        )
        return adjacencies


    def get_map_tile(self, x, y):
        return self.map_tiles[y][x]


    def init_ihm(self):
        ofs_x, ofs_y = OFFSET_SCREEN_TO_MAP
        for x in range(self.w):
            for y in range(ofs_y):
                self.rendered_tiles[y][x] = ["dark"]
            for y in range(self.h - ofs_y, self.h):
                self.rendered_tiles[y][x] = ["dark"]
        for y in range(self.h):
            for x in range(ofs_x):
                self.rendered_tiles[y][x] = ["dark"]
            for x in range(self.w - ofs_x, self.w):
                self.rendered_tiles[y][x] = ["dark"]
        self.render_koballd_launcher()


    def render_koballd_launcher(self):
        for koballd_launcher in self.koblau:
            self.rendered_tiles[koballd_launcher.y][koballd_launcher.x] = koballd_launcher.render()


    def init_level(self):
        for y in range(self.map_h):
            for x in range(self.map_w):
                self.get_map_tile(x, y).game_objects = ["ground"]

        self.get_map_tile(5, 5).game_objects = ["wall"]
        self.get_map_tile(8, 7).game_objects = ["ground", "cake"]


    def export_all_tiles(self):
        ofs_x, ofs_y = OFFSET_SCREEN_TO_MAP
        for y in range(self.map_h):
            for x in range(self.map_w):
                tile = self.get_map_tile(x, y)
                self.rendered_tiles[y + ofs_y][x + ofs_x] = tile.render()
        return self.rendered_tiles


    def on_click(self, x, y):
        for koballd_launcher in self.koblau:
            if koballd_launcher.x == x and koballd_launcher.y == y:
                koballd_launcher.select()
                self.render_koballd_launcher()

