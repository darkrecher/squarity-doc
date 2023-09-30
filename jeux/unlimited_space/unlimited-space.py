# Ludum Dare 54 : Limited space

# Unlimited space (ha ha ha).
# https://raw.githubusercontent.com/darkrecher/squarity-doc/master/jeux/unlimited_space/unlimited_space_tileset.png

# Lien vers le code actuel du jeu :
# https://github.com/darkrecher/squarity-doc/blob/master/jeux/unlimited_space/unlimited-space.py


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

 - dessiner 2 extra-terrestres et une balise spatiale
 - générer les positions de 10 extra-terrestres (avec des noms en emoji).
 - une balise indique, au hasard, entre 2 et 4 extra-terrestres parmi les 10.
 - gérer la récupération et le dépôt d'un extra-terrestre.




  {
    "game_area": {
        "nb_tile_width": 15,
        "nb_tile_height": 15
    },
    "tile_size": 32,
    "img_coords": {
      "bg": [0, 0],
      "hero": [32, 0],
      "scenery_01": [64, 0],
      "planet_01": [96, 0],

      "osef": [0, 0]
    }
  }


"""

import random

OFFSET_FROM_DIR_STR = {
    "U": (0, -1),
    "R": (+1, 0),
    "D": (0, +1),
    "L": (-1, 0),
}

HERO_LIMIT_ON_SCREEN_X1 = 5
HERO_LIMIT_ON_SCREEN_Y1 = 5
HERO_LIMIT_ON_SCREEN_X2 = 9
HERO_LIMIT_ON_SCREEN_Y2 = 9
BUFFER_SIZE_CELEST_BODIES = 250

class GameModel():

    def __init__(self):
        self.w = 15
        self.h = 15
        self.game_seed = str(random.randint(0, 1000000000))
        print("seed :", self.game_seed)
        self.tiles = [
            [
                [] for x in range(self.w)
            ]
            for y in range(self.h)
        ]
        self.hero_coord = [7, 7]
        self.corner_coord = [-7, -7]
        self.buffer_celestial_bodies = []


    def get_tile(self, x, y):
        return self.tiles[y][x]


    def compute_celestial_body(self, x, y):
        rand_seed = f"{self.game_seed}_{x}_{y}"
        random.seed(rand_seed)
        proba = random.randint(0, 1000)
        if proba < 5:
            return ["planet_01"]
        elif 5 <= proba < 90:
            return ["scenery_01"]
        else:
            return ["bg"]


    def compute_celestial_body_memoized(self, x, y):
        for buf_x, buf_y, celest_bod in self.buffer_celestial_bodies:
            if (buf_x, buf_y) == (x, y):
                return celest_bod
        celest_bod = self.compute_celestial_body(x, y)
        self.buffer_celestial_bodies.append((x, y, celest_bod))
        return celest_bod


    def export_all_tiles(self):
        for y in range(self.h):
            for x in range(self.w):
                x_univ = self.corner_coord[0] + x
                y_univ = self.corner_coord[1] + y
                self.tiles[y][x][:] = self.compute_celestial_body_memoized(x_univ, y_univ)
        if len(self.buffer_celestial_bodies) > BUFFER_SIZE_CELEST_BODIES:
            self.buffer_celestial_bodies = self.buffer_celestial_bodies[BUFFER_SIZE_CELEST_BODIES:]

        self.get_tile(*self.hero_coord).append("hero")
        return self.tiles


    def on_game_event(self, event_name):
        offset_coord = OFFSET_FROM_DIR_STR.get(event_name)
        if offset_coord is not None:
            self.hero_coord[0] += offset_coord[0]
            self.hero_coord[1] += offset_coord[1]
            moved_corner = False

            if self.hero_coord[0] < HERO_LIMIT_ON_SCREEN_X1:
                self.hero_coord[0] = HERO_LIMIT_ON_SCREEN_X1
                self.corner_coord[0] -= 1
                moved_corner = True
            if self.hero_coord[1] < HERO_LIMIT_ON_SCREEN_Y1:
                self.hero_coord[1] = HERO_LIMIT_ON_SCREEN_Y1
                self.corner_coord[1] -= 1
                moved_corner = True
            if self.hero_coord[0] > HERO_LIMIT_ON_SCREEN_X2:
                self.hero_coord[0] = HERO_LIMIT_ON_SCREEN_X2
                self.corner_coord[0] += 1
                moved_corner = True
            if self.hero_coord[1] > HERO_LIMIT_ON_SCREEN_Y2:
                self.hero_coord[1] = HERO_LIMIT_ON_SCREEN_Y2
                self.corner_coord[1] += 1
                moved_corner = True

            if moved_corner:
                pass

            hero_univ_x = self.hero_coord[0] + self.corner_coord[0]
            hero_univ_y = self.hero_coord[1] + self.corner_coord[1]
            if "planet_01" in self.compute_celestial_body_memoized(hero_univ_x, hero_univ_y):
                print("🪐 !!")



