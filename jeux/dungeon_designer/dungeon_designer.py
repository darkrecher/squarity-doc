# -------------------------------
# Script de résolution du puzzle "Dungeon Designer" sur CodinGame
# https://www.codingame.com/training/expert/dungeon-designer
# -------------------------------
# Ce superbe code a été réalisé avec l'aide de Squarity.
# Squarity est un moteur de jeu 2D.
# Vous dessinez un petit tileset, vous codez un peu de python,
# et hopla ! vous obtenez un jeu jouable dans votre navigateur web,
# que vous pouvez ensuite partager avec d'autres personnes.
# -------------------------------

# Image d'origine :
# https://s3.envato.com/files/103055288/01_dungeontiles_peview01.jpg

# Image utilisé dans le jeu :
# https://raw.githubusercontent.com/darkrecher/squarity-doc/master/jeux/dungeon_designer/dungeon_designer_tileset.png

"""
{
  "game_area": {
    "nb_tile_width": 13,
    "nb_tile_height": 21
  },
  "tile_size": 36,

  "img_coords": {
    "treasure": [52, 0],
    "empty": [98, 0],
    "wall": [145, 0],
    "monster": [194, 0],
    "red_transp": [0, 0],
    "gold": [234, 0],

    "osef": [0, 0]
  }
}
"""

SELECTED_TEST_INDEX = 3
RED_INTENSITY_MAX = 50

import math

EXAMPLE_FIRST = """
#.#####
#.#.#T#
#.#.#.#
#....X#
#####.#
"""

EXAMPLE_BIGGER_ONE = """
#.#########
#.#.#T#...#
#.#.#.###.#
#.#.#.....#
#.#.#####.#
#.#.#.#.#.#
#.#.#.#.#.#
#.#.#.#...#
#.#.#.###.#
#........X#
#########.#
"""

EXAMPLE_X_NOT_IN_FRONT_OF_BARRACKS = """
#.###########
#...#T..#...#
###.###.###.#
#...#.#.....#
###.#.#####.#
#.#.#.#.#.#.#
#.#.#.#.#.#.#
#...#...#...#
###.###.###.#
#.......#.#.#
#######.#.#.#
#.....#.#...#
#####.#.###.#
#...#.#.#.#.#
###.#.#.#.#.#
#..........X#
###########.#
#.#...#.....#
#.###.#####.#
#...........#
###########.#
"""

test_datas = (
    ((3, 2), (1723, 1579, 100000)),
    ((1, 1), (1619, 1699, 100000)),
    ((5, 5), (1619, 1607, 100000)),
    ((6, 10), (1619, 1663, 100000)),
    ((18, 12), (1619, 1699, 100000)),
    ((1, 7), (1747, 1811, 100000)),
    ((7, 1), (1831, 1667, 100000)),
)


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


# La question ultime à propos de la vie l'univers et le reste.
# print("quelle est le lcm de 14 et 21 ?", lcm(14, 21))


class Tile:
    def __init__(self, is_wall=False, special_gamobj=None):
        # self.adjacencies sera une liste de 8 éléments, contenant
        # des références vers les objets tiles adjacents.
        # l'ordre dans la liste indique les directions d'adjacences :
        # 701
        # 6*2
        # 543
        # Les tiles au bord de l'aire de jeu ont certains éléments
        # de cette liste à None.
        self.adjacencies = None
        self.is_wall = is_wall
        self.special_gamobj = special_gamobj
        self.red_intensity = None
        self.dist_to_entrance = None
        self.has_gold = False

    def get_gamobjs(self):
        gamobjs = []
        if self.is_wall:
            gamobjs.append("wall")
        else:
            gamobjs.append("empty")

        if self.red_intensity:
            gamobjs.extend(["red_transp"] * self.red_intensity)

        if self.special_gamobj is not None:
            gamobjs.append(self.special_gamobj)

        if self.has_gold:
            gamobjs.append("gold")

        return gamobjs

    def put_wall(self):
        self.is_wall = True

    def remove_wall(self):
        self.is_wall = False

    def get_codingame_char(self):
        if self.is_wall:
            return "#"
        if self.special_gamobj is None:
            return "."
        if self.special_gamobj == "treasure":
            return "T"
        if self.special_gamobj == "monster":
            return "X"
        raise Exception("Not supposed to happen.")


def on_traceback_add_gold_on_hero_path(tile):
    tile.has_gold = True
    return True


def on_traceback_put_monster_on_gold(tile):
    if tile.has_gold:
        if tile.special_gamobj != "treasure":
            tile.special_gamobj = "monster"
        tile.has_gold = False
        return False
    else:
        return True


class GameModel:
    def _make_adjacencies(self, x, y):
        """
        Renvoie les tiles adjacentes à la tile aux coordonnées x, y.
        On renvoie toujours une liste de 8 éléments (les 8 directions), mais certains éléments
        peuvent être None, si les coordonnées x, y sont sur un bord de l'aire de jeu.
        """
        adjacencies = (
            self.tiles[y - 1][x] if 0 <= y - 1 else None,
            self.tiles[y - 1][x + 1] if 0 <= y - 1 and x + 1 < self.map_w else None,
            self.tiles[y][x + 1] if x + 1 < self.map_w else None,
            self.tiles[y + 1][x + 1]
            if y + 1 < self.map_h and x + 1 < self.map_w
            else None,
            self.tiles[y + 1][x] if y + 1 < self.map_h else None,
            self.tiles[y + 1][x - 1] if y + 1 < self.map_h and 0 <= x - 1 else None,
            self.tiles[y][x - 1] if 0 <= x - 1 else None,
            self.tiles[y - 1][x - 1] if 0 <= y - 1 and 0 <= x - 1 else None,
        )
        return adjacencies

    def get_tile(self, map_x, map_y):
        return self.tiles[map_y][map_x]

    def wall_on_borders(self):
        for map_x in range(self.map_w):
            if map_x != 1:
                self.get_tile(map_x, 0).put_wall()
            if map_x != self.map_w - 2:
                self.get_tile(map_x, self.map_h - 1).put_wall()
        for map_y in range(self.map_h):
            self.get_tile(0, map_y).put_wall()
            self.get_tile(self.map_w - 1, map_y).put_wall()

        self.get_tile(1, 0).remove_wall()
        self.get_tile(self.map_w - 2, self.map_h - 1).remove_wall()

    def compute_random_val(self, puzzle_x, puzzle_y):
        # (R^(2^(x+y×W+1) mod lcm(P-1,Q-1)) mod P×Q)
        # pow(x, y, a)
        # (x ** y) % a
        val_inside = pow(2, puzzle_x + puzzle_y * self.puzzle_w + 1, self.rand_lcm_p_q)
        final_val = pow(self.rand_r, val_inside, self.rand_mul_p_q)
        return final_val % 2

    def put_wall_south_or_east(self, puzzle_x, puzzle_y):
        map_x = puzzle_x * 2 + 1
        map_y = puzzle_y * 2 + 1
        blum_blum_rand = self.compute_random_val(puzzle_x, puzzle_y)
        if blum_blum_rand:
            # wall to the east
            self.get_tile(map_x + 1, map_y).put_wall()
        else:
            # wall to the south
            self.get_tile(map_x, map_y + 1).put_wall()

    def put_walls_on_even_tiles(self):
        for map_x in range(self.map_w):
            for map_y in range(self.map_h):
                if map_x % 2 == 0 and map_y % 2 == 0:
                    self.get_tile(map_x, map_y).put_wall()

    def __init__(self):
        data_line_1, data_line_2 = get_input_data()
        self.puzzle_w, self.puzzle_h = data_line_1
        self.map_w = self.puzzle_w * 2 + 1
        self.map_h = self.puzzle_h * 2 + 1

        self.rand_p, self.rand_q, self.rand_r = data_line_2
        self.rand_lcm_p_q = lcm(self.rand_p - 1, self.rand_q - 1)
        self.rand_mul_p_q = self.rand_p * self.rand_q
        # print("le lcm de p-1, q-1 :", self.rand_lcm_p_q)
        self.tiles = []
        for map_y in range(self.map_h):
            line = []
            for map_x in range(self.map_w):
                line.append(Tile())
            self.tiles.append(line)

        # print("blum blum 0, 0 :", self.compute_random_val(0, 0))
        # print("blum blum 0, 1 :", self.compute_random_val(0, 1))

        # Définition des adjacences. Chaque objet Tile a une variable membre "adjacencies",
        # contenant des références vers les tiles adjacentes, selon les directions.
        for y in range(self.map_h):
            for x in range(self.map_w):
                adjacencies = self._make_adjacencies(x, y)
                self.tiles[y][x].adjacencies = adjacencies

        self.wall_on_borders()
        self.put_walls_on_even_tiles()
        for puzzle_x in range(self.puzzle_w - 1):
            for puzzle_y in range(self.puzzle_h - 1):
                self.put_wall_south_or_east(puzzle_x, puzzle_y)

        self.propagate_dijkstra()

        tiles_pot_treasure = []
        # Pour le futur : un petit itérateur qui parcourt toutes les tiles.
        # Ça éviterait de se faire ces deux boucles imbriquées.
        for map_x in range(self.map_w):
            for map_y in range(self.map_h):
                tile = self.get_tile(map_x, map_y)
                if not tile.is_wall:
                    tiles_pot_treasure.append(tile)

        tile_entrance_monster = self.get_tile(self.map_w - 2, self.map_h - 1)
        tiles_pot_treasure.remove(tile_entrance_monster)

        tile_farthest = max(tiles_pot_treasure, key=lambda tile: tile.dist_to_entrance)
        # print("tile_farthest", tile_farthest, tile_farthest.dist_to_entrance)
        tile_farthest.special_gamobj = "treasure"

        red_ratio = RED_INTENSITY_MAX / tile_farthest.dist_to_entrance

        for map_x in range(self.map_w):
            for map_y in range(self.map_h):
                tile = self.get_tile(map_x, map_y)
                if not tile.is_wall:
                    tile.red_intensity = int(tile.dist_to_entrance * red_ratio)

        tile_farthest.red_intensity = RED_INTENSITY_MAX * 2

        self.make_traceback_dist_to_entrance(
            tile_farthest, on_traceback_add_gold_on_hero_path
        )
        self.make_traceback_dist_to_entrance(
            tile_entrance_monster,
            on_traceback_put_monster_on_gold,
        )
        # print("gold on treasure :", tile_farthest.has_gold)
        # print("special_gamobj :", tile_farthest.special_gamobj)

    def propagate_dijkstra(self):
        """
        Définit la variable membre dist_to_entrance de toutes les tiles n'ayant pas de murs.
        """
        # On commence par la case à droite de la la case en haut à gauche.
        # C'est à dire l'entrée du dungeon.
        # C'est par là qu'arrivent les vilains héros.
        tile_start = self.tiles[0][0].adjacencies[2]
        tiles_to_process = [tile_start]
        tile_start.dist_to_entrance = 0

        while tiles_to_process:
            tile_current = tiles_to_process.pop(0)
            dist_current = tile_current.dist_to_entrance + 1

            for tile_adj in tile_current.adjacencies[::2]:
                if tile_adj is not None:
                    if not tile_adj.is_wall and tile_adj.dist_to_entrance is None:
                        tile_adj.dist_to_entrance = dist_current
                        tiles_to_process.append(tile_adj)

    def make_traceback_dist_to_entrance(self, tile_start, on_traceback_tile):
        tile_current = tile_start
        next_dist = tile_current.dist_to_entrance - 1
        must_continue = on_traceback_tile(tile_current)

        while next_dist and must_continue:
            found_next = False
            for tile_adj in tile_current.adjacencies[::2]:
                if (
                    tile_adj is not None
                    and tile_adj.dist_to_entrance is not None
                    and tile_adj.dist_to_entrance == next_dist
                ):
                    tile_current = tile_adj
                    found_next = True
            if not found_next:
                raise Exception(
                    f"Impossible de trouver la prochaine tile de {tile_current}"
                )
            next_dist = tile_current.dist_to_entrance - 1
            must_continue = on_traceback_tile(tile_current)

    def export_all_tiles(self):
        exported_tiles = []
        for map_y in range(self.map_h):
            exported_line = []
            for map_x in range(self.map_w):
                tile = self.tiles[map_y][map_x]
                exported_line.append(tile.get_gamobjs())
            exported_tiles.append(exported_line)

        return exported_tiles

    def print_codingame_answer(self):
        for map_y in range(self.map_h):
            current_str_line = ""
            for map_x in range(self.map_w):
                current_str_line += self.get_tile(map_x, map_y).get_codingame_char()
            print(current_str_line)

    def on_game_event(self, event_name):
        print()
        self.print_codingame_answer()
        print()


i_am_in_coding_game = False


def get_input_data():
    global i_am_in_coding_game
    if i_am_in_coding_game:
        data_line_1 = list(map(int, input().split()))
        data_line_2 = list(map(int, input().split()))
        return data_line_1, data_line_2
    else:
        return test_datas[SELECTED_TEST_INDEX]


if __name__ == "__main__":
    i_am_in_coding_game = True
    game_model = GameModel()
    game_model.print_codingame_answer()
