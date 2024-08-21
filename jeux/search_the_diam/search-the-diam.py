# https://i.ibb.co/Jd3207P/search-the-diam.png

"""
  {
    "name": "Un diamant cherche son pote",
    "version": "2.1.0",
    "game_area": {
      "nb_tile_width": 8,
      "nb_tile_height": 9
    },
    "tile_size": 40,
    "img_coords": {
      "gem_yellow": [0, 0, 40, 40, "center"],
      "gem_green": [58, 0, 40, 40, "center"],
      "background": [0, 40, 640, 400]
    }
  }
"""

"""
Origine de l'image de background:
https://opengameart.org/content/centered-around-the-hero

"""

# TODO : on devrait pouvoir configurer le "center" des sprites dans le code,
# et pas que dans la config json.

import random
import squarity

Coord = squarity.Coord
d = squarity.dirs


# TODO : dans la lib squarity ?
def on_rect_border(rect, coord):
    print("on border", rect, coord)
    if not rect.in_bounds(coord):
        return False
    if coord.x == rect.x:
        return True
    if coord.y == rect.y:
        return True
    if coord.x == rect.x + rect.w - 1:
        return True
    if coord.y == rect.y + rect.h - 1:
        return True
    return False


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
                    squarity.TransitionSteps("area_offset_x", ((scroll_time, 0), ))
                )
            if coord_vector.y:
                self.image_modifier.add_transition(
                    squarity.TransitionSteps("area_offset_y", ((scroll_time, 0), ))
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

    # TODO : foutre des constantes sur le coord upleft initial de la zone. Le déplacement x,y. La taille de la zone visible.

    def on_start(self):
        self.transition_delay = 100
        self.rect_big_world = squarity.Rect(0, 0, 32, 20)
        self.layer_gem = squarity.Layer(self, self.w, self.h)
        self.layers.append(self.layer_gem)
        self.gobj_bg = squarity.GameObject(
            Coord(0, 0),
            "background",
            image_modifier=squarity.ComponentImageModifier(
                area_scale_x=2.0, area_scale_y=2.0,
                area_offset_x=1, area_offset_y=1,
                img_size_x=640, img_size_y=400,
            )
        )
        self.gobj_bg.set_callback_end_transi(self.on_move_zone_end)
        self.gobj_bg.plock_transi = squarity.PlayerLockTransi.INVISIBLE
        self.layer_main.add_game_object(self.gobj_bg)
        self.coord_zone = Coord(0, 0)
        self.rect_visible = self.compute_rect_visible()

        self.gem_green = GameObjectInBigWorld(
            Coord(0, 0),
            "gem_green",
            image_modifier=squarity.ComponentImageModifier()
        )
        self.gem_green.plock_transi = squarity.PlayerLockTransi.INVISIBLE
        # self.gem_green.set_transition_delay(2000)
        self.gem_green.more_init(Coord(3, 3), self.rect_visible)
        if self.gem_green.must_set_visible:
            self.layer_gem.add_game_object(self.gem_green)
            self.gem_green.must_set_visible = False

        self.gem_yellow = GameObjectInBigWorld(
            Coord(0, 0),
            "gem_yellow",
            image_modifier=squarity.ComponentImageModifier(),
            back_caller=squarity.ComponentBackCaller(),
        )
        self.gem_yellow.plock_transi = squarity.PlayerLockTransi.INVISIBLE
        self.gem_yellow.more_init(Coord(8, 7), self.rect_visible)
        if self.gem_yellow.must_set_visible:
            self.layer_gem.add_game_object(self.gem_yellow)
            self.gem_yellow.must_set_visible = False
        self.debug_wesh_counter = 0


    def compute_rect_visible(self):
        rect_visible = squarity.Rect(
            self.coord_zone.x * 6 - 1,
            self.coord_zone.y * 7 - 1,
            8,
            9
        )
        return rect_visible


    def compute_move_details(self, rect_visible_prev, rect_visible_cur):
        coord_vector = Coord(
            rect_visible_cur.x - rect_visible_prev.x,
            rect_visible_cur.y - rect_visible_prev.y,
        )
        scroll_time = (abs(coord_vector.x) + abs(coord_vector.y)) * 75
        return coord_vector, scroll_time


    def on_button_direction(self, direction):
        self.debug_wesh_counter += 1
        # print("wesh", self.debug_wesh_counter) TODO WIP crap
        coord_test = self.gem_green.coord_big_world.clone().move_dir(direction)
        if not self.rect_big_world.in_bounds(coord_test):
            return
        self.gem_green.coord_big_world.move_dir(direction)
        # coord_green_test = self.gem_green._coord.clone().move_dir(direction)
        if on_rect_border(self.rect_visible, self.gem_green.coord_big_world):
            self.direction_move_zone = direction
            self.gem_green.move_dir(direction, callback=self.on_green_move_borders)
        elif coord_test == self.gem_yellow.coord_big_world:
            self.gem_green.move_dir(direction, callback=self.on_diamond_meets)
        else:
            self.gem_green.move_dir(direction)


    def on_diamond_meets(self):
        # TODO : factoriser les scales.
        self.gem_yellow.image_modifier.add_transition(
            squarity.TransitionSteps("area_offset_x", ((200, 1), (400, 1), (400, -1), (400, -1), (400, 1), ))
        )
        self.gem_yellow.image_modifier.add_transition(
            squarity.TransitionSteps("area_offset_y", ((200, -1), (400, 1), (400, 1), (400, -1), (400, -1), ))
        )
        self.gem_yellow.image_modifier.add_transition(
            squarity.TransitionSteps("area_scale_x", ((150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (225, 0), ))
        )
        self.gem_yellow.image_modifier.add_transition(
            squarity.TransitionSteps("area_scale_y", ((150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (225, 0), ))
        )
        # FUTURE : ça fait quand même beaucoup de code boiler plate juste pour balancer une callback.
        #        (et y'en a aussi dans l'init.)
        self.gem_yellow.back_caller.add_callback(squarity.DelayedCallBack(1875, self.on_met_yellow))

        self.gem_green.image_modifier.add_transition(
            squarity.TransitionSteps("area_offset_x", ((200, -1), (400, -1), (400, 1), (400, 1), (400, -1), (200, 0), ))
        )
        self.gem_green.image_modifier.add_transition(
            squarity.TransitionSteps("area_offset_y", ((200, 1), (400, -1), (400, -1), (400, 1), (400, 1), (200, 0)))
        )
        self.gem_green.image_modifier.add_transition(
            squarity.TransitionSteps("area_scale_x", ((150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (75, 1), ))
        )
        self.gem_green.image_modifier.add_transition(
            squarity.TransitionSteps("area_scale_y", ((150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5), (150, 0.5), (75, 1), ))
        )


    def on_green_move_borders(self):
        rect_visible_prev = self.rect_visible
        self.move_zone(self.direction_move_zone)
        self.rect_visible = self.compute_rect_visible()
        coord_vector, scroll_time = self.compute_move_details(rect_visible_prev, self.rect_visible)

        self.ack_zone_moved_for_background(rect_visible_prev, self.rect_visible, coord_vector, scroll_time)
        self.gem_yellow.ack_zone_moved(rect_visible_prev, self.rect_visible, coord_vector, scroll_time)
        if self.gem_yellow.must_set_visible:
            self.layer_gem.add_game_object(self.gem_yellow)
            self.gem_yellow.must_set_visible = False
        self.gem_green.ack_zone_moved(rect_visible_prev, self.rect_visible, coord_vector, scroll_time)
        if self.gem_green.must_set_visible:
            self.layer_gem.add_game_object(self.gem_green)
            self.gem_green.must_set_visible = False
        print("_transitions_to_record", self.gem_yellow.image_modifier._transitions_to_record)

        if self.gem_green.coord_big_world == self.gem_yellow.coord_big_world:
            event_result = squarity.EventResult()
            event_result.add_delayed_callback(squarity.DelayedCallBack(0, self.on_diamond_meets))
            return event_result


    def on_met_yellow(self):
        self.layer_gem.remove_game_object(self.gem_yellow)
        self.gem_yellow.must_hide = False
        # Il faut choisir un nouvel emplacement pour le diamant jaune, mais pas dans le visible rect.
        # (sinon ça fera bizarre, et surtout c'est plus compliqué à gérer.)
        nb_tries = 5
        new_yellow_coord = Coord(random.randrange(0, 32), random.randrange(0, 20))
        while self.rect_visible.in_bounds(new_yellow_coord):
            new_yellow_coord = Coord(random.randrange(0, 32), random.randrange(0, 20))
            nb_tries -= 1
            if nb_tries == 0:
                # On a essayé des coord random, et on n'arrive pas à être ailleurs que le visible rect.
                # alors on balance un truc par défaut, et osef.
                new_yellow_coord = Coord(0, 0)
            elif nb_tries == -1:
                # On a essayé des coord random, et on n'arrive pas à être ailleurs que le visible rect.
                # alors on balance un truc par défaut, et osef.
                new_yellow_coord = Coord(30, 20)
            elif nb_tries < -1:
                raise Exception("Not supposed to happen")

        self.gem_yellow.coord_big_world = new_yellow_coord.clone()
        self.gem_yellow.image_modifier.area_scale_x = 1.0
        self.gem_yellow.image_modifier.area_scale_y = 1.0
        print("Le diamant est maintenant en", new_yellow_coord)


    def move_zone(self, direction):
        if direction == d.Right:
            if self.coord_zone.x < 6:
                self.coord_zone.x += 1
        elif direction == d.Left:
            if self.coord_zone.x:
                self.coord_zone.x -= 1
        elif direction == d.Down:
            if self.coord_zone.y < 3:
                self.coord_zone.y += 1
        elif direction == d.Up:
            if self.coord_zone.y:
                self.coord_zone.y -= 1


    def ack_zone_moved_for_background(self, rect_visible_prev, rect_visible_cur, coord_vector, scroll_time):
        if coord_vector.x:
            transi_param = (scroll_time, -rect_visible_cur.x)
            self.gobj_bg.image_modifier.add_transition(
                squarity.TransitionSteps("area_offset_x", (transi_param, ))
            )
        if coord_vector.y:
            transi_param = (scroll_time, -rect_visible_cur.y)
            self.gobj_bg.image_modifier.add_transition(
                squarity.TransitionSteps("area_offset_y", (transi_param, ))
            )


    def on_button_action(self, action_name):
        print("Les boutons d'actions ne servent à rien dans ce jeu.")


    def on_move_zone_end(self):
        print("on_move_zone_end", self.coord_zone)
        if self.gem_yellow.must_hide:
            self.layer_gem.remove_game_object(self.gem_yellow)
            self.gem_yellow.must_hide = False
        if self.gem_green.must_hide:
            self.layer_gem.remove_game_object(self.gem_green)
            self.gem_green.must_hide = False

