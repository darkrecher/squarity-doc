# https://i.ibb.co/JCY3vsN/H2-Otileset2.png
# https://i.ibb.co/DfwsNbY/H2-Otileset2.png
# https://i.ibb.co/HXSkXQf/H2-Otileset2.png
# https://i.ibb.co/1bhGZnv/H2-Otileset2.png
# https://i.ibb.co/mcqSnbT/H2-Otileset2.png


"""


{
  "tile_size": 32,
  "tile_coords": {

    "water_right": [0, 0],
    "water_down": [32, 0],
    "water_left": [64, 0],
    "water_up": [96, 0],
    "ice_right": [0, 32],
    "ice_down": [32, 32],
    "ice_left": [64, 32],
    "ice_up": [96, 32],
    "gas_right": [0, 64],
    "gas_down": [32, 64],
    "gas_left": [64, 64],
    "gas_up": [96, 64],

    "water_right_pipe": [0, 96],
    "water_down_pipe": [32, 96],
    "water_left_pipe": [64, 96],
    "water_up_pipe": [96, 96],
    "gas_right_pipe": [0, 128],
    "gas_down_pipe": [32, 128],
    "gas_left_pipe": [64, 128],
    "gas_up_pipe": [96,128],

    "E": [64, 160],
    "wet_sponge": [96, 160],

    "O": [64, 192],
    "wet_grid": [96, 192],

    "S": [64, 224],
    "C": [96, 224],

    "=": [32, 256],
    "H": [96, 256],

    "gas_dead": [0, 288],
    ".": [96, 288],

    "X": [160, 64],
    "+": [0, 416],

    "pattern_*.*.XX*.*": [128, 0],
    "pattern_*.*XXX*.*": [160, 0],
    "pattern_*.*XX.*.*": [192, 0],
    "pattern_*.*.X.*X*": [224, 0],
    "pattern_*.*.XX*X*": [128, 32],
    "pattern_*.*XXX*X*": [160, 32],
    "pattern_*.*XX.*X*": [192, 32],
    "pattern_*X*.X.*X*": [224, 32],
    "pattern_*X*.XX*X*": [128, 64],
    "pattern_*X*XX.*X*": [192, 64],
    "pattern_*X*.X.*.*": [224, 64],
    "pattern_*X*.XX*.*": [128, 96],
    "pattern_*X*XXX*.*": [160, 96],
    "pattern_*X*XX.*.*": [192, 96],
    "pattern_*.*.X.*.*": [224, 96],
    "pattern_***XXX.XX": [128, 128],
    "pattern_***XXXXX.": [160, 128],
    "pattern_*X*XX..X*": [192, 128],
    "pattern_*X*.XX*X.": [224, 128],
    "pattern_*.*XX..X*": [192, 160],
    "pattern_*.*.XX*X.": [224, 160],
    "pattern_***XXX.X.": [160, 256],

    "pattern_*X*.-X***": [128, 192],
    "pattern_*X*X-.***": [160, 192],
    "pattern_***.-*.X*": [224, 192],
    "pattern_*X*.-*.X*": [128, 224],
    "-": [160, 224],
    "pattern_*X**-.*X.": [192, 224],
    "pattern_****-.*X.": [224, 224],
    "pattern_*X*.-.***": [160, 288],
    "pattern_*X*.-..X.": [192, 288],

    "pattern_*.**|**X*": [128, 256],
    "|": [224, 256],
    "pattern_*X**|**.*": [128, 288],
    "pattern_*.**|**.*": [224, 288],

    "I_wall_up": [0, 224],
    "I": [128, 320],
    "electroball_D": [0, 384],
    "electroball_U": [32, 384],
    "electroball_R": [64, 384],
    "electroball_L": [96, 384],

    "pattern_*X*.X=*.*": [0, 160],
    "pattern_*X*=X.*.*": [32, 160],
    "pattern_***XXX*I*": [0, 192],
    "pattern_*X*.X.*I*": [32, 192],
    "pattern_*X*XX=XX*": [0, 256],
    "pattern_*X*=XX*XX": [64, 256],

    "pattern_*X*.XX*I*": [32, 288],
    "pattern_*X*XX.*I*": [64, 288],

    "pattern_*.*.X=*.*": [0, 320],
    "pattern_*.*=X.*.*": [32, 320],
    "pattern_*.*XX=*.*": [64, 320],
    "pattern_*.*=XX*.*": [96, 320],

    "pattern_*X*.X=*I*": [160, 320],
    "pattern_*X*=X.*I*": [192, 320],
    "pattern_*X*=X=*I*": [224, 320],

    "pattern_*.*XX=XX*": [0, 352],
    "pattern_*.*=XX*XX": [32, 352],
    "pattern_*.*=X=*X*": [64, 352],
    "pattern_*.*=X.*X*": [96, 352],
    "pattern_*.*.X=*X*": [128, 352],

    "pattern_*I*=+=*.*": [32, 416]

  }
}


"""




LEVELS = (
    (
        "XXXXXXXXXXXXXXXXXXXX",
        "X..................X",
        "X....=..I..........X",
        "X....++++..........X",
        "X....I=.+=.........X",
        "X...+++++..........X",
        "X......X...........X",
        "S.....H.C..........X",
        "X..................X",
        "X...==...I.........X",
        "X........I.........X",
        "X..................X",
        "X.................OX",
        "XXXXXXXXXXXXXXXXXXXX",
    ),
    (
        "XXXXXX..XXXXXXXXXXXX",
        "X.-X..--.X-..-..-..X",
        "X.XX..XX.XX.XXX.X..X",
        "X..................X",
        "X.X..XX=X=XX.....X.X",
        "XXX..XX.X.XX....XX=X",
        "X.-.............XX.X",
        "S....I....X=X=X....X",
        "X....I.==.X.X.X....X",
        "X..H.C....X|X=XX=X.X",
        "X..X.X.X..X|.......X",
        "X..X=X=X..X|X..|...X",
        "X..I.I.I..........OX",
        "XXXXXXXXXXXXXXXXXXXX",
    ),
    (
        "XXXXXXXXXXXXXXXXXXXX",
        "X...-...X.X...I....X",
        "X..XXX..XXX..XXX...X",
        "S...E....H....-....X",
        "X..XXX..XXX..XXX.X.X",
        "X...I...X.X...E..X.X",
        "XXXXXXXXX.XXXXXXXX.X",
        "XXXXXXXXX.XXXXXXXXCX",
        "X.H.H...X.X...E..X.X",
        "X..CCC..XXX..XXX.XCX",
        "X.HCO.........I....X",
        "X..CCC..XXX..XXX.XXX",
        "X.H.H...XXX...-..XXX",
        "XXXXXXXXXXXXXXXXXXXX",
    ),
    (
        "X.H.XXX.C.XXX.H.XXXX",
        "S....-E...I.E.....XX",
        "X.C.XXX.H.XXX.C.X|XX",
        "XXXXXXXXXXXXXXXXX.XX",
        "X.H.XXX.C.XXX.H.X=XX",
        "XC..I.H....-C.....XX",
        "X...XXX.H.XXX.C.XXXX",
        "XX.XX.XXXXX.XXXXX...",
        "XXCX.X.X...XXXXXXX..",
        "XXHXXXXX..XX.....X..",
        "XXEX.H.XXXXX..O..X..",
        "XX......HCE......X..",
        "XXXX.C.XXXXXH...CX..",
        "XXXXXXXXXXXXXXXXXX..",
    ),
    (
        "XXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXX.....XXXXXXX",
        "XXXXXXXX.XXXHXXXXXXX",
        "XXXXXXXX.XXXHXXXXXXX",
        "X.H.XXXX.XXXCXXXXXXX",
        "S....E-..CCHE.....XX",
        "X.C.XXXX.XXXCXXX..XX",
        "XXXXX..X.XXXHX.....X",
        "X.--.||X.XXXCX.XXX.X",
        "X|XX..|X.....X..CH.X",
        "X|X.--.XXXXXXXXXHCXX",
        "X|XOXXXXXXX.----CHXX",
        "X.---------.XXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXX",
    ),
    (
        "E=EX===X===X========",
        "ECEI...I...I...IIIOI",
        "EEEI.I.I.I.I.I.III=I",
        "XI.I.I.I.I.I.I.I...I",
        "XI...I...I...I...I.I",
        "XX===X===X===X===IHI",
        "XXXXXXXXXXXXXXXXXEHE",
        "XEHEEEEEEEEEEEEEEX=X",
        "XE......EE.....EEEEE",
        "XEEEEEE....EEE.....E",
        "XEEEEEEEEEEEEEEEEE.E",
        "XE...E...E...E...E.E",
        "S..E...E...E...E...E",
        "XEEEEEEEEEEEEE-CEEEE",
    ),
    (
        "XXXXXXXXXXXXXXXXXXXX",
        "X.HHHH..H..H..H..H.X",
        "X.H.....H..HH.H..H.X",
        "X.HH....H..H.HH..H.X",
        "X.H.....H..H..H....X",
        "X.H.....H..H..H..H.X",
        "S..................X",
        "X.....CC.....CC....X",
        "X.....CC.....CC....X",
        "X..................X",
        "X...C...........C..X",
        "X....C.........C...X",
        "X.....CCCCCCCCC....X",
        "XXXXXXXXXXXXXXXXXXXX",
    ),
)

class BoardModel():

    def __init__(self, width=20, height=14):
        self.w = width
        self.h = height
        self.current_level_idx = 0
        self.init_level()
        print("Le tileset a été dessiné par Tacheul.")
        print("http://pixeljoint.com/p/121104.htm")
        print()

    def in_bound(self, x, y):
        return (0 <= x < self.w) and (0 <= y < self.h)

    def compile_match_patterns(self, str_patterns):
        patterns = []
        line_patterns = str_patterns.split()
        while line_patterns:
            l_1, l_2, l_3, *line_patterns = line_patterns
            pat = l_1 + l_2 + l_3
            patterns.append(pat)
        return tuple(patterns)

    def compile_replace_patterns(self, str_patterns):
        patterns = []
        line_patterns = str_patterns.split()
        while line_patterns:
            l_1, l_2, l_3, l_rep, *line_patterns = line_patterns
            pat = l_1 + l_2 + l_3
            l_rep = l_rep[2:]
            l_rep = l_rep.split(",")
            l_rep = tuple([
                (int(index), char_rep)
                for index, semicolon, char_rep in
                l_rep
            ])
            patterns.append((pat, l_rep))
        return tuple(patterns)

    def match_with_patterns(self, main_pattern, test_patterns):
        for test_pattern in test_patterns:
            correct = True
            for char_test, char_main in zip(test_pattern, main_pattern):
                if char_test != "*" and char_test != char_main:
                    correct = False
                    break
            if correct:
                return test_pattern
        return None

    def apply_replacement_patterns(self, main_pattern, replacement_patterns):
        applied_replacement = False
        for test_pat, repl_actions in replacement_patterns:
            correct = True
            for char_test, char_main in zip(test_pat, main_pattern):
                if char_test != "*" and char_test != char_main:
                    correct = False
                    break
            if correct:
                if not applied_replacement:
                    applied_replacement = True
                    main_pattern = list(main_pattern)
                for index, char_rep in repl_actions:
                    main_pattern[index] = char_rep

        if applied_replacement:
            return "".join(main_pattern)
        else:
            return main_pattern

    def stylify_tile(self, x, y):

        gamobj_mid = self.cur_level[y][x]
        if gamobj_mid not in ("X", "-", "|", "+"):
            return None

        main_pattern = ""
        for y_offset in (-1, 0, 1):
            for x_offset in (-1, 0, 1):
                x_check = x + x_offset
                y_check = y + y_offset
                # Les tiles à l'extérieur de la map sont considérées comme des murs.
                if not self.in_bound(x_check, y_check):
                    main_pattern += "X"
                else:
                    lvl_map_char = self.cur_level[y_check][x_check]
                    if lvl_map_char in ("X", "S"):
                        main_pattern += "X"
                    elif lvl_map_char in ("-", "|", "=", "I", "+"):
                        main_pattern += lvl_map_char
                    else:
                        main_pattern += "."


        # Dans la suite de cette fonction, on fait tout un tas de replace. C'est moche et pas optimisé.
        # Je n'ai pas de meilleure méthode pour le moment. Pouet pouet.

        if gamobj_mid == "X":

            main_pattern = self.apply_replacement_patterns(main_pattern, self.patterns_replacement_tunnels_too_far)
            main_pattern = main_pattern.replace("-", "X")
            main_pattern = main_pattern.replace("|", "X")
            matched_pattern = self.match_with_patterns(main_pattern, self.patterns_wall_with_laser)
            if matched_pattern is not None:
                return "pattern_" + matched_pattern

            main_pattern = main_pattern.replace("I", ".")
            main_pattern = main_pattern.replace("=", ".")
            main_pattern = main_pattern.replace("+", ".")
            # Il faut retenter les patterns de remplacment, car on vient de supprimer les lasers,
            # et ça a peut-être changé des choses.
            main_pattern = self.apply_replacement_patterns(main_pattern, self.patterns_replacement_tunnels_too_far)
            matched_pattern = self.match_with_patterns(main_pattern, self.patterns_wall_simple)
            if matched_pattern is not None:
                return "pattern_" + matched_pattern
            return None

        if gamobj_mid == "-":
            main_pattern = main_pattern.replace("I", ".")
            main_pattern = main_pattern.replace("=", ".")
            main_pattern = main_pattern.replace("+", ".")
            main_pattern = self.apply_replacement_patterns(main_pattern, self.patterns_replacement_tunnels_too_far)
            main_pattern = main_pattern.replace("-", "X")
            main_pattern = main_pattern.replace("|", "X")
            # On remet le gamobj_mid comme il faut.
            main_pattern = main_pattern[:4] + gamobj_mid + main_pattern[5:]
            matched_pattern = self.match_with_patterns(main_pattern, self.patterns_tunnel_horiz_simple)
            if matched_pattern is not None:
                return "pattern_" + matched_pattern
            return None

        if gamobj_mid == "|":
            main_pattern = main_pattern.replace("I", ".")
            main_pattern = main_pattern.replace("=", ".")
            main_pattern = main_pattern.replace("+", ".")
            # Pas besoin d'appliquer patterns_replacement_tunnels_too_far, car ça ne concerne que des cases
            # sur les diagonales. Or, le tunnel vertical s'en fiche de ce qu'il peut y avoir sur les cases diagonales.
            main_pattern = main_pattern.replace("-", "X")
            main_pattern = main_pattern.replace("|", "X")
            # On remet le gamobj_mid comme il faut.
            main_pattern = main_pattern[:4] + gamobj_mid + main_pattern[5:]
            matched_pattern = self.match_with_patterns(main_pattern, self.patterns_tunnel_vertic)
            if matched_pattern is not None:
                return "pattern_" + matched_pattern
            return None

        if gamobj_mid == "+":
            main_pattern = main_pattern.replace("-", ".")
            main_pattern = main_pattern.replace("|", ".")
            main_pattern = main_pattern.replace("X", ".")
            main_pattern = self.apply_replacement_patterns(main_pattern, self.patterns_replacement_cross_lasers)
            matched_pattern = self.match_with_patterns(main_pattern, self.patterns_cross_lasers)
            if matched_pattern is not None:
                return "pattern_" + matched_pattern
            return None

        return None

    def stylify_laser(self, x, y, lvl_map_char):
        len_str_prefix = len("pattern_")
        gamobjs_final = []

        # C'est un peu moche, parce qu'il y a du duplicate code, mais pas complètement.
        # Je préfère pas factoriser un truc comme ça.
        # Ça risque d'ajouter plus de complexité que ce qu'il y a déjà.

        if lvl_map_char == "I" or lvl_map_char == "+":

            electroball_U = True
            electroball_D = True

            # up
            gamobjs_up = self.tiles[y-1][x] if self.in_bound(x, y-1) else ["X"]
            for gamobj in gamobjs_up:
                if gamobj in ("I", "+"):
                    electroball_U = False
                elif gamobj.startswith("pattern_"):
                    # Exemple de pattern qui fonctionne : "pattern_***XXX.I."
                    if gamobj[len_str_prefix + 7] == "I":
                        electroball_U = False
                        gamobjs_final.append("I_wall_up")

            # down
            gamobjs_down = self.tiles[y+1][x] if self.in_bound(x, y+1) else ["X"]
            for gamobj in gamobjs_down:
                if gamobj in ("I", "+", "X"):
                    electroball_D = False

            # cross
            if lvl_map_char == "+":
                gamobjs_cur = self.tiles[y][x]
                for gamobj in gamobjs_cur:
                    if gamobj.startswith("pattern_"):
                        if gamobj[len_str_prefix + 7] == ".":
                            electroball_D = False
                        if gamobj[len_str_prefix + 1] == ".":
                            electroball_U = False

            if electroball_D:
                gamobjs_final.append("electroball_D")
            if electroball_U:
                gamobjs_final.append("electroball_U")


        if lvl_map_char == "=" or lvl_map_char == "+":

            electroball_L = True
            electroball_R = True

            # left
            gamobjs_adj = self.tiles[y][x-1] if self.in_bound(x-1, y) else ["X"]
            for gamobj in gamobjs_adj:
                if gamobj in ("=", "+"):
                    electroball_L = False
                elif gamobj.startswith("pattern_"):
                    # Exemple de pattern qui fonctionne : "pattern_*X*XX=XX*"
                    if gamobj[len_str_prefix + 5] == "=":
                        electroball_L = False

            # right
            gamobjs_adj = self.tiles[y][x+1] if self.in_bound(x+1, y) else ["X"]
            for gamobj in gamobjs_adj:
                if gamobj in ("=", "+"):
                    electroball_R = False
                elif gamobj.startswith("pattern_"):
                    # Exemple de pattern qui fonctionne : "pattern_*X*=XX*XX"
                    if gamobj[len_str_prefix + 3] == "=":
                        electroball_R = False

            # cross
            if lvl_map_char == "+":
                gamobjs_cur = self.tiles[y][x]
                for gamobj in gamobjs_cur:
                    if gamobj.startswith("pattern_"):
                        if gamobj[len_str_prefix + 3] == ".":
                            electroball_R = False
                        if gamobj[len_str_prefix + 5] == ".":
                            electroball_L = False

            if electroball_R:
                gamobjs_final.append("electroball_R")
            if electroball_L:
                gamobjs_final.append("electroball_L")

        return gamobjs_final


    def init_level(self):

        # Ce sont les patterns de suppression des tunnels en diagonale qui sont raccrochés à rien.
        PATTERNS_REPLACEMENT_TUNNELS_TOO_FAR = """

            -.*
            .**
            ***
            =>0:.

            |.*
            .**
            ***
            =>0:.

            *.-
            **.
            ***
            =>2:.

            *.|
            **.
            ***
            =>2:.

            ***
            .**
            -.*
            =>6:.

            ***
            .**
            |.*
            =>6:.

            ***
            **.
            *.-
            =>8:.

            ***
            **.
            *.|
            =>8:.

        """

        PATTERNS_REPLACEMENT_CROSS_LASERS = """

            *+*
            ***
            ***
            =>1:I

            ***
            +**
            ***
            =>3:=

            ***
            **+
            ***
            =>5:=

            ***
            ***
            *+*
            =>7:I

        """

        PATTERNS_WALL_WITH_LASER = """

            ***
            XXX
            *I*

            *X*
            .X.
            *I*

            *X*
            XX=
            XX*

            *X*
            =XX
            *XX

            *X*
            .X=
            *.*

            *X*
            =X.
            *.*

            *X*
            .XX
            *I*

            *X*
            XX.
            *I*

            *.*
            .X=
            *.*

            *.*
            =X.
            *.*

            *.*
            XX=
            *.*

            *.*
            =XX
            *.*

            *X*
            .X=
            *I*

            *X*
            =X.
            *I*

            *X*
            =X=
            *I*

            *.*
            XX=
            XX*

            *.*
            =XX
            *XX

            *.*
            =X=
            *X*

            *.*
            =X.
            *X*

            *.*
            .X=
            *X*

        """

        # TODO : faut pouvoir en mettre plusieurs sur la même ligne.
        PATTERNS_WALL_SIMPLE = """

            *X*
            XX.
            .X*

            *X*
            .XX
            *X.

            *.*
            XX.
            .X*

            *.*
            .XX
            *X.

            ***
            XXX
            .XX

            ***
            XXX
            XX.

            ***
            XXX
            .X.

            *.*
            .XX
            *.*

            *.*
            XXX
            *.*

            *.*
            XX.
            *.*

            *.*
            .X.
            *X*

            *.*
            .XX
            *X*

            *.*
            XXX
            *X*

            *.*
            XX.
            *X*

            *X*
            .X.
            *X*

            *X*
            .XX
            *X*

            *X*
            XX.
            *X*

            *X*
            .X.
            *.*

            *X*
            XXX
            *.*

            *X*
            .XX
            *.*

            *X*
            XX.
            *.*

            *.*
            .X.
            *.*

        """

        PATTERNS_TUNNEL_HORIZ_SIMPLE = """

            *X*
            .-.
            .X.

            *X*
            .-.
            ***

            *X*
            .-*
            .X*

            *X*
            *-.
            *X.

            *X*
            .-X
            ***

            *X*
            X-.
            ***

            ***
            .-*
            .X*

            ***
            *-.
            *X.

        """

        PATTERNS_TUNNEL_VERTIC = """

            *.*
            *|*
            *X*

            *X*
            *|*
            *.*

            *.*
            *|*
            *.*

        """

        PATTERNS_CROSS_LASERS = """

            *I*
            =+=
            *.*

        """

        # TODO : compiler ça une seule fois au début.
        self.patterns_replacement_tunnels_too_far = self.compile_replace_patterns(PATTERNS_REPLACEMENT_TUNNELS_TOO_FAR)
        self.patterns_replacement_cross_lasers = self.compile_replace_patterns(PATTERNS_REPLACEMENT_CROSS_LASERS)
        self.patterns_wall_with_laser = self.compile_match_patterns(PATTERNS_WALL_WITH_LASER)
        self.patterns_wall_simple = self.compile_match_patterns(PATTERNS_WALL_SIMPLE)
        self.patterns_tunnel_horiz_simple = self.compile_match_patterns(PATTERNS_TUNNEL_HORIZ_SIMPLE)
        self.patterns_tunnel_vertic = self.compile_match_patterns(PATTERNS_TUNNEL_VERTIC)
        self.patterns_cross_lasers = self.compile_match_patterns(PATTERNS_CROSS_LASERS)

        self.hero_alive = False
        self.tiles = tuple([
            tuple([
                [] for x in range(self.w)
            ])
            for y in range(self.h)
        ])
        self.cur_level = LEVELS[self.current_level_idx]

        for y in range(self.h):
            for x in range(self.w):
                gamobjs = []
                lvl_map_char = self.cur_level[y][x]
                if lvl_map_char == "S":
                    # Si le tuyau d'arrivée est tout à droite, ça fera planter le jeu.
                    # Faut juste pas faire des niveaux avec le tuyau d'arrivée tout à droite.
                    self.hero_x = x + 1
                    self.hero_y = y
                    self.hero_alive = True
                    self.hero_dir = "D"
                    self.hero_state = "water"
                if lvl_map_char != " ":
                    gamobjs.append(lvl_map_char)
                styled_wall = self.stylify_tile(x, y)
                if styled_wall is not None:
                    gamobjs.append(styled_wall)
                self.tiles[y][x][:] = gamobjs

        for y in range(self.h):
            for x in range(self.w):
                lvl_map_char = self.cur_level[y][x]
                if lvl_map_char in ("I", "=", "+"):
                    self.tiles[y][x].extend(self.stylify_laser(x, y, lvl_map_char))

    def get_size(self):
        return self.w, self.h

    def get_tile_gamobjs(self, x, y):
        return self.tiles[y][x]

    def export_all_tiles(self):
        rendered_tiles = [
            [
                list(self.tiles[y][x]) for x in range(self.w)
            ]
            for y in range(self.h)
        ]
        hero_dir_names = {
            "U": "up",
            "D": "down",
            "L": "left",
            "R": "right",
        }
        if self.hero_alive :
            tile_of_hero = rendered_tiles[self.hero_y][self.hero_x]
            hero_gamobj = "%s_%s" % (self.hero_state, hero_dir_names[self.hero_dir])
            if "-" in tile_of_hero or "|" in tile_of_hero:
                hero_gamobj += "_pipe"
            tile_of_hero.append(hero_gamobj)

        return rendered_tiles

    def can_move(self, start_tile_objs, dest_tile_objs, move_dir):
        if "X" in dest_tile_objs or "S" in dest_tile_objs:
            return False
        if "-" in (start_tile_objs + dest_tile_objs) and move_dir in ("U", "D"):
            return False
        if "|" in (start_tile_objs + dest_tile_objs) and move_dir in ("L", "R"):
            return False
        if self.hero_state == "ice" and ("-" in dest_tile_objs or "|" in dest_tile_objs):
            return False
        return True

    def on_game_event(self, event_name):

        if not self.hero_alive:
            self.init_level()
            return

        if event_name.startswith("action") and self.current_level_idx == 0:
            print("Les boutons d'actions ne servent à rien dans ce jeu.")

        must_move = False
        move_coord = squarity.MOVE_FROM_DIR.get(event_name)

        if move_coord is not None:
            new_hero_x = self.hero_x + move_coord[0]
            new_hero_y = self.hero_y + move_coord[1]
            if 0 <= new_hero_x < self.w and 0 <= new_hero_y < self.h:
                target_tile_objs = self.get_tile_gamobjs(new_hero_x, new_hero_y)
                must_move = self.can_move(
                    self.get_tile_gamobjs(self.hero_x, self.hero_y),
                    target_tile_objs,
                    event_name
                )

        if must_move:
            self.hero_dir = event_name
            self.hero_x = new_hero_x
            self.hero_y = new_hero_y

        tile_data_new_pos = self.get_tile_gamobjs(self.hero_x, self.hero_y)
        if must_move and "C" in tile_data_new_pos:
            to_cold = {
                "ice": "ice",
                "water": "ice",
                "gas": "water",
            }
            self.hero_state = to_cold[self.hero_state]
        if must_move and "H" in tile_data_new_pos:
            to_hot = {
                "ice": "water",
                "water": "gas",
                "gas": "gas",
            }
            self.hero_state = to_hot[self.hero_state]

        if "O" in tile_data_new_pos:
            if self.hero_state == "water":
                self.hero_alive = False
                tile_data_new_pos.remove("O")
                tile_data_new_pos.append("wet_grid")
                self.current_level_idx += 1
                print("Bravo, vous passez au niveau %s" % (self.current_level_idx + 1))
            elif self.current_level_idx == 0:
                print("Il faut être en état liquide.")

        #if ("=" in tile_data_new_pos or "I" in tile_data_new_pos) and self.hero_state == "gas":
        if set("=I+").intersection(set(tile_data_new_pos)) and self.hero_state == "gas":
            self.hero_alive = False
            tile_data_new_pos.append("gas_dead")
            print("Blarg ! Appuyez sur un bouton pour ressusciter")

        if "E" in tile_data_new_pos and self.hero_state == "water":
            self.hero_alive = False
            tile_data_new_pos.remove("E")
            tile_data_new_pos.append("wet_sponge")
            print("Blarg ! Appuyez sur un bouton pour ressusciter")

