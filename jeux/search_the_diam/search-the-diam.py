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


class GameObjectInBigWorld(squarity.GameObject):

    def more_init(self, coord_big_world, rect_visible):
        self.coord_big_world = coord_big_world
        self.move_to_xy(
            self.coord_big_world.x - rect_visible.x,
            self.coord_big_world.y - rect_visible.y
        )
        self.must_set_visible = rect_visible.in_bounds(self.coord_big_world)
        self.must_hide = False

    def ack_zone_moved(self, rect_visible_prev, rect_visible_cur, coord_vector, scroll_time):
        print("rects", rect_visible_prev, rect_visible_cur)
        print("coord_big_world", self.coord_big_world)
        is_visible_prev = rect_visible_prev.in_bounds(self.coord_big_world)
        is_visible_cur = rect_visible_cur.in_bounds(self.coord_big_world)
        print("is visibles", is_visible_prev, is_visible_cur)
        if is_visible_prev and is_visible_cur:
            # TODO : argh. Va falloir un truc pour multiplier les coordonnées,
            # et les les additionner, et les soustraire ?
            # self.move(Coord(-coord_vector.x, -coord_vector.y))
            self.add_transition(
                squarity.TransitionSteps("coord", ((scroll_time, Coord(self._coord.x-coord_vector.x, self._coord.y-coord_vector.y)), ))
            )

        elif not is_visible_prev and is_visible_cur:
            # L'objet devient visible dans la zone affichée.
            self.move_to_xy(
                self.coord_big_world.x - rect_visible_cur.x,
                self.coord_big_world.y - rect_visible_cur.y
            )
            self.image_modifier.area_offset_x = coord_vector.x
            self.image_modifier.area_offset_y = coord_vector.y
            print("area_offset_x", self.image_modifier.area_offset_x)
            if coord_vector.x:
                self.image_modifier.add_transition(
                    # TODO : le vilain 0.01 parce que sinon ça fait une erreur JS.
                    squarity.TransitionSteps("area_offset_x", ((scroll_time, 0.01), ))
                )
            if coord_vector.y:
                self.image_modifier.add_transition(
                    squarity.TransitionSteps("area_offset_y", ((scroll_time, 0.01), ))
                )
            self.must_set_visible = True
        elif is_visible_prev and not is_visible_cur:
            # L'objet disparaît de la zone affichée.
            if coord_vector.x:
                self.image_modifier.add_transition(
                    squarity.TransitionSteps("area_offset_x", ((scroll_time, -coord_vector.x), ))
                )
            if coord_vector.y:
                self.image_modifier.add_transition(
                    squarity.TransitionSteps("area_offset_y", ((scroll_time, -coord_vector.y), ))
                )
            self.must_hide = True


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
        self.rect_visible = self.compute_rect_visible()

        self.gem_yellow = GameObjectInBigWorld(
            Coord(0, 0),
            "gem_yellow",
            image_modifier=squarity.ComponentImageModifier()
        )
        self.gem_yellow.more_init(Coord(8, 6), self.rect_visible)
        if self.gem_yellow.must_set_visible:
            self.layer_gem.add_game_object(self.gem_yellow)


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


    def on_button_direction(self, direction):
        rect_visible_prev = self.compute_rect_visible()
        # Faudra pas le calculer comme ça, ce truc. Évidemment.
        scroll_time, coord_vector = self.move_zone(direction)
        self.rect_visible = self.compute_rect_visible()
        self.gem_yellow.ack_zone_moved(rect_visible_prev, self.rect_visible, coord_vector, scroll_time)
        if self.gem_yellow.must_set_visible:
            self.layer_gem.add_game_object(self.gem_yellow)
            self.gem_yellow.must_set_visible = False
        print("_transitions_to_record", self.gem_yellow.image_modifier._transitions_to_record)

        #if rect_visible.in_bounds(self.gem_yellow.coord_global) and self.gem_yellow.layer_owner is None:
        #    self.layer_gem.add_game_object(self.gem_yellow)
        #if not rect_visible.in_bounds(self.gem_yellow.coord_global) and self.gem_yellow.layer_owner is not None:
        #    self.layer_gem.remove_game_object(self.gem_yellow)


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
                # Haha. C'est area_offset et pas img_offset... J'ai vraiment tout mélangé.
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


    def on_button_action(self, action_name):
        print(action_name)
        self.gem_yellow.image_modifier.add_transition(
            squarity.TransitionSteps("area_offset_x", ((1000, 50), ))
        )



    def on_move_zone_end(self):
        print("on_move_zone_end", self.coord_zone)
        if self.gem_yellow.must_hide:
            self.layer_gem.remove_game_object(self.gem_yellow)
            self.gem_yellow.must_hide = False




