# Ludum Dare 54 : Limited space

# Unlimited space (ha ha ha).
# https://raw.githubusercontent.com/darkrecher/squarity-doc/master/jeux/unlimited_space/unlimited_space_tileset.png

# https://i.ibb.co/g6LMywf/unlimited-space-tileset.png

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

emoji d'argent :  💵 💴 💶 💷 🪙 💰 💎


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
      "customer_01": [128, 0],
      "customer_02": [160, 0],
      "beacon_customers": [32, 32],

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

STR_COORDS = "🇽 🇾"
STR_HERO = "👽"
STR_DEST = "🏁"
STR_NO_INFO = "❌"

class Customer():

    def __init__(self, start_coord, dest_coord):
        self.start_coord = start_coord
        self.dest_coord = dest_coord
        if random.randint(0, 1) == 0:
            self.game_object = "customer_01"
        else:
            self.game_object = "customer_02"
        self.life_time = random.randint(1000, 10000)
        self.name = "🟩🧩"
        # possible names for customer_01 : 🎾 , 🧩 , 🦠 , 💚 , ✳️ , 🟢  , 🟩
        self.beacon_compatibility = 2 ** random.randint(1, 5)

    def get_talks_on_boarding(self):
        dest_x, dest_y = self.dest_coord
        return [
            f"  {self.name}: 🖖",
            f"  {self.name}: 🛸 ({dest_x}, {dest_y})"
        ]

    def get_talks_off_boarding(self):
        return [
            f"  {self.name}: 🫶👌",
        ]


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
        self.customer_inside = None

        self.customers = {}
        self.logged_status = False
        self.latest_customer_info = []

        self.spawn_customer(0, 20)
        self.spawn_customer(70, 200)
        for _ in range(8):
            self.spawn_customer(2000, 2000)


    def get_tile(self, x, y):
        return self.tiles[y][x]


    def compute_celestial_body(self, x, y):
        rand_seed = f"{self.game_seed}_{x}_{y}"
        random.seed(rand_seed)
        proba = random.randint(0, 1000)
        if proba < 5:
            return ["beacon_customers"]
        elif 5 <= proba < 15:
            return ["planet_01"]
        elif 15 <= proba < 105:
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


    def is_coord_ok_for_customer(self, x, y):
        # On ne place pas de client trop proche du point de départ
        # du héros, parce que ça serait trop confusionnant.
        if (-1 <= x <= 1) and (-1 <= y <= 1):
            return False
        celest_bod = self.compute_celestial_body(x, y)
        if "planet_01" not in celest_bod:
            return False
        return True


    def find_planet_around(self, x, y):
        # Bon, faut faire des carrés autour du centre, de plus en plus grand.
        # Algo poucrave, on se croirait dans un clash of code.

        for dist_corner in range(20):
            cur_y = y - dist_corner
            for cur_x in range(x-dist_corner, x + dist_corner + 1):
                if self.is_coord_ok_for_customer(cur_x, cur_y):
                    return cur_x, cur_y
            cur_y = y + dist_corner
            for cur_x in range(x-dist_corner, x + dist_corner + 1):
                if self.is_coord_ok_for_customer(cur_x, cur_y):
                    return cur_x, cur_y

            cur_x = x - dist_corner
            for cur_y in range(y-dist_corner + 1, y + dist_corner):
                if self.is_coord_ok_for_customer(cur_x, cur_y):
                    return cur_x, cur_y
            cur_x = x + dist_corner
            for cur_y in range(y-dist_corner + 1, y + dist_corner):
                if self.is_coord_ok_for_customer(cur_x, cur_y):
                    return cur_x, cur_y

        return None


    def spawn_customer(self, start_dist, dest_dist):
        start_x = random.randint(-start_dist, +start_dist)
        start_y = random.randint(-start_dist, +start_dist)
        start_coord = self.find_planet_around(start_x, start_y)
        if start_coord is None:
            return None
        dest_x = random.randint(-dest_dist, +dest_dist)
        dest_y = random.randint(-dest_dist, +dest_dist)
        dest_coord = self.find_planet_around(dest_x, dest_y)
        if dest_coord is None:
            return None
        if start_coord == dest_coord:
            print("pas de bol.")
            return None

        new_customer = Customer(start_coord, dest_coord)
        self.customers[start_coord] = new_customer
        return new_customer


    def export_all_tiles(self):

        for y in range(self.h):
            for x in range(self.w):
                x_univ = self.corner_coord[0] + x
                y_univ = self.corner_coord[1] + y
                tile_current = self.get_tile(x, y)
                tile_current[:] = self.compute_celestial_body_memoized(x_univ, y_univ)
                customer = self.customers.get((x_univ, y_univ))
                if customer is not None:
                    tile_current.append(customer.game_object)

        if len(self.buffer_celestial_bodies) > BUFFER_SIZE_CELEST_BODIES:
            self.buffer_celestial_bodies = self.buffer_celestial_bodies[BUFFER_SIZE_CELEST_BODIES:]

        tile_hero = self.get_tile(*self.hero_coord)
        if self.customer_inside is not None:
            tile_hero.append(self.customer_inside.game_object)
        tile_hero.append("hero")

        return self.tiles


    def log_status(self):
        print()
        print()
        if self.customer_inside is not None:
            print()
            print()
            dest_x, dest_y = self.customer_inside.dest_coord
            print(f"  {STR_DEST} {STR_COORDS}: ({dest_x}, {dest_y})")
        else:
            # TODO : il faut éliminer de ce log
            # les clients qu'on a déjà transportés.
            for log_customer in self.latest_customer_info:
                print(log_customer)

        hero_univ_x = self.hero_coord[0] + self.corner_coord[0]
        hero_univ_y = self.hero_coord[1] + self.corner_coord[1]
        print(f"  {STR_HERO} {STR_COORDS}: ({hero_univ_x}, {hero_univ_y})", end="")


    def compute_customer_info(self, beacon_coord):
        beacon_compatibility = (beacon_coord[0] + 3 * beacon_coord[1]) % 64
        customers_to_reveal = []
        for customer in self.customers.values():
            if customer.beacon_compatibility & beacon_compatibility:
                customers_to_reveal.append(customer)
        customers_to_reveal = customers_to_reveal[:2]

        logs = []
        for customer in customers_to_reveal:
            cust_x, cust_y = customer.start_coord
            logs.append(f"  {customer.name} {STR_COORDS}: ({cust_x}, {cust_y})")

        if not logs:
            logs.append(STR_NO_INFO)
        return logs


    def on_game_event(self, event_name):
        offset_coord = OFFSET_FROM_DIR_STR.get(event_name)
        if offset_coord is not None:
            self.logged_status = False
            self.hero_coord[0] += offset_coord[0]
            self.hero_coord[1] += offset_coord[1]

            if self.hero_coord[0] < HERO_LIMIT_ON_SCREEN_X1:
                self.hero_coord[0] = HERO_LIMIT_ON_SCREEN_X1
                self.corner_coord[0] -= 1
            if self.hero_coord[1] < HERO_LIMIT_ON_SCREEN_Y1:
                self.hero_coord[1] = HERO_LIMIT_ON_SCREEN_Y1
                self.corner_coord[1] -= 1
            if self.hero_coord[0] > HERO_LIMIT_ON_SCREEN_X2:
                self.hero_coord[0] = HERO_LIMIT_ON_SCREEN_X2
                self.corner_coord[0] += 1
            if self.hero_coord[1] > HERO_LIMIT_ON_SCREEN_Y2:
                self.hero_coord[1] = HERO_LIMIT_ON_SCREEN_Y2
                self.corner_coord[1] += 1

            hero_univ_x = self.hero_coord[0] + self.corner_coord[0]
            hero_univ_y = self.hero_coord[1] + self.corner_coord[1]
            hero_univ_coord = (hero_univ_x, hero_univ_y)
            customer_on_hero = self.customers.get(hero_univ_coord)

            if self.customer_inside is None and customer_on_hero is not None:
                self.customer_inside = customer_on_hero
                del self.customers[hero_univ_coord]
                print()
                print()
                for log in self.customer_inside.get_talks_on_boarding():
                    print(log)

            if "beacon_customers" in self.compute_celestial_body_memoized(hero_univ_x, hero_univ_y):
                logs = self.compute_customer_info(hero_univ_coord)
                self.latest_customer_info = logs
                print()
                print()
                for log_line in logs:
                    print(log_line)

            if self.customer_inside is not None and self.customer_inside.dest_coord == hero_univ_coord:
                print()
                print()
                for log in self.customer_inside.get_talks_off_boarding():
                    print(log)
                # TODO : afficher le customer sur la planète
                # durant une durée limitée de tour.
                # TODO : gérer l'argent. Le customer paye le héros.
                self.customer_inside = None

        else:
            # Bouton d'action 1 ou 2. Ça logge le status.
            if not self.logged_status:
                self.log_status()
                self.logged_status = True









