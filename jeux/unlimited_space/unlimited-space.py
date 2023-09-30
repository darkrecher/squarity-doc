# Ludum Dare 54 : Limited space

# Unlimited space (ha ha ha).
# https://i.ibb.co/Ltm7xtY/unlimited-space-tileset.png


"""

Générer un nombre aléatoire qui sera toujours le même pour une coordonnée fixée :

    import random

    random.seed("12345_78_50")

    print("pouet")
    print(random.randint(0, 10000))
    print(random.randint(0, 10000))

🫠

Un taxi intergalactique qui transporte des extra-terrestres.

Dans l'espace, y'a des balises de taxi, qui indiquent les coordonnées d'extra-terrestres en attente de transport.

On gagne de l'argent à chaque course. Au bout d'une certaine somme, on met un message : "bravo, vous avez amassé suffisamment d'argent, vous pouvez prendre votre retraite, ou bien continuer de transporter des gens si ça vous plaît."




  {
    "game_area": {
        "nb_tile_width": 15,
        "nb_tile_height": 15
    },
    "tile_size": 32,
    "img_coords": {
      "bg": [0, 0],
      "hero": [32, 0],

      "osef": [0, 0]
    }
  }


"""

OFFSET_FROM_DIR_STR = {
    "U": (0, -1),
    "R": (+1, 0),
    "D": (0, +1),
    "L": (-1, 0),
}

# x1, y1 (upleft), x2, y2
HERO_LIMIT_ON_SCREEN_X1 = 5
HERO_LIMIT_ON_SCREEN_Y1 = 5
HERO_LIMIT_ON_SCREEN_X2 = 9
HERO_LIMIT_ON_SCREEN_Y2 = 9


class GameModel():

    def __init__(self):
        self.w = 15
        self.h = 15
        self.tiles = [
            [
                ["bg"] for x in range(self.w)
            ]
            for y in range(self.h)
        ]
        self.hero_coord = [7, 7]
        self.corner_coord = [-7, -7]


    def get_tile(self, x, y):
        return self.tiles[y][x]


    def export_all_tiles(self):
        for y in range(self.h):
            for x in range(self.w):
                self.tiles[y][x][:] = ["bg"]

        self.get_tile(*self.hero_coord).append("hero")
        return self.tiles


    def on_game_event(self, event_name):
        print(event_name)
        offset_coord = OFFSET_FROM_DIR_STR.get(event_name)
        if offset_coord is not None:
            self.hero_coord[0] += offset_coord[0]
            self.hero_coord[1] += offset_coord[1]
        if


