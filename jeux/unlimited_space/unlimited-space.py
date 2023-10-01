# Ludum Dare 54 : Limited space

# Unlimited space (ha ha ha).
# https://raw.githubusercontent.com/darkrecher/squarity-doc/master/jeux/unlimited_space/unlimited_space_tileset.png

# https://i.ibb.co/LrBT7LP/unlimited-space-tileset.png

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
        "nb_tile_width": 11,
        "nb_tile_height": 11
    },
    "tile_size": 32,
    "img_coords": {
      "bg": [0, 0],
      "hero": [32, 0],
      "scenery_01": [64, 0],
      "planet_01": [96, 0],
      "customer_green": [128, 0],
      "customer_rich": [160, 0],
      "customer_robot": [160, 32],
      "beacon_customers": [32, 96],
      "speak_bubble_left": [128, 32],
      "speak_bubble_right": [96, 32],

      "win_0_0": [96, 96],
      "win_1_0": [128, 96],
      "win_2_0": [160, 96],
      "win_0_1": [96, 128],
      "win_1_1": [128, 128],
      "win_2_1": [160, 128],
      "win_0_2": [96, 160],
      "win_1_2": [128, 160],
      "win_2_2": [160, 160],

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

HERO_LIMIT_ON_SCREEN_X1 = 3
HERO_LIMIT_ON_SCREEN_Y1 = 3
HERO_LIMIT_ON_SCREEN_X2 = 7
HERO_LIMIT_ON_SCREEN_Y2 = 7
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

LIFE_TIME_SPEAK_BUBBLE = 5


# C'est dégueux d'initialiser ça ici, mais j'ai pas le temps.
global_game_seed = str(random.randint(0, 1000000000))

class CelestialObjGen():
    """
    Générateur d'object céleste.
    Que des fonctions statiques.
    """
    def compute_celestial_body(x, y):
        rand_seed = f"{global_game_seed}_{x}_{y}"
        random.seed(rand_seed)
        proba = random.randint(0, 1000)
        if proba < 9:
            return ["beacon_customers"]
        elif 9 <= proba < 19:
            return ["planet_01"]
        elif 19 <= proba < 109:
            return ["scenery_01"]
        else:
            return ["bg"]


    def is_coord_ok_for_customer(x, y):
        # On ne place pas de client trop proche du point de départ
        # du héros, parce que ça serait trop confusionnant.
        if (-1 <= x <= 1) and (-1 <= y <= 1):
            return False
        celest_bod = CelestialObjGen.compute_celestial_body(x, y)
        if "planet_01" not in celest_bod:
            return False
        return True


    def find_planet_around(x, y):
        # Bon, faut faire des carrés autour du centre, de plus en plus grand.
        # Algo poucrave, on se croirait dans un clash of code.

        for dist_corner in range(20):
            cur_y = y - dist_corner
            for cur_x in range(x-dist_corner, x + dist_corner + 1):
                if CelestialObjGen.is_coord_ok_for_customer(cur_x, cur_y):
                    return cur_x, cur_y
            cur_y = y + dist_corner
            for cur_x in range(x-dist_corner, x + dist_corner + 1):
                if CelestialObjGen.is_coord_ok_for_customer(cur_x, cur_y):
                    return cur_x, cur_y

            cur_x = x - dist_corner
            for cur_y in range(y-dist_corner + 1, y + dist_corner):
                if CelestialObjGen.is_coord_ok_for_customer(cur_x, cur_y):
                    return cur_x, cur_y
            cur_x = x + dist_corner
            for cur_y in range(y-dist_corner + 1, y + dist_corner):
                if CelestialObjGen.is_coord_ok_for_customer(cur_x, cur_y):
                    return cur_x, cur_y

        return None

def get_money_str(money):
    if not money:
        return STR_MONEY_FROM_VALUE[0][1]

    money_str = ""
    for value, str_val in STR_MONEY_FROM_VALUE[:0:-1]:
        while money >= value:
            money -= value
            money_str += str_val + " "
    return money_str

class Conversationer():

    def __init__(self):
        self.customer = None

    def set_customer(self, customer):
        self.customer = customer

    def compute_dist_from_hero(self, hero_univ_coord):
        d_x = abs(self.customer.start_coord[0] - hero_univ_coord[0])
        d_y = abs(self.customer.start_coord[1] - hero_univ_coord[1])
        return d_x + d_y

    def get_hello_str(self, hero_univ_coord):
        """
        Renvoie une liste de string.
        Les trucs que dit le client avant qu'on l'embarque.
        Il y a plus de chance de parler si le héro est proche.
        """
        raise NotImplemented

    def get_on_board_str(self):
        """
        Renvoie une liste de string.
        Ce que dit le client au moment où on l'embarque.
        """
        raise NotImplemented

    def get_goodbye_str(self):
        """
        Renvoie une liste de string.
        Les trucs que dit le client quand on le dépose.
        """
        raise NotImplemented

    def get_speak_while_traveling(self):
        """
        Renvoie None, ou un tuple (string, id).
        L'id indique qui a parlé : 0: le client. 1: le héro.
        Une seule string à chaque fois.
        """
        raise NotImplemented


class Archetype():

    def __init__(self):
        self.gamobj_appearance = "customer_xx"
        self.conversationer = None
        self.money = 0
        self.name = ""
        self.start_coord = (3, 0)
        self.dest_coord = (4, 0)
        self.is_coord_valid = True

class ConversationerSympatheticGreenAlien(Conversationer):

    def __init__(self):
        self.said_hello = False
        self.words = "🎾 🧩 🦠 💚 ✳️ 🟢 🟩 🏕️ 🏜️ 🛣️ 🛤️ 🚀 🌍 🌎 🌏 🛞 😀 😃 😄 😁 😆 😅 🤣 😂 🙂 😉 😊 😇 🥰 😍 😋 😛 😜 🤪 😝 🗣️ 👤 👥 🧟 🧟‍♂️ 💐 🌹 🥀 🌻 🌱 🪴 🌲 🌳 🌴 🌵 🌾 🌿 🍀 🍃 🐸 🐢 🐍 🦕 🌞 🪐 🌟 🌠 🌌 🍈 🍏 🍐 🫒 🥑 🫑 🥒 🥬 🥦 🫛 📗 🈯 ❇️".split()
        self.reset_conversation()


    def reset_conversation(self):
        self.conversation_delay = -random.randint(10, 40)
        self.current_speaker = random.randint(0, 1)
        self.conv_length = random.randint(3, 5) * 5


    def get_hello_str(self, hero_univ_coord):
        if self.customer.arrived:
            return []
        if self.compute_dist_from_hero(hero_univ_coord) > 2:
            self.said_hello = False
            return []
        if self.said_hello:
            return []
        if random.randint(0, 10) >= 9:
            return []

        self.said_hello = True
        dest_x, dest_y = self.customer.dest_coord
        money_str = get_money_str(self.customer.money)
        return [
            f"👋😃 {STR_WALLET}: {money_str}",
            f"🛸 ({dest_x}, {dest_y})",
        ]


    def get_on_board_str(self):
        return ["🫶💚😃"]


    def get_goodbye_str(self):
        return ["👋👍😃"]


    def get_speak_while_traveling(self):
        self.conversation_delay += 1
        if self.conversation_delay >= self.conv_length:
            self.reset_conversation()
            return None

        if self.conversation_delay >= 0 and self.conversation_delay % 5 == 0:
            self.current_speaker = [1, 0][self.current_speaker]
            conv_length = random.randint(3, 8)
            talk_line = "".join((random.choice(self.words) for _ in range(conv_length)))
            return (talk_line, self.current_speaker)
        else:
            return None


class SympatheticGreenAlien(Archetype):

    def __init__(self, dist_start=50, dist_dest=50):
        self.gamobj_appearance = "customer_green"
        self.conversationer = ConversationerSympatheticGreenAlien()
        self.money = random.randint(10, 50)
        CHAR_NAME = "🧩 💚 ✳️ 🟢 🟩 🍏 📗 ❎ ❇️".split(" ")
        self.name = random.choice(CHAR_NAME) + random.choice(CHAR_NAME)

        self.is_coord_valid = False
        start_x = random.randint(-dist_start, +dist_start)
        start_y = random.randint(-dist_start, +dist_start)
        self.start_coord = CelestialObjGen.find_planet_around(start_x, start_y)
        if self.start_coord is None:
            return
        dest_x = random.randint(-dist_dest, +dist_dest)
        dest_y = random.randint(-dist_dest, +dist_dest)
        self.dest_coord = CelestialObjGen.find_planet_around(dest_x, dest_y)
        if self.dest_coord is None:
            return
        if self.start_coord == self.dest_coord:
            return
        self.is_coord_valid = True


class SympatheticGreenAlienNear(SympatheticGreenAlien):

    def __init__(self):
        super().__init__(15, 30)


class Customer():

    def __init__(self, single_archetype=None, archetypes=[]):
        if not archetypes:
            if single_archetype is None:
                raise Exception("Not supposed to happen")
            archetypes = [single_archetype] * 5
        (
            arch_name,
            arch_appearance,
            arch_conv,
            arch_coords,
            arch_money,
        ) = archetypes
        if not arch_coords.is_coord_valid:
            raise Exception("Not supposed to happen")

        self.start_coord = arch_coords.start_coord
        self.dest_coord = arch_coords.dest_coord
        self.money = arch_money.money
        self.game_object = arch_appearance.gamobj_appearance
        self.conversationer = arch_conv.conversationer
        self.conversationer.set_customer(self)
        self.name = arch_name.name
        self.beacon_compatibility = 2 ** random.randint(1, 5)
        self.arrived = False
        self.life_time = None
        self.speak_life_time = 0
        # 0: customer speaks. 1: hero answers to customer, while they travel together.
        self.speaker_id = 0

    def put_to_destination(self):
        self.arrived = True
        self.start_coord = self.dest_coord
        self.dest_coord = None
        self.money = 0
        self.life_time = random.randint(20, 200)

    def decorate_talks(self, talks, talker_id=0):
        str_talker = self.name if talker_id == 0 else STR_HERO
        return [
            f"  {str_talker}: \"{talk}\""
            for talk in talks
        ]

    def get_talks_near(self, hero_univ_coord):
        talks = self.conversationer.get_hello_str(hero_univ_coord)
        if talks:
            self.speak_life_time = LIFE_TIME_SPEAK_BUBBLE
            self.speaker_id = 0
        return self.decorate_talks(talks)

    def get_talks_on_boarding(self):
        self.speak_life_time = LIFE_TIME_SPEAK_BUBBLE
        self.speaker_id = 0
        return self.decorate_talks(self.conversationer.get_on_board_str())

    def get_talks_off_boarding(self):
        self.speak_life_time = LIFE_TIME_SPEAK_BUBBLE
        self.speaker_id = 0
        return self.decorate_talks(self.conversationer.get_goodbye_str())

    def get_speak_while_traveling(self):
        talk_result = self.conversationer.get_speak_while_traveling()
        if talk_result is None:
            return None
        else:
            talk_line, self.speaker_id = talk_result
            self.speak_life_time = LIFE_TIME_SPEAK_BUBBLE
            return self.decorate_talks([talk_line], self.speaker_id)

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
        self.w = 11
        self.h = 11
        self.tiles = [
            [
                [] for x in range(self.w)
            ]
            for y in range(self.h)
        ]
        self.hero_coord = [5, 5]
        self.corner_coord = [-5, -5]
        self.money = 0
        self.buffer_celestial_bodies = []
        self.customer_inside = None

        self.customers = {}
        self.prev_action = None
        self.customer_list = CustomerList()

        self.spawn_customer(SympatheticGreenAlienNear)
        for _ in range(4):
            self.spawn_customer(SympatheticGreenAlien)
        for _ in range(5):
            self.spawn_customer(SympatheticGreenAlien)
        self.spawn_timer = 10000


    def get_tile(self, x, y):
        return self.tiles[y][x]


    def compute_celestial_body_memoized(self, x, y):
        for buf_x, buf_y, celest_bod in self.buffer_celestial_bodies:
            if (buf_x, buf_y) == (x, y):
                return celest_bod
        celest_bod = CelestialObjGen.compute_celestial_body(x, y)
        self.buffer_celestial_bodies.append((x, y, celest_bod))
        return celest_bod


    def spawn_customer(self, single_archetype_class=None):
        random.seed()
        if single_archetype_class is None:
            raise Exception("TODO : code the archetypes selection, you dumb !!")
        forbidden_coords = []
        for cust in self.customers.values():
            forbidden_coords.append(cust.start_coord)
            forbidden_coords.append(cust.dest_coord)

        for _ in range(5):
            single_archetype = single_archetype_class()
            if single_archetype.is_coord_valid:
                # On vérifie que les coordonnées ne se confondent pas avec un customer existant.
                if single_archetype.start_coord not in forbidden_coords and single_archetype.dest_coord not in forbidden_coords:
                    break
            # Fail spawn du customer. Tant pis !
            return None

        new_customer = Customer(single_archetype)
        self.customers[new_customer.start_coord] = new_customer
        return new_customer


    def export_all_tiles(self):

        for y in range(self.h):
            add_speak_bubble = False
            for x in range(self.w):
                x_univ = self.corner_coord[0] + x
                y_univ = self.corner_coord[1] + y
                tile_current = self.get_tile(x, y)
                tile_current[:] = self.compute_celestial_body_memoized(x_univ, y_univ)
                customer = self.customers.get((x_univ, y_univ))

                if add_speak_bubble:
                    add_speak_bubble = False
                    tile_current.append("speak_bubble_right")
                if customer is not None:
                    tile_current.append(customer.game_object)
                    if customer.speak_life_time and x < self.w-1:
                        add_speak_bubble = True

        if len(self.buffer_celestial_bodies) > BUFFER_SIZE_CELEST_BODIES:
            self.buffer_celestial_bodies = self.buffer_celestial_bodies[BUFFER_SIZE_CELEST_BODIES:]

        tile_hero = self.get_tile(*self.hero_coord)
        if self.customer_inside is not None:
            tile_hero.append(self.customer_inside.game_object)
            if self.customer_inside.speak_life_time:
                talk_x, talk_y = self.hero_coord
                if self.customer_inside.speaker_id == 0:
                    talk_x += 1
                    talk_gamobj = "speak_bubble_right"
                else:
                    talk_x -= 1
                    talk_gamobj = "speak_bubble_left"
                tile_talk = self.get_tile(talk_x, talk_y)
                tile_talk.append(talk_gamobj)

        tile_hero.append("hero")

        return self.tiles


    def log_status(self):
        print("\n" * 3)

        log_money = "  " + STR_WALLET + ": " + get_money_str(self.money)
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

            for start_coord, cust in self.customers.items():
                # Raaahhh. Check de bounding rerct. Pourquoi j'ai pas une fonction générique pour ça ?
                dist_cust_x = abs(hero_univ_x - start_coord[0])
                dist_cust_y = abs(hero_univ_y - start_coord[1])
                if dist_cust_x < 4 and dist_cust_y < 4:
                    log_talks = cust.get_talks_near(hero_univ_coord)
                    if log_talks:
                        print("\n")
                        for log_line in log_talks:
                            print(log_line)

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

            if self.customer_inside is not None:
                if self.customer_inside.dest_coord == hero_univ_coord:
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
                else:
                    talk_result = self.customer_inside.get_speak_while_traveling()
                    if talk_result is not None:
                        print()
                        print(talk_result[0], end="")

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
            if customer.speak_life_time > 0:
                customer.speak_life_time -= 1
        if cust_coord_to_del is not None:
            del self.customers[cust_coord_to_del]

        if self.customer_inside is not None and self.customer_inside.speak_life_time > 0:
            self.customer_inside.speak_life_time -= 1

        if not self.customers:
            self.spawn_timer = 0
        else:
            self.spawn_timer -= (12-len(self.customers)) ** 2

        if self.spawn_timer <= 0:
            # TODO : spawn random customers.
            self.spawn_customer(SympatheticGreenAlien)
            self.spawn_timer += 10000


        self.prev_action = event_name


