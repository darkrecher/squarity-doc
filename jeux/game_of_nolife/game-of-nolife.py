# https://i.ibb.co/mczrkx2/game-of-nolife-tileset.png

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
    "blu_16": [60, 4]

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

class Player():

    def __init__(self, w, h, color, rightward, downward):
        self.w = w
        self.h = h
        self.color = color
        self.rightward = rightward
        self.downward = downward
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
        # TODO : faire des vraies sprites de towns.
        self.array_town_names[y_town][x_town] = self.color + "_16"

        self.update_bounding_rects()
        print("bounding rect", self.color)
        print(self.bounding_rect_x_min, self.bounding_rect_y_min, self.bounding_rect_x_max, self.bounding_rect_y_max)

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

    def update_bounding_rects(self):
        x_with_unit = []
        y_with_unit = []
        for y in range(self.h):
            for x in range(self.w):
                if self.array_units[y][x]:
                    x_with_unit.append(x)
                    y_with_unit.append(y)

        # Ça planterait dans le cas où le player n'a plus aucune unité.
        # On calculerait des min et des max de listes vide.
        # Mais y'a forcément toujours une unité, vu que dès le départ on a une ville
        # TODO : ouais mais le joueur vert, il va se passer quoi pour lui ?
        if self.rightward:
            self.bounding_rect_x_min = 0
            self.bounding_rect_x_max = max(x_with_unit) + 1
        else:
            self.bounding_rect_x_min = min(x_with_unit)
            self.bounding_rect_x_max = self.w

        if self.downward:
            self.bounding_rect_y_min = 0
            self.bounding_rect_y_max = max(y_with_unit) + 1
        else:
            self.bounding_rect_y_min = min(y_with_unit)
            self.bounding_rect_y_max = self.h

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

    def travel_one_tile(self, source_x, source_y, dest_x, dest_y):
        unit_source = self.array_units[source_y][source_x]
        if unit_source in (0, 1, -1):
            return
        unit_dest = self.array_units[dest_y][dest_x]
        if unit_dest in (16, -1):
            return
        if unit_source <= unit_dest + 1:
            return
        # TODO : dans une fonction, ce truc là.
        has_other_unit_dest = all(
            (
                player.array_units[dest_y][dest_x] != 0
                for player in self.other_players
            )
        )
        # Pas de déplacement à plus de 8 unités sur une tile qui a des unités ennemies.
        if has_other_unit_dest and unit_dest >= 8:
            return
        transfer_qty = int((unit_source - unit_dest) / 1.5)
        if transfer_qty == 0:
            transfer_qty = 1
        dest_cap = 8 if has_other_unit_dest else 16
        if unit_dest + transfer_qty > dest_cap:
            transfer_qty = dest_cap - unit_dest

        self.array_units[source_y][source_x] -= transfer_qty
        self.array_units[dest_y][dest_x] += transfer_qty

    def mode_travel_vertically(self):
        # TODO général. Ça y est j'ai commencé à foutre la merde entre source_y et y_source. Va falloir homogénéiser ça.
        self.update_bounding_rects()
        for x in range(self.bounding_rect_x_min, self.bounding_rect_x_max):
            for y_source, y_dest in self.iter_vertical_expansion_column(x):
                self.travel_one_tile(x, y_source, x, y_dest)

    def mode_travel_horizontally(self):
        self.update_bounding_rects()
        for y in range(self.bounding_rect_y_min, self.bounding_rect_y_max):
            for x_source, x_dest in self.iter_horizontal_expansion_line(y):
                self.travel_one_tile(x_source, y, x_dest, y)


    def mode_grow(self):
        # TODO : pas besoin de faire ça à chaque tour. Que au premier "grow".
        self.update_bounding_rects()
        coords_receive_growing = []
        nb_grow = 0
        for y in range(self.bounding_rect_y_min, self.bounding_rect_y_max):
            for x in range(self.bounding_rect_x_min, self.bounding_rect_x_max):
                unit_val = self.array_units[y][x]
                if unit_val:
                    has_other_unit = all(
                        (
                            player.array_units[y][x] != 0
                            for player in self.other_players
                        )
                    )
                    if has_other_unit:
                        continue
                    nb_grow += 1
                    if unit_val < 16 and unit_val != -1:
                        coords_receive_growing.append((x, y))
        nb_grow //= 8
        coords_to_grow = random.sample(
            coords_receive_growing,
            min(nb_grow, len(coords_receive_growing))
        )
        for x, y in coords_to_grow:
            self.array_units[y][x] += 1

    def process_turn(self):
        if self.mode == MODE_GROW:
            self.mode_grow()
        elif self.mode == MODE_TRAVEL_VERTICALLY:
            self.mode_travel_vertically()
        else:
            self.mode_travel_horizontally()


class GameModel():

    def __init__(self):
        self.w = 50
        self.h = 40
        self.tiles_to_export = []
        self.players = (
            Player(self.w, self.h, "red", rightward=True, downward=False),
            Player(self.w, self.h, "blu", rightward=False, downward=True),
        )
        self.players[0].set_other_players((self.players[1], ))
        self.players[1].set_other_players((self.players[0], ))
        self.must_start = True

        for y in range(self.h):
            line_to_export = []
            for x in range(self.w):
                line_to_export.append([])
            self.tiles_to_export.append(tuple(line_to_export))
        self.tiles_to_export = tuple(self.tiles_to_export)

        # TODO test.
        for val in self.players[0].iter_horizontal_expansion_line(39):
            print(val)

    def iter_on_tile_to_exports(self):
        for line_to_export in self.tiles_to_export:
            for cell_to_export in line_to_export:
                yield cell_to_export

    def update_tile_to_export(self):
        player_iterators = [player.iter_on_gamobjs() for player in  self.players]
        all_iterators = [self.iter_on_tile_to_exports()] + player_iterators
        for iterated_elems in zip(*all_iterators):
            cell, *player_units = iterated_elems
            cell[:] = [player_unit for player_unit in player_units if player_unit is not None]

    def export_all_tiles(self):
        self.update_tile_to_export()
        # print(self.tiles_to_export) # TODO : crap
        return self.tiles_to_export

    def on_process_turn(self):
        self.players[0].process_turn()
        self.players[1].process_turn()
        # TODO : calculer approximativement un délai plus ou moins long selon la quantité de trucs à gérer.
        return """ { "delayed_actions": [ {"name": "process_turn", "delay_ms": 200} ] } """

    def on_game_event(self, event_name):
        if event_name == "process_turn":
            return self.on_process_turn()
        if self.must_start:
            self.must_start = False
            return """ { "delayed_actions": [ {"name": "process_turn", "delay_ms": 200} ] } """
        else:
            for player in self.players:
                player.mode += 1
                # TODO : ça c'est crade.
                if player.mode > 2:
                    player.mode = 0
                print("player.mode", player.mode, player.color)
