# https://i.ibb.co/k3NBpGq/grreeny.png
# https://i.ibb.co/yFrz7Pk/grreeny.png
# https://i.ibb.co/FbVkCRz/grreeny.png

"""
  {
    "game_area": {
        "nb_tile_width": 7,
        "nb_tile_height": 7
    },
    "tile_size": 32,
    "img_coords": {
      "grreeny": [0,  0],
      "col_red": [32, 0],
      "col_grn": [64, 0],
      "col_blu": [96, 0],

      "col_red_red_blu": [128, 0],
      "col_red_grn_grn": [0,  32],
      "col_red_red_grn": [32, 32],
      "col_grn_blu_blu": [64, 32],
      "col_grn_grn_blu": [96, 32],
      "col_red_blu_blu": [128, 32],

      "timer_1": [0, 64],
      "timer_2": [32, 64],
      "timer_3": [64, 64],

      "skull": [160, 0],
      "background": [160, 32],

      "void": [0, 0]
    }
  }
"""

"""
TODO :
 X générer les couleurs de plus en plus vite.
 X un timer 3-2-1 lors de la génération d'une couleur.
 X on peut déclencher une génération sur grreeny (il a 3 tours pour se pousser)
 X fin de la partie lorsqu'une couleur est générée sur greeny
 - action 1 : glandouille. on avance d'un tour, ça augmente le score de 5, et ça génère une couleur.
 - action 2 : message qui donne le score, et qui fait réinitialiser si on re-appuie dessus.
 - redémarrage de partie lorsqu'on fait l'action 2 deux fois.
 X icône de tête de mort lorsque greeny meurt, et message que il faut faire l'action 2.
 - calcul et affichage du score à la fin de la partie.
 - dessin un peu mieux foutus (meme si ce sera pas top)
 X tile de background.
 - docstring pour expliquer le jeu et donner le pitch.
 - publier tout ce bazar, créer la tinyurl.
"""

import random

DIR_INT_FROM_STR = {
    "U": 0,
    "R": 2,
    "D": 4,
    "L": 6,
}


def dir_turn_clockwise(init_dir):
    return (init_dir + 2) % 8


def dir_turn_anticlockwise(init_dir):
    return (init_dir - 2) % 8


class Tile:

    GEN_MULTICOL_OK = 0
    GEN_MULTICOL_FAIL_COL = 1
    GEN_MULTICOL_FAIL_GRREENY = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.adjacencies = None
        self.has_grreeny = False
        self.reset_all()

    def reset_all(self):
        self.has_grreeny = False
        self.set_color(0, 0, 0)
        self.timer = 0
        self.has_skull = False

    def set_color(self, red, grn, blu):
        self.col_red = red
        self.col_grn = grn
        self.col_blu = blu

    def set_random_multicol(self):
        rgb_random = [2, 1, 0]
        random.shuffle(rgb_random)
        self.set_color(*rgb_random)

    def has_color(self):
        return bool(self.col_red) or bool(self.col_grn) or bool(self.col_blu)

    def is_mono_color(self):
        nb_distinct_colors = sum(
            (
                int(bool(self.col_red)),
                int(bool(self.col_grn)),
                int(bool(self.col_blu)),
            )
        )
        return nb_distinct_colors == 1

    def has_same_mono_color(self, other_tile):
        if not self.is_mono_color():
            return False
        if not other_tile.is_mono_color():
            return False
        return all(
            (
                bool(self.col_red) == bool(other_tile.col_red),
                bool(self.col_grn) == bool(other_tile.col_grn),
                bool(self.col_blu) == bool(other_tile.col_blu),
            )
        )

    def is_splittable(self, dir_grreeny):
        if self.is_mono_color():
            return False
        all_color = (
            self.col_red,
            self.col_grn,
            self.col_blu,
        )
        if sum(all_color) != 3:
            return False
        dir_grreeny_c = dir_turn_clockwise(dir_grreeny)
        dir_grreeny_a_c = dir_turn_anticlockwise(dir_grreeny)
        for dir_ in (dir_grreeny, dir_grreeny_c, dir_grreeny_a_c):
            adj_tile = self.adjacencies[dir_]
            if adj_tile is None:
                return False
            if adj_tile.has_color():
                return False
        return True

    def render(self):
        gamobjs = ["background"]

        if self.is_mono_color():
            # Le 0.7 est un peu arbitraire. Pouet.
            gamobjs.extend(["col_red"] * int(self.col_red**0.7))
            gamobjs.extend(["col_grn"] * int(self.col_grn**0.7))
            gamobjs.extend(["col_blu"] * int(self.col_blu**0.7))
        elif self.has_color():
            gamobj_name = (
                "col"
                + "_red" * self.col_red
                + "_grn" * self.col_grn
                + "_blu" * self.col_blu
            )
            gamobjs.append(gamobj_name)

        if self.has_grreeny:
            if self.has_skull:
                gamobjs.append("skull")
            else:
                gamobjs.append("grreeny")

        if self.timer:
            gamobjs.append(f"timer_{self.timer}")

        return gamobjs

    def set_timer(self):
        self.timer = 3

    def countdown_and_generate(self):
        if not self.timer:
            return Tile.GEN_MULTICOL_OK

        self.timer -= 1
        if self.timer:
            return Tile.GEN_MULTICOL_OK
        if not self.timer:
            if self.has_color():
                return Tile.GEN_MULTICOL_FAIL_COL
            elif self.has_grreeny:
                return Tile.GEN_MULTICOL_FAIL_GRREENY
            else:
                self.set_random_multicol()
                return Tile.GEN_MULTICOL_OK


class GameModel:

    GEN_POINTS_THRESHOLD = 1000
    GEN_POINTS_INC_INC = 0.125

    def __init__(self):
        self.w = 7
        self.h = 7
        self.turn_index = 0
        self.gen_points = 0
        self.gen_points_inc = 30.0
        self.tiles = []
        for y in range(self.h):
            line = []
            for x in range(self.w):
                line.append(Tile(x, y))
            self.tiles.append(line)

        for y in range(self.h):
            for x in range(self.w):
                self.get_tile(x, y).adjacencies = self._make_adjacencies(x, y)

        self.start_game()

    def start_game(self):
        for line in self.tiles:
            for tile in line:
                tile.reset_all()

        self.grreeny_coords = (3, 4)
        self.get_tile(*self.grreeny_coords).has_grreeny = True

        for _ in range(2):
            tile_generation = self.random_select_empty_tile(False)
            tile_generation.set_random_multicol()

        self.game_ended = False

    def _make_adjacencies(self, x, y):
        """
        Renvoie les tiles adjacentes à la tile située aux coordonnées x, y.
        On renvoie toujours une liste de 8 éléments (les 8 directions), mais certains éléments
        peuvent être None, si les coordonnées x, y sont sur un bord de l'aire de jeu.
        """
        adjacencies = (
            self.tiles[y - 1][x] if 0 <= y - 1 else None,
            self.tiles[y - 1][x + 1] if 0 <= y - 1 and x + 1 < self.w else None,
            self.tiles[y][x + 1] if x + 1 < self.w else None,
            self.tiles[y + 1][x + 1] if y + 1 < self.h and x + 1 < self.w else None,
            self.tiles[y + 1][x] if y + 1 < self.h else None,
            self.tiles[y + 1][x - 1] if y + 1 < self.h and 0 <= x - 1 else None,
            self.tiles[y][x - 1] if 0 <= x - 1 else None,
            self.tiles[y - 1][x - 1] if 0 <= y - 1 and 0 <= x - 1 else None,
        )
        return adjacencies

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def export_all_tiles(self):
        exported_tiles = []
        for line_tiles in self.tiles:
            exported_line = []
            for tile in line_tiles:
                exported_line.append(tile.render())
            exported_tiles.append(exported_line)

        return exported_tiles

    def random_select_empty_tile(self, can_select_grreeny):
        if can_select_grreeny:
            func_check_tile = lambda tile: (not tile.has_color() and not tile.timer)
        else:
            func_check_tile = lambda tile: (
                not tile.has_color() and not tile.timer and not tile.has_grreeny
            )
        empty_tiles_border = []
        empty_tiles_inside = []

        for line in self.tiles:
            for tile in line:
                if func_check_tile(tile):
                    if any(
                        (
                            tile.x == 0,
                            tile.x == self.w - 1,
                            tile.y == 0,
                            tile.y == self.h - 1,
                        )
                    ):
                        empty_tiles_border.append(tile)
                    else:
                        empty_tiles_inside.append(tile)

        if empty_tiles_inside:
            return random.choice(empty_tiles_inside)
        elif empty_tiles_border:
            return random.choice(empty_tiles_border)
        else:
            return None

    def move_color(self, tile_src, tile_dst):
        tile_dst.col_red = tile_src.col_red
        tile_dst.col_grn = tile_src.col_grn
        tile_dst.col_blu = tile_src.col_blu
        tile_src.col_red = 0
        tile_src.col_grn = 0
        tile_src.col_blu = 0

    def merge_color(self, tile_src, tile_dst):
        tile_dst.col_red += tile_src.col_red
        tile_dst.col_grn += tile_src.col_grn
        tile_dst.col_blu += tile_src.col_blu
        tile_src.col_red = 0
        tile_src.col_grn = 0
        tile_src.col_blu = 0

    def split_color(self, tile, dir_grreeny):
        dir_grreeny_c = dir_turn_clockwise(dir_grreeny)
        dir_grreeny_a_c = dir_turn_anticlockwise(dir_grreeny)
        rgb_front = (
            int(tile.col_red == 1),
            int(tile.col_grn == 1),
            int(tile.col_blu == 1),
        )
        rgb_side = (
            int(tile.col_red == 2),
            int(tile.col_grn == 2),
            int(tile.col_blu == 2),
        )
        tile_front = tile.adjacencies[dir_grreeny]
        tile_front.set_color(*rgb_front)
        tile_side = tile.adjacencies[dir_grreeny_c]
        tile_side.set_color(*rgb_side)
        tile_side = tile.adjacencies[dir_grreeny_a_c]
        tile_side.set_color(*rgb_side)
        tile.set_color(0, 0, 0)

    def move_grreeny(self, move_dir):
        """
        Déplace greeny, ainsi que les couleurs.
        Renvoie un booléen, indiquant si un mouvement
        a pu être effectué, ou pas.
        """
        tile_g_cur = self.get_tile(*self.grreeny_coords)
        tile_g_next = tile_g_cur.adjacencies[move_dir]
        if tile_g_next is None:
            return False

        if tile_g_next.has_color():
            if tile_g_next.is_splittable(move_dir):
                self.split_color(tile_g_next, move_dir)
            else:
                tile_g_next_next = tile_g_next.adjacencies[move_dir]
                if tile_g_next_next is None:
                    return False
                if tile_g_next_next.has_color():
                    if tile_g_next.has_same_mono_color(tile_g_next_next):
                        self.merge_color(tile_g_next, tile_g_next_next)
                    else:
                        return False
                else:
                    self.move_color(tile_g_next, tile_g_next_next)

        tile_g_cur.has_grreeny = False
        self.grreeny_coords = (tile_g_next.x, tile_g_next.y)
        tile_g_next.has_grreeny = True
        return True

    def on_game_event(self, event_name):

        move_dir = DIR_INT_FROM_STR.get(event_name)
        advanced_turn = False
        if not self.game_ended:
            if move_dir is not None:
                move_result = self.move_grreeny(move_dir)
                self.turn_index += 1
                advanced_turn = True
        else:
            if event_name == "action_2":
                print("-" * 20)
                self.start_game()

        if advanced_turn:

            for line in self.tiles:
                for tile in line:
                    gen_result = tile.countdown_and_generate()
                    if gen_result == Tile.GEN_MULTICOL_FAIL_COL:
                        print("TODO fail col", gen_result)
                    elif gen_result == Tile.GEN_MULTICOL_FAIL_GRREENY:
                        self.game_ended = True
                        self.get_tile(*self.grreeny_coords).has_skull = True
                        print("TODO. Fin de la partie. show score")
                        print("Appuyez sur le bouton '2' pour redémarrer une partie.")

            self.gen_points += int(self.gen_points_inc)
            self.gen_points_inc += GameModel.GEN_POINTS_INC_INC
            if self.gen_points >= GameModel.GEN_POINTS_THRESHOLD:
                self.gen_points -= GameModel.GEN_POINTS_THRESHOLD
                tile_generation = self.random_select_empty_tile(True)
                if tile_generation is None:
                    pass
                    print("fail gen color")
                else:
                    tile_generation.set_timer()
