# https://raw.githubusercontent.com/darkrecher/squarity-doc/master/image_workshop_gif/roadmap/game_engine/draft.png

"""
TODO (dessins) :
 - ciel entièrement bleu
 - earth "left et right"
 - earth "up, left et right"
"""

"""



  {
    "tile_size": 32,
    "game_area": {
        "nb_tile_width": 12,
        "nb_tile_height": 10
    },

    "img_coords": {

      "earth": [0, 0],
      "earth_left": [32, 0],
      "earth_right": [64, 0],
      "earth_up": [96, 0],
      "earth_up_left": [128, 0],
      "earth_up_right": [160, 0],

      "spell_eye": [0, 96],
      "spell_heap": [0, 128],
      "spell_monster": [0, 160],
      "scroll_left": [32, 160],
      "scroll": [64, 160],
      "scroll_right": [96, 160],



      "sky": [192, 0],

      "vide": [0, 0]

    }
  }


"""

INITIAL_MAP = """
E*..........
H*..........
M*..........
............
............
......./....
.......|....
.......|-...
./=-...|1...
=###===##===
"""

ANIM_STEPS = (
    ((1, 2, "+"),),
    (
        (1, 2, "~"),
        (2, 2, "*"),
    ),
    ((2, 2, "+"),),
    (
        (2, 2, "~"),
        (3, 2, "*"),
    ),
    ((3, 2, "+"),),
    (
        (3, 2, "~"),
        (4, 2, "*"),
    ),
)


class GameModel:

    DICT_GAMOBJ_FROM_CHAR = {
        "#": "earth",
        "|": "earth_left",
        "1": "earth_right",
        "=": "earth_up",
        "/": "earth_up_left",
        "-": "earth_up_right",
        ".": "sky",
        "E": "spell_eye",
        "H": "spell_heap",
        "M": "spell_monster",
        "*": "scroll_left",
        "~": "scroll",
        "+": "scroll_right",
    }

    def __init__(self):
        self.w = 12
        self.h = 10
        self.tiles = [[[] for x in range(self.w)] for y in range(self.h)]

        initial_map = INITIAL_MAP.strip().split("\n")
        for y in range(self.h):
            for x in range(self.w):
                tile_char = initial_map[y][x]
                self.tiles[y][x].append(GameModel.DICT_GAMOBJ_FROM_CHAR[tile_char])

        self.current_step_index = 0

    def apply_anim_step(self, anim_step):
        for x, y, tile_char in anim_step:
            self.tiles[y][x][:] = [GameModel.DICT_GAMOBJ_FROM_CHAR[tile_char]]

    def export_all_tiles(self):
        return self.tiles

    def on_game_event(self, event_name):
        if self.current_step_index >= len(ANIM_STEPS):
            print("C'est fini !!")
            return

        current_anim_step = ANIM_STEPS[self.current_step_index]
        self.apply_anim_step(current_anim_step)
        self.current_step_index += 1
