# https://i.ibb.co/mczrkx2/game-of-nolife-tileset.png (old)
# https://i.ibb.co/qgVyDdR/game-of-nolife-tileset.png (old)
# https://i.ibb.co/VHQh8sr/game-of-nolife-tileset.png

"""
{
  "game_area": {
    "nb_tile_width": 50,
    "nb_tile_height": 40
  },
  "tile_size": 4,
  "img_coords": {
    "red_01": [0, 0],
    "red_02": [4, 0],
    "red_03": [8, 0],
    "red_04": [12, 0],
    "red_05": [16, 0],
    "red_06": [20, 0],
    "red_07": [24, 0],
    "red_08": [28, 0],
    "red_09": [32, 0],
    "red_10": [36, 0],
    "red_11": [40, 0],
    "red_12": [44, 0],
    "red_13": [48, 0],
    "red_14": [52, 0],
    "red_15": [56, 0],
    "red_16": [60, 0],
    "red_town_1x1": [68, 0],
    "red_controls": [64, 0],
    "red_road_horiz": [72, 0],
    "red_road_vertic": [76, 0],
    "red_road_both": [80, 0],
    "red_cursor": [12, 8],

    "blu_01": [0, 4],
    "blu_02": [4, 4],
    "blu_03": [8, 4],
    "blu_04": [12, 4],
    "blu_05": [16, 4],
    "blu_06": [20, 4],
    "blu_07": [24, 4],
    "blu_08": [28, 4],
    "blu_09": [32, 4],
    "blu_10": [36, 4],
    "blu_11": [40, 4],
    "blu_12": [44, 4],
    "blu_13": [48, 4],
    "blu_14": [52, 4],
    "blu_15": [56, 4],
    "blu_16": [60, 4],
    "blu_town_1x1": [68, 4],
    "blu_controls": [64, 4],
    "blu_road_horiz": [72, 8],
    "blu_road_vertic": [76, 8],
    "blu_road_both": [80, 8],
    "blu_cursor": [12, 8],


    "bla": [0, 0]

  }
}
"""

# Prochains trucs :
# fonction pour répartir équitablement les units sur les routes.
# petit code de démo, avec une grande route pleine de unit.
# On y connecte une route plus petite, avec moins de unit.
# Création d'une ville, gestion des suburbs.

import random

# Moche, mais ça permet de convertir plus rapidement.
GAMOBJ_NAME_TO_NB_UNIT = tuple(
    "00;01;02;03;04;05;06;07;08;09;10;11;12;13;14;15;16".split(";")
)

# TODO crap
#                if x < 10 and y >= self.h-15:
#                    unit_val = 1 # min((x*(self.h-y)) // 5, 16)
#                if x >= self.w-10 and y < 15:
#                    unit_val = 1 # min(((self.w-x)*y) // 5, 16)
def coord_move(x, y, direction):
    if direction == "R":
        x += 1
    elif direction == "L":
        x -= 1
    if direction == "D":
        y += 1
    if direction == "U":
        y -= 1
    return (x, y)


MODE_TRAVEL_VERTICALLY = 1
MODE_TRAVEL_HORIZONTALLY = 2


class Player:
    def __init__(self, player_id, w, h, color, game_master, rightward, downward):
        self.player_id = player_id
        self.w = w
        self.h = h
        self.color = color
        self.game_master = game_master
        self.rightward = rightward
        self.downward = downward
        self._controlled_tiles = []
        self._controlled_roads = []
        # Faut indexer là-dessus, parce qu'en général, on n'a plein de bare tiles
        # avec une seule unité, et pas beaucoup avec plusieurs. Donc quand faut
        # bouger les "plusieurs", c'est mieux de savoir tout de suite où elles sont.
        self.controlled_bare_tiles_with_many_units = []
        self.town_tiles = []
        self.total_units = 0

    def __str__(self):
        return "player_%s" % self.player_id

    def add_controlled_tile(self, tile):
        self._controlled_tiles.append(tile)
        # TODO : faut trier ces tiles, selon le sens dans lequel on les résout.
        # pour des trucs genre le mouvement en diagonal arrière, y'a besoin.
        # TODO : Ou alors, on trie que quand y'a besoin. Comme ça, on triera pas plusieurs fois pour rien.

    def remove_controlled_tile(self, tile):
        self._controlled_tiles.remove(tile)
        # TODO : faut trier ces tiles, selon le sens dans lequel on les résout.
        # pour des trucs genre le mouvement en diagonal arrière, y'a besoin.
        # TODO : même chose pour les roads et les bare_tiles_many.

    def add_controlled_road(self, tile):
        self._controlled_roads.append(tile)

    def remove_controlled_road(self, tile):
        self._controlled_roads.remove(tile)


class Town:
    def __init__(self, x_left, y_up, player_owner, size):
        self.x_left = x_left
        self.y_up = y_up
        self.player_owner = player_owner
        self.size = size
        self.rect = (x, y, x + size, y + size)


REVERSE_DIRS = (4, 5, 6, 7, 0, 1, 2, 3)


class Suburb:
    """
    Un suburb peut contenir des towns de différents players.
    """

    def __init__(self):
        self.town_tiles = []
        self.around_tiles = []
        self.roads = []
        # Liste de 4 int. x1, y1, x2, y2. On englobe les towns et les cases autour.
        self.bounding_rect = None

    def merge(self, other_suburb):
        pass


class Tile:

    GAMOBJ_BACKGROUND_FROM_ROADS = {
        (False, False): "_controls",
        (True, False): "_road_horiz",
        (False, True): "_road_vertic",
        (True, True): "_road_both",
    }

    def __init__(self, x, y, linked_gamobjs, game_master):
        self.x = x
        self.y = y
        self.linked_gamobjs = linked_gamobjs
        self.game_master = game_master
        self.adjacencies = [None for _ in range(8)]
        self.road_adjacencies_same_player = [False for _ in range(8)]
        self.road_vertic = False
        self.road_horiz = False
        self.player_owner = None
        self.nb_unit = 0
        self.town = None
        self.suburb_owner = None

    def _update_linked_gamobjs(self):
        if self.player_owner is None:
            # TODO : il manque le cas des routes sans owner.
            self.linked_gamobjs[:] = []
            return
        color = self.player_owner.color
        gamobj_bg_suffix = Tile.GAMOBJ_BACKGROUND_FROM_ROADS[
            (self.road_horiz, self.road_vertic)
        ]
        gamobj_background = color + gamobj_bg_suffix
        gamobj_unit = color + "_" + GAMOBJ_NAME_TO_NB_UNIT[self.nb_unit]
        self.linked_gamobjs[:] = [gamobj_background, gamobj_unit]

    def __str__(self):
        return "".join(
            map(
                str,
                (
                    "Tile",
                    " x:",
                    self.x,
                    " y:",
                    self.y,
                    " player_owner:",
                    self.player_owner,
                    " nb_unit:",
                    self.nb_unit,
                    " town:",
                    self.town,
                    " road:",
                    "|" * self.road_vertic,
                    "-" * self.road_horiz,
                    " road_adjacencies_same_player",
                    list(map(int, self.road_adjacencies_same_player)),
                    " suburb_owner:",
                    self.suburb_owner,
                ),
            )
        )

    def _update_road_adjacency(self, direction):
        other_tile = self.adjacencies[direction]
        if other_tile is None:
            self.road_adjacencies_same_player[direction] = False
            return

        if direction in (0, 4):
            roads_to_check = self.road_vertic and other_tile.road_vertic
        elif direction in (6, 2):
            roads_to_check = self.road_horiz and other_tile.road_horiz
        else:
            # Not supposed to happen.
            return

        connection_ok = all(
            (
                roads_to_check,
                self.player_owner is not None,
                self.player_owner == other_tile.player_owner,
            )
        )

        self.road_adjacencies_same_player[direction] = connection_ok
        reversed_direction = REVERSE_DIRS[direction]
        other_tile.road_adjacencies_same_player[reversed_direction] = connection_ok

    def _update_all_road_adjacencies(self):
        self._update_road_adjacency(0)
        self._update_road_adjacency(2)
        self._update_road_adjacency(4)
        self._update_road_adjacency(6)

    def _update_all_road_adjacencies_with_current_roads(self):
        if self.road_horiz:
            self._update_road_adjacency(2)
            self._update_road_adjacency(6)
        if self.road_vertic:
            self._update_road_adjacency(0)
            self._update_road_adjacency(4)

    def add_unit(self, player, qty=1):
        if not qty:
            return

        initial_nb_unit = self.nb_unit
        if self.player_owner == player:
            # Pas de check pour vérifier que ça dépasse pas 16. Faut le faire avant.
            self.nb_unit += qty
            player.total_units += qty

        elif self.player_owner is None:
            self.player_owner = player
            player.add_controlled_tile(self)
            if self.road_vertic or self.road_horiz:
                player.add_controlled_road(self)
            self.nb_unit += qty
            player.total_units += qty
        else:
            if qty < self.nb_unit:
                self.remove_unit(qty)
            else:
                qty_unit_left_after = qty - self.nb_unit
                self.remove_unit(self.nb_unit)
                # Ha ha. Récursivité. Mais juste une seule fois.
                self.add_unit(player, qty_unit_left_after)

        if (
            not self.road_vertic
            and not self.road_horiz
            and self.town is None
            and self.nb_unit > 1
            and initial_nb_unit <= 1
        ):
            self.player_owner.controlled_bare_tiles_with_many_units.append(self)

        self._update_all_road_adjacencies_with_current_roads()
        self._update_linked_gamobjs()

    def remove_unit(self, qty=1):
        if not qty:
            return
        if self.player_owner is None:
            raise Exception("Not supposed to happen.")

        initial_nb_unit = self.nb_unit
        qty = min(qty, self.nb_unit)
        self.nb_unit -= qty
        self.player_owner.total_units -= qty

        if (
            not self.road_vertic
            and not self.road_horiz
            and self.town is None
            and self.nb_unit <= 1
            and initial_nb_unit > 1
        ):
            self.player_owner.controlled_bare_tiles_with_many_units.remove(self)

        if self.nb_unit == 0:
            self.player_owner.remove_controlled_tile(self)
            if self.road_vertic or self.road_horiz:
                player.remove_controlled_road(self)
            self.player_owner = None

        self._update_all_road_adjacencies_with_current_roads()
        self._update_linked_gamobjs()

    def add_road(self, horiz=False, vertic=False):
        if not (horiz or vertic):
            return
        if horiz == self.road_horiz and vertic == self.road_vertic:
            return

        previous_road_qty = self.road_horiz + self.road_vertic
        self.road_horiz = self.road_horiz or horiz
        self.road_vertic = self.road_vertic or vertic
        current_road_qty = self.road_horiz + self.road_vertic
        self._update_all_road_adjacencies_with_current_roads()
        if previous_road_qty == 0 and current_road_qty > 0:
            self.player_owner.add_controlled_road(self)
        self._update_linked_gamobjs()


class GameMaster:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.game_area = []
        self.gamobjs_to_export = []
        for y in range(self.h):
            line = []
            line_gamobjs = []
            for x in range(self.w):
                cell_gamobjs = []
                line_gamobjs.append(cell_gamobjs)
                tile = Tile(x, y, cell_gamobjs, self)
                line.append(tile)
            self.gamobjs_to_export.append(tuple(line_gamobjs))
            self.game_area.append(tuple(line))
        self.game_area = tuple(self.game_area)
        self.gamobjs_to_export = tuple(self.gamobjs_to_export)

        # Définition des adjacences de tiles.
        for y in range(self.h):
            for x in range(self.w):
                adjacencies = self.make_adjacencies(x, y)
                self.game_area[y][x].adjacencies = adjacencies

        self.suburbs = []
        self.towns = []

        # TODO : Faut les créer en dehors ces trucs. Et les passer en params.
        player_0 = Player(
            0, self.w, self.h, "red", self, rightward=True, downward=False
        )
        player_1 = Player(
            1, self.w, self.h, "blu", self, rightward=False, downward=True
        )
        self.players = {0: player_0, 1: player_1}

    def make_adjacencies(self, x, y):
        adjacencies = (
            self.game_area[y - 1][x] if 0 <= y - 1 else None,
            self.game_area[y - 1][x + 1] if 0 <= y - 1 and x + 1 < self.w else None,
            self.game_area[y][x + 1] if x + 1 < self.w else None,
            self.game_area[y + 1][x + 1] if y + 1 < self.h and x + 1 < self.w else None,
            self.game_area[y + 1][x] if y + 1 < self.h else None,
            self.game_area[y + 1][x - 1] if y + 1 < self.h and 0 <= x - 1 else None,
            self.game_area[y][x - 1] if 0 <= x - 1 else None,
            self.game_area[y - 1][x - 1] if 0 <= y - 1 and 0 <= x - 1 else None,
        )
        return adjacencies

    def move_unit_without_check(self, x_source, y_source, x_dest, y_dest, qty=1):
        """
        On vérifie pas les changements d'owner.
        À utiliser que quand on est sûr de ce qu'on fait.
        Par exemple, pour équilibrer les unités entre deux routes adjacentes.
        """
        # TODO
        pass


def test_add_and_remove_unit(game_master):
    game_master.game_area[2][2].add_unit(game_master.players[0])
    game_master.game_area[3][2].add_unit(game_master.players[0], 2)
    game_master.game_area[3][2].add_unit(game_master.players[1])
    game_master.game_area[3][2].add_unit(game_master.players[1])
    print("check 1. tile player 0")
    for tile in game_master.players[0]._controlled_tiles:
        print(tile)
    print("check 1. tile player 1")
    for tile in game_master.players[1]._controlled_tiles:
        print(tile)

    game_master.game_area[3][2].add_unit(game_master.players[1])
    print("check 2. tile player 0")
    for tile in game_master.players[0]._controlled_tiles:
        print(tile)
    print("check 2. tile player 1")
    for tile in game_master.players[1]._controlled_tiles:
        print(tile)

    game_master.game_area[3][2].add_unit(game_master.players[0], 5)
    print("check 3. tile player 0")
    for tile in game_master.players[0]._controlled_tiles:
        print(tile)
    print("check 3. tile player 1")
    for tile in game_master.players[1]._controlled_tiles:
        print(tile)


def test_adjacencies_and_add_roads(game_master):
    for adj_tile in game_master.game_area[1][1].adjacencies:
        print(str(adj_tile))
    print("")
    for adj_tile in game_master.game_area[4][4].adjacencies:
        print(str(adj_tile))
    print("")
    game_master.game_area[2][1].add_unit(game_master.players[0], 2)
    game_master.game_area[1][1].add_unit(game_master.players[0])
    print(game_master.game_area[1][1])
    print(game_master.game_area[2][1])
    print("add roads vertic")
    game_master.game_area[1][1].add_road(vertic=True)
    game_master.game_area[2][1].add_road(vertic=True)
    print(game_master.game_area[1][1])
    print(game_master.game_area[2][1])
    print("")
    print(game_master.players[0]._controlled_roads)


def main():
    game_master = GameMaster(5, 5)
    test_adjacencies_and_add_roads(game_master)


if __name__ == "__main__":
    main()


class GameModel:
    def __init__(self):
        self.w = 50
        self.h = 40
        self.game_master = GameMaster(self.w, self.h)

        test_adjacencies_and_add_roads(self.game_master)

        # TODO : crap.
        # self.players[0].set_other_players((self.players[1], ))
        # self.players[1].set_other_players((self.players[0], ))
        # self.nb_players = len(self.players)
        self.must_start = True

    def export_all_tiles(self):
        return self.game_master.gamobjs_to_export

    def on_process_turn(self):
        self.update_indexations()
        self.players[0].process_turn()
        # self.players[1].process_turn()
        self.update_tile_to_export()
        # TODO : calculer approximativement un délai plus ou moins long selon la quantité de trucs à gérer.
        return (
            """ { "delayed_actions": [ {"name": "process_turn", "delay_ms": 20} ] } """
        )

    def on_game_event(self, event_name):
        # TODO crap.
        return

        if event_name == "process_turn":
            return self.on_process_turn()
        if self.must_start:
            self.must_start = False
            return """ { "delayed_actions": [ {"name": "process_turn", "delay_ms": 10} ] } """
        else:
            for player in self.players:
                player.mode += 1
                # TODO : ça c'est crade.
                if player.mode > 3:
                    player.mode = 0
                print("player.mode", player.mode, player.color)
