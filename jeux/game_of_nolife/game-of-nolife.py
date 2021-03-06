# https://i.ibb.co/mczrkx2/game-of-nolife-tileset.png

"""
{
  "game_area": {
    "nb_tile_width": 40,
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



class Player():

    def __init__(self, w, h, color, rightward, downward):
        self.w = w
        self.h = h
        self.color = color
        self.rightward = rightward
        self.downward = downward
        self.other_players = None
        self.array_units = []
        for y in range(self.h):
            line = []
            for x in range(self.w):
                unit_val = 0
                line.append(unit_val)
            self.array_units.append(line)
        self.array_units = tuple(self.array_units)

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
        self.array_units[y_town][x_town] = 16

        self.update_bounding_rects()
        print("bounding rect", self.color)
        print(self.bounding_rect_x_min, self.bounding_rect_y_min, self.bounding_rect_x_max, self.bounding_rect_y_max)

    def set_other_players(self, other_players):
        self.other_players = other_players

    def iter_on_gamobjs(self):
        for line in self.array_units:
            for unit_val in line:
                if unit_val:
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

    def mode_grow(self):
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
                    if unit_val < 16:
                        coords_receive_growing.append((x, y))
        nb_grow //= 4
        coords_to_grow = random.sample(
            coords_receive_growing,
            min(nb_grow, len(coords_receive_growing))
        )
        for x, y in coords_to_grow:
            self.array_units[y][x] += 1


class GameModel():

    def __init__(self):
        self.w = 40
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
        self.players[0].update_bounding_rects()
        self.players[0].mode_grow()
        self.players[1].update_bounding_rects()
        self.players[1].mode_grow()
        # TODO : calculer approximativement un délai plus ou moins long selon la quantité de trucs à gérer.
        return """ { "delayed_actions": [ {"name": "process_turn", "delay_ms": 300} ] } """

    def on_game_event(self, event_name):
        if event_name == "process_turn":
            return self.on_process_turn()
        if self.must_start:
            self.must_start = False
            return """ { "delayed_actions": [ {"name": "process_turn", "delay_ms": 300} ] } """
