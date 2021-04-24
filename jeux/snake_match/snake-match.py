# https://i.postimg.cc/XJdtF6nF/snake-match-tileset.png

# Note pour plus tard : imgbb c'est de la daube comme hébergeur d'images.
# Ça, ça marche mieux. Et ça retaille pas stupidement les images sans prévenir.
# https://postimages.org/

"""
{
    "game_area": {
        "nb_tile_width": 10,
        "nb_tile_height": 15
    },
    "tile_size": 32,
    "img_coords": {
        "fruit_01": [0, 0],
        "bla": [0, 0]
    }
}
"""


class Tile:
    def __init__(self):
        self.fruit = None
        self.game_objects = ["fruit_01"]


class GameModel:
    def __init__(self):
        self.w = 10
        self.h = 15
        self.game_w = 9
        self.game_h = 13
        self.offset_interface_x = 1
        self.offset_interface_y = 2
        tiles = []
        for y in range(self.game_h):
            line = [Tile() for x in range(self.game_w)]
            line = tuple(line)
            tiles.append(line)
        self.tiles = tuple(tiles)

    def export_all_tiles(self):
        exported_tiles = []
        for y in range(self.offset_interface_y):
            # Pas d'interface pour l'instant, mais ça va venir.
            line = [[] for x in range(self.w)]
            exported_tiles.append(line)
        for y_game in range(self.game_h):
            line = []
            for x in range(self.offset_interface_x):
                line.append([])
            for x_game in range(self.game_w):
                # TODO : Faut itérer directement sur self.tiles. C'est moche ça.
                line.append(self.tiles[y_game][x_game].game_objects)
            exported_tiles.append(line)
        return exported_tiles

    def on_game_event(self, event_name):
        print("pouet")

