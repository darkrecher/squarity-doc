# https://i.ibb.co/PsvKxFgH/radioactive-tileset.png
# taille de l'aire de jeu : 40, 25 ??
"""
{
  "name": "Radioactive Sweeper",
  "version": "2.1.0",
  "game_area": {
    "nb_tile_width": 15,
    "nb_tile_height": 10
  },
  "tile_size": 32,
  "img_coords": {
    "rad_01": [32, 0],
    "rad_02": [64, 0],
    "rad_03": [96, 0],
    "rad_04": [128, 0],
    "rad_05": [160, 0],
    "rad_06": [192, 0],
    "rad_07": [224, 0],
    "rad_08": [256, 0],
    "rad_09": [288, 0],
    "rad_10": [0, 32],
    "rad_11": [32, 32],
    "rad_12": [64, 32],
    "rad_13": [96, 32],
    "rad_14": [128, 32],
    "rad_15": [160, 32],
    "rad_16": [192, 32],
    "rad_17": [224, 32],
    "rad_18": [256, 32],
    "rad_19": [288, 32],

    "block": [0, 64],
    "rad_ylw_source": [32, 64],
    "rad_ylw_barrel": [64, 64],

    "background": [0, 0]
  },
  "show_code_at_start": true,
  "appendices": {

  }
}
"""

import random
from enum import IntEnum
import squarity
Coord = squarity.Coord
dirs = squarity.dirs
GameObject = squarity.GameObject


# class syntax
class RadColor(IntEnum):
    YELLOW = 0
    GREEN = 1
    PURPLE = 2

PATTERN_RAD_YELLOW_1 = (
    (0, -1, 6), (1, -1, 6), (1, 0, 6), (1, 1, 6),
    (0, 1, 6), (-1, 1, 6), (-1, 0, 6), (-1, -1, 6),
    (0, -2, 4), (2, 0, 4), (0, 2, 4), (-2, 0, 4),
    (0, -3, 2), (3, 0, 2), (0, 3, 2), (-3, 0, 2),
)

class RadTile(squarity.Tile):

    def __init__(self, layer_owner, coord):
        super().__init__(layer_owner, coord)
        self.rad_strengths = [0, 0, 0]
        self.barrel_color = None
        self.barrel_strength = None
        self._update_previous_values()

    def _update_previous_values(self):
        self.prev_rad_strengths = list(self.rad_strengths)
        self.prev_barrel_color = self.barrel_color
        self.prev_barrel_strength = self.barrel_strength

    def has_changed(self):
        return any(
            (
                self.prev_rad_strengths != self.rad_strengths,
                self.prev_barrel_color != self.barrel_color,
                self.prev_barrel_strength != self.barrel_strength,
            )
        )

    def compute_game_objects(self):

        if not self.has_changed():
            return

        for gobj in self.game_objects:
            self.layer_owner.remove_game_object(gobj)

        if self.barrel_color == RadColor.YELLOW and self.barrel_strength == 1:
            # TODO LIB : ça fait du yo-yo. On devrait avoir une fonction dans Tile,
            # pour ajouter/supprimer des game objects directement dedans.
            gobj_source = GameObject(self._coord, "rad_ylw_source")
            self.layer_owner.add_game_object(gobj_source)
            gobj_barrel = GameObject(self._coord, "rad_ylw_barrel")
            self.layer_owner.add_game_object(gobj_barrel)

        sum_strength = min(19, sum(self.rad_strengths))
        #print("WIP", self._coord, sum_strength)
        if sum_strength:
            if sum_strength > 19:
                raise Exception("TODO : Pas de sprite de radioactivité après 19 !!!")
            gobj_rad_indic = GameObject(self._coord, f"rad_{sum_strength:02d}")
            self.layer_owner.add_game_object(gobj_rad_indic)

        self._update_previous_values()

class RadioactivityLayer(squarity.Layer):

    # TODO : une vraie fonction init, please.
    def init(self):
        self.rect = squarity.Rect(0, 0, self.w, self.h)
        # TODO LIB : on doit pouvoir indiquer une autre classe Tile, que le Layer instanciera dans tiles.
        self.tiles = [
            [
                RadTile(self, Coord(x, y)) for x in range(self.w)
            ]
            for y in range(self.h)
        ]
        for y in range(self.h):
            for x in range(self.w):
                self.tiles[y][x].adjacencies = self._make_adjacencies(x, y)

    def add_barrel(self, coord_barrel, rad_color, strength=1):
        if rad_color != RadColor.YELLOW:
            raise Exception("TODO Rad !!")
        tile_dest = self.get_tile(coord_barrel)
        tile_dest.barrel_color = rad_color
        tile_dest.barrel_strength = strength

    def compute_rad_indicators(self):

        for c in squarity.RectIterator(self.rect):
            self.get_tile(c).rad_strengths[:] = [0, 0, 0]

        for c in squarity.RectIterator(self.rect):
            tile_barrel = self.get_tile(c)
            if tile_barrel.barrel_color == RadColor.YELLOW and tile_barrel.barrel_strength == 1:
                pattern = PATTERN_RAD_YELLOW_1
                rad_color_index = RadColor.YELLOW
                for ofs_x, ofs_y, strength in pattern:
                    coord_indic = c.clone().move_by_vect(x=ofs_x, y=ofs_y)
                    if self.rect.in_bounds(coord_indic):
                        tile_indic = self.get_tile(coord_indic)
                        tile_indic.rad_strengths[rad_color_index] += strength
                        #print("WIP", tile_indic.rad_strengths)

        for c in squarity.RectIterator(self.rect):
            self.get_tile(c).compute_game_objects()


class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.layer_background = self.layer_main
        self.layer_radact = RadioactivityLayer(self, self.w, self.h, show_transitions=False)
        self.layer_radact.init()
        self.layers.append(self.layer_radact)
        self.layer_block = squarity.Layer(self, self.w, self.h, show_transitions=False)
        self.layers.append(self.layer_block)

        for c in squarity.RectIterator(self.rect):
            gobj = GameObject(c, "block")
            self.layer_block.add_game_object(gobj)

        for _ in range(10):
            x_barrel = random.randrange(0, self.w)
            y_barrel = random.randrange(0, self.h)
            self.layer_radact.add_barrel(Coord(x_barrel, y_barrel), RadColor.YELLOW)

        self.layer_radact.compute_rad_indicators()

    def on_click(self, coord):
        self.layer_block.remove_at_coord(coord)

    def on_button_direction(self, direction):
        pass

    def on_button_action(self, action_name):
        pass
