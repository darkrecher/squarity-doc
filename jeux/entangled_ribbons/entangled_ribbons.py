# https://ibb.co/rHsfXWK
# https://i.ibb.co/GRT3rhf/ent-rib-tileset.png

"""
  {
    "name": "Entangled ribbon",
    "version": "2.1.0",
    "game_area": {
      "nb_tile_width": 20,
      "nb_tile_height": 20
    },
    "tile_size": 32,
    "img_coords": {
      "rib_red_horiz": [0, 32],
      "rib_red_vertic": [32, 32],
      "rib_red_turn_06": [64, 32],
      "rib_red_turn_02": [96, 32],
      "rib_red_turn_24": [128, 32],
      "rib_red_turn_46": [160, 32],
      "rib_red_extr_6": [192, 32],
      "rib_red_extr_0": [224, 32],
      "rib_red_extr_4": [256, 32],
      "rib_red_extr_2": [288, 32],
      "background": [0, 0]
    }
  }
"""

import squarity
Coord = squarity.Coord
GameObject = squarity.GameObject

WORLD_WIDTH = 100
WORLD_HEIGHT = 100

class Ribbon():

    def __init__(self, ribbons_world):
        self.gobjs = []
        self.color = "red"
        self.ribbons_world = ribbons_world
        self.hard_code_path()

    def hard_code_path(self):
        self.gobjs = [
            GameObject(Coord(18, 18), "rib_red_extr_4"),
            GameObject(Coord(18, 19), "rib_red_vertic"),
            GameObject(Coord(18, 20), "rib_red_turn_02"),
            GameObject(Coord(19, 20), "rib_red_horiz"),
            GameObject(Coord(20, 20), "rib_red_horiz"),
            GameObject(Coord(21, 20), "rib_red_extr_6"),
        ]
        for gobj in self.gobjs:
            self.ribbons_world.add_game_object(gobj)


class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.ribbons_world = squarity.Layer(self, WORLD_WIDTH, WORLD_HEIGHT)
        self.ribbons_view = squarity.Layer(self, self.w, self.h)
        self.layers.append(self.ribbons_view)
        self.gobj = squarity.GameObject(
            Coord(18, 19), "rib_red_vertic")
        self.ribbons_world.add_game_object(self.gobj)
        self.view_rect = squarity.Rect(15, 15, self.w-2, self.h-2)

        rect_background = squarity.Rect(1, 1, self.w-2, self.h-2)
        for c in squarity.Sequencer.iter_on_rect(rect_background):
            self.layer_main.add_game_object(GameObject(c, "background"))

        self.rib = Ribbon(self.ribbons_world)
        self.render_world()

    def render_world(self):
        view_corner_x = self.view_rect.x
        view_corner_y = self.view_rect.y
        c_view = Coord(0, 0)
        for c_world in squarity.Sequencer.iter_on_rect(self.view_rect):
            c_view.x = c_world.x - view_corner_x + 1
            c_view.y = c_world.y - view_corner_y + 1
            self.ribbons_view.remove_at_coord(c_view)
            for gobj_world in self.ribbons_world.get_game_objects(c_world):
                gobj_view = GameObject(c_view, gobj_world.sprite_name)
                self.ribbons_view.add_game_object(gobj_view)

    def on_button_direction(self, direction):
        dx, dy = direction.vector
        self.view_rect.x += dx
        self.view_rect.y += dy
        self.render_world()




