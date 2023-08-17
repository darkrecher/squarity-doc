

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
        "whatever": [0, 0]
    }
}
"""

INIT_TILES = [
    [
        ["epiderm_top"],["epiderm_top"],["epiderm_top"],["epiderm_top"],["epiderm_top"],
        ["epiderm_top"],["epiderm_top"],["epiderm_top"],["epiderm_top"],["epiderm_top"],
        ["epiderm_top"],["epiderm_top"],["epiderm_top"],["epiderm_top"],["epiderm_top"],
    ],
    [
        ["epiderm_vi_up_1"], ["epiderm_vi_up_diag_down_1"], ["epiderm_vi_down_1"], ["epiderm_vi_down_1"], ["epiderm_vi_up_diag_up_1"],
        ["epiderm_vi_up_1"], ["epiderm_vi_up_1"], ["epiderm_vi_up_diag_down_1"], ["epiderm_vi_down_1"], ["epiderm_vi_up_diag_up_1"],
        ["epiderm_vi_up_1"], ["epiderm_vi_up_1"], ["epiderm_vi_up_1"], ["epiderm_vi_up_1"], ["epiderm_vi_up_1"],
    ],
    [
        [], ["epiderm_vi_up_diag_down_2"], ["epiderm_vi_down_2"], ["epiderm_vi_down_2"], ["epiderm_vi_up_diag_up_2"],
        [], [], ["epiderm_vi_up_diag_down_2"], ["epiderm_vi_down_2"], ["epiderm_vi_up_diag_up_2"],
        [], [], [], [], [],
    ],
    [
        [], [], [], [], [],
        [], [], [], [], [],
        [], [], [], [], [],
    ],
    [
        [], [], [], [], [],
        [], [], [], [], [],
        [], [], [], [], [],
    ],
    [
        [], [], [], [], [],
        [], [], [], [], [],
        [], [], [], [], [],
    ],
    [
        [], [], [], [], [],
        [], [], [], [], [],
        [], [], [], [], [],
    ],
    [
        [], [], [], [], [],
        [], [], [], [], [],
        [], [], [], [], [],
    ],
    [
        [], [], [], [], [],
        [], [], [], [], [],
        [], [], [], [], [],
    ],
    [
        [], [], [], [], [],
        [], [], [], [], [],
        [], [], [], [], [],
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
        for y in range(self.h):
            for x in range(self.w):
                self.tiles[y][x] = ["background"] + INIT_TILES[y][x]

        print(self.tiles)
        print("coucou !")


    def export_all_tiles(self):
        return self.tiles


    def on_game_event(self, event_name):
        return None
