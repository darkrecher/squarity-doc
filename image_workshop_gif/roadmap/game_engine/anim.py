"""
Ceci n'est pas un jeu !

C'est une petite animation qui sera utilisée pour créer une gif animée.

Cette gif animée sera placée dans la road-map, sur le carré "moteur du jeu", juste au-dessus du carré de départ.

Appuyez sur les flèches droite et gauche pour faire avancer/reculer l'animation. C'est tout.

Lorsque la gif sera créée, je la mettrais sur le site PixelJoint. Si vous avez un compte, ce serait gentil de mettre un petit like.


"""

# https://raw.githubusercontent.com/darkrecher/squarity-doc/master/image_workshop_gif/roadmap/game_engine/draft.png

"""

  {
    "tile_size": 32,
    "game_area": {
        "nb_tile_width": 12,
        "nb_tile_height": 8
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
      "mouse_cursor_2_0_l": [292, 36],
      "mouse_cursor_2_0_r": [324, 36],
      "mouse_cursor_2_1_f": [307, 30],
      "mouse_cursor_2_2_u": [304, 22],
      "mouse_cursor_2_2_d": [304, 54],
      "mouse_cursor_2_3_f": [300, 39],
      "mouse_cursor_3_0_f": [318, 35],
      "mouse_cursor_3_1_f": [309, 32],

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

      "monster_blue_0u": [32, 220],
      "monster_blue_0d": [32, 252],
      "monster_blue_1u": [32, 216],
      "monster_blue_1d": [32, 248],
      "monster_blue_2u": [32, 212],
      "monster_blue_2d": [32, 244],
      "monster_blue_3u": [32, 208],
      "monster_blue_3d": [32, 240],
      "monster_blue_4u": [32, 204],
      "monster_blue_4d": [32, 236],
      "monster_blue_5u": [32, 200],
      "monster_blue_5d": [32, 232],
      "monster_blue_6u": [32, 196],
      "monster_blue_6d": [32, 228],
      "monster_blue_7u": [32, 192],
      "monster_blue_7d": [32, 224],
      "monster_blue": [32, 224],

      "monster_white_0u": [64, 220],
      "monster_white_0d": [64, 252],
      "monster_white_1u": [64, 216],
      "monster_white_1d": [64, 248],
      "monster_white_2u": [64, 212],
      "monster_white_2d": [64, 244],
      "monster_white_3u": [64, 208],
      "monster_white_3d": [64, 240],
      "monster_white_4u": [64, 204],
      "monster_white_4d": [64, 236],
      "monster_white_5u": [64, 200],
      "monster_white_5d": [64, 232],
      "monster_white_6u": [64, 196],
      "monster_white_6d": [64, 228],
      "monster_white_7u": [64, 192],
      "monster_white_7d": [64, 224],
      "monster_white": [64, 224],

      "monster_red_0u": [96, 220],
      "monster_red_0d": [96, 252],
      "monster_red_1u": [96, 216],
      "monster_red_1d": [96, 248],
      "monster_red_2u": [96, 212],
      "monster_red_2d": [96, 244],
      "monster_red_3u": [96, 208],
      "monster_red_3d": [96, 240],
      "monster_red_4u": [96, 204],
      "monster_red_4d": [96, 236],
      "monster_red_5u": [96, 200],
      "monster_red_5d": [96, 232],
      "monster_red_6u": [96, 196],
      "monster_red_6d": [96, 228],
      "monster_red_7u": [96, 192],
      "monster_red_7d": [96, 224],
      "monster_red": [96, 224],

      "monster_red_rot_0l": [160, 32],
      "monster_red_rot_0r": [192, 32],
      "monster_red_rot_1l": [160, 64],
      "monster_red_rot_1r": [192, 64],
      "monster_red_rot_2l": [160, 96],
      "monster_red_rot_2r": [192, 96],
      "monster_red_rot_3l": [160, 128],
      "monster_red_rot_3r": [192, 128],
      "monster_red_rot_4l": [160, 160],
      "monster_red_rot_4r": [192, 160],
      "monster_red_rot_5l": [160, 192],
      "monster_red_rot_5r": [192, 192],
      "monster_red_rot_6l": [160, 224],
      "monster_red_rot_6r": [192, 224],
      "monster_red_rot_7l": [160, 256],
      "monster_red_rot_7r": [192, 256],

      "monster_red_rot_0l": [160, 32],
      "monster_red_rot_0r": [192, 32],
      "monster_red_rot_1l": [160, 64],
      "monster_red_rot_1r": [192, 64],
      "monster_red_rot_2l": [160, 96],
      "monster_red_rot_2r": [192, 96],
      "monster_red_rot_3l": [160, 128],
      "monster_red_rot_3r": [192, 128],
      "monster_red_rot_4l": [160, 160],
      "monster_red_rot_4r": [192, 160],
      "monster_red_rot_5l": [160, 192],
      "monster_red_rot_5r": [192, 192],
      "monster_red_rot_6l": [160, 224],
      "monster_red_rot_6r": [192, 224],
      "monster_red_rot_7l": [160, 256],
      "monster_red_rot_7r": [192, 256],

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

      "text_ouch_l": [32, 96],
      "text_ouch_r": [64, 96],

      "star_0_0": [307, 144],
      "star_0_1": [307, 208],
      "star_1_0": [304, 151],
      "star_1_1": [304, 215],
      "star_2_0": [297, 141],
      "star_2_1": [297, 205],
      "star_3_0": [312, 147],
      "star_3_1": [312, 211],
      "star_4_0_0": [287, 141],
      "star_4_0_1": [319, 141],
      "star_4_1_0": [287, 205],
      "star_4_1_1": [319, 205],
      "star_5_0_0": [309, 126],
      "star_5_0_1": [309, 158],
      "star_5_1_0": [309, 190],
      "star_5_1_1": [309, 222],
      "star_6_0": [310, 135],
      "star_6_1": [310, 199],

      "flowers_0": [64, 64],
      "flowers_1": [96, 64],
      "flowers_2": [0, 64],
      "flowers_3": [32, 64],

      "sky": [256, 0]

    }
  }

"""

INITIAL_MAP = """
E*..........
H*..........
M...........
............
............
....../-....
..+...I#-...
==#===###===
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

SEQ_MOUSE_CURSOR_TO_GAME = (
    ((1, 2, "mouse_cursor_1_0_f"),),
    ((3, 2, "mouse_cursor_1_1_f"),),
    ((5, 2, "mouse_cursor_1_2_f"),),
    ((6, 2, "mouse_cursor_1_3_f"),),
)

SEQ_STATIC_MOUSE_CURSOR_ON_GAME = (((7, 2, "mouse_cursor_1_4_f"),),) * 4

SEQ_MOUSE_DRAW_SPELL_RECT = (
    (
        (7, 2, "mouse_cursor_2_0_l"),
        (8, 2, "mouse_cursor_2_0_r"),
    ),
    ((8, 2, "mouse_cursor_2_1_f"),),
    (
        (8, 2, "mouse_cursor_2_2_u"),
        (8, 3, "mouse_cursor_2_2_d"),
    ),
    ((8, 3, "mouse_cursor_2_3_f"),),
    ((8, 3, "mouse_cursor_2_3_f"),),
    ((8, 3, "mouse_cursor_2_3_f"),),
    ((9, 3, "mouse_cursor_3_0_f"),),
)


SEQ_MOUSE = (
    SEQ_MOUSE_CURSOR_TO_SPELL
    + SEQ_STATIC_MOUSE_CURSOR_ON_SPELL
    + SEQ_MOUSE_CURSOR_TO_GAME
    + SEQ_STATIC_MOUSE_CURSOR_ON_GAME
    + SEQ_MOUSE_DRAW_SPELL_RECT
)

SEQ_STATIC_MOUSE_CURSOR_ON_END = (((9, 3, "mouse_cursor_3_1_f"),),)

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
    (
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
    ),
    (
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
    ),
    (
        (7, 2, "magi_selection_middle"),
        (7, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
    ),
    (
        (7, 2, "magi_selection_middle"),
        (8, 2, "magi_selection_middle"),
        (7, 3, "magi_selection_middle"),
        (8, 3, "magi_selection_middle"),
    ),
)

SEQ_MAGI_STARS = (
    ((7, 2, "star_0_0"),),
    (
        (7, 2, "star_0_1"),
        (7, 2, "star_4_0_0"),
        (8, 2, "star_4_0_1"),
    ),
    (
        (8, 2, "star_1_0"),
        (7, 2, "star_0_0"),
        (7, 2, "star_4_1_0"),
        (8, 2, "star_4_1_1"),
    ),
    (
        (8, 2, "star_1_1"),
        (7, 3, "star_2_0"),
        (7, 2, "star_4_0_0"),
        (8, 2, "star_4_0_1"),
    ),
    (
        (8, 2, "star_1_0"),
        (7, 3, "star_2_1"),
        (8, 2, "star_2_0"),
        (8, 3, "star_1_0"),
        (7, 3, "star_6_0"),
    ),
    (
        (7, 3, "star_2_0"),
        (8, 3, "star_3_0"),
        (8, 2, "star_2_1"),
        (7, 2, "star_5_0_0"),
        (7, 3, "star_5_0_1"),
        (8, 3, "star_1_1"),
        (8, 3, "star_2_0"),
        (7, 3, "star_6_1"),
    ),
    (
        (8, 3, "star_3_1"),
        (8, 2, "star_2_0"),
        (7, 2, "star_5_1_0"),
        (7, 3, "star_5_1_1"),
        (8, 3, "star_1_0"),
        (8, 3, "star_2_1"),
        (7, 3, "star_6_0"),
    ),
    (
        (8, 3, "star_3_0"),
        (7, 2, "star_5_0_0"),
        (7, 3, "star_5_0_1"),
        (8, 3, "star_2_0"),
    ),
)

SEQ_TEMPLATE_MONSTER_FALL = (
    (
        (0, 0, "{{monster}}_0u"),
        (0, 1, "{{monster}}_0d"),
    ),
    (
        (0, 0, "{{monster}}_1u"),
        (0, 1, "{{monster}}_1d"),
    ),
    (
        (0, 0, "{{monster}}_2u"),
        (0, 1, "{{monster}}_2d"),
    ),
    (
        (0, 0, "{{monster}}_3u"),
        (0, 1, "{{monster}}_3d"),
    ),
    (
        (0, 0, "{{monster}}_4u"),
        (0, 1, "{{monster}}_4d"),
    ),
    (
        (0, 0, "{{monster}}_5u"),
        (0, 1, "{{monster}}_5d"),
    ),
    (
        (0, 0, "{{monster}}_6u"),
        (0, 1, "{{monster}}_6d"),
    ),
    (
        (0, 0, "{{monster}}_7u"),
        (0, 1, "{{monster}}_7d"),
    ),
)

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

SEQ_STATIC_GREEN_ON_START = (((7, 3, "monster_green"),),) * 5

SEQ_STATIC_GREEN_ON_END = (((7, 4, "monster_green"),),)

SEQ_GREEN = SEQ_STATIC_GREEN_ON_START + untemplatize_seq(
    SEQ_TEMPLATE_MONSTER_FALL, 7, 3, "monster", "monster_green"
)

SEQ_STATIC_BLUE_ON_START = (((8, 3, "monster_blue"),),) * 5

SEQ_STATIC_BLUE_ON_END = (((8, 5, "monster_blue"),),)

SEQ_BLUE = (
    SEQ_STATIC_BLUE_ON_START
    + untemplatize_seq(SEQ_TEMPLATE_MONSTER_FALL, 8, 3, "monster", "monster_blue")
    + untemplatize_seq(SEQ_TEMPLATE_MONSTER_FALL, 8, 4, "monster", "monster_blue")
)

SEQ_STATIC_RED_ON_START = (((7, 2, "monster_red"),),) * 5

SEQ_RED = (
    SEQ_STATIC_RED_ON_START
    + untemplatize_seq(SEQ_TEMPLATE_MONSTER_FALL, 7, 2, "monster", "monster_red")
    + untemplatize_seq(SEQ_TEMPLATE_MONSTER_ROT, 6, 3, "monster", "monster_red")
    + untemplatize_seq(SEQ_TEMPLATE_MONSTER_FALL, 6, 3, "monster", "monster_red")
)

SEQ_STATIC_RED_ON_END = (((6, 4, "monster_red"),),)

SEQ_STATIC_WHITE_ON_START = (((8, 2, "monster_white"),),) * 5

SEQ_WHITE = (
    SEQ_STATIC_WHITE_ON_START
    + untemplatize_seq(SEQ_TEMPLATE_MONSTER_FALL, 8, 2, "monster", "monster_white")
    + untemplatize_seq(SEQ_TEMPLATE_MONSTER_FALL, 8, 3, "monster", "monster_white")
    + untemplatize_seq(SEQ_TEMPLATE_MONSTER_ROT, 8, 4, "monster", "monster_white")
    + untemplatize_seq(SEQ_TEMPLATE_MONSTER_FALL, 9, 4, "monster", "monster_white")
    + untemplatize_seq(SEQ_TEMPLATE_MONSTER_FALL, 9, 5, "monster", "monster_white")
)
SEQ_STATIC_WHITE_ON_END = (((9, 6, "monster_white"),),)

DATE_START_MONSTERS = 27

SEQ_TEXT_OUCH_GREEN = (((6, 4, "text_ouch_l"),),) * 6
SEQ_TEXT_OUCH_BLUE = (((9, 5, "text_ouch_r"),),) * 6
SEQ_TEXT_OUCH_RED = (((5, 4, "text_ouch_l"),),) * 6
SEQ_TEXT_OUCH_WHITE = (((10, 6, "text_ouch_r"),),) * 6 + (((10, 6, "sky"),),)

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
        "E": "spell_eye",
        "H": "spell_heap",
        "M": "spell_monster",
        "*": "scroll_and_parchment",
        ".": None,
    }

    def __init__(self):
        self.w = 12
        self.h = 8
        self.anim_sequences = (
            AnimationSequence(SEQ_FLOWERS, 0, loop=True),
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
            AnimationSequence(SEQ_GREEN, DATE_START_MONSTERS),
            AnimationSequence(SEQ_BLUE, DATE_START_MONSTERS),
            AnimationSequence(SEQ_RED, DATE_START_MONSTERS),
            AnimationSequence(SEQ_WHITE, DATE_START_MONSTERS),
            AnimationSequence(SEQ_MAGI_SQUARE, DATE_START_LAUNCH_SPELL),
            AnimationSequence(SEQ_MAGI_STARS, DATE_START_LAUNCH_SPELL + 1),
            AnimationSequence(SEQ_MOUSE, 0),
            AnimationSequence(SEQ_TEXT_OUCH_GREEN, DATE_START_MONSTERS + 13),
            AnimationSequence(SEQ_TEXT_OUCH_BLUE, DATE_START_MONSTERS + 21),
            AnimationSequence(SEQ_TEXT_OUCH_RED, DATE_START_MONSTERS + 29),
            AnimationSequence(SEQ_TEXT_OUCH_WHITE, DATE_START_MONSTERS + 45),
            AnimationSequence(
                SEQ_STATIC_MOUSE_CURSOR_ON_END, len(SEQ_MOUSE), loop=True
            ),
            AnimationSequence(
                SEQ_STATIC_GREEN_ON_END, DATE_START_MONSTERS + len(SEQ_GREEN), loop=True
            ),
            AnimationSequence(
                SEQ_STATIC_RED_ON_END, DATE_START_MONSTERS + len(SEQ_RED), loop=True
            ),
            AnimationSequence(
                SEQ_STATIC_BLUE_ON_END, DATE_START_MONSTERS + len(SEQ_BLUE), loop=True
            ),
            AnimationSequence(
                SEQ_STATIC_WHITE_ON_END,
                DATE_START_MONSTERS + len(SEQ_WHITE),
                loop=True,
            ),
        )
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
