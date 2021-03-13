# https://i.ibb.co/mczrkx2/game-of-nolife-tileset.png (old)
# https://i.ibb.co/qgVyDdR/game-of-nolife-tileset.png (old)
# https://i.ibb.co/VHQh8sr/game-of-nolife-tileset.png

"""
{
  "game_area": {
    "nb_tile_width": 20,
    "nb_tile_height": 20
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

    "red_town_build_00": [0, 0],
    "red_town_build_01": [20, 8],
    "red_town_build_02": [24, 8],
    "red_town_build_03": [28, 8],
    "red_town_build_04": [32, 8],
    "red_town_build_05": [36, 8],
    "red_town_build_06": [40, 8],
    "red_town_build_07": [44, 8],
    "red_town_build_08": [48, 8],
    "red_town_build_09": [52, 8],

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
    "blu_road_horiz": [72, 4],
    "blu_road_vertic": [76, 4],
    "blu_road_both": [80, 4],
    "blu_cursor": [12, 8],

    "blu_town_build_00": [0, 0],
    "blu_town_build_01": [20, 8],
    "blu_town_build_02": [24, 8],
    "blu_town_build_03": [28, 8],
    "blu_town_build_04": [32, 8],
    "blu_town_build_05": [36, 8],
    "blu_town_build_06": [40, 8],
    "blu_town_build_07": [44, 8],
    "blu_town_build_08": [48, 8],
    "blu_town_build_09": [52, 8],

    "neutral_road_horiz": [72, 8],
    "neutral_road_vertic": [76, 8],
    "neutral_road_both": [80, 8],

    "bla": [0, 0]

  }
}
"""

# Prochains trucs :
# Création d'une ville, gestion des suburbs.
# Des missiles bactériologiques !!! Qui partent en diagonale depuis une ville.

import random

# Moche, mais ça permet de convertir plus rapidement.
GAMOBJ_NAME_TO_NB_UNIT = tuple(
    "00;01;02;03;04;05;06;07;08;09;10;11;12;13;14;15;16".split(";")
)

# TODO : crap ??
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


NB_TURNS_TOWN_BUILDING = 9
NB_TURNS_TOWN_BUILDING_TIMEOUT = 25


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
        self.tile_building_town = None
        self.building_time = 0

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

    def move_unit_without_check(self, tile_source, tile_dest, qty=1):
        """
        On vérifie pas les changements d'owner.
        À utiliser que quand on est sûr de ce qu'on fait.
        Par exemple, pour équilibrer les unités entre deux routes adjacentes.
        """
        tile_source.nb_unit -= qty
        tile_dest.nb_unit += qty
        tile_source._update_linked_gamobjs()
        tile_dest._update_linked_gamobjs()

    def conquest_road(self):
        for tile in self._controlled_roads:
            if tile.nb_unit > 2:
                for adj_tile in tile.adjacencies[::2]:
                    if (
                        adj_tile is not None
                        and (adj_tile.road_horiz or adj_tile.road_vertic)
                        and adj_tile.player_owner is None
                    ):
                        tile.remove_unit()
                        adj_tile.add_unit(self)

    def spread_units_on_roads(self):
        for tile in self._controlled_roads:
            if tile.town_building_step:
                # La tile qui construit une ville ne transfère pas ses unités aux autres.
                continue
            nb_unit_source = tile.nb_unit
            # TODO : on itère sur les 8 cases alors que y'aurait besoin que de 2.
            for adj_tile, adj_is_road in zip(
                tile.adjacencies, tile.road_adjacencies_same_player
            ):
                if (
                    adj_is_road
                    and nb_unit_source > 2
                    and nb_unit_source - adj_tile.nb_unit > 1
                ):
                    self.move_unit_without_check(tile, adj_tile)

    def process_town_building(self):
        if self.tile_building_town is None:
            return
        self.building_time += 1
        if self.building_time >= NB_TURNS_TOWN_BUILDING_TIMEOUT:
            # La construction de la ville a pris trop de temps.
            # Parce que les unités qui sont dessus n'ont pas arrêté de se faire éliminer.
            # Tant pis, on arrête tout.
            self.tile_building_town.cancel_town_building()
            self.building_time = 0
            self.tile_building_town = None
            return

        if self.tile_building_town.nb_unit >= 16:
            # Pas de problème, il y a toujours 16 unités dans la ville en construction.
            # On avance la construction de 1.
            self.tile_building_town.advance_town_building()
            if self.tile_building_town.town_building_step >= NB_TURNS_TOWN_BUILDING:
                # TODO : faut créer la ville, voyez.
                self.building_time = 0
                self.tile_building_town = None
            return

        # On peut pas avancer la construction de la ville, car y'a des unités qui sont parties.
        # On essaie de ramener des unités autour pour reprendre la construction.
        for adj_tile in self.tile_building_town.adjacencies:
            if adj_tile.player_owner == self and adj_tile.nb_unit > 1:
                self.move_unit_without_check(adj_tile, self.tile_building_town)
                break


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
        self.town_building_step = 0

    def _update_linked_gamobjs(self):
        if self.player_owner is None:
            if self.road_horiz or self.road_vertic:
                gamobj_bg_suffix = Tile.GAMOBJ_BACKGROUND_FROM_ROADS[
                    (self.road_horiz, self.road_vertic)
                ]
                gamobj_background = "neutral" + gamobj_bg_suffix
                self.linked_gamobjs[:] = [gamobj_background]
            else:
                self.linked_gamobjs[:] = []
            return
        color = self.player_owner.color
        gamobj_bg_suffix = Tile.GAMOBJ_BACKGROUND_FROM_ROADS[
            (self.road_horiz, self.road_vertic)
        ]
        gamobj_background = color + gamobj_bg_suffix
        # Il ne devrait jamais y avoir plus de 16 unités sur une même tile,
        # mais on sait jamais. Donc on met un min.
        gamobj_unit = color + "_" + GAMOBJ_NAME_TO_NB_UNIT[min(self.nb_unit, 16)]
        gamobjs = [gamobj_background, gamobj_unit]
        if self.town_building_step:
            gamobjs.append(
                color + "_town_build_" + str(self.town_building_step).zfill(2)
            )
        self.linked_gamobjs[:] = gamobjs

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
                self.game_master.nb_uncontrolled_roads -= 1
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
                self.player_owner.remove_controlled_road(self)
                self.game_master.nb_uncontrolled_roads += 1
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
            if self.player_owner is None:
                self.game_master.nb_uncontrolled_roads += 1
            else:
                self.player_owner.add_controlled_road(self)
        self._update_linked_gamobjs()

    def remove_all_roads(self):
        """
        Supprime toutes les routes de la tile.
        Il n'y a pas de fonction pour supprimer une seule des deux routes, car pas besoin.
        Le seul moment où on supprime des routes, c'est pour mettre une ville à la place.
        """
        if not self.road_vertic and not self.road_horiz:
            return
        self.road_vertic = False
        self.road_horiz = False
        if self.player_owner is None:
            self.game_master.nb_uncontrolled_roads -= 1
        else:
            self.player_owner.remove_controlled_road(self)
        self._update_linked_gamobjs()

    def advance_town_building(self):
        if self.town_building_step >= NB_TURNS_TOWN_BUILDING:
            return
        self.town_building_step += 1
        self._update_linked_gamobjs()

    def cancel_town_building(self):
        self.town_building_step = 0
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
        # J'ai besoin de ça pour savoir si il faut checker des conquêtes de roads.
        # C'est assez rare qu'il y ait des routes inocuppées, mais quand c'est le cas,
        # faut boucler sur toutes les routes occupées pour voir si on peut se propager.
        # Donc c'est cool de savoir les moments où on n'a pas besoin de faire ça.
        # TODO : faudra peut-être avoir une liste, et pas juste la quantité.
        # On verra si le jeu devient lent quand il y a des routes incontrôlées.
        self.nb_uncontrolled_roads = 0

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
    game_master.game_area[2][1].add_unit(game_master.players[0], 10)
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
    player_0 = game_master.players[0]

    player_0.spread_units_on_roads()

    # game_master.game_area[3][3].add_unit(game_master.players[1])
    game_master.game_area[3][3].add_road(horiz=True)
    game_master.game_area[3][3].add_road(vertic=True)
    # game_master.game_area[3][3].add_unit(game_master.players[1])
    game_master.game_area[3][4].add_unit(game_master.players[1], 5)


def test_spread_units(game_master):
    player_0 = game_master.players[0]

    game_master.game_area[1][5].add_road(vertic=True)
    game_master.game_area[2][5].add_road(horiz=True)
    game_master.game_area[2][5].add_road(vertic=True)
    game_master.game_area[2][5].add_unit(game_master.players[1], 7)
    for x in range(3, 12):
        game_master.game_area[2][x].add_road(horiz=True)
        game_master.game_area[5][x].add_road(horiz=True)
        game_master.game_area[2][x].add_unit(player_0)
        game_master.game_area[5][x].add_unit(player_0)

    for y in range(2, 6):
        game_master.game_area[y][3].add_road(vertic=True)
        game_master.game_area[y][11].add_road(vertic=True)
        game_master.game_area[y][3].add_unit(player_0)
        game_master.game_area[y][11].add_unit(player_0)

    game_master.game_area[4][13].add_unit(player_0, 7)
    game_master.game_area[5][13].add_unit(player_0, 3)
    for y in range(2, 6):
        game_master.game_area[y][13].add_road(vertic=True)

    game_master.game_area[2][4].add_unit(player_0, 15)
    game_master.game_area[2][7].add_unit(player_0, 15)


def test_build_town(game_master):
    player_0 = game_master.players[0]
    test_spread_units(game_master)
    game_master.game_area[2][8].add_unit(player_0, 10)
    player_0.tile_building_town = game_master.game_area[2][7]


def main():
    game_master = GameMaster(5, 5)
    # test_adjacencies_and_add_roads(game_master)
    test_spread_units(game_master)


if __name__ == "__main__":
    main()


class GameModel:
    def __init__(self):
        self.w = 20
        self.h = 20
        self.game_master = GameMaster(self.w, self.h)

        # test_adjacencies_and_add_roads(self.game_master)
        test_build_town(self.game_master)

        # TODO : crap.
        # self.players[0].set_other_players((self.players[1], ))
        # self.players[1].set_other_players((self.players[0], ))
        # self.nb_players = len(self.players)
        self.must_start = True

        self.todo_test_attack = False

    def export_all_tiles(self):
        return self.game_master.gamobjs_to_export

    def on_process_turn(self):
        if self.todo_test_attack:
            self.game_master.game_area[2][7].add_unit(self.game_master.players[1], 2)
            self.todo_test_attack = False

        for _, player in self.game_master.players.items():
            if self.game_master.nb_uncontrolled_roads:
                print("Faut checker les conquêtes de routes.")
                player.conquest_road()
            player.process_town_building()
            player.spread_units_on_roads()
        # TODO : calculer approximativement un délai plus ou moins long selon la quantité de trucs à gérer.
        return (
            """ { "delayed_actions": [ {"name": "process_turn", "delay_ms": 300} ] } """
        )

    def on_game_event(self, event_name):
        if event_name == "process_turn":
            return self.on_process_turn()
        if self.must_start:
            self.must_start = False
            return """ { "delayed_actions": [ {"name": "process_turn", "delay_ms": 10} ] } """
        if event_name == "action_2":
            self.todo_test_attack = True
        # else:
        #     for player in self.players:
        #         player.mode += 1
        #         # TODO : ça c'est crade.
        #         if player.mode > 3:
        #             player.mode = 0
        #         print("player.mode", player.mode, player.color)
