# https://i.ibb.co/mczrkx2/game-of-nolife-tileset.png (old)
# https://i.ibb.co/qgVyDdR/game-of-nolife-tileset.png (old)
# https://i.ibb.co/VHQh8sr/game-of-nolife-tileset.png (old)
# https://i.ibb.co/LhqpFs2/game-of-nolife-tileset.png

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

    "town_desactivate": [68, 8],
    "neutral_road_horiz": [72, 8],
    "neutral_road_vertic": [76, 8],
    "neutral_road_both": [80, 8],

    "bla": [0, 0]

  }
}
"""

# Prochains trucs :
# Des missiles bactériologiques !!! Qui partent en diagonale depuis une ville.

# Les routes mettent un petit temps à se construire ?
# (Elles ne coûtent rien et la construction ne peut être interrompue).

import random

# Moche, mais ça permet de convertir plus rapidement.
GAMOBJ_NAME_TO_NB_UNIT = tuple(
    "00;01;02;03;04;05;06;07;08;09;10;11;12;13;14;15;16".split(";")
)


NB_TURNS_TOWN_BUILDING = 9
NB_TURNS_TOWN_BUILDING_TIMEOUT = 25
UNIT_GEN_TOWN_POINT_REQUIRED = 5  # 16
UNIT_GEN_TOWN_POINT_MAX_CUMUL = UNIT_GEN_TOWN_POINT_REQUIRED * 2


def bounding_rect_overlaps(b_rect_1, b_rect_2):
    x_min_1, y_min_1, x_max_1, y_max_1 = b_rect_1
    x_min_2, y_min_2, x_max_2, y_max_2 = b_rect_2
    if x_max_1 < x_min_2 or x_max_2 < x_min_1:
        return False
    if y_max_1 < y_min_2 or y_max_2 < y_min_1:
        return False
    return True


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
        # On a besoin d'indexer là-dessus, parce qu'en général, on n'a plein de bare tiles
        # avec une seule unité, et pas beaucoup avec plusieurs. Donc quand faut
        # bouger les "plusieurs", c'est mieux de savoir tout de suite où elles sont.
        self.controlled_bare_tiles_with_many_units = []
        # TODO : faut les trier de façon à les parcourir le long de diagonales.
        # Ça servira lorsqu'on fusionnera les towns.
        # La diagonale dépend des xxx_wards du player.
        self.towns = []
        self.active_towns = []
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
        tile_source.update_linked_gamobjs()
        tile_dest.update_linked_gamobjs()

    def spread_units_on_roads(self):
        for tile in self._controlled_roads:
            if tile.town_building_step:
                # La tile qui construit une ville ne transfère pas ses unités aux autres.
                continue
            nb_unit_source = tile.nb_unit
            # TODO : on itère sur les 8 cases alors que y'aurait besoin que de 2.
            # D'abord parce que y'a jamais les diagonales.
            # Et ensuite parce qu'on peut ... ah non. Ah si, mais faut calculer la différence absolue.
            # et ensuite déterminer si on bouge de la tile 1 -> 2, ou l'inverse.
            # Mais faut le faire, parce que ça optimiserait bien.
            for adj_tile, adj_connexion_type in zip(
                tile.adjacencies, tile.road_adjacencies_same_player
            ):
                if (
                    adj_tile is not None
                    and adj_connexion_type == 1
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
                self.tile_building_town.build_town()
                self.building_time = 0
                self.tile_building_town = None
            return

        # On peut pas avancer la construction de la ville, car y'a des unités qui sont parties.
        # On essaie de ramener des unités autour pour reprendre la construction.
        for adj_tile in self.tile_building_town.adjacencies:
            if (
                adj_tile is not None
                and adj_tile.player_owner == self
                and adj_tile.nb_unit > 1
            ):
                self.move_unit_without_check(adj_tile, self.tile_building_town)
                break

    def update_active_towns(self):
        self.active_towns = [town for town in self.towns if town.is_active]

    def process_unit_generation_town(self):
        for town in self.active_towns:
            town.process_unit_generation()


class Town:
    def __init__(self, x_left, y_up, size, player_owner, game_master):
        self.x_left = x_left
        self.y_up = y_up
        self.size = size
        self.player_owner = player_owner
        self.game_master = game_master
        self.rect = (x_left, y_up, x_left + size, y_up + size)
        self.is_active = True
        self.unit_gen_horiz = True
        self.unit_gen_points = 0
        self.unit_gen_speed = size ** 2 + size // 2

        self.tiles_position = []
        for x in range(x_left, x_left + size):
            for y in range(y_up, y_up + size):
                self.tiles_position.append(self.game_master.game_area[y][x])

        self._compute_unit_gen_tiles()
        self.adjacent_tiles = tuple([tile for tile in self.unit_gen_tiles_horiz_first])
        self.update_unit_gen_tiles()
        # TODO : calculer la tile diagonale backward, qui sera la tile utilisée pour
        # envoyer les units en backward conquest.
        self.player_owner.towns.append(self)
        self.player_owner.update_active_towns()
        suburb_of_this_town = Suburb(self, self.game_master)

    def get_suburb_owner(self):
        # Toutes les tiles d'une même town ont le même suburb owner. Puisque c'est la même town.
        # Donc on se prend pas la tête, on renvoie le suburb owner de la première tile de la town.
        # Pas besoin de checker les autres ni de vérifier que c'est le même suburb owner pour
        # tout le monde.
        return self.tiles_position[0].suburb_owner

    def _compute_unit_gen_tiles(self):
        """
        Calcule unit_gen_tiles_horiz_first et unit_gen_tiles_vertic_first.
        C'est à dire la liste des tiles où on pose les units. Par ordre de priorité horiz/vertic,
        et en accord avec les rightward/leftward, downward/upward du player.
        """
        size = self.size
        wardnesses = (self.player_owner.rightward, self.player_owner.downward)
        if wardnesses == (True, False):
            unit_gen_offsets = (
                tuple([(size, size - 1 - offset) for offset in range(size)]),
                tuple([(offset, -1) for offset in range(size)]),
                tuple([(-1, size - 1 - offset) for offset in range(size)]),
                tuple([(offset, size) for offset in range(size)]),
            )
        elif wardnesses == (False, True):
            unit_gen_offsets = (
                tuple([(-1, offset) for offset in range(size)]),
                tuple([(size - 1 - offset, size) for offset in range(size)]),
                tuple([(size, offset) for offset in range(size)]),
                tuple([(size - 1 - offset, -1) for offset in range(size)]),
            )
        elif wardnesses == (True, True):
            unit_gen_offsets = (
                tuple([(size, offset) for offset in range(size)]),
                tuple([(offset, -1) for offset in range(size)]),
                tuple([(-1, offset) for offset in range(size)]),
                tuple([(offset, size) for offset in range(size)]),
            )
        elif wardnesses == (False, False):
            unit_gen_offsets = (
                tuple([(-1, size - 1 - offset) for offset in range(size)]),
                tuple([(size - 1 - offset, -1) for offset in range(size)]),
                tuple([(size, size - 1 - offset) for offset in range(size)]),
                tuple([(size - 1 - offset, size) for offset in range(size)]),
            )
        else:
            raise Exception("Bad wardnesses. Not supposed to happen.")
        (horiz_first, vertic_first, horiz_second, vertic_second) = unit_gen_offsets
        unit_gen_horiz_first_offsets = (
            horiz_first + vertic_first + horiz_second + vertic_second
        )
        unit_gen_vertic_first_offsets = (
            vertic_first + horiz_first + vertic_second + horiz_second
        )
        # On checke que ça dépasse pas les bords de l'aire de jeu.
        self.unit_gen_tiles_horiz_first = [
            self.game_master.game_area[self.y_up + y_offset][self.x_left + x_offset]
            for (x_offset, y_offset) in unit_gen_horiz_first_offsets
            if 0 <= self.x_left + x_offset < self.game_master.w
            and 0 <= self.y_up + y_offset < self.game_master.h
        ]
        self.unit_gen_tiles_vertic_first = [
            self.game_master.game_area[self.y_up + y_offset][self.x_left + x_offset]
            for (x_offset, y_offset) in unit_gen_vertic_first_offsets
            if 0 <= self.x_left + x_offset < self.game_master.w
            and 0 <= self.y_up + y_offset < self.game_master.h
        ]

    def update_unit_gen_tiles(self):
        """
        Met à jour les variables unit_gen_tiles_horiz_first et unit_gen_tiles_vertic_first,
        ainsi que self.is_active, en fonction des towns autour.
        """
        print("--- town update_unit_gen_tiles")
        print(self.x_left, self.y_up)
        self.unit_gen_tiles_horiz_first = [
            tile for tile in self.unit_gen_tiles_horiz_first if tile.town is None
        ]
        print(
            "unit_gen_tiles_horiz_first",
            " ; ".join(
                (f"{tile.x},{tile.y}") for tile in self.unit_gen_tiles_horiz_first
            ),
        )
        self.unit_gen_tiles_vertic_first = [
            tile for tile in self.unit_gen_tiles_vertic_first if tile.town is None
        ]
        print(
            "unit_gen_tiles_vertic_first",
            " ; ".join(
                (f"{tile.x},{tile.y}") for tile in self.unit_gen_tiles_vertic_first
            ),
        )
        print("---")

        if not self.unit_gen_tiles_horiz_first:
            self.is_active = False
            # TODO : transférer une partie des points de génération de unit de cette town
            # à la génération de unit par terrain.
            print("TODO desactivation town", self.x_left, self.y_up, self.size)
            self.player_owner.update_active_towns()
            # Il faut updater la liste des gamobjects de chaque tile de la town,
            # car lorsque la town est désactivée, on l'affiche en plus foncée.
            for tile in self.tiles_position:
                tile.update_linked_gamobjs()

    def process_unit_generation(self):
        self.unit_gen_points += self.unit_gen_speed
        self.unit_gen_points = min(self.unit_gen_points, UNIT_GEN_TOWN_POINT_MAX_CUMUL)
        if self.unit_gen_points > UNIT_GEN_TOWN_POINT_REQUIRED:

            if self.unit_gen_horiz:
                unit_gen_tiles = self.unit_gen_tiles_horiz_first
            else:
                unit_gen_tiles = self.unit_gen_tiles_vertic_first

            for tile in unit_gen_tiles:
                if tile.player_owner != self.player_owner or tile.nb_unit < 16:
                    tile.add_unit(self.player_owner)
                    self.unit_gen_points -= UNIT_GEN_TOWN_POINT_REQUIRED
                    self.unit_gen_horiz = not self.unit_gen_horiz
                    if (
                        (not tile.road_horiz or not tile.road_vertic)
                        and self.player_owner == tile.player_owner
                        and tile.nb_unit >= 2
                    ):
                        tile.add_road(True, True)
                    return
            # Si on est arrivé là, on aurait du générer une unit, mais on n'a aucun
            # endroit où la placer. Tant pis, on testera au prochain tour.
            # C'est pour ça qu'on peut cumuler plus de points de génération que le coût de
            # création d'une unit. Ça permet d'avoir un petit délai dans la génération,
            # sans perdre de points.


REVERSE_DIRS = (4, 5, 6, 7, 0, 1, 2, 3)


class Suburb:
    """
    Un suburb peut contenir des towns de différents players.
    Les suburbs sont neutres et sont gérés pas le game_master. Les players n'en on pas besoin.
    Les suburbs servent uniquement à répartir les units autour.

    Les suburbs ont :
     - des real tiles : toutes les tiles de roads adjacentes à une ville du suburb.
     - des potential tiles : les tiles non-road et non-ville, adjacentes à une ville du suburb.
     - bounding rect qui englobe toutes les tiles et potential tiles
       (juste pour accélerer les traitements).

    Lorsqu'une ville est créée sur une potential ou real tile d'un suburb existant, on crée le mini-suburb autour
    de la nouvelle ville, et on la fusionne tout de suite avec le suburb existant.

    Lorsqu'une route est créée, il faut vérifier si la tile n'appartient pas aux potential tiles de un ou plusieurs
    de suburb. Lorsque c'est le cas, on transfère cette tile de potential à real.
    Si on l'a fait pour plusieurs suburbs, on fusionne tous ces suburbs ensemble.

    On a besoin que de deux choses pour gérer l'évolution des suburbs.
    La fonction de merge, et une petite fonction, dans la classe Town ou la classe Tile,
    qui va créer un mini-suburb de 4 tiles potentielles autour d'une town.
    """

    def __init__(self, initial_town, game_master):
        self.game_master = game_master
        if initial_town.size != 1:
            raise Exception(
                "Pas de création de suburb sur des grandes towns. Désolé, j'ai pas besoin de cas."
            )
        self.town_tiles = list(initial_town.tiles_position)
        for tile in self.town_tiles:
            tile.suburb_owner = self
        all_suburb_tiles = [
            tile for tile in initial_town.adjacent_tiles if tile.town is None
        ]
        # Ici, on ne gère pas le cas de la coupure de connexions entre deux roads qui sont dans
        # le même suburb. Ça arrive jamais, car les nouveaux suburbs ne sont créés que avec des
        # towns ayant une size de 1.
        # Mais si on avait voulu pinailler, il aurait fallu exécuter
        # transfer_potential_road à chaque tile de route.
        self.real_suburb_tiles = []
        self.potential_tiles = []
        for tile in all_suburb_tiles:
            if tile.road_horiz or tile.road_vertic:
                self.real_suburb_tiles.append(tile)
                tile.suburb_owner = self
            else:
                self.potential_tiles.append(tile)
        self._update_bounding_rect()
        self.game_master.suburbs.append(self)

    def _update_bounding_rect(self):
        """
        Définit self.bounding_rect. Une liste de 4 int. x1, y1, x2, y2.
        On englobe toutes les tiles du suburb.
        Comme d'hab' en python, le rect s'étend de x1 à x2 - 1, et de y1 à y2 - 1.
        Comme les ranges.
        """
        all_tiles = self.town_tiles + self.real_suburb_tiles + self.potential_tiles
        xs = [tile.x for tile in all_tiles]
        ys = [tile.y for tile in all_tiles]
        self.bounding_rect = (min(xs), min(ys), max(xs) + 1, max(ys) + 1)

    def transfer_potential_road(self, tile):
        if tile not in self.potential_tiles:
            return
        if not tile.road_horiz and not tile.road_vertic:
            return
        self.potential_tiles.remove(tile)
        self.real_suburb_tiles.append(tile)
        tile.suburb_owner = self
        # Il faudrait mettre des valeurs "2" dans les connexions entre roads du même suburb.
        # C'est la classe Tile qui s'en charge.

    def merge(self, other_suburb):
        roads_other_suburb = other_suburb.real_suburb_tiles
        all_tiles_two_suburbs = (
            self.potential_tiles
            + self.real_suburb_tiles
            + self.town_tiles
            + other_suburb.potential_tiles
            + other_suburb.real_suburb_tiles
            + other_suburb.town_tiles
        )
        self.town_tiles = []
        self.real_suburb_tiles = []
        self.potential_tiles = []

        for tile in all_tiles_two_suburbs:
            if tile.town is not None:
                tile.suburb_owner = self
                if tile not in self.town_tiles:
                    self.town_tiles.append(tile)
            elif tile.road_horiz or tile.road_vertic:
                tile.suburb_owner = self
                if tile not in self.real_suburb_tiles:
                    self.real_suburb_tiles.append(tile)
            else:
                if tile not in self.potential_tiles:
                    self.potential_tiles.append(tile)

        for road_tile in roads_other_suburb:
            # On met des connexions à 2 entre les routes d'un même suburb.
            # C'est à dire qu'on coupe ces connexions. Car l'équilibrage des
            # unités sera géré par le suburb lui-même.
            # Il faut checker toutes les routes du suburb mergé.
            # D'où l'intérêt de prendre le plus gros suburb et d'exécuter sa fonction merge,
            # avec le plus petit suburb en paramètre. Et non pas le contraire.
            # Sinon on se retrouve à rechecker plein de connexions déjà annulées.
            #
            # TODO : du coup j'appelle une fonction privée depuis une autre classe.
            # Sémantiquement c'est mal. Faudra régler ça.
            road_tile._update_all_road_adjacencies()

        self._update_bounding_rect()
        print("merged suburb: " + str(self))
        self.game_master.suburbs.remove(other_suburb)

    def __str__(self):
        coords_towns = [(tile.x, tile.y) for tile in self.town_tiles]
        coords_real = [(tile.x, tile.y) for tile in self.real_suburb_tiles]
        coords_poten = [(tile.x, tile.y) for tile in self.potential_tiles]
        return (
            f"Suburb. bounding rect : {self.bounding_rect}\n"
            f"Towns: {coords_towns}"
            f"Real : {coords_real}"
            f"Poten: {coords_poten}"
        )


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
        # Indique si la route est adjacente avec une autre route contrôlée par le même joueur.
        # 0 : non
        # 1 : oui, ça veut dire qu'on doit transférer automatiquement des unités d'une tile à l'autre,
        #     si jamais c'est trop déséquilibré.
        # 2 : il y a une connexion, mais c'est entre deux routes d'un même suburb.
        #     Ça veut dire qu'on équilibre pas par les routes. Ça s'équilibre tout seul par le suburb.
        self.road_adjacencies_same_player = [0 for _ in range(8)]
        self.road_vertic = False
        self.road_horiz = False
        self.player_owner = None
        self.nb_unit = 0
        self.town = None
        # La variable suburb_owner est définie par les Suburb.
        # Soit lors de la création d'un nouveau suburb, soit lors d'un merge.
        self.suburb_owner = None
        self.town_building_step = 0

    def update_linked_gamobjs(self):

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

        gamobjs = []
        color = self.player_owner.color
        if self.town:
            gamobjs.append(color + "_town_1x1")
            if not self.town.is_active:
                gamobjs.append("town_desactivate")
        else:
            gamobj_bg_suffix = Tile.GAMOBJ_BACKGROUND_FROM_ROADS[
                (self.road_horiz, self.road_vertic)
            ]
            gamobj_background = color + gamobj_bg_suffix
            gamobjs.append(gamobj_background)
            if self.nb_unit:
                # Il ne devrait jamais y avoir plus de 16 unités sur une même tile,
                # mais on sait jamais. Donc on met un min.
                gamobjs.append(
                    color + "_" + GAMOBJ_NAME_TO_NB_UNIT[min(self.nb_unit, 16)]
                )
            if self.town_building_step:
                gamobjs.append(
                    color + "_town_build_" + str(self.town_building_step).zfill(2)
                )
        self.linked_gamobjs[:] = gamobjs

    def __str__(self):
        # TODO : f-string bordel !
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
                    self.road_adjacencies_same_player,
                    " suburb_owner:",
                    self.suburb_owner,
                ),
            )
        )

    def _update_road_adjacency(self, direction):
        other_tile = self.adjacencies[direction]
        if other_tile is None:
            self.road_adjacencies_same_player[direction] = 0
            return

        # Pas de pre-check. On fixe systématiquement à 0, 1 ou 2 selon l'état en cours.
        # Si ça redéfinit à la même valeur, osef.
        # Comme ça on gère automatiquement le passage de 2 à 0, lorsqu'on construit une ville
        # à l'endroit où il y avait une route de suburb.
        if self.town is not None or other_tile.town is not None:
            # Jamais de connexion de route entre une town et une tile adjacente.
            # Même si il y a une road sur la tile adjacente.
            # L'équilibrage des unités dans ce cas est géré par le suburb.
            connection_type = 0
        elif (
            self.suburb_owner is not None
            and self.suburb_owner == other_tile.suburb_owner
        ):
            # C'est pas une vraie connexion.
            # Il y a des routes, mais on considère qu'elles ne sont pas connectées.
            # Dans ce cas aussi, l'équilibrage des unités est géré par le suburb.
            connection_type = 2
        else:
            if direction in (0, 4):
                roads_to_check = self.road_vertic and other_tile.road_vertic
            elif direction in (6, 2):
                roads_to_check = self.road_horiz and other_tile.road_horiz
            else:
                raise Exception("Road adj with diag dir. Not supposed to happen.")
            connection_ok = all(
                (
                    roads_to_check,
                    self.player_owner is not None,
                    self.player_owner == other_tile.player_owner,
                )
            )
            connection_type = int(connection_ok)

        self.road_adjacencies_same_player[direction] = connection_type
        reversed_direction = REVERSE_DIRS[direction]
        other_tile.road_adjacencies_same_player[reversed_direction] = connection_type

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
        if self.town is not None:
            raise Exception(
                "Ajout de unit sur une ville. Not supposed to happen." + str(self)
            )

        initial_nb_unit = self.nb_unit
        must_check_road_adjacencies = True
        if self.player_owner == player:
            # Pas de check pour vérifier que ça dépasse pas 16. Faut le faire avant.
            self.nb_unit += qty
            player.total_units += qty
            # On ne fait que ajouter des unités d'une couleur à une tile qui en a déjà.
            # Ça change rien au niveau des routes, des contrôles, etc.
            must_check_road_adjacencies = False
        elif self.player_owner is None:
            self.player_owner = player
            player.add_controlled_tile(self)
            if self.road_vertic or self.road_horiz:
                player.add_controlled_road(self)
                self.game_master.uncontrolled_roads.remove(self)
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

        if must_check_road_adjacencies:
            # L'ajout d'unité a provoqué un changement important.
            # Par exemple, la tile a changé d'owner.
            # Il faut donc vérifier tous les contrôles et les adjacences de routes.
            self._update_all_road_adjacencies_with_current_roads()
        self.update_linked_gamobjs()

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
                self.game_master.uncontrolled_roads.append(self)
            self.player_owner = None
            self._update_all_road_adjacencies_with_current_roads()

        self.update_linked_gamobjs()

    def add_road(self, horiz=False, vertic=False):
        if not (horiz or vertic):
            return
        adj_towns = [
            adj_tile.town
            for adj_tile in self.adjacencies[::2]
            if adj_tile is not None and adj_tile.town is not None
        ]
        if adj_towns:
            # Si c'est à côté d'une ville, on ajoute obligatoirement les deux routes.
            horiz = True
            vertic = True

        if horiz == self.road_horiz and vertic == self.road_vertic:
            return
        if self.town is not None:
            raise Exception("Ajout de road sur une town. Not supposed to happen.")

        previous_road_qty = self.road_horiz + self.road_vertic
        self.road_horiz = self.road_horiz or horiz
        self.road_vertic = self.road_vertic or vertic
        current_road_qty = self.road_horiz + self.road_vertic
        self._update_all_road_adjacencies_with_current_roads()
        if previous_road_qty == 0 and current_road_qty > 0:
            if self.player_owner is None:
                self.game_master.uncontrolled_roads.append(self)
            else:
                self.player_owner.add_controlled_road(self)

        if adj_towns:
            adj_suburbs = set((town.get_suburb_owner() for town in adj_towns))
            for suburb in adj_suburbs:
                # Dans le ou les suburbs concernés, la construction de route transfère la tile
                # des potential_tiles vers real_suburb_tiles.
                suburb.transfer_potential_road(self)
            if len(adj_suburbs) > 1:
                # Ce transfert de tile peut faire merger un ou plusieurs suburbs.
                self.game_master.check_suburb_merging_by_list(list(adj_suburbs))
            # Et du coup, maintenant qu'on a mergé, on met à jour les connexions entre route.
            # On va en annuler certaines (mettre une connexion à 2),
            # car ce sont devenues des routes d'un même suburb.
            self._update_all_road_adjacencies()
        self.update_linked_gamobjs()

    def _remove_all_roads(self):
        """
        Supprime toutes les routes de la tile.
        Il n'y a pas de fonction pour supprimer une seule des deux routes, car pas besoin.
        Le seul moment où on supprime des routes, c'est pour mettre une ville à la place.
        Du coup, la suppression de roads ne provoque jamais de diminution ou de split de suburb,
        donc on gère pas ça non plus, et ça va très bien.
        """
        if not self.road_vertic and not self.road_horiz:
            return
        self.road_vertic = False
        self.road_horiz = False
        if self.player_owner is None:
            self.game_master.uncontrolled_roads.remove(self)
        else:
            self.player_owner.remove_controlled_road(self)
        self._update_all_road_adjacencies()
        self.update_linked_gamobjs()

    def advance_town_building(self):
        if self.town_building_step >= NB_TURNS_TOWN_BUILDING:
            return
        self.town_building_step += 1
        self.update_linked_gamobjs()

    def cancel_town_building(self):
        self.town_building_step = 0
        self.update_linked_gamobjs()

    # TODO : on n'aura pas besoin du param size, mais c'est juste pour tester.
    def build_town(self, size=1):
        print("start build town", self)
        if self.player_owner is None:
            raise Exception("Town without owner. Not supposed to happen.")

        if not self.road_horiz and not self.road_vertic and self.nb_unit > 1:
            self.player_owner.controlled_bare_tiles_with_many_units.remove(self)
        self._remove_all_roads()
        for tile_adj in self.adjacencies[::2]:
            if tile_adj is not None:
                # Si y'a des routes autour, il faut automatiquement les transformer en carrefour
                # La tile adjacente doit avoir road_vertic et road_horiz.
                if int(tile_adj.road_horiz) + int(tile_adj.road_vertic) == 1:
                    tile_adj.add_road(True, True)
        # Pour enlever les units, on aurait dû passer par la fonction remove_units.
        # Mais on va pas le faire, parce que ça mettrait player_owner à None.
        self.nb_unit = 0
        self.town = Town(self.x, self.y, size, self.player_owner, self.game_master)
        for tile_adj in self.adjacencies[::2]:
            if tile_adj is not None and tile_adj.town is not None:
                tile_adj.town.update_unit_gen_tiles()
        self.game_master.check_suburb_merging_with_all_others(
            self.town.get_suburb_owner()
        )
        self.update_linked_gamobjs()
        print("end build town")


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
        # J'ai besoin de ça pour savoir si il faut checker des conquêtes de roads.
        # C'est assez rare qu'il y ait des routes inocuppées, mais quand c'est le cas,
        # faut boucler dessus pour voir si on peut y propager des unités.
        self.uncontrolled_roads = []

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

    def conquest_neutral_roads(self):
        """
        Lorsqu'une tile de road n'a pas de owner, et qu'elle est connectée à une road adjacente,
        et que cette road est contrôlée par quelqu'un,
        alors on déplace automatiquement une unité dessus pour la conquérir.
        Si il y a différents owner sur les tiles adjacentes, on ne fait rien.
        """
        if not self.uncontrolled_roads:
            return

        # On fait une copie de la liste,
        # car elle risque de changer pendant qu'on boucle dessus.
        uncontrolled_roads_copy = list(self.uncontrolled_roads)
        for tile in uncontrolled_roads_copy:
            conqueror_tiles = []
            conqueror_players = set()
            if tile.road_vertic:
                for adj_tile in (tile.adjacencies[0], tile.adjacencies[4]):
                    if (
                        adj_tile is not None
                        and adj_tile.player_owner is not None
                        and adj_tile.nb_unit > 1
                        and adj_tile.road_vertic
                    ):
                        conqueror_tiles.append(adj_tile)
                        conqueror_players.add(adj_tile.player_owner)
            if tile.road_horiz:
                for adj_tile in (tile.adjacencies[2], tile.adjacencies[6]):
                    if (
                        adj_tile is not None
                        and adj_tile.player_owner is not None
                        and adj_tile.nb_unit > 1
                        and adj_tile.road_horiz
                    ):
                        conqueror_tiles.append(adj_tile)
                        conqueror_players.add(adj_tile.player_owner)

            if len(conqueror_players) == 1:
                conqueror_tile = conqueror_tiles[0]
                conqueror_player = list(conqueror_players)[0]
                conqueror_tile.remove_unit()
                tile.add_unit(conqueror_player)

    def check_two_suburbs_merge(self, suburb_1, suburb_2):
        suburb_1_all_tiles = (
            suburb_1.town_tiles + suburb_1.real_suburb_tiles + suburb_1.potential_tiles
        )
        if not set(suburb_1_all_tiles).isdisjoint(set(suburb_2.town_tiles)):
            return True
        suburb_2_all_tiles = (
            suburb_2.town_tiles + suburb_2.real_suburb_tiles + suburb_2.potential_tiles
        )
        if not set(suburb_2_all_tiles).isdisjoint(set(suburb_1.town_tiles)):
            return True
        if not set(suburb_2.real_suburb_tiles).isdisjoint(
            set(suburb_1.real_suburb_tiles)
        ):
            return True
        return False

    def check_suburb_merging_by_list(self, many_suburbs):
        # TODO pas encore codé.
        print("check_suburb_merging_by_list")
        # TODO : faut les trier pour repérer le plus grand.
        # On merge le plus grand avec les autres,
        # c'est plus rapide que de merger un petit avec d'autres.
        first_suburb = many_suburbs.pop(0)
        print("rect", first_suburb.bounding_rect)
        while many_suburbs:
            other_suburb = many_suburbs.pop(0)
            print("rect", other_suburb.bounding_rect)
            if self.check_two_suburbs_merge(first_suburb, other_suburb):
                print("must_merge from list")
                first_suburb.merge(other_suburb)

    def check_suburb_merging_with_all_others(self, one_suburb):
        print("check_suburb_merging_with_all_others")
        print(one_suburb.bounding_rect)
        suburbs_to_merge = []
        for other_suburb in self.suburbs:
            if one_suburb == other_suburb:
                continue
            if bounding_rect_overlaps(
                one_suburb.bounding_rect, other_suburb.bounding_rect
            ):
                print("overlaps", one_suburb.bounding_rect, other_suburb.bounding_rect)
                if self.check_two_suburbs_merge(one_suburb, other_suburb):
                    print("must_merge from one with other.")
                    suburbs_to_merge.append(other_suburb)

        for other_suburb in suburbs_to_merge:
            # TODO Là aussi, faut merger le plus grand avec le plus petit.
            # C'est plus rapide.
            one_suburb.merge(other_suburb)

    def _equilibrate_units_in_one_suburb(self, suburb, turn_index):
        # Clé : un player ayant des unités dans ce suburb.
        # Valeur : tuple de 2 éléments : tile avec le max d'unité, tile avec le min d'unité.
        most_unequilibrateds = {}
        un_owned_tile = None
        func_get_unit = lambda tile: tile.nb_unit
        for tile in suburb.real_suburb_tiles:
            player_tile = tile.player_owner
            if player_tile is None:
                if un_owned_tile is None:
                    un_owned_tile = tile
            else:
                if player_tile not in most_unequilibrateds:
                    most_unequilibrateds[player_tile] = [tile, tile]
                else:
                    tile_unit_min, tile_unit_max = most_unequilibrateds[player_tile]
                    most_unequilibrateds[player_tile] = [
                        min(tile_unit_min, tile, key=func_get_unit),
                        max(tile_unit_max, tile, key=func_get_unit),
                    ]
        if not most_unequilibrateds:
            return

        if len(most_unequilibrateds) == 1:
            player_tile, tile_extrems = next(iter(most_unequilibrateds.items()))
            tile_unit_min, tile_unit_max = tile_extrems
            if tile_unit_max.nb_unit > 2:
                if un_owned_tile:
                    tile_unit_max.remove_unit()
                    un_owned_tile.add_unit(player_tile)
                else:
                    diff = tile_unit_max.nb_unit - tile_unit_min.nb_unit
                    if diff > 1:
                        player_tile.move_unit_without_check(
                            tile_unit_max, tile_unit_min, diff // 2
                        )
        # elif len(most_unequilibrateds) == 2:
        else:
            iter_uneq = iter(most_unequilibrateds.items())
            player_tile_1, tile_extrems_1 = next(iter_uneq)
            player_tile_2, tile_extrems_2 = next(iter_uneq)
            tile_unit_max_1 = tile_extrems_1[1]
            tile_unit_max_2 = tile_extrems_2[1]
            tile_unit_max_1.remove_unit()
            tile_unit_max_2.remove_unit()
        # else:
        #     Si on a plus que 2 players, faut déterminer équitablement quelles unités on élimine.
        #     On éliminera une unité pour 2 players parmi toutes la liste. Mais lesquels ?
        #     Un round-robin shufflé basé sur le numéro de tour de jeu ?
        #     TODO WIP.
        #     for x in range(6):
        #         a = x % 3
        #         b = x % 2
        #         if b >= a:
        #             b+=1
        #         print(a,b)

    def equilibrate_units_in_suburbs(self, turn_index):
        for suburb in self.suburbs:
            self._equilibrate_units_in_one_suburb(suburb, turn_index)


def main():
    game_master = GameMaster(5, 5)
    # test_adjacencies_and_add_roads(game_master)
    test_spread_units(game_master)


if __name__ == "__main__":
    main()

SANDBOX_MODES = [
    "add red unit",
    "add blu unit",
    "add horiz road",
    "add vertic road",
    "add town",
    "describe",
]

# Utile uniquement pour le mode sandbox.
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


class GameModel:
    def __init__(self):
        self.w = 20
        self.h = 25
        self.game_master = GameMaster(self.w, self.h)

        # test_adjacencies_and_add_roads(self.game_master)
        # test_build_town(self.game_master)
        # test_unit_gen_town_start(self.game_master)
        # test_unit_gen_town_2(self.game_master)
        # test_conquest_roads(self.game_master)

        self.must_start = True
        self.sandbox_action = False
        self.x_cursor = 0
        self.y_cursor = 0
        self.sandbox_mode_index = 0
        self.turn_index = 0
        print("mode actuel :", SANDBOX_MODES[self.sandbox_mode_index])

    def export_all_tiles(self):
        gamobjs_source = self.game_master.gamobjs_to_export
        gamobjs_copy = []
        for line_source in gamobjs_source:
            line = [list(gamobjs) for gamobjs in line_source]
            gamobjs_copy.append(line)

        gamobjs_copy[self.y_cursor][self.x_cursor].append("red_cursor")
        return gamobjs_copy

    def on_process_turn(self):
        if self.sandbox_action:
            sandbox_mode = SANDBOX_MODES[self.sandbox_mode_index]
            tile_target = self.game_master.game_area[self.y_cursor][self.x_cursor]
            if sandbox_mode == "add red unit":
                tile_target.add_unit(self.game_master.players[0], 1)
            elif sandbox_mode == "add blu unit":
                tile_target.add_unit(self.game_master.players[1], 1)
            elif sandbox_mode == "add horiz road":
                if tile_target.town is not None:
                    print("Pas de route sur une town")
                else:
                    tile_target.add_road(horiz=True)
            elif sandbox_mode == "add vertic road":
                if tile_target.town is not None:
                    print("Pas de route sur une town")
                else:
                    tile_target.add_road(vertic=True)
            elif sandbox_mode == "add town":
                if tile_target.player_owner is None:
                    print("On ne peut construire une ville que sur une case occupée.")
                    print("Et la construction avance seulement si il y a 16 unités.")
                else:
                    if tile_target.player_owner.tile_building_town is not None:
                        print("Ville déjà en construction pour cette couleur.")
                    else:
                        tile_target.player_owner.tile_building_town = tile_target
            elif sandbox_mode == "describe":
                print("-----")
                print(tile_target)
            # TODO crap.
            # self.game_master.game_area[2][7].add_unit(self.game_master.players[1], 2)
            # if self.game_master.game_area[2][8].town is None:
            #     self.game_master.game_area[2][8].add_unit(
            #         self.game_master.players[1], 16
            #     )
            #     self.game_master.game_area[2][8].build_town()
            self.sandbox_action = False

        # test_unit_gen_town_each_turn(self.game_master)
        # test_build_town_on_full_tiles_0(self.game_master)
        # test_build_town_on_full_tiles_1(self.game_master)

        self.game_master.conquest_neutral_roads()
        self.game_master.equilibrate_units_in_suburbs(self.turn_index)
        self.turn_index += 1

        for _, player in self.game_master.players.items():
            player.process_town_building()
            player.spread_units_on_roads()
            player.process_unit_generation_town()
        # TODO : calculer approximativement un délai plus ou moins long selon la quantité de trucs à gérer.
        return (
            """ { "delayed_actions": [ {"name": "process_turn", "delay_ms": 100} ] } """
        )

    def on_game_event(self, event_name):
        if event_name == "process_turn":
            return self.on_process_turn()
        if self.must_start:
            self.must_start = False
            return """ { "delayed_actions": [ {"name": "process_turn", "delay_ms": 10} ] } """

        if event_name == "action_1":
            self.sandbox_mode_index += 1
            if self.sandbox_mode_index >= len(SANDBOX_MODES):
                self.sandbox_mode_index = 0
            print("mode actuel :", SANDBOX_MODES[self.sandbox_mode_index])
            return
        if event_name == "action_2":
            self.sandbox_action = True
            return
        if event_name in "URDL":
            x_cursor_new, y_cursor_new = coord_move(
                self.x_cursor, self.y_cursor, event_name
            )
            if 0 <= x_cursor_new < self.w and 0 <= y_cursor_new < self.h:
                self.x_cursor, self.y_cursor = x_cursor_new, y_cursor_new
            return

