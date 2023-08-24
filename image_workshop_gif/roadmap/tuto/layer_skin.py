

# https://raw.githubusercontent.com/darkrecher/squarity-doc/master/image_workshop_gif/roadmap/tuto/skin_tileset.png

"""
{
    "game_area": {
        "nb_tile_width": 15,
        "nb_tile_height": 10
    },
    "tile_size": 32,
    "img_coords": {
        "background": [0, 64],
        "epiderm_top": [0, 0],
        "epiderm_vi_up_1": [0, 32],
        "epiderm_vi_up_diag_down_1": [32, 32],
        "epiderm_vi_up_diag_down_2": [32, 64],
        "epiderm_vi_down_1": [64, 32],
        "epiderm_vi_down_2": [64, 64],
        "epiderm_vi_up_diag_up_1": [96, 32],
        "epiderm_vi_up_diag_up_2": [96, 64],
        "epiderm_vi_up_2": [128, 32],

        "hair_1": [160,0],
        "hair_2": [160,32],
        "hair_3": [160,64],
        "hair_4": [160,96],
        "hair_5": [160,128],
        "hair_6": [160,160],

        "sk_b_1_1": [0,160],
        "sk_b_2_1": [32,160],
        "sk_b_1_2": [0,192],
        "sk_b_2_2": [32,192],
        "sk_b_r_1_1": [64,160],
        "sk_b_r_2_1": [96,160],
        "sk_b_r_1_2": [64,192],
        "sk_b_r_2_2": [96,192],

        "red_ves_big_1": [0,128],
        "red_ves_big_2": [32,128],
        "red_ves_big_3": [64,128],
        "red_ves_big_4": [96,128],
        "red_ves_big_5": [128,128],

        "red_ves_lit_1": [224,96],
        "red_ves_lit_2": [224,128],
        "red_ves_lit_3": [224,160],

        "blu_ves_big_1": [0,96],
        "blu_ves_big_2": [32,96],
        "blu_ves_big_3": [64,96],
        "blu_ves_big_4": [96,96],
        "blu_ves_big_5": [128,96],

        "blu_ves_lit_1": [224,0],
        "blu_ves_lit_2": [224,32],
        "blu_ves_lit_3": [224,64],

        "bulb_1": [192,10],
        "bulb_2": [192,42],
        "bulb_3": [192,74],
        "bulb_4": [192,106],
        "bulb_5": [192,138],

        "melanocyte": [160,192],

        "whatever": [0, 0]
    }
}
"""

INIT_TILES = [
    [
        [], ["hair_1"], [], [], [],
        ["hair_1"], [], [], [], ["hair_1"],
        [], [], ["hair_1"], [], [],
    ],
    [
        [], ["hair_2"], [], [], [],
        ["hair_2"], [], [], [], ["hair_2"],
        [], [], ["hair_2"], [], [],
    ],
    [
        ["epiderm_top"],["epiderm_top"],["epiderm_top"],["epiderm_top"],["epiderm_top"],
        ["epiderm_top", "hair_3"],["epiderm_top"],["epiderm_top"],["epiderm_top", "bulb_1"],["epiderm_top"],
        ["epiderm_top"],["epiderm_top"],["epiderm_top", "hair_3"],["epiderm_top"],["epiderm_top"],
    ],
    [
        ["epiderm_vi_up_1"], ["epiderm_vi_up_diag_down_1"], ["epiderm_vi_down_1"], ["epiderm_vi_down_1"], ["epiderm_vi_up_diag_up_1"],
        ["epiderm_vi_up_1", "hair_4"], ["epiderm_vi_up_1"], ["epiderm_vi_up_diag_down_1"], ["epiderm_vi_down_1", "bulb_2"], ["epiderm_vi_up_diag_up_1"],
        ["epiderm_vi_up_1", "melanocyte"], ["epiderm_vi_up_1"], ["epiderm_vi_up_1", "hair_4"], ["epiderm_vi_up_1", "melanocyte"], ["epiderm_vi_up_diag_down_1"],
    ],
    [
        [], ["epiderm_vi_up_diag_down_2"], ["epiderm_vi_down_2", "melanocyte"], ["epiderm_vi_down_2"], ["epiderm_vi_up_diag_up_2"],
        ["hair_5"], [], ["epiderm_vi_up_diag_down_2"], ["epiderm_vi_down_2", "bulb_3"], ["epiderm_vi_up_diag_up_2"],
        [], [], ["hair_5"], [], ["epiderm_vi_up_diag_down_2"],
    ],
    [
        [], [], [], ["red_ves_lit_1"], [],
        ["hair_6"], [], [], ["bulb_4"], [],
        [], ["blu_ves_lit_1"], ["hair_6"], [], [],
    ],
    [
        [], [], [], ["red_ves_lit_2"], [],
        [], [], [], ["bulb_5"], [],
        [], ["blu_ves_lit_2"], [], [], [],
    ],
    [
        [], ["red_ves_big_1"], ["red_ves_big_2"], ["red_ves_big_3", "red_ves_lit_3"], ["red_ves_big_4"],
        ["red_ves_big_5"], [], [], [], ["blu_ves_big_1"],
        ["blu_ves_big_2"], ["blu_ves_big_3", "blu_ves_lit_3"], ["blu_ves_big_4"], ["blu_ves_big_5"], [],
    ],
    [
        ["sk_b_1_1"], ["sk_b_2_1"], ["sk_b_1_1"], ["sk_b_2_1"], ["sk_b_r_1_1"],
        ["sk_b_r_2_1"], ["sk_b_1_1"], ["sk_b_2_1"], ["sk_b_r_1_1"], ["sk_b_r_2_1"],
        ["sk_b_r_1_1"], ["sk_b_r_2_1"], ["sk_b_1_1"], ["sk_b_2_1"], ["sk_b_1_1"],
    ],
    [
        ["sk_b_1_2"], ["sk_b_2_2"], ["sk_b_1_2"], ["sk_b_2_2"], ["sk_b_r_1_2"],
        ["sk_b_r_2_2"], ["sk_b_1_2"], ["sk_b_2_2"], ["sk_b_r_1_2"], ["sk_b_r_2_2"],
        ["sk_b_r_1_2"], ["sk_b_r_2_2"], ["sk_b_1_2"], ["sk_b_2_2"], ["sk_b_1_2"],
    ],
]

class GameModel():

    def __init__(self):
        self.w = 15
        self.h = 10
        self.tiles = [
            [
                [] for x in range(self.w)
            ]
            for y in range(self.h)
        ]
        has_background = False
        for y in range(self.h):
            if y == 2:
                has_background = True
            for x in range(self.w):
                self.tiles[y][x] = ["background"]*has_background + INIT_TILES[y][x]

        print(self.tiles)
        print("coucou !")


    def export_all_tiles(self):
        return self.tiles


    def on_game_event(self, event_name):
        return None
