"""
Ceci n'est pas un jeu !

C'est une toute petite animation pour créer la gif animée de preview de l'autre gif animée principale de game engine.

Cette preview est nécessaire pour publier sur le site PixelJoint.

"""

# https://raw.githubusercontent.com/darkrecher/squarity-doc/master/image_workshop_gif/roadmap/game_engine/draft.png
# https://i.ibb.co/SKXSDgs/draft.png
# https://i.ibb.co/W5Kcnpr/draft.png

"""

  {
    "tile_size": 32,
    "game_area": {
        "nb_tile_width": 4,
        "nb_tile_height": 4
    },

    "img_coords": {

      "earth": [0, 0],
      "earth_left": [32, 0],
      "earth_right": [64, 0],
      "earth_up": [96, 0],
      "earth_up_left": [128, 0],
      "earth_up_right": [160, 0],
      "earth_left_right": [192, 0],
      "earth_top": [224, 0],

      "flowers_0": [0, 64],
      "flowers_1": [32, 64],
      "flowers_2": [64, 64],
      "flowers_3": [96, 64],

      "monster_blue": [32, 224],

      "monster_white": [64, 224],

      "monster_white_rot_0l": [224, 32],
      "monster_white_rot_0r": [256, 32],
      "monster_white_rot_1l": [224, 64],
      "monster_white_rot_1r": [256, 64],
      "monster_white_rot_2l": [224, 96],
      "monster_white_rot_2r": [256, 96],
      "monster_white_rot_3l": [224, 128],
      "monster_white_rot_3r": [256, 128],
      "monster_white_rot_4l": [224, 160],
      "monster_white_rot_4r": [256, 160],
      "monster_white_rot_5l": [224, 192],
      "monster_white_rot_5r": [256, 192],
      "monster_white_rot_6l": [224, 224],
      "monster_white_rot_6r": [256, 224],
      "monster_white_rot_7l": [224, 256],
      "monster_white_rot_7r": [256, 256],

      "flowers_0": [64, 64],
      "flowers_1": [96, 64],
      "flowers_2": [0, 64],
      "flowers_3": [32, 64],

      "text_preview_0": [288, 256],
      "text_preview_1": [320, 256],

      "sky": [256, 0]

    }
  }

"""

INITIAL_MAP = """
....
Oab.
-...
#==.
"""


def untemplatize_seq(sequence, offset_x, offset_y, template_tag, template_value):
    new_sequence = []
    for step in sequence:
        new_step = [
            (
                x + offset_x,
                y + offset_y,
                gamobj.replace("{{" + template_tag + "}}", template_value),
            )
            for x, y, gamobj in step
        ]
        new_sequence.append(tuple(new_step))
    return tuple(new_sequence)


SEQ_TEMPLATE_MONSTER_ROT = (
    (
        (0, 0, "{{monster}}_rot_0l"),
        (1, 0, "{{monster}}_rot_0r"),
    ),
    (
        (0, 0, "{{monster}}_rot_1l"),
        (1, 0, "{{monster}}_rot_1r"),
    ),
    (
        (0, 0, "{{monster}}_rot_2l"),
        (1, 0, "{{monster}}_rot_2r"),
    ),
    (
        (0, 0, "{{monster}}_rot_3l"),
        (1, 0, "{{monster}}_rot_3r"),
    ),
    (
        (0, 0, "{{monster}}_rot_4l"),
        (1, 0, "{{monster}}_rot_4r"),
    ),
    (
        (0, 0, "{{monster}}_rot_5l"),
        (1, 0, "{{monster}}_rot_5r"),
    ),
    (
        (0, 0, "{{monster}}_rot_6l"),
        (1, 0, "{{monster}}_rot_6r"),
    ),
    (
        (0, 0, "{{monster}}_rot_7l"),
        (1, 0, "{{monster}}_rot_7r"),
    ),
)

SEQ_STATIC_WHITE_ON_START = (((8, 2, "monster_white"),),) * 5

SEQ_WHITE = untemplatize_seq(
    SEQ_TEMPLATE_MONSTER_ROT, 1, 2, "monster", "monster_white"
) + untemplatize_seq(SEQ_TEMPLATE_MONSTER_ROT, 2, 2, "monster", "monster_white")

SEQ_STATIC_WHITE_ON_END = (((9, 6, "monster_white"),),)

SEQ_FLOWERS = (
    (((2, 5, "flowers_0"),),) * 5
    + (
        ((2, 5, "flowers_1"),),
        ((2, 5, "flowers_2"),),
        ((2, 5, "flowers_3"),),
    )
    + (((2, 5, "flowers_0"),),) * 15
    + (((2, 5, "flowers_1"),),) * 7
    + (((2, 5, "flowers_0"),),) * 2
)


class AnimationSequence:
    def __init__(self, gamobj_sequence, start_date, loop=False):
        self.gamobj_sequence = gamobj_sequence
        self.start_date = start_date
        self.loop = loop
        if loop:
            self.end_date = None
        else:
            self.end_date = self.start_date + len(self.gamobj_sequence)

    def get_end_date(self):
        return self.end_date

    def get_gamobjs_at_date(self, current_date):
        if current_date < self.start_date:
            return ()
        if self.end_date is not None and current_date >= self.end_date:
            return ()

        current_date -= self.start_date
        gamobjs_at_date = self.gamobj_sequence[current_date % len(self.gamobj_sequence)]
        return gamobjs_at_date


class GameModel:

    DICT_GAMOBJ_FROM_CHAR = {
        "#": "earth",
        "I": "earth_left",
        "1": "earth_right",
        "=": "earth_up",
        "/": "earth_up_left",
        "-": "earth_up_right",
        "|": "earth_left_right",
        "+": "earth_top",
        "O": "monster_blue",
        "a": "text_preview_0",
        "b": "text_preview_1",
        ".": None,
    }

    def __init__(self):
        self.w = 4
        self.h = 4
        self.anim_sequences = (AnimationSequence(SEQ_WHITE, 0),)
        self.tiles = [[[] for x in range(self.w)] for y in range(self.h)]
        end_dates = [
            anim_seq.end_date
            for anim_seq in self.anim_sequences
            if anim_seq.end_date is not None
        ]
        self.end_date = max(end_dates)

        self.initial_map = INITIAL_MAP.strip().split("\n")
        self.current_step_index = 0
        self.apply_anim_step()

    def reset_game_area(self):
        for y in range(self.h):
            for x in range(self.w):
                tile_char = self.initial_map[y][x]
                gamobj = GameModel.DICT_GAMOBJ_FROM_CHAR[tile_char]
                if gamobj is None:
                    current_game_objects = ["sky"]
                else:
                    current_game_objects = ["sky", gamobj]
                self.tiles[y][x][:] = current_game_objects

    def apply_anim_step(self):
        self.reset_game_area()
        for anim_seq in self.anim_sequences:
            seq_gamobjs = anim_seq.get_gamobjs_at_date(self.current_step_index)
            for x, y, gamobj in seq_gamobjs:
                self.tiles[y][x].append(gamobj)

    def export_all_tiles(self):
        return self.tiles

    def on_game_event(self, event_name):
        if event_name in ("U", "L"):
            self.current_step_index -= 1
            if self.current_step_index < 0:
                self.current_step_index = 0
        elif event_name in ("D", "R"):
            self.current_step_index += 1
            if self.current_step_index >= self.end_date:
                self.current_step_index = self.end_date - 1

        self.apply_anim_step()
