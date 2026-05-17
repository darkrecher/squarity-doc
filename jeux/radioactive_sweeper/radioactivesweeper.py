# https://squarity.fr/game/#fetchez_githubgist_darkrecher/6ac1768472ecd954d4818ef1dbd59d6c/raw/radioactivesweeper.txt
# https://tinyurl.com/radswp123
# https://raw.githubusercontent.com/darkrecher/squarity-doc/refs/heads/master/jeux/radioactive_sweeper/radioactive_tileset.png
# taille de l'aire de jeu : 30, 20 ??

# TODO : réajuster les images des dômes et des dessins de couleur, pour que le dessin touche pas les bords.

"""
{
  "name": "Radioactive Sweeper",
  "version": "2.1.0",
  "game_area": {
    "nb_tile_width": 30,
    "nb_tile_height": 20
  },
  "tile_size": 32,
  "img_coords": {
    "digi_sing_1": [32, 0],
    "digi_sing_2": [64, 0],
    "digi_sing_3": [96, 0],
    "digi_sing_4": [128, 0],
    "digi_sing_5": [160, 0],
    "digi_sing_6": [192, 0],
    "digi_sing_7": [224, 0],
    "digi_sing_8": [256, 0],
    "digi_sing_9": [288, 0],
    "digi_unit_0": [0, 32],
    "digi_unit_1": [32, 32],
    "digi_unit_2": [64, 32],
    "digi_unit_3": [96, 32],
    "digi_unit_4": [128, 32],
    "digi_unit_5": [160, 32],
    "digi_unit_6": [192, 32],
    "digi_unit_7": [224, 32],
    "digi_unit_8": [256, 32],
    "digi_unit_9": [288, 32],
    "digi_ten_1": [0, 256],
    "digi_ten_2": [32, 256],
    "digi_ten_3": [64, 256],
    "digi_ten_4": [96, 256],
    "digi_ten_5": [128, 256],
    "digi_ten_6": [160, 256],
    "digi_ten_7": [192, 256],
    "digi_ten_8": [224, 256],
    "digi_ten_9": [256, 256],
    "digi_infinity": [288, 64],

    "block": [0, 64],
    "rad_ylw_source": [32, 64],
    "rad_ylw_barrel": [64, 64],
    "rad_grn_source": [32, 96],
    "rad_grn_barrel": [64, 96],
    "rad_prp_source": [32, 128],
    "rad_prp_barrel": [64, 128],
    "rad_indic_ylw": [96, 160],
    "rad_indic_grn": [128, 160],
    "rad_indic_prp": [160, 160],
    "rad_indic_hid": [128, 192],
    "red_cross": [0, 96],
    "dome_ground_base": [0, 160, 96, 96],
    "dome_full": [96, 64, 96, 96],
    "dome_border_0": [448, 0, 96, 64],
    "dome_border_1": [352, 96, 64, 96],
    "dome_border_2": [448, 64, 96, 64],
    "dome_border_3": [288, 96, 64, 96],
    "dome_corner_0": [608, 0, 64, 64],
    "dome_corner_1": [608, 64, 64, 64],
    "dome_corner_2": [544, 64, 64, 64],
    "dome_corner_3": [544, 0, 64, 64],
    "dome_tshape_0": [192, 64, 96, 64],
    "dome_tshape_1": [320, 0, 64, 96],
    "dome_tshape_2": [192, 128, 96, 64],
    "dome_tshape_3": [384, 0, 64, 96],
    "dome_color_ylw": [416, 96],
    "dome_color_grn": [416, 128],
    "dome_color_prp": [416, 160],

    "building_shop": [256, 192, 64, 64],
    "money": [160, 192],
    "flask_ylw": [96, 224, 32, 32, "center"],
    "flask_grn": [128, 224, 32, 32, "center"],
    "flask_prp": [160, 224, 32, 32, "center"],

    "background": [0, 128]
  },
  "show_code_at_start": true,
  "appendices": {

  }
}
"""
# "building_shop": [256, 192, 64, 64],
INDEX_LEVEL = 1

import random
from enum import Enum, IntEnum
import squarity
Coord = squarity.Coord
dirs = squarity.dirs
GameObject = squarity.GameObject


class RadColor(IntEnum):
    YELLOW = 0
    GREEN = 1
    PURPLE = 2

NAME_FROM_RAD_COLOR = {
    RadColor.YELLOW: "ylw",
    RadColor.GREEN: "grn",
    RadColor.PURPLE: "prp",
}

PATTER_RAD_BASIC = (
    (0, -1, 6), (1, -1, 6), (1, 0, 6), (1, 1, 6),
    (0, 1, 6), (-1, 1, 6), (-1, 0, 6), (-1, -1, 6),
)

PATTERN_RAD_YELLOW_1 = PATTER_RAD_BASIC + (
    (0, -2, 4), (2, 0, 4), (0, 2, 4), (-2, 0, 4),
    (0, -3, 2), (3, 0, 2), (0, 3, 2), (-3, 0, 2),
)

PATTERN_RAD_GREEN_1 = PATTER_RAD_BASIC + (
    (-2, -2, 4), (2, -2, 4), (2, 2, 4), (-2, 2, 4),
    (-3, -3, 2), (3, -3, 2), (3, 3, 2), (-3, 3, 2),
)

PATTERN_RAD_PURPLE_1 = PATTER_RAD_BASIC + (
    (-2, -2, 2), (2, -2, 2), (2, 2, 2), (-2, 2, 2),
    (0, -2, 2), (2, 0, 2), (0, 2, 2), (-2, 0, 2),
    (-3, -3, 1), (3, -3, 1), (3, 3, 1), (-3, 3, 1),
    (-3, -1, 1), (-3, 1, 1), (3, -1, 1), (3, 1, 1),
    (1, 3, 1), (-1, 3, 1), (1, -3, 1), (-1, -3, 1),
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

        if self.barrel_color is not None:
            # Si y'a un baril sur la case, on affiche pas la valeur de radioactivité,
            # ni les indications de couleur.
            sprite_col = NAME_FROM_RAD_COLOR[self.barrel_color]
            if self.barrel_strength:
                # TODO LIB : ça fait du yo-yo. On devrait avoir une fonction dans Tile,
                # pour ajouter/supprimer des game objects directement dedans.
                gobj_src = GameObject(self._coord, f"rad_{sprite_col}_source")
                self.layer_owner.add_game_object(gobj_src)
            else:
                # TODO LIB : re du yo-yo.
                gobj_src = GameObject(self._coord, f"rad_indic_hid")
                self.layer_owner.add_game_object(gobj_src)
            gobj_barrel = GameObject(self._coord, f"rad_{sprite_col}_barrel")
            self.layer_owner.add_game_object(gobj_barrel)

        else:

            for rad_color in RadColor:
                if self.rad_strengths[rad_color]:
                    spr_name = "rad_indic_" + NAME_FROM_RAD_COLOR[rad_color]
                    gobj_rad_indic_color = GameObject(self._coord, spr_name)
                    self.layer_owner.add_game_object(gobj_rad_indic_color)
            sum_strength = sum(self.rad_strengths)
            #print("WIP", self._coord, sum_strength)
            # TODO : le 40 est arbitraire. Ce sera géré avec des objets dans le jeu.
            if sum_strength > 40:
                gobj_rad_indic = GameObject(self._coord, f"rad_infinity")
                self.layer_owner.add_game_object(gobj_rad_indic)
            elif sum_strength >= 10:
                digit_unit = sum_strength % 10
                gobj_rad_indic = GameObject(self._coord, f"digi_unit_{digit_unit}")
                self.layer_owner.add_game_object(gobj_rad_indic)
                digit_tens = sum_strength // 10
                gobj_rad_indic = GameObject(self._coord, f"digi_ten_{digit_tens}")
                self.layer_owner.add_game_object(gobj_rad_indic)
            elif sum_strength:
                gobj_rad_indic = GameObject(self._coord, f"digi_sing_{sum_strength}")
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

    PATTERN_FROM_COLOR = {
            RadColor.YELLOW: PATTERN_RAD_YELLOW_1,
            RadColor.GREEN: PATTERN_RAD_GREEN_1,
            RadColor.PURPLE: PATTERN_RAD_PURPLE_1,
    }

    def init_with_rad_tiles(self):
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
            pattern = (
                None if tile_barrel.barrel_strength != 1
                else self.PATTERN_FROM_COLOR.get(tile_barrel.barrel_color)
            )
            if pattern is not None:
                rad_color_index = tile_barrel.barrel_color
                for ofs_x, ofs_y, strength in pattern:
                    coord_indic = c.clone().move_by_vect(x=ofs_x, y=ofs_y)
                    if self.rect.in_bounds(coord_indic):
                        tile_indic = self.get_tile(coord_indic)
                        tile_indic.rad_strengths[rad_color_index] += strength
                        #print("WIP", tile_indic.rad_strengths)

        #print("----------------")
        for c in squarity.RectIterator(self.rect):
            self.get_tile(c).compute_game_objects()


class DesacDomeShape(Enum):
    FULL = 0
    BORDER = 1
    CORNER = 2
    TSHAPE = 3

# Clé : un DesacDomeShape
# Valeur : une liste, dont chaque élément représente une rotation du dome.
#          (liste de taille 1 ou 4)
#          Dans chaque élément de la liste, un tuple, avec :
#           - sprite_name
#           - coord. offset_sprite_pos. décalage (en tiles) du sprite à afficher.
#           - liste de coords. offset_positions_to_check.
#           - décalage des cases à vérifier quand on essaye une désactivation.
#           - liste des offsets de coordonnées, pour les pièces de monnaie.
DESAC_DOME_CONFIGS = {
    DesacDomeShape.FULL: [
        (
            "dome_full",
            Coord(0, 0),
            (
                (0, -1), (1, -1), (1, 0), (1, 1),
                (0, 1), (-1, 1), (-1, 0), (-1, -1),
            ),
            (
                (-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1),
                (+1, -1), (+1, 0), (+1, +1),
                (-1, -1, 0.5, 0.5), (-1, +1, 0.5, -0.5),
                (+1, -1, -0.5, 0.5), (+1, +1, -0.5, -0.5),
            )
        ),
    ],
    DesacDomeShape.BORDER: [
        (
            "dome_border_0",
            Coord(0, 0),
            ((0, -1), (1, -1), (1, 0), (-1, 0), (-1, -1), ),
            (
                (0, 0), (0, -1), (1, -1), (1, 0), (-1, 0), (-1, -1),
                (-1, -1, 0.5, 0.5), (+1, -1, -0.5, 0.5),
            ),
        ),
        (
            "dome_border_1",
            Coord(1, 0),
            ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), ),
            (
                (0, 0), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1),
                (+1, -1, -0.5, 0.5), (+1, +1, -0.5, -0.5),
            ),
        ),
        (
            "dome_border_2",
            Coord(0, 1),
            ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), ),
            (
                (0, 0), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0),
                (+1, +1, -0.5, -0.5), (-1, +1, 0.5, -0.5),
            )
        ),
        (
            "dome_border_3",
            Coord(0, 0),
            ((0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), ),
            (
                (0, 0), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1),
                (-1, +1, 0.5, -0.5), (-1, -1, 0.5, 0.5),
            )
        ),
    ],
    DesacDomeShape.CORNER: [
        (
            "dome_corner_0",
            Coord(1, 0),
            ((0, -1), (1, -1), (1, 0), ),
            ((0, 0), (0, -1), (1, -1), (1, 0), (1, -1, -0.5, 0.5))
        ),
        (
            "dome_corner_1",
            Coord(1, 1),
            ((1, 0), (1, 1), (0, 1), ),
            ((0, 0), (1, 0), (1, 1), (0, 1), (1, 1, -0.5, -0.5))
        ),
        (
            "dome_corner_2",
            Coord(0, 1),
            ((0, 1), (-1, 1), (-1, 0), ),
            ((0, 0), (0, 1), (-1, 1), (-1, 0), (-1, 1, 0.5, -0.5))
        ),
        (
            "dome_corner_3",
            Coord(0, 0),
            ((-1, 0), (-1, -1), (0, -1), ),
            ((0, 0), (-1, 0), (-1, -1), (0, -1), (-1, -1, 0.5, 0.5))
        ),
    ],
    DesacDomeShape.TSHAPE: [
        (
            "dome_tshape_0",
            Coord(0, 0),
            ((0, -1), (1, -1), (-1, -1), ),
            ((0, 0), (0, -1), (1, -1), (-1, -1), )
        ),
        (
            "dome_tshape_1",
            Coord(1, 0),
            ((1, -1), (1, 0), (1, 1), ),
            ((0, 0), (1, -1), (1, 0), (1, 1), )
        ),
        (
            "dome_tshape_2",
            Coord(0, 1),
            ((1, 1), (0, 1), (-1, 1), ),
            ((0, 0), (1, 1), (0, 1), (-1, 1), )
        ),
        (
            "dome_tshape_3",
            Coord(0, 0),
            ((-1, 1), (-1, 0), (-1, -1), ),
            ((0, 0), (-1, 1), (-1, 0), (-1, -1), )
        ),
    ]
}


class FixedDesacDome():
    """
    "Fixed desactivation dome", c'est à dire une rotation spécifique
    d'une shape spécifique d'un dôme.
    """

    def __init__(self, dome_conf, pos_upleft):
        (
            sprite_name, offset_sprite,
            offsets_to_check, money_offset_details
        ) = dome_conf
        self.offset_sprite = offset_sprite
        self.coord_dome = pos_upleft.clone().move_by_vect(self.offset_sprite)
        self.gobj_dome = GameObject(self.coord_dome, sprite_name)
        self.offset_positions_to_check = [
            Coord(ofs[0], ofs[1]) for ofs in offsets_to_check
        ]
        self.money_offset_details = money_offset_details
        # TODO : money_precise_positions, ça devrait pas être ici.
        self.money_precise_positions = []
        for ofs in money_offset_details:
            money_coord_offset = Coord(x=ofs[0], y=ofs[1])
            if len(ofs) >= 4:
                money_modifier_offset = tuple(ofs[2:4])
            else:
                money_modifier_offset = (0.0, 0.0)
            self.money_precise_positions.append(
                (money_coord_offset, money_modifier_offset)
            )
        # Liste de gobj à ajouter/enlever pour montrer que ce dôme est sélectionné.
        # TODO : faudra aussi mettre un cadre rouge. Pas ici, mais dans le DesacDome.
        self.gobjs_show_selection = tuple([
            GameObject(self.coord_dome, sprite_name)
            for _ in range(3)
        ])


class DesacRes(Enum):
    FAIL_UNREVEALED_TILES = 0
    FAIL_MAIN_TILE_REVEALED = 1
    FAIL_BREAK_NO_BARREL = 2
    FAIL_BREAK_COLOR_MISMATCH = 3
    SUCCESS = 4
    SUCCESS_WITH_ROTATION = 5


class DesactivationResult():
    """
    Mini-classe, représentant le résultat de la désactivation
    d'une tile contenant (ou pas) un baril radioactif.

    Résultats possibles :
    - refusé, car la tile principale est déjà révélée - failed_coords
    - refusé car tout n'est pas révélé, ou alors c'est au bord - failed_coords.
    - le dôme casse sur une tile vide.
    - le dôme casse sur une tile avec un baril n'ayant pas la bonne couleur.
    - ok
    - ok, mais faudrait tourner le dôme - rot_index et rot_steps.
    """

    # Temps, en milliseconde, pour parcourir une case du jeu.
    # C'est l'inverse d'une vitesse, c'est une "ralentesse".
    DEFAULT_DOME_SLOWNESS = 25

    def __init__(
        self,
        desac_res,
        failed_coords=[],
        rot_index=None,
        rot_steps=[],
        rad_color=None
    ):
        self.desac_res = desac_res
        self.failed_coords = failed_coords
        self.rot_index = rot_index
        self.rot_steps = rot_steps
        # Les variables ci-dessous ne sont utilisés
        # que pour les désactivations qui sont ok.
        self.desac_dome = None
        self.coord_dest_dome = None
        self.anim_step = None
        self.coord_desac = None
        self.dome_travel_delay = None
        self.rad_color = rad_color

    def is_desactivation_ok(self):
        return self.desac_res in (
            DesacRes.SUCCESS,
            DesacRes.SUCCESS_WITH_ROTATION
        )

    def has_failed_from_reveals(self):
        return self.desac_res in (
            DesacRes.FAIL_MAIN_TILE_REVEALED,
            DesacRes.FAIL_UNREVEALED_TILES
        )

    def compute_dome_travel_delay(self, coord_return_dome):
        dist = (
            (self.coord_dest_dome.x - coord_return_dome.x) ** 2
            + (self.coord_dest_dome.y - coord_return_dome.y) ** 2
        )
        dist = dist ** 0.5
        self.dome_travel_delay = int(dist * self.DEFAULT_DOME_SLOWNESS)


class DesacDome():
    """
    Un dôme spécifique, placé dans l'aire de jeu.
    Gère les rotations et la validation d'une désactivation.
    """

    def __init__(self, game, shape, pos_upleft, rad_color):
        self.game = game
        self.layer_dome = self.game.layer_movable_objs_1
        self.layer_color_indicator = self.game.layer_movable_objs_2
        self.shape = shape
        self.pos_upleft = pos_upleft.clone()
        self.rad_color = rad_color
        # -- Création des Fixed desactivation dome --
        # Au max, on a 4 instances de DesacDome, indiquant les différentes positions du dôme.
        # Quand c'est le dôme circulaire, on a une seule instance.
        self.dome_rotations = [
            FixedDesacDome(dome_conf, self.pos_upleft)
            for dome_conf in DESAC_DOME_CONFIGS[shape]
        ]
        self.gobj_dome_cur = None
        self.gobjs_show_selection = []
        self.rot_index_cur = 0
        self.selected = False
        self.selection_rect = squarity.Rect(
            self.pos_upleft.x, self.pos_upleft.y, 3, 3
        )

        # -- Placement du background --
        # TODO LIB : faudrait qu'on puisse directement itérer avec un rect.
        for coord_bg in squarity.Sequencer.iter_on_rect(self.selection_rect):
            self.game.layer_background.remove_at_coord(coord_bg)
        self.gobj_ground_base = GameObject(pos_upleft, "dome_ground_base")
        self.game.layer_background.add_game_object(self.gobj_ground_base)

        # -- Placement du game object indiquant la couleur du dôme --
        sprite_name_col = "dome_color_" + NAME_FROM_RAD_COLOR[self.rad_color]
        self.coord_color_indicator = pos_upleft.clone().move_by_vect(x=1, y=1)
        self.gobj_dome_color = GameObject(
            self.coord_color_indicator,
            sprite_name_col
        )
        self.layer_color_indicator.add_game_object(self.gobj_dome_color)
        # -- Placement du game object représentant le dôme --
        self._show_current_dome()

    def get_fixed_dome_cur(self):
        return self.dome_rotations[self.rot_index_cur]

    def select(self):
        self.selected = True
        for gobj in self.gobjs_show_selection:
            self.layer_dome.add_game_object(gobj)

    def unselect(self):
        self.selected = False
        for gobj in self.gobjs_show_selection:
            self.layer_dome.remove_game_object(gobj)

    def _show_current_dome(self):
        was_selected = self.selected
        if was_selected:
            self.unselect()
        if self.gobj_dome_cur is not None:
            self.layer_dome.remove_game_object(self.gobj_dome_cur)
        dome_rotation_cur = self.get_fixed_dome_cur()
        self.gobj_dome_cur = dome_rotation_cur.gobj_dome
        self.gobjs_show_selection = dome_rotation_cur.gobjs_show_selection
        #print(self.gobj_dome_cur)
        self.layer_dome.add_game_object(self.gobj_dome_cur)
        if was_selected:
            self.select()

    def rotate(self, rot_offset):
        self.rot_index_cur += rot_offset
        self.rot_index_cur %= len(self.dome_rotations)
        #print(self.rot_index_cur)
        self._show_current_dome()

    def check_desactivation(self, coord_desac):

        if self.game.is_revealed(coord_desac):
            return DesactivationResult(
                DesacRes.FAIL_MAIN_TILE_REVEALED,
                failed_coords=[coord_desac]
            )

        possible_rotations = [
            (self.rot_index_cur, [])
        ]
        if len(self.dome_rotations) == 4:
            possible_rotations.extend(
                [
                    ((self.rot_index_cur + 1) % 4, (+1, )),
                    ((self.rot_index_cur - 1) % 4, (-1, )),
                    ((self.rot_index_cur + 2) % 4, (+1, +1))
                ]
            )

        possible_rot_ok = None
        game_rect = self.game.rect
        for rot_index_try, rot_steps in possible_rotations:
            dome_rotation = self.dome_rotations[rot_index_try]
            offsets = dome_rotation.offset_positions_to_check
            all_around_ok = True
            for offset in offsets:
                coord_to_check = coord_desac.clone().move_by_vect(offset)
                if not game_rect.in_bounds(coord_to_check):
                    #print("coord_to_check out of bounds", coord_to_check, self.rect)
                    all_around_ok = False
                    break
                if not self.game.is_revealed(coord_to_check):
                    #print("coord_to_check fails", coord_to_check)
                    all_around_ok = False
                    break
            if all_around_ok:
                possible_rot_ok = rot_index_try, rot_steps
                break

        if possible_rot_ok is None:
            failed_coords = [coord_desac]
            for d in squarity.dirs.as_list:
                c = coord_desac.clone().move_dir(d)
                if game_rect.in_bounds(c) and not self.game.is_revealed(c):
                    failed_coords.append(c)
            return DesactivationResult(
                DesacRes.FAIL_UNREVEALED_TILES,
                failed_coords=failed_coords
            )

        tile_radac = self.game.layer_radact.get_tile(coord_desac)
        if tile_radac.barrel_color is None:
            print("EPIC FAIL! Vous méritez de perdre la partie !!")
            return DesactivationResult(DesacRes.FAIL_BREAK_NO_BARREL)
        if tile_radac.barrel_color != self.rad_color:
            print("EPIC FAIL! Vous méritez de perdre la partie !!")
            return DesactivationResult(DesacRes.FAIL_BREAK_COLOR_MISMATCH)

        rot_index_ok, rot_steps_ok = possible_rot_ok
        if rot_index_ok == self.rot_index_cur:
            return DesactivationResult(
                DesacRes.SUCCESS,
                rot_index=rot_index_ok,
                rad_color=self.rad_color,
            )
        else:
            return DesactivationResult(
                DesacRes.SUCCESS_WITH_ROTATION,
                rot_index=rot_index_ok,
                rot_steps=list(rot_steps_ok),
                rad_color=self.rad_color,
            )


class DesacDomeManager():
    """
    Manager de tous les dômes placés dans l'aire de jeu.

    Gère les rotations, sélections/déselections, validation d'une désactivation,
    animation d'une désactivation, etc.

    Mais c'est toujours le GameModel qui désactive les barils.
    """

    def __init__(self, layer_ihm):
        self.layer_ihm = layer_ihm
        self.desac_domes = []
        self.selected_dome = None
        self.gobjs_red_crosses = []

    def process_dome_click(self, coord):
        for desac_dome in self.desac_domes:
            if desac_dome.selection_rect.in_bounds(coord):
                if self.selected_dome is not None:
                    self.selected_dome.unselect()
                if self.selected_dome != desac_dome:
                    desac_dome.select()
                    self.selected_dome = desac_dome
                else:
                    self.selected_dome = None
                return True
        return False

    def process_desac_try(self, coord_desac):
        desac_result = self.selected_dome.check_desactivation(coord_desac)
        #print("desac_result", desac_result.desac_res)
        #print(desac_result.failed_coords, desac_result.rot_index)

        if desac_result.has_failed_from_reveals():

            for failed_coord in desac_result.failed_coords:
                gobj = GameObject(failed_coord, "red_cross")
                self.gobjs_red_crosses.append(gobj)
                self.layer_ihm.add_game_object(gobj)

        elif desac_result.is_desactivation_ok():

            self.selected_dome.unselect()
            fixed_desac_dome = self.selected_dome.dome_rotations[
                desac_result.rot_index
            ]
            coord_dest = coord_desac.clone()
            coord_dest.move_by_vect(fixed_desac_dome.offset_sprite)
            coord_dest.move_by_vect(x=-1, y=-1)
            desac_result.desac_dome = self.selected_dome
            desac_result.coord_dest_dome = coord_dest
            desac_result.anim_step = 0 if desac_result.rot_steps else 1
            desac_result.coord_desac = coord_desac
            desac_result.compute_dome_travel_delay(fixed_desac_dome.coord_dome)
            self.selected_dome = None

        return desac_result

    def remove_red_crosses(self):
        for gobj in self.gobjs_red_crosses:
            self.layer_ihm.remove_game_object(gobj)
        self.gobjs_red_crosses[:] = []


class LootManager():

    LOOT_SLOWNESS = 15

    def __init__(self, layer_loot, rect_shop):
        self.layer_loot = layer_loot
        self.coord_dest = rect_shop.coord_upleft()
        self.money = 0
        self.flasks = [0, 0, 0]

    def can_pay(self, pay_money, pay_flasks):
        pass

    def widthdraw(self, pay_money, pay_flasks):
        pass

    def get_amount(self):
        return self.money, self.flasks

    def _add_transitions_to_gobj_loot(self, gobj_loot, delay_index, coord_start, area_offset_start):
        delay_before_move = 800 + delay_index * 50
        dist = (
            (coord_start.x + area_offset_start[0] - self.coord_dest.x) ** 2
            + (coord_start.y + area_offset_start[1] - self.coord_dest.y) ** 2
        )
        dist = dist ** 0.5
        delay_move = int(dist * self.LOOT_SLOWNESS)
        gobj_loot.add_transition(
            squarity.TransitionSteps(
                "coord",
                (
                    (delay_before_move, coord_start),
                    (delay_move, self.coord_dest),
                )
            )
        )
        # TODO LIB : c'est pas pratique du tout,
        # de devoir ajouter 2 transition pour une pauvre coord.
        field_names = ("area_offset_x", "area_offset_y")
        for ao_one_coord, field_name in zip(area_offset_start, field_names):
            if ao_one_coord != 0.5:
                gobj_loot.image_modifier.add_transition(
                    squarity.TransitionSteps(
                        field_name,
                        (
                            (delay_before_move, ao_one_coord),
                            (delay_move, 0.5),
                        )
                    )
                )


    def add_loot_gobjs_from_desac(self, fixed_desac_dome, color, coord_desac):
        gobjs_loot_added = []
        delay_indexes = list(range(len(
            fixed_desac_dome.money_offset_details
        )))
        random.shuffle(delay_indexes)
        for money_details, delay_index in zip(
            fixed_desac_dome.money_offset_details,
            delay_indexes
        ):
            coord_money = Coord(money_details[0], money_details[1])
            coord_money.move_by_vect(coord_desac)
            if len(money_details) >= 4:
                area_offset_start = money_details[2:4]
            else:
                area_offset_start = [0.0, 0.0]
            gobj_money = GameObject(
                coord_money,
                "money",
                image_modifier=squarity.ComponentImageModifier(
                    area_offset_x=area_offset_start[0],
                    area_offset_y=area_offset_start[1]
                )
            )
            gobj_money.loot_color = None
            self.layer_loot.add_game_object(gobj_money)
            self._add_transitions_to_gobj_loot(
                gobj_money, delay_index, coord_money, area_offset_start
            )
            gobjs_loot_added.append(gobj_money)

        if (0, 0) not in fixed_desac_dome.money_offset_details:
            sprite_name_flask = "flask_" + NAME_FROM_RAD_COLOR[color]
            gobj_flask = GameObject(
                coord_desac,
                sprite_name_flask,
                image_modifier=squarity.ComponentImageModifier(
                    area_scale_x=2.0,
                    area_scale_y=2.0,
                )
            )
            gobj_flask.loot_color = color
            self.layer_loot.add_game_object(gobj_flask)
            delay_index = len(fixed_desac_dome.money_offset_details)
            self._add_transitions_to_gobj_loot(
                gobj_flask, delay_index, coord_desac, (0, 0)
            )
            gobjs_loot_added.append(gobj_flask)

        if gobjs_loot_added:
            last_gobj = gobjs_loot_added[-1]
            last_gobj.set_callback_end_transi(
                lambda: self._remove_loot_gobjs(gobjs_loot_added)
            )

    def _remove_loot_gobjs(self, gobjs_loot):
        print("remove some gobj")
        for gobj in gobjs_loot:
            self.layer_loot.remove_game_object(gobj)
            if gobj.loot_color is None:
                self.money += 1
            else:
                index_color = int(gobj.loot_color)
                self.flasks[index_color] += 1


# Ça changera selon les niveaux.
SHOP_POSITION = Coord(1, 3)

class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.layer_background = self.layer_main
        # TODO LIB : les params width et height devraient être des params facultatifs.
        self.layer_radact = RadioactivityLayer(self, self.w, self.h, False)
        self.layer_radact.init_with_rad_tiles()
        self.layers.append(self.layer_radact)
        self.layer_block = squarity.Layer(self, self.w, self.h, False)
        self.layers.append(self.layer_block)
        # Contient les objets :
        # dome_full, dome_border_x, dome_corner_x, dome_tshape_x
        self.layer_movable_objs_1 = squarity.Layer(self, self.w, self.h, True)
        self.layers.append(self.layer_movable_objs_1)
        # Contient les objets : dome_color_xxxx
        self.layer_movable_objs_2 = squarity.Layer(self, self.w, self.h, True)
        self.layers.append(self.layer_movable_objs_2)
        self.layer_ihm = squarity.Layer(self, self.w, self.h, False)
        self.layers.append(self.layer_ihm)
        self.gobjs_red_crosses = []
        self.ended_game = False
        self.end_game_phrase = ""
        self.score = 0

        self.rect_shop = squarity.Rect(SHOP_POSITION.x, SHOP_POSITION.y, 2, 2)
        self.loot_manager = LootManager(self.layer_movable_objs_1, self.rect_shop)

        rect_dome_zone = squarity.Rect(0, 0, 9, 12)
        for c in squarity.RectIterator(self.rect):
            gobj = GameObject(c, "block")
            if not rect_dome_zone.in_bounds(c):
                self.layer_block.add_game_object(gobj)
            if not self.rect_shop.in_bounds(c):
                gobj = GameObject(c, "background")
                self.layer_background.add_game_object(gobj)

        self.gobj_shop = GameObject(
            self.rect_shop.coord_upleft(),
            "building_shop"
        )
        self.layer_background.add_game_object(self.gobj_shop)
        self.desac_dome_manager = DesacDomeManager(self.layer_ihm)
        desac_dome = DesacDome(self, DesacDomeShape.FULL, Coord(3, 0), RadColor.GREEN)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, DesacDomeShape.BORDER, Coord(3, 3), RadColor.GREEN)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, DesacDomeShape.CORNER, Coord(3, 6), RadColor.GREEN)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, DesacDomeShape.TSHAPE, Coord(3, 9), RadColor.GREEN)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, DesacDomeShape.FULL, Coord(0, 0), RadColor.YELLOW)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        # desac_dome = DesacDome(self, DesacDomeShape.BORDER, Coord(0, 3), RadColor.YELLOW)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, DesacDomeShape.CORNER, Coord(0, 6), RadColor.YELLOW)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, DesacDomeShape.TSHAPE, Coord(0, 9), RadColor.YELLOW)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, DesacDomeShape.FULL, Coord(6, 0), RadColor.PURPLE)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, DesacDomeShape.BORDER, Coord(6, 3), RadColor.PURPLE)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, DesacDomeShape.CORNER, Coord(6, 6), RadColor.PURPLE)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, DesacDomeShape.TSHAPE, Coord(6, 9), RadColor.PURPLE)
        self.desac_dome_manager.desac_domes.append(desac_dome)


        if INDEX_LEVEL == 1:
            self.put_barrels_level_1()
        else:
            self.put_barrels_level_2()

        self.layer_radact.compute_rad_indicators()

    def put_barrels_level_1(self):
        forbidden_rect_1 = squarity.Rect(0, 0, 9, 13)
        #forbidden_rect_2 = squarity.Rect(0, 0, 6, 3) TODO WIP booo !!
        for _ in range(12):
            coord_barrel = Coord(
                random.randrange(0, self.w),
                random.randrange(0, self.h)
            )
            barrel_color = random.choice((RadColor.YELLOW, RadColor.GREEN, RadColor.PURPLE))
            # booo !!
            if _ == 0:
                coord_barrel = Coord(9, 3)
                barrel_color = RadColor.PURPLE
            if not forbidden_rect_1.in_bounds(coord_barrel): # and not forbidden_rect_2.in_bounds(coord_barrel):
                tile_radact = self.layer_radact.get_tile(coord_barrel)
                no_barrel_around = all(
                    (tile_adj is None) or not tile_adj.barrel_strength
                    for tile_adj in tile_radact.adjacencies
                )
                if no_barrel_around:
                    self.layer_radact.add_barrel(coord_barrel, barrel_color)

    def put_barrels_level_2(self):

        forbidden_rect_1 = squarity.Rect(0, 0, 9, 12)
        xs = []
        increase_delay = 3
        cur_delay = increase_delay
        cur_mul = 1
        for x in range(self.w):
            xs.extend([x] * cur_mul)
            cur_delay -= 1
            if cur_delay == 0:
                cur_delay = increase_delay
                cur_mul += 1
        ys = []
        cur_delay = increase_delay
        cur_mul = 1
        for y in range(self.h):
            ys.extend([y] * cur_mul)
            cur_delay -= 1
            if cur_delay == 0:
                cur_delay = increase_delay
                cur_mul += 1

        candidate_coords = []
        for x in xs:
            for y in ys:
                c = Coord(x, y)
                if not forbidden_rect_1.in_bounds(c):
                    candidate_coords.append(c)
        random.shuffle(candidate_coords)
        barrel_coords = set()
        while len(barrel_coords) < 45:
            barrel_coords.add(candidate_coords.pop(0))

        #for _ in range(25):
        for coord_barrel in barrel_coords:
            #coord_barrel = Coord(
            #    random.randrange(0, self.w),
            #    random.randrange(0, self.h)
            #)
            barrel_color = random.choice((RadColor.YELLOW, RadColor.GREEN, RadColor.PURPLE))
            #if not forbidden_rect_1.in_bounds(coord_barrel):
            self.layer_radact.add_barrel(coord_barrel, barrel_color)

    def is_revealed(self, coord):
        return not bool(self.layer_block.get_game_objects(coord))

    def deradioactivize(self, coord):
        tile_to_deradact = self.layer_radact.get_tile(coord)
        tile_to_deradact.deradioactivize()
        self.layer_block.remove_at_coord(coord)
        self.layer_radact.compute_rad_indicators()
        if self.layer_radact.no_more_barrels():
            self.ended_game = True
            self.score += 100
            if INDEX_LEVEL == 1:
                self.end_game_phrase = "Bravo !!! Augmentez de 1 la valeur de INDEX_LEVEL au début du code source, puis, relancez une partie"
            else:
                if self.score > 119:
                    self.end_game_phrase = "Bravo !!! Vous avez gagné ! Bientôt, de nouvelles versions de ce jeu seront créées."
                else:
                    self.end_game_phrase = "Bravo !!! Vous avez gagné ! Essayez de faire un score d'au moins 120."
            print(self.end_game_phrase)
            print(f"score: {self.score}")

    def process_desactivation_anim(self, desac_result):
        # FUTURE LIB : c'est relou cette gestion avec des callbacks.
        # Si je pouvais arriver à faire du async/await dans squarity, ce serait trop cool.
        delay_ms = None

        if desac_result.anim_step == 0:
            rot_step = desac_result.rot_steps.pop(0)
            desac_result.desac_dome.rotate(rot_step)
            delay_ms = 200
            if not desac_result.rot_steps:
                desac_result.anim_step += 1

        elif desac_result.anim_step == 1:
            fixed_desac_dome = desac_result.desac_dome.get_fixed_dome_cur()
            dome_move_delay = desac_result.dome_travel_delay
            fixed_desac_dome.gobj_dome.add_transition(
                squarity.TransitionSteps(
                    "coord",
                    ((dome_move_delay, desac_result.coord_dest_dome), )
                )
            )
            desac_result.desac_dome.gobj_dome_color.add_transition(
                squarity.TransitionSteps(
                    "coord",
                    ((dome_move_delay, desac_result.coord_desac), )
                )
            )
            delay_ms = dome_move_delay + 300
            desac_result.anim_step += 1

        elif desac_result.anim_step == 2:
            #  TODO : animation avec une explosion dans le dôme. Boum !!!
            self.deradioactivize(desac_result.coord_desac)
            fixed_desac_dome = desac_result.desac_dome.get_fixed_dome_cur()
            self.loot_manager.add_loot_gobjs_from_desac(
                fixed_desac_dome,
                desac_result.rad_color,
                desac_result.coord_desac
            )
            delay_ms = 300
            desac_result.anim_step += 1

        elif desac_result.anim_step == 3:
            fixed_desac_dome = desac_result.desac_dome.get_fixed_dome_cur()
            dome_move_delay = desac_result.dome_travel_delay
            fixed_desac_dome.gobj_dome.add_transition(
                squarity.TransitionSteps(
                    "coord",
                    ((dome_move_delay, fixed_desac_dome.coord_dome), )
                )
            )
            coord_return_color = desac_result.desac_dome.coord_color_indicator
            desac_result.desac_dome.gobj_dome_color.add_transition(
                squarity.TransitionSteps(
                    "coord",
                    ((dome_move_delay, coord_return_color), )
                )
            )
            delay_ms = dome_move_delay
            desac_result.anim_step += 1

        else:
            delay_ms = None

        ev = squarity.EventResult()
        if delay_ms is None:
            #print("ok release lock")
            ev.punlocks_custom.append("lock_desactivation")
        else:
            func = lambda: self.process_desactivation_anim(desac_result)
            ev.add_delayed_callback(squarity.DelayedCallBack(delay_ms, func))
        return ev

    def process_click_normal_mode(self, coord):
        if self.layer_radact.get_tile(coord).barrel_strength:
            self.ended_game = True
            self.end_game_phrase = "Fail !!! Cliquez sur Exécutez pour recommencer une partie."
            for c in squarity.RectIterator(self.rect):
                self.layer_block.remove_at_coord(c)
            print(self.end_game_phrase)
            print(f"score: {self.score}")
        else:
            self.layer_block.remove_at_coord(coord)
        return None

    def process_click_selected_dome(self, coord):
        desac_result = self.desac_dome_manager.process_desac_try(coord)
        if desac_result.has_failed_from_reveals():
            #print("need to remove red crosses.")
            ev = squarity.EventResult()
            ev.add_delayed_callback(
                squarity.DelayedCallBack(
                    700,
                    self.desac_dome_manager.remove_red_crosses
                )
            )
            return ev
        elif desac_result.is_desactivation_ok():
            ev = squarity.EventResult()
            if desac_result.desac_dome.shape == DesacDomeShape.FULL:
                self.score += 1
            func = lambda: self.process_desactivation_anim(desac_result)
            ev.add_delayed_callback(squarity.DelayedCallBack(1, func))
            ev.plocks_custom.append("lock_desactivation")
            return ev
        else:
            # TODO : là, faudrait juste casser le dôme, et non pas terminer le jeu.
            self.ended_game = True
            self.end_game_phrase = "Fail !! Mauvais couleur, ou bien pas de baril !!! Cliquez sur Exécutez pour recommencer une partie."
            for c in squarity.RectIterator(self.rect):
                self.layer_block.remove_at_coord(c)
            print(self.end_game_phrase)
            print(f"score: {self.score}")
            return None

    def on_click(self, coord):
        if self.ended_game:
            print(self.end_game_phrase)
            return
        if self.rect_shop.in_bounds(coord):
            money, flasks = self.loot_manager.get_amount()
            print(f"Vous avez {money} moulageiger et {flasks} fioles.")
            return
        if self.desac_dome_manager.process_dome_click(coord):
            return
        if self.desac_dome_manager.selected_dome is None:
            return self.process_click_normal_mode(coord)
        else:
            return self.process_click_selected_dome(coord)

