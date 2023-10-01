# Ludum Dare 54 : Limited space

# Unlimited space (ha ha ha).
# https://raw.githubusercontent.com/darkrecher/squarity-doc/master/jeux/unlimited_space/unlimited_space_tileset.png

# https://i.ibb.co/J324DDM/unlimited-space-tileset.png

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
🟤 ⚪ 🟡 🪙 💵 💶 💷 💴 💰 💎 🏆 👑


👛 💼


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
      "beacon_customers": [32, 96],

      "osef": [0, 0]
    }
  }




http://squarity.fr/#fetchez_githubgist_darkrecher/099fdc3c77980e90b3c89d2e26cde792/raw/unlimited-space.txt


Pour jouer à la version actuelle du jeu "Unlimited Space" :

http://squarity.fr/#fetchez_githubgist_darkrecher/099fdc3c77980e90b3c89d2e26cde792/raw/unlimited-space.txt


https://ldj.am/$377455


https://www.twitch.tv/recher_squarity


archétypes d'extra-terrestres :

## emoji générique
  destination : 🛸
  argent : STR_WALLET

## L'extra-terrestre vert :

money : entre 10 et 50
point de départ et d'arrivée : centré sur (0, 0). amplitude 50.
bonjour : 👋😃
au revoir : 👋😃 🫶
nom : deux au choix parmi :  🧩 💚 ✳️ 🟢 🟩 🍏 📗 ❎ ❇️
conversation :
  entre 3 et 8 parmi :
    🎾 🧩 🦠 💚 ✳️ 🟢 🟩 🏕️ 🏜️ 🛣️ 🛤️ 🚀 🌍 🌎 🌏 🛞 😀 😃 😄 😁 😆 😅 🤣 😂 🙂 😉 😊 😇 🥰 😍 😋 😛 😜 🤪 😝 🗣️ 👤 👥 🧟 🧟‍♂️ 💐 🌹 🥀 🌻 🌱 🪴 🌲 🌳 🌴 🌵 🌾 🌿 🍀 🍃 🐸 🐢 🐍 🦕 🌞 🪐 🌟 🌠 🌌 🍈 🍏 🍐 🫒 🥑 🫑 🥒 🥬 🥦 🫛 📗 🈯 ❇️
  entre 2 et 4 lignes de conversation, c'est lui qui commence ou c'est le héro.

## Un robot (faudra refaire son apparence)

money : entre 40 et 120
point de départ : centré sur (-30, -30). amplitude 40
point d'arrivée : centrée sur (10, 10). amplitude 40.
bonjour : ☎️
au revoir : ☎️
nom : d'abord 🤖 , puis un parmi :#️⃣ *️⃣ 0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ 🔟 🔢 🔣
conversation :
  entre 2 et 5 parmi :
    📱 📞 🦾 🦿 ☄️ 🪐 🍴 🥄 🔪 🫙 🎮 🕹️ 🎰 🚀 🛵 🦽 🦼 🛺 🚲 🛴 🛢️ ⛽ 💺 🎙️ 🎚️ 🎛️ 🎤 🎧 📻 🔈 🔊 📢 📟 📠 🔋 🪫 🔌 💻 🖥️ 🖨️ 🖱️ 🖲️ 💽 💾 💿 📀 📺 📷 📹 📼 📎 🖇️ ✂️ 🗑️ 🔨 🪓 ⛏️ ⚒️ 🛠️ 🪚 🔧 🪛 🔩 ⚙️ 🗜️ ⛓️ 🪝 🧲 🔭 🧷 🧯 🛒
  2 lignes de conversation à chaque fois.

## un poulpe volant

amplitude 300
paye pas très bien

## le personnage jaune

amplitude 700, mais trajet très court.
paye très bien. ne parle que d'argent.

👌

## un cristal bleu

parle très mal. paye pas beaucoup.
trajet assez long. au moins 400.
ne donne pas la somme qu'il paye avant qu'on l'embarque.

Je sais vraiment pas si j'aurais le temps de faire tout ça.


Archetype :
 - apparence (nom de game object)
 - nom du personnage (une string)
 - conversation (fonctions : bonjour, on-boarding, au revoir, blabla. faut que ce soit une sous-classe)
 - money (nombre)
 - point de départ et d'arrivée (2 coords)

On peut tout prendre du même archetype, ou bien piocher des trucs différents.

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
STR_SELECT_BEG = ""
STR_SELECT_END = "  ◀️"
STR_WALLET = "💼"

STR_MONEY_FROM_VALUE = (
    (0, "🕸️"),
    (1, "🟤"),
    (2, "⚪"),
    (5, "🟡"),
    (8, "🪙"),
    (10, "💵"),
    (20, "💶"),
    (50, "💷"),
    (80, "💴"),
    (100, "💰"),
    (200, "💎"),
    (500, "🏆"),
    (800, "👑"),
)

class Conversationer():

    def __init__(self, customer):
        self.customer = customer

    def get_hello_str(self, hero_coord):
        """
        Renvoie None ou une string.
        Les trucs que dit le client avant qu'on l'embarque.
        Il y a plus de chance de parler si le héro est proche.
        """
        raise NotImplemented

    def get_on_board_str(self):
        """
        Renvoie une string.
        Ce que dit le client au moment où on l'embarque.
        (au minimum : les coordonnées de destination)
        """
        raise NotImplemented

    def get_goodbye_str(self):
        """
        Renvoie None ou une string.
        Les trucs que dit le client quand on le dépose.
        """
        raise NotImplemented

    def get_speak_while_traveling(self):
        """
        Renvoie None, ou un tuple (string, id).
        L'id indique qui a parlé : 0: le client. 1: le héro
        """
        raise NotImplemented


class Customer():

    def __init__(self, start_coord, dest_coord):
        self.start_coord = start_coord
        self.dest_coord = dest_coord
        self.money = random.randint(10, 100)
        if random.randint(0, 1) == 0:
            self.game_object = "customer_01"
        else:
            self.game_object = "customer_02"
        self.life_time = None
        self.name = "🟩🧩"
        self.beacon_compatibility = 2 ** random.randint(1, 5)
        self.arrived = False

    def put_to_destination(self):
        self.arrived = True
        self.start_coord = self.dest_coord
        self.dest_coord = None
        self.money = 0
        self.life_time = random.randint(20, 200)

    def get_talks_on_boarding(self):
        dest_x, dest_y = self.dest_coord
        return [
            f"  {self.name}: \"🖖\"",
            f"  {self.name}: \"🛸 ({dest_x}, {dest_y})\""
        ]

    def get_talks_off_boarding(self):
        return [
            f"  {self.name}: \"🫶👌\"",
        ]

    def get_log_line_start(self, selected=False):
        x, y = self.start_coord
        log_line = f"  {self.name} {STR_COORDS}: ({x}, {y})"
        if selected:
            log_line = STR_SELECT_BEG + log_line + STR_SELECT_END
        return log_line


class CustomerList():

    def __init__(self):
        # liste de tuple de 3 elem :
        # distance par rapport au point (0, 0)
        # boolean : selected ou pas.
        # référence vers un objet Customer.
        self.customers = []

    def _get_index_selected(self):
        for index, cust_info in enumerate(self.customers):
            if cust_info[1]:
                return index
        return None

    def get_selected_customer(self):
        for dist_orig, selected, cust in self.customers:
            if selected:
                return cust
        return None

    def add_customer(self, customer):

        for cust_info in self.customers:
            if cust_info[2] == customer:
                # On connait déjà ce client, on le rajoute pas.
                return

        cust_x, cust_y = customer.start_coord
        dist_orig = cust_x**2 + cust_y**2
        if not self.customers:
            self.customers.append([dist_orig, True, customer])
        else:
            self.customers.append([dist_orig, False, customer])
            self.customers.sort(key=lambda x:x[0])

    def remove_customer(self, customer_to_remove):
        prev_index_selected = self._get_index_selected()
        self.customers = [
            cust_info for cust_info in self.customers
            if cust_info[2] != customer_to_remove
        ]
        cur_index_selected = self._get_index_selected()
        if prev_index_selected is not None and cur_index_selected is None:
            if prev_index_selected >= len(self.customers):
                prev_index_selected = len(self.customers)-1
            self.customers[prev_index_selected][1] = True

    def cycle_selection(self):
        index_selected = self._get_index_selected()
        if index_selected is not None:
            self.customers[index_selected][1] = False
            index_selected = (index_selected + 1) % len(self.customers)
            self.customers[index_selected][1] = True

    def get_customer_list_info(self):
        """
        Renvoie un log de la liste, avec le customer sélectionné en dernier,
        puis les précédents, puis on fait le tour pour afficher l'autre partie de la liste.
        """
        index_selected = self._get_index_selected()
        if index_selected is not None:
            reordered_customers = self.customers[index_selected:] + self.customers[:index_selected]
            reordered_customers = reordered_customers[::-1]
            logs = []
            for cust_info in reordered_customers:
                dist_orig, sel, cust = cust_info
                logs.append(cust.get_log_line_start(sel))
            return logs
        else:
            # On va rien logger si on a des customers alors
            # qu'aucun d'eux n'a été sélectionné.
            # Mais c'est pas censé arriver.
            return ["  " + STR_NO_INFO]


class GameModel():

    def __init__(self):
        self.w = 15
        self.h = 15
        self.game_seed = str(random.randint(0, 1000000000))
        self.tiles = [
            [
                [] for x in range(self.w)
            ]
            for y in range(self.h)
        ]
        self.hero_coord = [7, 7]
        self.corner_coord = [-7, -7]
        self.money = 0
        self.buffer_celestial_bodies = []
        self.customer_inside = None

        self.customers = {}
        self.prev_action = None
        self.customer_list = CustomerList()

        self.spawn_customer(0, 20)
        for _ in range(4):
            self.spawn_customer(70, 200)
        for _ in range(5):
            self.spawn_customer(2000, 2000)

        self.spawn_timer = 10000


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
        print("\n" * 3)

        log_money = "  " + STR_WALLET + ": "
        if not self.money:
            log_money += STR_MONEY_FROM_VALUE[0][1]
        else:
            temp_money = self.money
            for value, str_val in STR_MONEY_FROM_VALUE[:0:-1]:
                while temp_money >= value:
                    temp_money -= value
                    log_money += str_val + " "
        print(log_money)

        hero_univ_x = self.hero_coord[0] + self.corner_coord[0]
        hero_univ_y = self.hero_coord[1] + self.corner_coord[1]
        print(f"  {STR_HERO} {STR_COORDS}: ({hero_univ_x}, {hero_univ_y})")

        if self.customer_inside is not None:
            dest_x, dest_y = self.customer_inside.dest_coord
            print(f"  {STR_DEST} {STR_COORDS}: ({dest_x}, {dest_y})", end="")
        else:
            selected_cust = self.customer_list.get_selected_customer()
            if selected_cust != None:
                print(selected_cust.get_log_line_start(True), end="")

    def add_customers_from_beacon(self, beacon_coord):
        beacon_compatibility = (beacon_coord[0] + 3 * beacon_coord[1]) % 64
        customers_to_reveal = []
        for customer in self.customers.values():
            if customer.beacon_compatibility & beacon_compatibility:
                customers_to_reveal.append(customer)
        customers_to_reveal = customers_to_reveal[:2]

        print("\n")
        if not customers_to_reveal:
            print("  " + STR_NO_INFO)
        else:
            for customer in customers_to_reveal:
                self.customer_list.add_customer(customer)
                print(customer.get_log_line_start())


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

            if self.customer_inside is None and customer_on_hero is not None and not customer_on_hero.arrived:
                self.customer_inside = customer_on_hero
                del self.customers[hero_univ_coord]
                self.customer_list.remove_customer(customer_on_hero)
                print()
                print()
                for log in self.customer_inside.get_talks_on_boarding():
                    print(log)

            if "beacon_customers" in self.compute_celestial_body_memoized(hero_univ_x, hero_univ_y):
                self.add_customers_from_beacon(hero_univ_coord)

            if self.customer_inside is not None and self.customer_inside.dest_coord == hero_univ_coord:
                print("\n")
                for log in self.customer_inside.get_talks_off_boarding():
                    print(log)
                self.money += self.customer_inside.money
                # On affiche le customer sur la planète,
                # durant une durée limitée de tour.
                self.customer_inside.put_to_destination()
                cust_coord = self.customer_inside.start_coord
                self.customers[cust_coord] = self.customer_inside

                self.customer_inside = None

        elif event_name == "action_1":
            if self.prev_action != event_name:
                self.log_status()

        elif event_name == "action_2":
            self.customer_list.cycle_selection()
            print("\n")
            for log_line in self.customer_list.get_customer_list_info():
                print(log_line)

        cust_coord_to_del = None
        for coord, customer in self.customers.items():
            if customer.life_time is not None:
                customer.life_time -= 1
                if customer.life_time < 0:
                    cust_coord_to_del = coord
        if cust_coord_to_del is not None:
            del self.customers[cust_coord_to_del]

        if not self.customers:
            self.spawn_timer = 0
        else:
            self.spawn_timer -= (12-len(self.customers)) ** 2

        if self.spawn_timer <= 0:
            self.spawn_customer(2000, 2000)
            self.spawn_timer += 10000


        self.prev_action = event_name


