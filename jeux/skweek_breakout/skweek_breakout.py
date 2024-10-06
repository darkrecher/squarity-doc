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
import random
import squarity
from squarity import Coord

RATIO_GE_TO_BR = 240
# Tous les angles sont en radians.

class BouncePoint:

    def __init__(self, cbr_pos, bounce_angle, block_owner=None):
        self.cbr_pos = cbr_pos
        self.bounce_angle = bounce_angle
        self.block_owner = block_owner

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
        print("collided_points")
        for p in collided_points:
            print(p.cbr_pos, (p.bounce_angle*360)/(math.pi*2))
        print("----------")
        return collided_points

    def compute_bounced_angle(self, collided_points, skweek):
        angles = [bounce_point.bounce_angle for bounce_point in collided_points]
        bouncing_angle = sum(angles) / len(angles)
        # Formule retrouvée grâce à une longue réflexion à 5 heures du matin,
        # et des sacrifices de chèvres une nuit de pleine Lune.
        bounced_angle = 2 * bouncing_angle - skweek.angle + math.pi
        bounced_angle = bounced_angle % (2*math.pi)
        print("bounced_angle", (bounced_angle*360)/(math.pi*2))
        return bounced_angle


class BlockTemplate():

    BEZEL_SHAPE = (
        (0, 60, (180.0+135.0)/2), (20, 40, 135.0), (40, 20, 135.0), (60, 0, (135.0+90.0)/2),
        (80, 0, 90.0), (100, 0, 90.0), (120, 0, 90.0), (140, 0, 90.0), (160, 0, 90.0),

        (180, 0, (90.0+45.0)/2), (200, 20, 45.0), (220, 40, 45.0), (240, 60, 45.0/2),
        (240, 80, 0.0), (240, 100, 0.0), (240, 120, 0.0), (240, 140, 0.0), (240, 160, 0.0),

        (240, 180, (315.0+360.0)/2), (220, 200, 315.0), (200, 220, 315.0), (180, 240, (270.0+315.0)/2),
        (160, 240, 270.0), (140, 240, 270.0), (120, 240, 270.0), (100, 240, 270.0), (80, 240, 270.0),

        (60, 240, (270.0+225.0)/2), (40, 220, 225.0), (20, 200, 225.0), (0, 180, (225.0+180.0)/2),
        (0, 160, 180.0), (0, 140, 180.0), (0, 120, 180.0), (0, 100, 180.0), (0, 80, 180.0),
    )

    SQUARE_SHAPE = (
        (0, 1, 180.0), (0, 0, 135.0), (1, 0, 90.0),
        (20, 0, 90.0), (40, 0, 90.0), (60, 0, 90.0), (80, 0, 90.0), (100, 0, 90.0), (120, 0, 90.0),
        (140, 0, 90.0), (160, 0, 90.0), (180, 0, 90.0), (200, 0, 90.0), (220, 0, 90.0),
        (239, 0, 90.0), (240, 0, 45.0), (240, 1, 0.0),
        (240, 20, 0.0), (240, 40, 0.0), (240, 60, 0.0), (240, 80, 0.0), (240, 100, 0.0), (240, 120, 0.0),
        (240, 140, 0.0), (240, 160, 0.0), (240, 180, 0.0), (240, 200, 0.0), (240, 220, 0.0),
        (240, 239, 0.0), (240, 240, 315.0), (239, 240, 270.0),
        (220, 240, 270.0), (200, 240, 270.0), (180, 240, 270.0), (160, 240, 270.0), (140, 240, 270.0), (120, 240, 270.0),
        (100, 240, 270.0), (80, 240, 270.0), (60, 240, 270.0), (40, 240, 270.0), (40, 240, 270.0),
        (1, 240, 270.0), (0, 240, 225.0), (0, 239, 180.0),
        (0, 220, 180.0), (0, 200, 180.0), (0, 180, 180.0), (0, 160, 180.0), (0, 140, 180.0), (0, 120, 180.0),
        (0, 100, 180.0), (0, 80, 180.0), (0, 60, 180.0), (0, 40, 180.0), (0, 20, 180.0),
    )

    def _convert_template(template_deg):
        template_rad = [
            (x, y, (angle * 2 * math.pi) / 360.0)
            for (x, y, angle) in template_deg
        ]
        return tuple(template_rad)

    def init_templates():
        BlockTemplate.bezel_shape = BlockTemplate._convert_template(BlockTemplate.BEZEL_SHAPE)
        BlockTemplate.square_shape = BlockTemplate._convert_template(BlockTemplate.SQUARE_SHAPE)

        BlockTemplate.template_from_spritename = {
            "block_blue": BlockTemplate.square_shape,
            "block_white": BlockTemplate.square_shape,
            "bezel_blue": BlockTemplate.bezel_shape,
        }


class Block(squarity.GameObject):

    def initialize(self):
        base_x = self._coord.x * RATIO_GE_TO_BR
        base_y = self._coord.y * RATIO_GE_TO_BR
        template = BlockTemplate.template_from_spritename[self.sprite_name]
        self.bounce_points = [
            BouncePoint(
                Coord(base_x + offset_x, base_y + offset_y), angle, self
            ) for (offset_x, offset_y, angle)
            in template
        ]
        self.immune = 0
        self.must_remove = False

    def decrease_immune(self):
        if self.immune:
            self.immune -= 1

    def on_hit_by_skweek(self, skweek):
        # J'aime pas ce truc de immune. Mais j'ai pas mieux.
        self.immune = 10
        self.must_remove = True


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

        self.cbr_pos = Coord(RATIO_GE_TO_BR * 11, RATIO_GE_TO_BR * 9 + RATIO_GE_TO_BR-5)
        self.angle = 0
        self.speed = 1
        self.set_angle((random.randrange(360) * 2 * math.pi) / 360.0)
        self.set_speed(25)
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
        print("set vect", self.cbr_move)

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
        BlockTemplate.init_templates()
        self.collision_handler = CollisionHandler()
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

        """
        block = Block(squarity.Coord(11, 5), "block_blue")
        block.initialize()
        self.layer_main.add_game_object(block)
        self.collision_handler.add_bounce_points(block.bounce_points)

        block = Block(squarity.Coord(10, 5), "block_white")
        block.initialize()
        self.layer_main.add_game_object(block)
        self.collision_handler.add_bounce_points(block.bounce_points)
        """
        self.put_blocks()

        self.playing = True
        return self.game_tick()

    def put_blocks(self):
        sprites = ["block_white", "block_blue"]
        for x_tile in range(self.w):
            # TODO : duplicate code de gros dégueulasse.
            coord = Coord(x_tile, 0)
            block = Block(coord, sprites[(coord.x+coord.y) % 2])
            block.initialize()
            self.layer_main.add_game_object(block)
            self.collision_handler.add_bounce_points(block.bounce_points)

            coord = Coord(x_tile, self.h-1)
            block = Block(coord, sprites[(coord.x+coord.y) % 2])
            block.initialize()
            self.layer_main.add_game_object(block)
            self.collision_handler.add_bounce_points(block.bounce_points)

        for y_tile in range(1, self.h - 1):
            # TODO : meta-duplicate code de meta-gros dégueulasse.
            coord = Coord(0, y_tile)
            block = Block(coord, sprites[(coord.x+coord.y) % 2])
            block.initialize()
            self.layer_main.add_game_object(block)
            self.collision_handler.add_bounce_points(block.bounce_points)

            coord = Coord(self.w-1, y_tile)
            block = Block(coord, sprites[(coord.x+coord.y) % 2])
            block.initialize()
            self.layer_main.add_game_object(block)
            self.collision_handler.add_bounce_points(block.bounce_points)



    def iter_on_blocks(self):
        for block in squarity.Sequencer.seq_iter(
            squarity.Sequencer.iter_on_rect(self.rect),
            squarity.Sequencer.gobj_on_layers([self.layer_main]),
        ):
            yield block

    def game_tick(self):
        if not self.playing:
            return
        skweek = self.skweeks[0]

        for block in self.iter_on_blocks():
            block.decrease_immune()

        collided_points = self.collision_handler.collides_with(skweek)
        if collided_points:
            bounced_angle = self.collision_handler.compute_bounced_angle(
                collided_points,
                skweek,
            )
            skweek.set_angle(bounced_angle)
            for coll_p in collided_points:
                coll_p.block_owner.on_hit_by_skweek(skweek)

        blocks_to_remove = [
            block for block in self.iter_on_blocks() if block.must_remove
        ]
        for block in blocks_to_remove:
            self.layer_main.remove_game_object(block)

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
