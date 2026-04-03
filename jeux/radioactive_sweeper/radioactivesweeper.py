# https://i.ibb.co/whNpJc2T/radioactive-tileset.png
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
    "red_cross": [0, 96],
    "dome_3x3_neutral": [96, 64, 96, 96],

    "background": [0, 0]
  },
  "show_code_at_start": true,
  "appendices": {

  }
}
"""

INDEX_LEVEL = 1

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
        # Lorsque le barrel a été trouvé, on garde la couleur, mais on indique une strength de 0.
        self.barrel_color = None
        self.barrel_strength = None
        self._update_previous_values()

    def deradioactivize(self):
        self.barrel_strength = 0

    def compute_game_objects(self):

        if not self._has_changed():
            return

        #print("change on", self._coord, self.rad_strengths, "b", self.barrel_strength, self.prev_rad_strengths, "prevb", self.prev_barrel_strength)
        while self.game_objects:
            gobj = self.game_objects[0]
            #print("remove", gobj.sprite_name)
            self.layer_owner.remove_game_object(gobj)
        #print("self.game_objects", self.game_objects)

        if self.barrel_color == RadColor.YELLOW:
            if self.barrel_strength == 1:
                # TODO LIB : ça fait du yo-yo. On devrait avoir une fonction dans Tile,
                # pour ajouter/supprimer des game objects directement dedans.
                gobj_source = GameObject(self._coord, "rad_ylw_source")
                self.layer_owner.add_game_object(gobj_source)
            gobj_barrel = GameObject(self._coord, "rad_ylw_barrel")
            self.layer_owner.add_game_object(gobj_barrel)

        sum_strength = min(19, sum(self.rad_strengths))
        if self.barrel_color is not None:
            sum_strength = 0
        #print("WIP", self._coord, sum_strength)
        if sum_strength:
            if sum_strength > 19:
                raise Exception("TODO : Pas de sprite de radioactivité après 19 !!!")
            gobj_rad_indic = GameObject(self._coord, f"rad_{sum_strength:02d}")
            self.layer_owner.add_game_object(gobj_rad_indic)

        #print("self.game_objects", self.game_objects)
        self._update_previous_values()

    def _update_previous_values(self):
        self.prev_rad_strengths = list(self.rad_strengths)
        self.prev_barrel_color = self.barrel_color
        self.prev_barrel_strength = self.barrel_strength

    def _has_changed(self):
        return any(
            (
                self.prev_rad_strengths != self.rad_strengths,
                self.prev_barrel_color != self.barrel_color,
                self.prev_barrel_strength != self.barrel_strength,
            )
        )

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

    def no_more_barrels(self):
        for c in squarity.RectIterator(self.rect):
            if self.get_tile(c).barrel_strength:
                return False
        return True

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

        #print("----------------")
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
        self.layer_buildings = squarity.Layer(self, self.w, self.h, show_transitions=True)
        self.layers.append(self.layer_buildings)
        self.mode_lay_dome = False
        self.layer_ihm = squarity.Layer(self, self.w, self.h, show_transitions=False)
        self.layers.append(self.layer_ihm)
        self.gobjs_red_crosses = []
        self.gobjs_selected_dome = []
        self.ended_game = False
        self.end_game_phrase = ""

        for c in squarity.RectIterator(self.rect):
            gobj = GameObject(c, "block")
            if c.x >= 3 or c.y >= 3:
                self.layer_block.add_game_object(gobj)
        self.gobj_dome = GameObject(
            Coord(0, 0),
            "dome_3x3_neutral",
            back_caller=squarity.ComponentBackCaller()
        )
        self.gobj_dome.plock_transi = squarity.PlayerLockTransi.LOCK
        self.layer_buildings.add_game_object(self.gobj_dome)

        #for _ in range(11):
        #    coord_barrel = Coord(
        #        random.randrange(0, self.w),
        #        random.randrange(0, self.h)
        #    )
        #    if coord_barrel.x >= 5 or coord_barrel.y >= 5:
        #        self.layer_radact.add_barrel(coord_barrel, RadColor.YELLOW)
        if INDEX_LEVEL == 1:
            self.put_barrels_level_1()
        else:
            self.put_barrels_level_2()

        self.layer_radact.compute_rad_indicators()

    def put_barrels_level_1(self):
        forbidden_rect_1 = squarity.Rect(0, 0, 4, 6)
        forbidden_rect_2 = squarity.Rect(0, 0, 6, 3)
        for _ in range(7):
            coord_barrel = Coord(
                random.randrange(1, self.w - 1),
                random.randrange(1, self.h - 1)
            )
            if not forbidden_rect_1.in_bounds(coord_barrel) and not forbidden_rect_2.in_bounds(coord_barrel):
                tile_radact = self.layer_radact.get_tile(coord_barrel)
                no_barrel_around = all(
                    (tile_adj is None) or not tile_adj.barrel_strength
                    for tile_adj in tile_radact.adjacencies
                )
                if no_barrel_around:
                    self.layer_radact.add_barrel(coord_barrel, RadColor.YELLOW)

    def put_barrels_level_2(self):
        for _ in range(14):
            coord_barrel = Coord(
                random.randrange(0, self.w),
                random.randrange(0, self.h)
            )
            if coord_barrel.x >= 4 or coord_barrel.y >= 4:
                self.layer_radact.add_barrel(coord_barrel, RadColor.YELLOW)

    def check_dome_laying(self, coord_dome_laying):
        """
        Si ça marche, renvoie True.
        Sinon, rajoute des objets de red cross, et renvoie False.
        """
        if self.rect.on_border(coord_dome_laying):
            gobj = GameObject(coord_dome_laying, "red_cross")
            self.gobjs_red_crosses.append(gobj)
            self.layer_ihm.add_game_object(gobj)
            print("On ne peut pas poser le dôme sur les bords de l'aire de jeu")
            return False

        laying_ok = True
        tile_block = self.layer_block.get_tile(coord_dome_laying)
        if not tile_block.game_objects:
            gobj = GameObject(coord_dome_laying, "red_cross")
            self.gobjs_red_crosses.append(gobj)
            self.layer_ihm.add_game_object(gobj)
            laying_ok = False
        for tile_adj in tile_block.adjacencies:
            if tile_adj.game_objects:
                gobj = GameObject(tile_adj.get_coord(), "red_cross")
                self.gobjs_red_crosses.append(gobj)
                self.layer_ihm.add_game_object(gobj)
                laying_ok = False

        tile_radac = self.layer_radact.get_tile(coord_dome_laying)
        if laying_ok:
            if tile_radac.barrel_color is None:
                print("EPIC FAIL! Vous méritez de perdre la partie !!")
                self.ended_game = True
                self.end_game_phrase = "EPIC FAIL! Vous méritez de perdre la partie !!"
                laying_ok = False
        return laying_ok

    def deradioactivize(self, coord):
        tile_to_deradact = self.layer_radact.get_tile(coord)
        tile_to_deradact.deradioactivize()
        self.layer_block.remove_at_coord(coord)
        self.layer_radact.compute_rad_indicators()
        if self.layer_radact.no_more_barrels():
            self.ended_game = True
            if INDEX_LEVEL == 1:
                self.end_game_phrase = "Bravo !!! Augmentez de 1 la valeur de INDEX_LEVEL au début du code source, puis, relancez une partie"
            else:
                self.end_game_phrase = "Bravo !!! Vous avez gagné ! Bientôt, de nouvelles versions de ce jeu seront créées."
            print(self.end_game_phrase)

    def on_click(self, coord):

        #self.tas_de_log(coord)

        if self.ended_game:
            print(self.end_game_phrase)
            return

        if coord.x < 3 and coord.y < 3:

            self.mode_lay_dome = not self.mode_lay_dome
            if self.mode_lay_dome:
                print("Mode: posage du dome de dé-radioactivisation.")
                for _ in range(2):
                    # TODO : éviter de crééer/détruire des gobjs à chaque fois.
                    gobj_dome = GameObject(Coord(0, 0), "dome_3x3_neutral")
                    self.layer_ihm.add_game_object(gobj_dome)
                    self.gobjs_selected_dome.append(gobj_dome)
            else:
                for gobj in self.gobjs_selected_dome:
                    self.layer_ihm.remove_game_object(gobj)
                self.gobjs_selected_dome[:] = []
                print("Mode: exploration des cases.")

        else:

            if not self.mode_lay_dome:
                if self.layer_radact.get_tile(coord).barrel_strength:
                    self.ended_game = True
                    self.end_game_phrase = "Fail !!! Cliquez sur Exécutez pour recommencer une partie."
                    for c in squarity.RectIterator(self.rect):
                        self.layer_block.remove_at_coord(c)
                    print(self.end_game_phrase)
                else:
                    self.layer_block.remove_at_coord(coord)

            else:
                dome_laying_ok = self.check_dome_laying(coord)
                if not dome_laying_ok:
                    ev = squarity.EventResult()
                    ev.add_delayed_callback(
                        squarity.DelayedCallBack(700, self.remove_red_cross)
                    )
                    return ev
                else:
                    self.mode_lay_dome = False
                    for gobj in self.gobjs_selected_dome:
                        self.layer_ihm.remove_game_object(gobj)
                    self.gobjs_selected_dome[:] = []
                    dest_dome = coord.clone().move_dir(dirs.UpLeft)
                    self.gobj_dome.add_transition(
                        squarity.TransitionSteps(
                            "coord",
                            (
                                (500, dest_dome),
                                (600, dest_dome),
                                (500, Coord(0, 0))
                            )
                        )
                    )
                    self.gobj_dome.back_caller.add_callback(
                        squarity.DelayedCallBack(
                            800,
                            lambda: self.deradioactivize(coord)
                        )
                    )

    def remove_red_cross(self):
        for gobj in self.gobjs_red_crosses:
            self.layer_ihm.remove_game_object(gobj)
        self.gobjs_red_crosses[:] = []

    def on_button_direction(self, direction):
        pass

    def on_button_action(self, action_name):
        pass

    # TODO WIP voilà voilà.
    def tas_de_log(self, coord):
        print("layers details")
        for layer in self.layers:
            print("----")
            for gobj in layer.get_tile(coord).game_objects:
                print(gobj._coord, gobj.sprite_name)