# https://i.ibb.co/mczrkx2/game-of-nolife-tileset.png (old)
# https://i.ibb.co/qgVyDdR/game-of-nolife-tileset.png

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

    "bla": [0, 0]

  }
}
"""

import random

# Moche, mais ça permet de convertir plus rapidement.
GAMOBJ_NAME_TO_NB_UNIT = (
    "00",
    "01", "02", "03", "04", "05", "06", "07", "08",
    "09", "10", "11", "12", "13", "14", "15", "16",
)

# Gros TODO global : est-ce que ça aurait pas été mieux avec un seul array,
# dans chaque case il y a une classe, avec tous le bordel dedans.
# les unités des players, les villes, les adjacences pour les déplacements, ...
# Bordel de merde. N'aurait-je pas tout foutu à l'envers ?

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


MODE_GROW = 0
MODE_TRAVEL_VERTICALLY = 1
MODE_TRAVEL_HORIZONTALLY = 2
MODE_FIGHT = 3

class Player():

    def __init__(self, player_id, w, h, color, tiles_control, tiles_town, rightward, downward):
        self.player_id = player_id
        self.w = w
        self.h = h
        self.color = color
        self.tiles_control = tiles_control
        self.tiles_town = tiles_town
        self.rightward = rightward
        self.downward = downward
        self.bounding_rect_exists = False
        self.mode = MODE_GROW
        self.other_players = None
        self.array_units = []
        self.array_town_names = []
        for y in range(self.h):
            unit_line = []
            town_line = []
            for x in range(self.w):
                unit_val = 0
                town_name = None
                unit_line.append(unit_val)
                town_line.append(town_name)
            self.array_units.append(unit_line)
            self.array_town_names.append(town_line)
        self.array_units = tuple(self.array_units)
        self.array_town_names = tuple(self.array_town_names)

        x_around_2 = (1, 2, 3, 1, 3, 1, 2, 3)
        x_around_1 = (0, 1, 2, 3, 4, 0, 4, 0, 4, 0, 4, 0, 1, 2, 3, 4)
        y_around_2 = sorted(x_around_2)
        y_around_1 = sorted(x_around_1)
        if rightward:
            x_town = 2
            x_with_2 = x_around_2
            x_with_1 = x_around_1
        else:
            x_town = self.w - 3
            x_with_2 = (self.w - x - 1 for x in x_around_2)
            x_with_1 = (self.w - x - 1 for x in x_around_1)

        if downward:
            y_town = 2
            y_with_2 = y_around_2
            y_with_1 = y_around_1
        else:
            y_town = self.h - 3
            y_with_2 = (self.h - y - 1 for y in y_around_2)
            y_with_1 = (self.h - y - 1 for y in y_around_1)

        for x, y in zip(x_with_1, y_with_1):
            self.array_units[y][x] = 1
        for x, y in zip(x_with_2, y_with_2):
            self.array_units[y][x] = 2
        # Quand c'est une ville, on met -1.
        self.array_units[y_town][x_town] = -1
        # TODO : faire des sprites de towns 2x2 tiles, 4x4 tiles, etc.
        self.array_town_names[y_town][x_town] = self.color + "_town_1x1"

    def set_other_players(self, other_players):
        self.other_players = other_players

    def iter_on_gamobjs(self):
        for unit_line, town_line in zip(self.array_units, self.array_town_names):
            for unit_val, town_name in zip(unit_line, town_line):
                if town_name:
                    yield town_name
                elif unit_val:
                    if unit_val > 16:
                        unit_val = 16
                    yield self.color + "_" + GAMOBJ_NAME_TO_NB_UNIT[unit_val]
                else:
                    yield None

    def update_bounding_rects(self, xs_with_unit, ys_with_unit, nb_controlled_tiles):
        self.nb_controlled_tiles = nb_controlled_tiles
        if not xs_with_unit or not ys_with_unit:
            self.bounding_rect_exists = False
            self.bounding_rect_x_min = None
            self.bounding_rect_x_max = None
            self.bounding_rect_y_min = None
            self.bounding_rect_y_max = None
            return

        self.bounding_rect_exists = True

        if self.rightward:
            self.bounding_rect_x_min = 0
            # On met des +1 pour faire dépasser le bounding rect à droite et en bas.
            # Pour rester homogène avec le principe du range(a, b) qui va que jusqu'à b-1.
            self.bounding_rect_x_max = max(xs_with_unit) + 1
        else:
            self.bounding_rect_x_min = min(xs_with_unit)
            self.bounding_rect_x_max = self.w

        if self.downward:
            self.bounding_rect_y_min = 0
            self.bounding_rect_y_max = max(ys_with_unit) + 1
        else:
            self.bounding_rect_y_min = min(ys_with_unit)
            self.bounding_rect_y_max = self.h

        # todo crap.
        # print("bounding rect", self.color)
        # print(self.bounding_rect_x_min, self.bounding_rect_y_min, self.bounding_rect_x_max, self.bounding_rect_y_max)

    def iter_vertical_expansion_column(self, x_column):
        if self.downward:
            y_dest = self.bounding_rect_y_max
            if y_dest >= self.h:
                y_dest = self.h - 1
            while y_dest > 0:
                y_source = y_dest - 1
                while y_source >= 0 and self.array_town_names[y_source][x_column]:
                    y_source = y_source - 1
                if y_source >= 0:
                    yield (y_source, y_dest)
                y_dest = y_source
        else:
            y_dest = self.bounding_rect_y_min - 1
            if y_dest < 0:
                y_dest = 0
            while y_dest < self.h - 1:
                y_source = y_dest + 1
                while y_source <= self.h - 1 and self.array_town_names[y_source][x_column]:
                    y_source = y_source + 1
                if y_source <= self.h - 1:
                    yield (y_source, y_dest)
                y_dest = y_source

    def iter_horizontal_expansion_line(self, y_line):
        if self.rightward:
            x_dest = self.bounding_rect_x_max
            if x_dest >= self.w:
                x_dest = self.w - 1
            while x_dest > 0:
                x_source = x_dest - 1
                while x_source >= 0 and self.array_town_names[y_line][x_source]:
                    x_source = x_source - 1
                if x_source >= 0:
                    yield (x_source, x_dest)
                x_dest = x_source
        else:
            x_dest = self.bounding_rect_x_min - 1
            if x_dest < 0:
                x_dest = 0
            while x_dest < self.w - 1:
                x_source = x_dest + 1
                while x_source <= self.w - 1 and self.array_town_names[y_line][x_source]:
                    x_source = x_source + 1
                if x_source <= self.w - 1:
                    yield (x_source, x_dest)
                x_dest = x_source

    def travel_one_tile(self, x_source, y_source, x_dest, y_dest):
        unit_source = self.array_units[y_source][x_source]
        if unit_source in (0, 1, -1):
            return
        unit_dest = self.array_units[y_dest][x_dest]
        if unit_dest in (16, -1):
            return
        if unit_source <= unit_dest + 1:
            return
        if self.tiles_town[y_dest][x_dest]:
            return
        # Si personne ne contrôle la tile de destination,
        # ça veut dire qu'il y a plusieurs players dessus
        has_other_unit_dest = self.tiles_control[y_dest][x_dest] is None
        # Pas de déplacement à plus de 12 unités sur une tile qui a des unités ennemies.
        DEST_CAP_ON_UNCONTROLLED_TILES = 12
        if has_other_unit_dest and unit_dest >= DEST_CAP_ON_UNCONTROLLED_TILES:
            return
        transfer_qty = int((unit_source - unit_dest) / 1.5)
        if transfer_qty == 0:
            transfer_qty = 1
        dest_cap = DEST_CAP_ON_UNCONTROLLED_TILES if has_other_unit_dest else 16
        if unit_dest + transfer_qty > dest_cap:
            transfer_qty = dest_cap - unit_dest

        if transfer_qty:
            self.array_units[y_source][x_source] -= transfer_qty
            self.array_units[y_dest][x_dest] += transfer_qty

    def mode_travel_vertically(self):
        if not self.bounding_rect_exists:
            return
        for x in range(self.bounding_rect_x_min, self.bounding_rect_x_max):
            for y_source, y_dest in self.iter_vertical_expansion_column(x):
                self.travel_one_tile(x, y_source, x, y_dest)

    def mode_travel_horizontally(self):
        if not self.bounding_rect_exists:
            return
        for y in range(self.bounding_rect_y_min, self.bounding_rect_y_max):
            for x_source, x_dest in self.iter_horizontal_expansion_line(y):
                self.travel_one_tile(x_source, y, x_dest, y)

    def mode_grow(self):
        if not self.bounding_rect_exists:
            return
        coords_receive_growing = []
        for y in range(self.bounding_rect_y_min, self.bounding_rect_y_max):
            for x in range(self.bounding_rect_x_min, self.bounding_rect_x_max):
                if self.tiles_control[y][x] != self.player_id:
                    # Personne ne contrôle cette tile (donc pas moi)
                    # Ça veut dire qu'il y a des unités ennemies dessus.
                    # On peut pas grower sur cette tile.
                    continue
                unit_val = self.array_units[y][x]
                if unit_val < 16 and unit_val != -1:
                    coords_receive_growing.append((x, y))

        nb_grow = self.nb_controlled_tiles // 8
        coords_to_grow = random.sample(
            coords_receive_growing,
            min(nb_grow, len(coords_receive_growing))
        )
        for x, y in coords_to_grow:
            self.array_units[y][x] += 1

    def fight_one_tile(self, x, y):
        if self.tiles_control[y][x] is not None:
            # Quelqu'un contrôle cette tile (moi ou un autre)
            # Pas de combat dessus
            return
        unit_val = self.array_units[y][x]
        if not unit_val:
            # Pas de combat car pas d'unité à moi sur cette tile.
            return
        for player_opponent in self.other_players:
            unit_opponent = player_opponent.array_units[y][x]
            if unit_opponent:
                break
        if not unit_opponent:
            # Not supposed to happen, mais on sait jamais.
            return
        # On enlève une unité dans chaque camp.
        unit_val -= 1
        unit_opponent -= 1
        # Suppression gratuite d'une unité de l'opponent (avantage à la personne qui attaque)
        if unit_opponent:
            unit_opponent -= 1
        # Et pour finir, on enlève encore une unité dans chaque camp, si c'est possible.
        if unit_val and unit_opponent:
            unit_val -= 1
            unit_opponent -= 1
        self.array_units[y][x] = unit_val
        player_opponent.array_units[y][x] = unit_opponent

    def mode_fight(self):
        if not self.bounding_rect_exists:
            return
        for y in range(self.bounding_rect_y_min, self.bounding_rect_y_max):
            for x in range(self.bounding_rect_x_min, self.bounding_rect_x_max):
                self.fight_one_tile(x, y)

    def process_turn(self):
        if self.mode == MODE_GROW:
            self.mode_grow()
        elif self.mode == MODE_TRAVEL_VERTICALLY:
            self.mode_travel_vertically()
        elif self.mode == MODE_TRAVEL_HORIZONTALLY:
            self.mode_travel_horizontally()
        else:
            self.mode_fight()


class GameModel():

    def __init__(self):
        self.w = 50
        self.h = 40

        self.tiles_to_export = []
        self.tiles_control = []
        self.tiles_town = []
        for y in range(self.h):
            line_to_export = []
            line_control = []
            line_town = []
            for x in range(self.w):
                line_to_export.append([])
                line_control.append(None)
                line_town.append(False)
            self.tiles_to_export.append(tuple(line_to_export))
            self.tiles_control.append(line_control)
            self.tiles_town.append(line_town)
        self.tiles_to_export = tuple(self.tiles_to_export)
        self.tiles_control = tuple(self.tiles_control)
        self.tiles_town = tuple(self.tiles_town)

        self.players = (
            Player(
                0,
                self.w,
                self.h,
                "red",
                self.tiles_control,
                self.tiles_town,
                rightward=True,
                downward=False,
            ),
            Player(
                1,
                self.w,
                self.h,
                "blu",
                self.tiles_control,
                self.tiles_town,
                rightward=False,
                downward=True,
            ),
        )
        self.players[0].set_other_players((self.players[1], ))
        self.players[1].set_other_players((self.players[0], ))
        self.nb_players = len(self.players)

        self.update_indexations()
        self.update_towns()
        self.update_tile_to_export()
        self.must_start = True

        # TODO test.
        #for val in self.players[0].iter_horizontal_expansion_line(39):
        #    print(val)

    def iter_on_tiles_to_export(self):
        for line_to_export in self.tiles_to_export:
            for cell_to_export in line_to_export:
                yield cell_to_export

    def iter_on_tiles_control(self):
        for line_control in self.tiles_control:
            for cell_control in line_control:
                yield cell_control

    def update_indexations(self):
        """
        Met à jour le tableau indiquant quel joueur contrôle quelle tile.
        (On contrôle si on est le seul dessus).
        Compte le nombre de tile contrôlée pour chaque joueur.

        Met à jour les bounding rects.
        Les villes ne rentrent pas dans les bounding rects.
        Mais elles sont quand même comptées dans les cases contrôlées.
        On fera une indexation à part de tout ce qui concerne les villes.
        """
        xs_by_player = {}
        ys_by_player = {}
        nb_controlled_tiles_by_player = {}
        for player in self.players:
            xs_by_player[player.player_id] = []
            ys_by_player[player.player_id] = []
            nb_controlled_tiles_by_player[player.player_id] = 0

        for y in range(self.h):
            for x in range(self.w):
                controlled_by = []
                for player in self.players:
                    unit_val = player.array_units[y][x]
                    if unit_val:
                        controlled_by.append(player.player_id)
                    if unit_val != -1:
                        xs_by_player[player.player_id].append(x)
                        ys_by_player[player.player_id].append(y)
                if len(controlled_by) == 1:
                    controller_player_id = controlled_by[0]
                    self.tiles_control[y][x] = controller_player_id
                    nb_controlled_tiles_by_player[controller_player_id] += 1
                else:
                    self.tiles_control[y][x] = None

        # On envoie les xs et ys à chaque player pour qu'ils fassent leur bounding rects.
        # on envoie aussi le nombre de tiles contrôlées.
        for player in self.players:
            player.update_bounding_rects(
                xs_by_player[player.player_id],
                ys_by_player[player.player_id],
                nb_controlled_tiles_by_player[player.player_id],
            )

    def update_towns(self):
        """
        Met à jour uniquement le tableau des towns.
        """
        for y in range(self.h):
            for x in range(self.w):
                is_town = any(
                    (
                        player.array_units[y][x] == -1
                        for player
                        in self.players
                    )
                )
                self.tiles_town[y][x] = is_town

    def update_tile_to_export(self):
        general_iterators = [self.iter_on_tiles_to_export(), self.iter_on_tiles_control()]
        player_iterators = [player.iter_on_gamobjs() for player in self.players]
        all_iterators = general_iterators + player_iterators
        for iterated_elems in zip(*all_iterators):
            cell, controller_id, *player_units = iterated_elems
            if controller_id is not None:
                # C'est vilain parce qu'on utilise un id de player comme index dans une liste.
                # Mais bon, pouet, ça passe.
                cell[:] = [self.players[controller_id].color + "_controls"]
            else:
                cell[:] = []
            cell.extend([player_unit for player_unit in player_units if player_unit is not None])

    def export_all_tiles(self):
        return self.tiles_to_export

    def on_process_turn(self):
        self.update_indexations()
        self.players[0].process_turn()
        # self.players[1].process_turn()
        self.update_tile_to_export()
        # TODO : calculer approximativement un délai plus ou moins long selon la quantité de trucs à gérer.
        return """ { "delayed_actions": [ {"name": "process_turn", "delay_ms": 20} ] } """

    def on_game_event(self, event_name):
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
