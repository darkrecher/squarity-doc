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

import math
import squarity
from squarity import Coord

RATIO_GE_TO_BR = 240
# Tous les angles sont en radians.

class BouncePoint:

    def __init__(self, cbr_pos, bounce_angles, block_owners=None):
        self.cbr_pos = cbr_pos
        # TODO : on aura peut-être pas besoin de tout ça. Avec juste un angle et un owner, ça pourrait passer.
        self.bounce_angles = bounce_angles
        if len(self.bounce_angles) == 1:
            self.bounce_angle = self.bounce_angles[0]
        else:
            self.bounce_angle = sum(self.bounce_angles) / len(self.bounce_angles)
        self.block_owners = [] if block_owners is None else block_owners
        # TODO : stupide
        if block_owners is not None:
            self.block_owner = block_owners[0]

    def collides_with(self, skweek):
        if not skweek.rbr_skweek_bounds.in_bounds(skweek.cbr_pos):
            return None
        br_dist_sq = (skweek.cbr_pos.x - self.cbr_pos.x)**2 + (skweek.cbr_pos.y - self.cbr_pos.y)**2
        if br_dist_sq >= skweek.br_ray_squared or self.block_owner.immune:
            return None
        else:
            return br_dist_sq


class CollisionHandler:

    def __init__(self):
        self.bounce_points = []
        # TODO : les bounce_points indexés par cbr_pos, dans un dict.

    def add_bounce_points(self, bounce_points):
        self.bounce_points.extend(bounce_points)

    def on_destroyed_block(self, block):
        self.bounce_points = [
            bounce_point for bounce_point
            in self.bounce_points
            if self.bounce_points.block_owner != block
        ]

    def collides_with(self, skweek):
        collisions = []
        for bounce_point in self.bounce_points:
            br_dist_sq = bounce_point.collides_with(skweek)
            if br_dist_sq is not None:
                collisions.append((br_dist_sq, bounce_point))
        if not collisions:
            return []
        nearest_colli = min(collisions, key=lambda x:x[0])
        print("collision", nearest_colli[0], nearest_colli[1].cbr_pos)
        cbr_collision_pos = nearest_colli[1].cbr_pos
        collided_points = [
            bounce_point
            for (br_dist_sq, bounce_point) in collisions
            if bounce_point.cbr_pos == cbr_collision_pos
        ]
        print("collided_points", collided_points)
        return collided_points

    def compute_bounced_angle(self, collided_points, skweek):
        angles = [bounce_point.bounce_angle for bounce_point in collided_points]
        bouncing_angle = sum(angles) / len(angles)
        # Formule retrouvée grâce à une longue réflexion à 5 heures du matin,
        # et des sacrifices de chèvres une nuit de pleine Lune
        bounced_angle = 2 * bouncing_angle - skweek.angle + math.pi
        bounced_angle = bounced_angle % (2*math.pi)
        return bounced_angle


class Block(squarity.GameObject):

    def initialize(self):
        self.bounce_points = [
            BouncePoint(Coord(self._coord.x*RATIO_GE_TO_BR - 0, self._coord.y*RATIO_GE_TO_BR + 240), [(225.0 * 2 * math.pi) / 360.0], [self])
        ]
        self.immune = False


class Skweek(squarity.GameObject):

    def intialize(self, rge_game_bounds):
        # RGE = Rect Game Engine. Les coordonnées avec les unités du moteur de jeu.
        # CBR = Coord Breakout. Les coordonnées avec les unités du jeu de casse-brique
        # Il suffit juste de faire un scaling pour changer
        # entre les coord Game Engine et les coord Breakout.
        margin = RATIO_GE_TO_BR // 2
        self.rbr_game_bounds = squarity.Rect(
            -margin,
            -margin,
            rge_game_bounds.w*RATIO_GE_TO_BR + 2*margin,
            rge_game_bounds.h*RATIO_GE_TO_BR + 2*margin,
        )
        print("rbr_game_bounds", self.rbr_game_bounds)
        self.cbr_move = Coord(1, 1)

        self.cbr_pos = Coord(RATIO_GE_TO_BR * 8 - 0*RATIO_GE_TO_BR//2, RATIO_GE_TO_BR * 9 + RATIO_GE_TO_BR-5)
        self.angle = 0
        self.speed = 1
        self.set_angle((45.0 * 2 * math.pi) / 360.0)
        self.set_speed(5)
        self._set_vect_from_angle()
        self.set_ray(120)
        self._update_pos_screen()

    def set_angle(self, angle):
        self.angle = angle
        self._set_vect_from_angle()

    def set_speed(self, speed):
        self.speed = speed
        self._set_vect_from_angle()

    def set_ray(self, ray):
        self.br_ray = ray
        self.image_modifier.area_scale_x = (self.br_ray * 2) / RATIO_GE_TO_BR
        self.image_modifier.area_scale_y = (self.br_ray * 2) / RATIO_GE_TO_BR
        self.br_ray_squared = self.br_ray ** 2
        self._set_skweek_bounds()

    def play_turn(self):
        self.cbr_pos.move_by_vect(self.cbr_move)
        self._set_skweek_bounds()
        self._update_pos_screen()

    def is_in_game(self):
        return self.rbr_game_bounds.in_bounds(self.cbr_pos)

    def _set_vect_from_angle(self):
        self.cbr_move.x = math.cos(self.angle) * self.speed
        self.cbr_move.y = -math.sin(self.angle) * self.speed

    def _set_skweek_bounds(self):
        self.rbr_skweek_bounds = squarity.Rect(
            self.cbr_pos.x - self.br_ray - 1,
            self.cbr_pos.y - self.br_ray - 1,
            self.br_ray*2 + 2,
            self.br_ray*2 + 2,
        )

    def _update_pos_screen(self):
        self.image_modifier.area_offset_x = self.cbr_pos.x/RATIO_GE_TO_BR - 0.5
        self.image_modifier.area_offset_y = self.cbr_pos.y/RATIO_GE_TO_BR - 0.5

    def print_state(self):
        print("area offset: ", self.image_modifier.area_offset_x, self.image_modifier.area_offset_y)
        print("coord cbr", self.cbr_pos)


class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.transition_delay = 10
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

        block = Block(squarity.Coord(12, 5), "block_blue")
        block.initialize()
        self.layer_main.add_game_object(block)

        self.collision_handler = CollisionHandler()
        self.collision_handler.add_bounce_points(block.bounce_points)

        self.playing = True
        return self.game_tick()

    def game_tick(self):
        if not self.playing:
            return
        skweek = self.skweeks[0]

        collided_points = self.collision_handler.collides_with(skweek)
        if collided_points:
            bounced_angle = self.collision_handler.compute_bounced_angle(
                collided_points,
                skweek,
            )
            skweek.set_angle(bounced_angle)
        skweek.play_turn()
        if not skweek.is_in_game():
            print("Le skweek est sorti")
            self.playing = False
            return

        event_result = squarity.EventResult()
        event_result.add_delayed_callback(
            squarity.DelayedCallBack(10, self.game_tick)
        )
        event_result.no_redraw = True
        return event_result

    def on_click(self, coord):
        print("plop")
        self.playing = False
