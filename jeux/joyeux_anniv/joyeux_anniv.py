# https://raw.githubusercontent.com/darkrecher/squarity-doc/master/jeux/joyeux_anniv/jeu_anniv.png
# http://squarity.fr/#fetchez_githubgist_darkrecher/ca78c1d959e221a6ea306cf41c94efbd/raw/joyeux-anniv
# https://tinyurl.com/jeulolilol

"""
{
    "tile_size": 32,
    "img_coords": {
        "*": [0, 89],
        "light": [32, 89],
        " ": [64, 89],
        "/": [96, 89],
        ":": [128, 89],
        ".": [160, 89],
        "|": [192, 89],
        "[": [224, 89],
        "]": [256, 89],
        "{": [288, 89],
        "}": [320, 89],
        "_": [352, 89],
        "-": [384, 89],
        "(": [416, 89],
        ")": [448, 89],
        "A": [0, 0],
        "B": [32, 0],
        "C": [64, 0],
        "D": [96, 0],
        "E": [128, 0],
        "F": [160, 0],
        "G": [192, 0],
        "H": [224, 0],
        "I": [256, 0],
        "J": [288, 0],
        "K": [320, 0],
        "L": [350, 0],
        "M": [384, 0],
        "N": [0, 43],
        "O": [32, 43],
        "P": [64, 43],
        "Q": [96, 43],
        "R": [128, 43],
        "S": [160, 43],
        "T": [192, 43],
        "U": [224, 43],
        "V": [255, 43],
        "W": [288, 43],
        "X": [322, 43],
        "Y": [352, 43],
        "Z": [384, 43]
    }
}
"""

"""
Le jeu s'intitule "Joyeux Anniversaire"
car je l'ai créé pour l'anniv' d'un pote.

Mais sinon ça n'a rien à voir.
C'est une sorte de mot-mêlé.

Comment ça va fonctionner (mais pour l'instant c'est pas encore codé comme ça).

Placez le personnage sur la première lettre du mot que vous
voulez former.
Appuyez sur le bouton "1" pour activer la récupération de lettres.
Déplacez-vous sur les lettres du mot.
Re-appuyez sur le bouton "1".
Si le mot est correct, il apparaît en haut de l'aire de jeu.
La liste des mots à trouver s'affiche en bas,
dans la fenêtre de log.

"""

LEVEL_MAP = (
    "  |               ] ",
    "                 )  ",
    "     }              ",
    " (        _-        ",
    "                    ",
    "     GROUCHEUKZ     ",
    "}    SCHLRFMKIR     ",
    "| *  OETUORLUGT    |",
    ")    CLNESEUISR    ]",
    "}(    PASSOIRE    [|",
    "]|)|            ] ]}",
    "}( [))|     |](|[[((",
    "(})])[)|(| |[])] [  ",
    "))[ })[(}(]|([[ (| {",
)

# SERF GUISE CHOUCROUTE PASSOIRE ROSES LUIRE SCHLUCHE

class GameModel():

    def __init__(self):
        self.w = 20
        self.h = 14
        self.tiles = []
        self.current_message = ""
        self.lit_positions = []
        self.y_limit_text = 3
        self.message_pos_y = 0
        self.show_link = False

        for y, map_line in enumerate(LEVEL_MAP):
            current_line = []
            for x, map_char in enumerate(map_line):
                if map_char == "*":
                    self.player_x = x
                    self.player_y = y
                if map_char == "_":
                    self.y_limit_text = y
                current_line.append([" ", map_char])
            self.tiles.append(current_line)

    def export_all_tiles(self):
        if self.show_link:
            tile_with_link = self.tiles[:-3]
            line = [[gamobj] for gamobj in "                    "]
            tile_with_link.append(line)
            line = [[gamobj] for gamobj in "TRALALALA           "]
            tile_with_link.append(line)
            line = [[gamobj] for gamobj in "YOUPI              {"]
            line[-1] = [" ", "{", "*"]
            tile_with_link.append(line)
            return tile_with_link
        else:
            return self.tiles

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def is_a_letter(self, gamobj):
        return len(gamobj) == 1 and gamobj.isupper()

    def coord_mouvement(self, x, y, direction):
        if direction == "R":
            x += 1
        elif direction == "L":
            x -= 1
        if direction == "D":
            y += 1
        if direction == "U":
            y -= 1
        return (x, y)

    def verifier_mouvement(self, dest_x, dest_y):
        if not (0 <= dest_x < self.w and 0 <= dest_y < self.h):
            return False
        return True


    def add_message_on_area(self, message, y_msg):
        line = self.tiles[y_msg]
        for x, gamobjs in enumerate(line):
            filtered_gamobs = filter(lambda gobj:not self.is_a_letter(gobj), gamobjs)
            line[x][:] = filtered_gamobs
        offset_center = max(0, (self.w-len(message)) // 2)
        for x, message_char in enumerate(message[:self.w], offset_center):
            line[x].append(message_char)


    def on_game_event(self, event_name):

        if event_name == "action_1":
            print(self.current_message)
            self.add_message_on_area(self.current_message, self.message_pos_y)
            self.current_message = ""
            for pos_lit_x, pos_lit_y in self.lit_positions:
                gamobjs_with_light = self.get_tile(pos_lit_x, pos_lit_y)
                gamobjs_with_light[:] = filter(lambda gobj:gobj != "light", gamobjs_with_light)
            self.lit_positions = []
            self.message_pos_y += 1
            if self.message_pos_y >= self.y_limit_text:
                self.message_pos_y = 0
            return

        player_dest_x, player_dest_y = self.coord_mouvement(
            self.player_x,
            self.player_y,
            event_name
        )
        if not self.verifier_mouvement(player_dest_x, player_dest_y):
            return

        tile_start_player = self.get_tile(self.player_x, self.player_y)
        tile_dest_player = self.get_tile(player_dest_x, player_dest_y)

        tile_start_player.remove("*")
        tile_dest_player.append("*")
        self.player_x = player_dest_x
        self.player_y = player_dest_y

        if self.player_y >= self.y_limit_text:
            for gamobj in tile_dest_player:
                if self.is_a_letter(gamobj):
                    self.current_message += gamobj
                    self.lit_positions.append((player_dest_x, player_dest_y))
                    tile_dest_player.append("light")
                    break

        self.show_link = "{" in tile_dest_player
        if self.show_link:
            print("")
            print(" PAF")

# Police de caractère :
# https://www.1001fonts.com/vtks-white-page-font.html (54 pts)

