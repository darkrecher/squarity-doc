# https://i.ibb.co/Jd3207P/search-the-diam.png

"""
  {
    "name": "Un diamant cherche son pote",
    "version": "2.1.0",
    "game_area": {
      "nb_tile_width": 6,
      "nb_tile_height": 8
    },
    "tile_size": 40,
    "img_coords": {
      "gem_yellow": [0, 0],
      "gem_green": [58, 0],
      "background": [0, 40, 120, 160]
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
        self.gobj_bg = squarity.GameObject(
            Coord(2, 2),
            "background",
            image_modifier=squarity.ComponentImageModifier(
                img_size_x=120, img_size_y=160,
                area_scale_x=2.0, area_scale_y=2.0,
            )
        )
        self.layer_main.add_game_object(self.gobj_bg)
        self.coord_zone = Coord(0, 0)

    def on_button_direction(self, direction):
        self.move_zone(direction)

    def move_zone(self, direction):
        if direction == d.Right:
            if self.coord_zone.x == 0:
                self.gobj_bg.add_transition(
                    squarity.TransitionSteps(
                        "coord",
                        ((200, Coord(0, 2)), )
                    )
                )
                self.gobj_bg.image_modifier.add_transition(
                    squarity.TransitionSteps(
                        "img_offset_x",
                        ((200, 0.001), (600, 80), )
                    )
                )
                self.coord_zone.x += 1
            elif self.coord_zone.x < 5:
                self.gobj_bg.image_modifier.add_transition(
                    squarity.TransitionSteps(
                        "img_offset_x",
                        ((800, 80 + 120 * self.coord_zone.x), )
                    )
                )
                self.coord_zone.x += 1
        elif direction == d.Left:
            if self.coord_zone.x == 1:
                self.gobj_bg.image_modifier.add_transition(
                    squarity.TransitionSteps(
                        "img_offset_x",
                        ((600, 0.001), )
                    )
                )
                self.gobj_bg.add_transition(
                    squarity.TransitionSteps(
                        "coord",
                        ((600, Coord(0, 2)), (200, Coord(2, 2)), )
                    )
                )
                self.coord_zone.x -= 1
            elif self.coord_zone.x > 1:
                self.gobj_bg.image_modifier.add_transition(
                    squarity.TransitionSteps(
                        "img_offset_x",
                        ((800, -160 + 120 * self.coord_zone.x), )
                    )
                )
                self.coord_zone.x -= 1



