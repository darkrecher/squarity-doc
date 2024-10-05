# https://i.ibb.co/LhK8pLm/skweek-breakout.png


"""
  {
    "name": "Skweek breakout",
    "version": "2.1.0",
    "game_area": {
      "nb_tile_width": 16,
      "nb_tile_height": 18
    },
    "tile_size": 48,
    "img_coords": {
      "skweek": [0, 0, 48, 48, "center"],
      "block_blue": [48, 0],
      "block_white": [96, 0]
    }
  }

"""

import squarity
from squarity import Coord


class Skweek(squarity.GameObject):

    def intialize(self, rge_bounds):
        # RGE = Rect Game Engine. Les coordonnées avec les unités du moteur de jeu.
        # CBR = Coord Breakout. Les coordonnées avec les unités du jeu de casse-brique
        # Il suffit juste de faire un scaling pour changer
        # entre les coord Game Engine et les coord Breakout.
        margin = 100
        self.rbr_bounds = squarity.Rect(
            -margin, -margin,
            rge_bounds.w * 240 + margin, rge_bounds.h * 240 + margin,
        )
        #self.cbr_pos = Coord(240*8, 240*9)
        self.cbr_pos = Coord(0, 0)
        self.cbr_move = Coord(-50, 30)
        self.set_size(240*5)
        self.update_pos_screen()

    def set_size(self, size):
        self.size = size
        self.image_modifier.area_scale_x = size / 240
        self.image_modifier.area_scale_y = size / 240

    def update_pos_screen(self):
        self.image_modifier.area_offset_x = self.cbr_pos.x/240 -0.5
        self.image_modifier.area_offset_y = self.cbr_pos.y/240 -0.5

    def play_turn(self):
        # self.cbr_pos.move_by_vect(self.cbr_move)
        self.update_pos_screen()

    def in_game(self):
        return self.rbr_bounds.in_bounds(self.cbr_pos)


class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.transition_delay = 50
        self.skweeks = []
        skweek = Skweek(
            squarity.Coord(0, 0),
            "skweek",
            image_modifier=squarity.ComponentImageModifier()
        )
        skweek.intialize(self.rect)
        self.skweeks.append(skweek)
        layer_skweek = squarity.Layer(self, self.w, self.h)
        layer_skweek.add_game_object(skweek)
        self.layers.append(layer_skweek)
        self.playing = True
        return self.game_tick()

    def game_tick(self):
        if not self.playing:
            return
        skweek = self.skweeks[0]
        skweek.play_turn()
        if not skweek.in_game():
            print("Le skweek est sorti")
            self.playing = False
            return

        event_result = squarity.EventResult()
        event_result.add_delayed_callback(
            squarity.DelayedCallBack(50, self.game_tick)
        )
        event_result.no_redraw = True
        return event_result

    def on_click(self, coord):
        print("plop")
        self.playing = False
