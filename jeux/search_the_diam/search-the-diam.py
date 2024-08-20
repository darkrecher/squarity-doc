# https://i.ibb.co/Jd3207P/search-the-diam.png

"""
  {
    "name": "Un diamant cherche son pote",
    "version": "2.1.0",
    "game_area": {
      "nb_tile_width": 7,
      "nb_tile_height": 8
    },
    "tile_size": 40,
    "img_coords": {
      "gem_yellow": [0, 0],
      "gem_green": [58, 0],
      "background": [0, 40, 640, 400]
    }
  }
"""

"""
Origine de l'image de background:
https://opengameart.org/content/centered-around-the-hero

"""

import squarity

Coord = squarity.Coord
d = squarity.dirs

class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.layer_gem = squarity.Layer(self, self.w, self.h)
        self.layers.append(self.layer_gem)
        self.gobj_bg = squarity.GameObject(
            Coord(0, 0),
            "background",
            image_modifier=squarity.ComponentImageModifier(
                area_scale_x=2.0, area_scale_y=2.0,
                img_offset_x=-20, img_offset_y=-20,
                img_size_x=640, img_size_y=400,
            )
        )
        self.gobj_bg.set_callback_end_transi(self.on_move_zone_end)
        self.layer_main.add_game_object(self.gobj_bg)
        self.coord_zone = Coord(0, 0)

        self.gem_yellow = squarity.GameObject(
            Coord(2, 3),
            "gem_yellow",
            image_modifier=squarity.ComponentImageModifier()
        )
        self.gem_yellow.coord_global = Coord(2, 3)
        self.layer_gem.add_game_object(self.gem_yellow)


    def on_button_direction(self, direction):
        self.move_zone(direction)
        rect_visible = self.compute_rect_visible()
        if rect_visible.in_bounds(self.gem_yellow.coord_global) and self.gem_yellow.layer_owner is None:
            self.layer_gem.add_game_object(self.gem_yellow)
        if not rect_visible.in_bounds(self.gem_yellow.coord_global) and self.gem_yellow.layer_owner is not None:
            self.layer_gem.remove_game_object(self.gem_yellow)


    def compute_rect_visible(self):
        rect_visible = squarity.Rect(
            self.coord_zone.x * 7 - 1,
            self.coord_zone.y * 7 - 1,
            7,
            8
        )
        if self.coord_zone.x == 4:
            rect_visible.x -= 1
        return rect_visible


    def move_zone(self, direction):
        scroll_vector = Coord(0, 0)
        scroll_time = 0
        if direction == d.Right:
            if self.coord_zone.x < 4:
                self.coord_zone.x += 1
                if self.coord_zone.x == 4:
                    scroll_vector = Coord(6, 0)
                    scroll_time = 800
                    transi_param = (scroll_time, -20 + 140 * self.coord_zone.x - 20)
                else:
                    scroll_vector = Coord(7, 0)
                    scroll_time = 1000
                    transi_param = (scroll_time, -20 + 140 * self.coord_zone.x)
                self.gobj_bg.image_modifier.add_transition(
                    squarity.TransitionSteps("img_offset_x", (transi_param, ))
                )
        elif direction == d.Left:
            if self.coord_zone.x:
                self.coord_zone.x -= 1
                if self.coord_zone.x == 4:
                    scroll_vector = Coord(-6, 0)
                    scroll_time = 800
                    transi_param = (scroll_time, -20 + 140 * self.coord_zone.x)
                else:
                    scroll_vector = Coord(-7, 0)
                    scroll_time = 1000
                    transi_param = (scroll_time, -20 + 140 * self.coord_zone.x)
                self.gobj_bg.image_modifier.add_transition(
                    squarity.TransitionSteps("img_offset_x", (transi_param, ))
                )
        elif direction == d.Down:
            if self.coord_zone.y < 2:
                self.coord_zone.y += 1
                scroll_vector = Coord(0, 7)
                scroll_time = 1000
                transi_param = (scroll_time, -20 + 140 * self.coord_zone.y)
                self.gobj_bg.image_modifier.add_transition(
                    squarity.TransitionSteps("img_offset_y", (transi_param, ))
                )
        elif direction == d.Up:
            if self.coord_zone.y:
                self.coord_zone.y -= 1
                scroll_vector = Coord(0, -7)
                scroll_time = 1000
                transi_param = (scroll_time, -20 + 140 * self.coord_zone.y)
                self.gobj_bg.image_modifier.add_transition(
                    squarity.TransitionSteps("img_offset_y", (transi_param, ))
                )
        return scroll_time, scroll_vector


    def on_move_zone_end(self):
        print("on_move_zone_end", self.coord_zone)



