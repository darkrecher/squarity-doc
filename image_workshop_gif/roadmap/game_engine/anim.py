# https://raw.githubusercontent.com/darkrecher/squarity-doc/master/image_workshop_gif/roadmap/game_engine/draft.png
# https://i.ibb.co/zmdNtcL/draft.png


"""

  {
    "tile_size": 32,
    "game_area": {
        "nb_tile_width": 12,
        "nb_tile_height": 9
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

      "spell_eye": [0, 96],
      "spell_heap": [0, 128],
      "spell_monster": [0, 160],
      "spell_monster_activated": [96, 128],
      "scroll_and_parchment": [32, 160],
      "parchment": [64, 160],
      "unrolled_parchment": [96, 160],
      "unrolled_scroll": [128, 160],
      "rolled_parchment": [32, 128],
      "rolled_scroll": [64, 128],

      "text_spell_norm_0": [192, 288],
      "text_spell_norm_1": [224, 288],
      "text_spell_norm_2": [256, 288],
      "text_spell_norm_3": [288, 288],
      "text_spell_norm_4": [320, 288],
      "text_spell_activ_0": [0, 288],
      "text_spell_activ_1": [32, 288],
      "text_spell_activ_2": [64, 288],
      "text_spell_activ_3": [96, 288],
      "text_spell_activ_4": [128, 288],


      "mouse_cursor_0_0_f": [299, 39],
      "mouse_cursor_0_1_u": [302, 21],
      "mouse_cursor_0_1_d": [302, 53],
      "mouse_cursor_0_2_f": [304, 28],
      "mouse_cursor_1_0_f": [294, 30],
      "mouse_cursor_1_1_f": [306, 34],
      "mouse_cursor_1_2_f": [318, 38],
      "mouse_cursor_1_3_f": [316, 40],
      "mouse_cursor_1_4_f": [314, 42],

      "flowers_0": [0, 64],
      "flowers_1": [32, 64],
      "flowers_2": [64, 64],
      "flowers_3": [96, 64],

      "magi_selection_up": [0, 32],
      "magi_selection_right": [32, 32],
      "magi_selection_down": [64, 32],
      "magi_selection_left": [96, 32],
      "magi_selection_middle": [128, 32],

      "monster_green_0u": [0, 220],
      "monster_green_0d": [0, 252],
      "monster_green_1u": [0, 216],
      "monster_green_1d": [0, 248],
      "monster_green_2u": [0, 212],
      "monster_green_2d": [0, 244],
      "monster_green_3u": [0, 208],
      "monster_green_3d": [0, 240],
      "monster_green_4u": [0, 204],
      "monster_green_4d": [0, 236],
      "monster_green_5u": [0, 200],
      "monster_green_5d": [0, 232],
      "monster_green_6u": [0, 196],
      "monster_green_6d": [0, 228],
      "monster_green_7u": [0, 192],
      "monster_green_7d": [0, 224],
      "monster_green": [0, 224],

      "sky": [256, 0],

      "vide": [0, 0]

    }
  }

"""

INITIAL_MAP = """
E*..........
H*..........
M...........
............
............
.......+....
.......I-...
./=-...I1...
=###===##===
"""

SEQ_MOUSE_CURSOR_TO_SPELL = (
    ((0, 3, "mouse_cursor_0_0_f"),),
    (
        (0, 2, "mouse_cursor_0_1_u"),
        (0, 3, "mouse_cursor_0_1_d"),
    ),
)

SEQ_STATIC_ROLLED_SPELL = (
    (
        (1, 2, "rolled_parchment"),
        (1, 2, "rolled_scroll"),
    ),
) * 1

SEQ_MOUSE_CURSOR_TO_GAME = (
    ((1, 2, "mouse_cursor_1_0_f"),),
    ((3, 2, "mouse_cursor_1_1_f"),),
    ((5, 2, "mouse_cursor_1_2_f"),),
    ((6, 2, "mouse_cursor_1_3_f"),),
)

SEQ_STATIC_MOUSE_CURSOR_ON_GAME = (((7, 2, "mouse_cursor_1_4_f"),),) * 6

SEQ_UNROLL_SPELL_TEXT_NORM = (
    (
        (1, 2, "unrolled_parchment"),
        (1, 2, "text_spell_norm_0"),
        (1, 2, "unrolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_norm_0"),
        (2, 2, "rolled_parchment"),
        (2, 2, "rolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_norm_0"),
        (2, 2, "unrolled_parchment"),
        (2, 2, "text_spell_norm_1"),
        (2, 2, "unrolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_norm_0"),
        (2, 2, "parchment"),
        (2, 2, "text_spell_norm_1"),
        (3, 2, "rolled_parchment"),
        (3, 2, "rolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_norm_0"),
        (2, 2, "parchment"),
        (2, 2, "text_spell_norm_1"),
        (3, 2, "unrolled_parchment"),
        (3, 2, "text_spell_norm_2"),
        (3, 2, "unrolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_norm_0"),
        (2, 2, "parchment"),
        (2, 2, "text_spell_norm_1"),
        (3, 2, "parchment"),
        (3, 2, "text_spell_norm_2"),
        (4, 2, "rolled_parchment"),
        (4, 2, "rolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_norm_0"),
        (2, 2, "parchment"),
        (2, 2, "text_spell_norm_1"),
        (3, 2, "parchment"),
        (3, 2, "text_spell_norm_2"),
        (4, 2, "unrolled_parchment"),
        (4, 2, "text_spell_norm_3"),
        (4, 2, "unrolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_norm_0"),
        (2, 2, "parchment"),
        (2, 2, "text_spell_norm_1"),
        (3, 2, "parchment"),
        (3, 2, "text_spell_norm_2"),
        (4, 2, "parchment"),
        (4, 2, "text_spell_norm_3"),
        (5, 2, "rolled_parchment"),
        (5, 2, "rolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_norm_0"),
        (2, 2, "parchment"),
        (2, 2, "text_spell_norm_1"),
        (3, 2, "parchment"),
        (3, 2, "text_spell_norm_2"),
        (4, 2, "parchment"),
        (4, 2, "text_spell_norm_3"),
        (5, 2, "unrolled_parchment"),
        (5, 2, "text_spell_norm_4"),
        (5, 2, "unrolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_norm_0"),
        (2, 2, "parchment"),
        (2, 2, "text_spell_norm_1"),
        (3, 2, "parchment"),
        (3, 2, "text_spell_norm_2"),
        (4, 2, "parchment"),
        (4, 2, "text_spell_norm_3"),
        (5, 2, "parchment"),
        (5, 2, "text_spell_norm_4"),
        (6, 2, "rolled_parchment"),
        (6, 2, "rolled_scroll"),
    ),
)

SEQ_UNROLL_SPELL_TEXT_ACTIV = (
    (
        (1, 2, "unrolled_parchment"),
        (1, 2, "text_spell_activ_0"),
        (1, 2, "unrolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_activ_0"),
        (2, 2, "rolled_parchment"),
        (2, 2, "rolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_activ_0"),
        (2, 2, "unrolled_parchment"),
        (2, 2, "text_spell_activ_1"),
        (2, 2, "unrolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_activ_0"),
        (2, 2, "parchment"),
        (2, 2, "text_spell_activ_1"),
        (3, 2, "rolled_parchment"),
        (3, 2, "rolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_activ_0"),
        (2, 2, "parchment"),
        (2, 2, "text_spell_activ_1"),
        (3, 2, "unrolled_parchment"),
        (3, 2, "text_spell_activ_2"),
        (3, 2, "unrolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_activ_0"),
        (2, 2, "parchment"),
        (2, 2, "text_spell_activ_1"),
        (3, 2, "parchment"),
        (3, 2, "text_spell_activ_2"),
        (4, 2, "rolled_parchment"),
        (4, 2, "rolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_activ_0"),
        (2, 2, "parchment"),
        (2, 2, "text_spell_activ_1"),
        (3, 2, "parchment"),
        (3, 2, "text_spell_activ_2"),
        (4, 2, "unrolled_parchment"),
        (4, 2, "text_spell_activ_3"),
        (4, 2, "unrolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_activ_0"),
        (2, 2, "parchment"),
        (2, 2, "text_spell_activ_1"),
        (3, 2, "parchment"),
        (3, 2, "text_spell_activ_2"),
        (4, 2, "parchment"),
        (4, 2, "text_spell_activ_3"),
        (5, 2, "rolled_parchment"),
        (5, 2, "rolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_activ_0"),
        (2, 2, "parchment"),
        (2, 2, "text_spell_activ_1"),
        (3, 2, "parchment"),
        (3, 2, "text_spell_activ_2"),
        (4, 2, "parchment"),
        (4, 2, "text_spell_activ_3"),
        (5, 2, "unrolled_parchment"),
        (5, 2, "text_spell_activ_4"),
        (5, 2, "unrolled_scroll"),
    ),
    (
        (1, 2, "parchment"),
        (1, 2, "text_spell_activ_0"),
        (2, 2, "parchment"),
        (2, 2, "text_spell_activ_1"),
        (3, 2, "parchment"),
        (3, 2, "text_spell_activ_2"),
        (4, 2, "parchment"),
        (4, 2, "text_spell_activ_3"),
        (5, 2, "parchment"),
        (5, 2, "text_spell_activ_4"),
        (6, 2, "rolled_parchment"),
        (6, 2, "rolled_scroll"),
    ),
)

SEQ_ROLL_SPELL_TEXT_ACTIV = SEQ_UNROLL_SPELL_TEXT_ACTIV[::-1]

SEQ_STATIC_ACTIVATED_SPELL_AND_TEXT = (
    (
        (0, 2, "spell_monster_activated"),
        (1, 2, "parchment"),
        (1, 2, "text_spell_activ_0"),
        (2, 2, "parchment"),
        (2, 2, "text_spell_activ_1"),
        (3, 2, "parchment"),
        (3, 2, "text_spell_activ_2"),
        (4, 2, "parchment"),
        (4, 2, "text_spell_activ_3"),
        (5, 2, "parchment"),
        (5, 2, "text_spell_activ_4"),
        (6, 2, "rolled_parchment"),
        (6, 2, "rolled_scroll"),
    ),
) * 2

SEQ_STATIC_ACTIVATED_SPELL = (((0, 2, "spell_monster_activated"),),)

SEQ_SPELL = (
    SEQ_STATIC_ROLLED_SPELL
    + SEQ_UNROLL_SPELL_TEXT_NORM
    + SEQ_STATIC_ACTIVATED_SPELL_AND_TEXT
    + SEQ_ROLL_SPELL_TEXT_ACTIV
)

LEN_STATIC_MOUSE = len(SEQ_UNROLL_SPELL_TEXT_NORM) + len(
    SEQ_STATIC_ACTIVATED_SPELL_AND_TEXT
)
SEQ_STATIC_MOUSE_CURSOR_ON_SPELL = (((0, 2, "mouse_cursor_0_2_f"),),) * LEN_STATIC_MOUSE

SEQ_MOUSE = (
    SEQ_MOUSE_CURSOR_TO_SPELL
    + SEQ_STATIC_MOUSE_CURSOR_ON_SPELL
    + SEQ_MOUSE_CURSOR_TO_GAME
    + SEQ_STATIC_MOUSE_CURSOR_ON_GAME
)

DATE_START_LAUNCH_SPELL = 21

SEQ_MAGI_SQUARE = (
    (
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_up"),
        (7, 2, "magi_selection_right"),
        (7, 2, "magi_selection_left"),
        (7, 2, "magi_selection_down"),
    ),
    (
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_up"),
        (7, 2, "magi_selection_right"),
        (7, 2, "magi_selection_left"),
        (7, 2, "magi_selection_down"),
    ),
    (
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_up"),
        (7, 2, "magi_selection_left"),
        (7, 2, "magi_selection_down"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_up"),
        (8, 2, "magi_selection_right"),
        (8, 2, "magi_selection_down"),
    ),
    (
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_up"),
        (7, 2, "magi_selection_left"),
        (7, 2, "magi_selection_down"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_up"),
        (8, 2, "magi_selection_right"),
        (8, 2, "magi_selection_down"),
    ),
    (
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_up"),
        (7, 2, "magi_selection_left"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_up"),
        (8, 2, "magi_selection_right"),
        (7, 3, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (7, 3, "magi_selection_down"),
        (7, 3, "magi_selection_left"),
        (8, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_right"),
        (8, 3, "magi_selection_down"),
    ),
    (
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_up"),
        (7, 2, "magi_selection_left"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_up"),
        (8, 2, "magi_selection_right"),
        (7, 3, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (7, 3, "magi_selection_down"),
        (7, 3, "magi_selection_left"),
        (8, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_right"),
        (8, 3, "magi_selection_down"),
    ),
)

SEQ_GREEN_FALL = (
    ((7, 3, "monster_green"),),
    ((7, 3, "monster_green"),),
    (
        (7, 3, "monster_green_0u"),
        (7, 4, "monster_green_0d"),
    ),
    (
        (7, 3, "monster_green_1u"),
        (7, 4, "monster_green_1d"),
    ),
    (
        (7, 3, "monster_green_2u"),
        (7, 4, "monster_green_2d"),
    ),
    (
        (7, 3, "monster_green_3u"),
        (7, 4, "monster_green_3d"),
    ),
    (
        (7, 3, "monster_green_4u"),
        (7, 4, "monster_green_4d"),
    ),
    (
        (7, 3, "monster_green_5u"),
        (7, 4, "monster_green_5d"),
    ),
    (
        (7, 3, "monster_green_6u"),
        (7, 4, "monster_green_6d"),
    ),
    (
        (7, 3, "monster_green_7u"),
        (7, 4, "monster_green_7d"),
    ),
    ((7, 4, "monster_green"),),
    ((7, 4, "monster_green"),),
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
        "E": "spell_eye",
        "H": "spell_heap",
        "M": "spell_monster",
        "*": "scroll_and_parchment",
        ".": None,
    }

    def __init__(self):
        self.w = 12
        self.h = 9
        self.anim_sequences = (
            AnimationSequence(SEQ_SPELL, 0),
            AnimationSequence(
                SEQ_STATIC_ACTIVATED_SPELL,
                len(SEQ_UNROLL_SPELL_TEXT_NORM)
                + len(SEQ_STATIC_ACTIVATED_SPELL_AND_TEXT),
                loop=True,
            ),
            AnimationSequence(
                SEQ_STATIC_ROLLED_SPELL,
                len(SEQ_SPELL),
                loop=True,
            ),
            AnimationSequence(SEQ_GREEN_FALL, 40),
            AnimationSequence(SEQ_MAGI_SQUARE, DATE_START_LAUNCH_SPELL),
            AnimationSequence(SEQ_MOUSE, 0),
        )
        self.tiles = [[[] for x in range(self.w)] for y in range(self.h)]
        end_dates = [
            anim_seq.end_date
            for anim_seq in self.anim_sequences
            if anim_seq.end_date is not None
        ]
        self.end_date = max(end_dates)

        # TODO
        self.calculated_game_areas = []

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
