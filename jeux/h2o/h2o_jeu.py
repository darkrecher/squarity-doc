# https://i.ibb.co/JCY3vsN/H2-Otileset2.png
# https://i.ibb.co/DfwsNbY/H2-Otileset2.png
# https://i.ibb.co/HXSkXQf/H2-Otileset2.png



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

    "=": [0, 224],
    "S": [64, 224],
    "C": [96, 224],

    "I": [32, 256],
    "H": [96, 256],

    "gas_dead": [0, 288],
    ".": [96, 288],

    "X": [160, 64],

    "|": [224, 256],
    "-": [160, 224],

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
    "pattern_*X*XXX.XX": [128, 128],
    "pattern_*X*XXXXX.": [160, 128],
    "pattern_*X*XX..X*": [192, 128],
    "pattern_*X*.XX*X.": [224, 128],
    "pattern_*.*XX..X*": [192, 160],
    "pattern_*.*.XX*X.": [224, 160],
    "pattern_***XXX.X.": [160, 256],

    "pattern_XXX.-X.XX": [224, 192], "pattern_....-X.XX": [224, 192]

  }
}


"""




LEVELS = (
    (
        "XXXXX...XXXXXXXXXXXX",
        "X.-X..--...........X",
        "X.XX..XX...........X",
        "X..................X",
        "X.X................X",
        "XXXX...............X",
        "X.-................X",
        "S..................X",
        "X..................X",
        "X..................X",
        "X..................X",
        "X..................X",
        "X.................OX",
        "XXXXXXXXXXXXXXXXXXXX",
    ),
    (
        "XXXXXXXXXXXXXXXXXXXX",
        "X...-...X.X...=....X",
        "X..XXX..XXX..XXX...X",
        "S...E....H....-....X",
        "X..XXX..XXX..XXX.X.X",
        "X...=...X.X...E..X.X",
        "XXXXXXXXX.XXXXXXXX.X",
        "XXXXXXXXX.XXXXXXXXCX",
        "X.H.H...X.X...E..X.X",
        "X..CCC..XXX..XXX.XCX",
        "X.HCO.........=....X",
        "X..CCC..XXX..XXX.XXX",
        "X.H.H...XXX...-..XXX",
        "XXXXXXXXXXXXXXXXXXXX",
    ),
    (
        "X.H.XXX.C.XXX.H.XXXX",
        "S...-.E...=.E.....XX",
        "X.C.XXX.H.XXX.C.X|XX",
        "XXXXXXXXXXXXXXXXX.XX",
        "X.H.XXX.C.XXX.H.XIXX",
        "XC..=.H...-.C.....XX",
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
        "EIEXIIIXIIIXIIIIIIII",
        "ECE=...=...=...===O=",
        "EEE=.=.=.=.=.=.===I=",
        "X=.=.=.=.=.=.=.=...=",
        "X=...=...=...=...=.=",
        "XXIIIXIIIXIIIXIII=H=",
        "XXXXXXXXXXXXXXXXXEHE",
        "XEHEEEEEEEEEEEEEEXIX",
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
        print("Ce jeu est inspiré de \"H2O\", sur la mini-console Storio.")
        print("https://www.vtechda.com/Store/ITMax/ContentDetail/FR_fre_1838_58-126805-000-289_False.html")
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
        if gamobj_mid not in ("X", "-"):
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
                    elif lvl_map_char in ("-", "|"):
                        main_pattern += lvl_map_char
                    else:
                        main_pattern += "."

        if gamobj_mid == "X":
            main_pattern = self.apply_replacement_patterns(main_pattern, self.patterns_tunnels_passing_by_replacement)
            main_pattern = main_pattern.replace("-", ".")
            main_pattern = main_pattern.replace("|", ".")
            matched_pattern = self.match_with_patterns(main_pattern, self.patterns_wall_simple)
            if matched_pattern is not None:
                return "pattern_" + matched_pattern
            return None

        if gamobj_mid == "-":
            main_pattern = self.apply_replacement_patterns(main_pattern, self.patterns_tunnels_passing_by_replacement)
            main_pattern = self.apply_replacement_patterns(main_pattern, self.patterns_replacement_tunnel_continuity)
            # TODO : pattern de suppression des tunnels en diagonale qui sont raccorché à rien.
            # ou alors, bourrin. on supprime tous les tunnels, sauf celui du milieu.
            matched_pattern = self.match_with_patterns(main_pattern, self.patterns_tunnel_simple)
            if matched_pattern is not None:
                return "pattern_" + matched_pattern
            return None


        return None


    def init_level(self):

        PATTERNS_TUNNELS_PASSING_BY_REPLACEMENT = """

            ***
            ***
            *--
            =>8:X

            ***
            ***
            --*
            =>6:X

            ***
            ***
            *-*
            =>7:X

            --*
            ***
            ***
            =>0:X

            *--
            ***
            ***
            =>2:X

            *-*
            ***
            ***
            =>1:X

            |**
            |**
            ***
            =>0:X

            ***
            |**
            |**
            =>6:X

            ***
            |**
            ***
            =>3:X

            **|
            **|
            ***
            =>2:X

            ***
            **|
            **|
            =>8:X

            ***
            **|
            ***
            =>5:X


        """

        PATTERNS_REPLACEMENT_TUNNEL_CONTINUITY = """

            *|*
            *|*
            ***
            =>2:X

            ***
            *--
            ***
            =>5:X

            ***
            *|*
            *|*
            =>7:X

            ***
            --*
            ***
            =>3:X

        """

        # TODO : faut pouvoir en mettre plusieurs sur la même ligne.
        PATTERNS_WALL_SIMPLE = """

            *X*
            XXX
            .XX

            *X*
            XXX
            XX.

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

        PATTERNS_TUNNEL_SIMPLE = """

            XXX
            .-X
            .XX

            ...
            .-X
            .XX

        """

        # TODO : rename var.
        self.patterns_tunnels_passing_by_replacement = self.compile_replace_patterns(PATTERNS_TUNNELS_PASSING_BY_REPLACEMENT)
        self.patterns_replacement_tunnel_continuity = self.compile_replace_patterns(PATTERNS_REPLACEMENT_TUNNEL_CONTINUITY)
        self.patterns_wall_simple = self.compile_match_patterns(PATTERNS_WALL_SIMPLE)
        self.patterns_tunnel_simple = self.compile_match_patterns(PATTERNS_TUNNEL_SIMPLE)

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

        # Juste pour libérer la mémoire.
        self.patterns_wall_simple = None

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
        if {"-", "="}.intersection(set(start_tile_objs + dest_tile_objs)) and move_dir in ("U", "D"):
            return False
        if {"|", "I"}.intersection(set(start_tile_objs + dest_tile_objs)) and move_dir in ("L", "R"):
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

        if ("=" in tile_data_new_pos or "I" in tile_data_new_pos) and self.hero_state == "gas":
            self.hero_alive = False
            tile_data_new_pos.append("gas_dead")
            print("Blarg ! Appuyez sur un bouton pour ressusciter")

        if "E" in tile_data_new_pos and self.hero_state == "water":
            self.hero_alive = False
            tile_data_new_pos.remove("E")
            tile_data_new_pos.append("wet_sponge")
            print("Blarg ! Appuyez sur un bouton pour ressusciter")

