# https://squarity.fr/game/#fetchez_githubgist_darkrecher/6ac1768472ecd954d4818ef1dbd59d6c/raw/radioactivesweeper.txt
# https://tinyurl.com/radswp123
# https://raw.githubusercontent.com/darkrecher/squarity-doc/refs/heads/master/jeux/radioactive_sweeper/radioactive_tileset.png
# taille de l'aire de jeu : 30, 20 ??

# TODO : réajuster les images des dômes et des dessins de couleur, pour que le dessin touche pas les bords.
# TODO : chiffre plus blanc, couleur de radioactivité derrière les chiffres plus foncées.

"""
{
  "name": "Radioactive Sweeper",
  "version": "2.1.0",
  "game_area": {
    "nb_tile_width": 25,
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

    "background": [0, 128]
  },
  "show_code_at_start": true,
  "appendices": {

  }
}
"""

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
                # TODO : re du yo-yo.
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
            pattern = None
            if tile_barrel.barrel_color == RadColor.YELLOW and tile_barrel.barrel_strength == 1:
                pattern = PATTERN_RAD_YELLOW_1
            elif tile_barrel.barrel_color == RadColor.GREEN and tile_barrel.barrel_strength == 1:
                pattern = PATTERN_RAD_GREEN_1
            elif tile_barrel.barrel_color == RadColor.PURPLE and tile_barrel.barrel_strength == 1:
                pattern = PATTERN_RAD_PURPLE_1
            # TODO: implement other barrels

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


"""
Une config avec juste des données dedans. (image, offsets, offsets de verif).

une classe FixedDesacDome

, qui gère les rotations, sélections/déselections. Validation d'une désactivation. Animation d'une désactivation.

Mais c'est toujours le GameModel qui désactive les barils.
"""

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
DESAC_DOME_CONFIGS = {
    DesacDomeShape.FULL: [
        (
            "dome_full",
            Coord(0, 0),
            (
                Coord(0, -1), Coord(1, -1), Coord(1, 0), Coord(1, 1),
                Coord(0, 1), Coord(-1, 1), Coord(-1, 0), Coord(-1, -1),
            )
        ),
    ],
    DesacDomeShape.BORDER: [
        (
            "dome_border_0",
            Coord(0, 0),
            (
                Coord(0, -1), Coord(1, -1), Coord(1, 0),
                Coord(-1, 0), Coord(-1, -1),
            )
        ),
        (
            "dome_border_1",
            Coord(1, 0),
            (
                Coord(0, -1), Coord(1, -1), Coord(1, 0),
                Coord(1, 1), Coord(0, 1),
            )
        ),
        (
            "dome_border_2",
            Coord(0, 1),
            (
                Coord(1, 0), Coord(1, 1),
                Coord(0, 1), Coord(-1, 1), Coord(-1, 0),
            )
        ),
        (
            "dome_border_3",
            Coord(0, 0),
            (
                Coord(0, 1), Coord(-1, 1), Coord(-1, 0), Coord(-1, -1),
                Coord(0, -1),
            )
        ),
    ],
    DesacDomeShape.CORNER: [
        (
            "dome_corner_0",
            Coord(1, 0),
            (
                Coord(0, -1), Coord(1, -1), Coord(1, 0),
            )
        ),
        (
            "dome_corner_1",
            Coord(1, 1),
            (
                Coord(1, 0), Coord(1, 1), Coord(0, 1),
            )
        ),
        (
            "dome_corner_2",
            Coord(0, 1),
            (
                Coord(0, 1), Coord(-1, 1), Coord(-1, 0),
            )
        ),
        (
            "dome_corner_3",
            Coord(0, 0),
            (
                Coord(-1, 0), Coord(-1, -1), Coord(0, -1),
            )
        ),
    ],
    DesacDomeShape.TSHAPE: [
        (
            "dome_tshape_0",
            Coord(0, 0),
            (
                Coord(0, -1), Coord(1, -1), Coord(-1, -1),
            )
        ),
        (
            "dome_tshape_1",
            Coord(1, 0),
            (
                Coord(1, -1), Coord(1, 0), Coord(1, 1),
            )
        ),
        (
            "dome_tshape_2",
            Coord(0, 1),
            (
                Coord(1, 1), Coord(0, 1), Coord(-1, 1),
            )
        ),
        (
            "dome_tshape_3",
            Coord(0, 0),
            (
                Coord(-1, 1), Coord(-1, 0), Coord(-1, -1),
            )
        ),
    ]
}


class FixedDesacDome():
    """
    "Fixed desactivation dome", c'est à dire une rotation spécifique
    d'une shape spécifique d'un dôme.
    """

    def __init__(self, dome_conf, pos_upleft):
        sprite_name, offset_sprite_pos, offset_positions_to_check = dome_conf
        self.offset_sprite_pos = offset_sprite_pos
        self.gobj_dome = GameObject(
            pos_upleft.clone().move_by_vect(self.offset_sprite_pos),
            sprite_name
        )
        # TODO : en fait non, faudrait pas locker le jeu quand on désactive un truc.
        # faut mettre les actions en queue et les dépiler. Mais c'est compliqué à faire...
        self.gobj_dome.plock_transi = squarity.PlayerLockTransi.LOCK
        self.offset_positions_to_check = offset_positions_to_check
        # Liste de gobj à ajouter/enlever pour montrer que ce dôme est sélectionné.
        self.gobjs_show_selection = tuple([
            GameObject(
                pos_upleft.clone().move_by_vect(self.offset_sprite_pos),
                sprite_name
            ) for _ in range(3)
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

    def __init__(self, desac_res, failed_coords=[], rot_index=None, rot_steps=[]):
        self.desac_res = desac_res
        self.failed_coords = failed_coords
        self.rot_index = rot_index
        self.rot_steps = rot_steps
        # Les variables ci-dessous ne sont utilisés
        # que pour les désactivations qui sont ok.
        self.desac_dome = None
        self.coord_dest_dome = None
        self.coord_return_dome = None
        self.anim_step = None
        self.coord_desac = None

    # TODO : petite fonction pour calculer le temps de trajet du dôme,
    # proportionnel à la distance de trajet.


class DesacDome():
    """
    Un dôme spécifique, placé dans l'aire de jeu.
    Gère les rotations et la validation d'une désactivation.
    """

    def __init__(self, game, layer_owner, shape, pos_upleft, rad_color):
        self.game = game
        # TODO : est-ce une bonne idée de prendre tout ça?
        # On pourrait juste garder la ref vers "game".
        self.layer_radact = game.layer_radact
        self.is_revealed = game.is_revealed
        self.rect = game.rect
        self.layer_owner = layer_owner
        self.shape = shape
        self.pos_upleft = pos_upleft.clone()
        self.rad_color = rad_color
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
        # TODO : ça va dans le layer de background, ce truc là.
        # D'où l'intérêt de garder que la ref vers game, et choper tout ce qu'on a besoin dedans.
        self.gobj_ground_base = GameObject(pos_upleft, "dome_ground_base")
        self.layer_owner.add_game_object(self.gobj_ground_base)
        self.selection_rect = squarity.Rect(
            self.pos_upleft.x, self.pos_upleft.y, 3, 3
        )
        sprite_name_col = "dome_color_" + NAME_FROM_RAD_COLOR[self.rad_color]
        self.gobj_dome_color = GameObject(
            pos_upleft.move_by_vect(x=1, y=1),
            sprite_name_col
        )
        self.game.layer_buildings_2.add_game_object(self.gobj_dome_color)
        self._show_current_dome()
        # TODO : gérer le game object indiquant la couleur du dôme. Dans un autre layer, du coup. Argh.

    def select(self):
        self.selected = True
        for gobj in self.gobjs_show_selection:
            self.layer_owner.add_game_object(gobj)

    def unselect(self):
        self.selected = False
        for gobj in self.gobjs_show_selection:
            self.layer_owner.remove_game_object(gobj)

    def _show_current_dome(self):
        was_selected = self.selected
        if was_selected:
            self.unselect()
        if self.gobj_dome_cur is not None:
            self.layer_owner.remove_game_object(self.gobj_dome_cur)
        dome_rotation_cur = self.dome_rotations[self.rot_index_cur]
        self.gobj_dome_cur = dome_rotation_cur.gobj_dome
        self.gobjs_show_selection = dome_rotation_cur.gobjs_show_selection
        #print(self.gobj_dome_cur)
        self.layer_owner.add_game_object(self.gobj_dome_cur)
        if was_selected:
            self.select()

    def rotate(self, rot_offset):
        self.rot_index_cur += rot_offset
        self.rot_index_cur %= len(self.dome_rotations)
        #print(self.rot_index_cur)
        self._show_current_dome()

    def check_desactivation(self, coord_desac):

        if self.is_revealed(coord_desac):
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
        for rot_index_try, rot_steps in possible_rotations:
            dome_rotation = self.dome_rotations[rot_index_try]
            offsets = dome_rotation.offset_positions_to_check
            all_around_ok = True
            for offset in offsets:
                coord_to_check = coord_desac.clone().move_by_vect(offset)
                if not self.rect.in_bounds(coord_to_check):
                    #print("coord_to_check out of bounds", coord_to_check, self.rect)
                    all_around_ok = False
                    break
                if not self.is_revealed(coord_to_check):
                    #print("coord_to_check fails", coord_to_check)
                    all_around_ok = False
                    break
            if all_around_ok:
                possible_rot_ok = rot_index_try, rot_steps
                break
        if possible_rot_ok is None:
            # TODO : failed_coords doit être initialisé mieux que ça.
            return DesactivationResult(
                DesacRes.FAIL_UNREVEALED_TILES,
                failed_coords=[coord_desac]
            )

        tile_radac = self.layer_radact.get_tile(coord_desac)
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
            )
        else:
            return DesactivationResult(
                DesacRes.SUCCESS_WITH_ROTATION,
                rot_index=rot_index_ok,
                rot_steps=list(rot_steps_ok)
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
        self.fails_with_red_cross = (
            DesacRes.FAIL_MAIN_TILE_REVEALED,
            DesacRes.FAIL_UNREVEALED_TILES
        )

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

        if desac_result.desac_res in self.fails_with_red_cross:

            for failed_coord in desac_result.failed_coords:
                gobj = GameObject(failed_coord, "red_cross")
                self.gobjs_red_crosses.append(gobj)
                self.layer_ihm.add_game_object(gobj)

        # TODO : mettre une mini-fonction dans le desac_result, pour checker fail ou success.
        elif desac_result.desac_res in (DesacRes.SUCCESS, DesacRes.SUCCESS_WITH_ROTATION):

            self.selected_dome.unselect()
            # TODO : fonction dans desac_dome pour renvoyer le fixed desac dome courant, mais ça servira pas ici. haha.
            fixed_desac_dome = self.selected_dome.dome_rotations[
                desac_result.rot_index
            ]
            coord_dest = coord_desac.clone().move_by_vect(
                fixed_desac_dome.offset_sprite_pos
            ).move_by_vect(
                x=-1, y=-1
            )
            coord_return = self.selected_dome.pos_upleft.clone()
            coord_return.move_by_vect(
                fixed_desac_dome.offset_sprite_pos
            )
            desac_result.desac_dome = self.selected_dome
            desac_result.coord_dest_dome = coord_dest
            desac_result.coord_return_dome = coord_return
            desac_result.anim_step = 0 if desac_result.rot_steps else 1
            desac_result.coord_desac = coord_desac
            self.selected_dome = None

        return desac_result

    def remove_red_crosses(self):
        for gobj in self.gobjs_red_crosses:
            self.layer_ihm.remove_game_object(gobj)
        self.gobjs_red_crosses[:] = []


class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.layer_background = self.layer_main
        # TODO LIB : les width et height devraient être des params facultatifs.
        self.layer_radact = RadioactivityLayer(self, self.w, self.h, False)
        self.layer_radact.init_with_rad_tiles()
        self.layers.append(self.layer_radact)
        self.layer_block = squarity.Layer(self, self.w, self.h, False)
        self.layers.append(self.layer_block)
        self.layer_buildings = squarity.Layer(self, self.w, self.h, True)
        self.layers.append(self.layer_buildings)
        # TODO : nom de merde : layer_buildings_2
        self.layer_buildings_2 = squarity.Layer(self, self.w, self.h, True)
        self.layers.append(self.layer_buildings_2)
        self.layer_ihm = squarity.Layer(self, self.w, self.h, False)
        self.layers.append(self.layer_ihm)
        self.gobjs_red_crosses = []
        self.ended_game = False
        self.end_game_phrase = ""
        self.score = 0

        rect_dome_zone = squarity.Rect(0, 0, 9, 12)
        for c in squarity.RectIterator(self.rect):
            gobj = GameObject(c, "block")
            if not rect_dome_zone.in_bounds(c):
                self.layer_block.add_game_object(gobj)
            gobj = GameObject(c, "background")
            self.layer_background.add_game_object(gobj)

        self.desac_dome_manager = DesacDomeManager(self.layer_ihm)
        desac_dome = DesacDome(self, self.layer_buildings, DesacDomeShape.FULL, Coord(3, 0), RadColor.GREEN)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, self.layer_buildings, DesacDomeShape.BORDER, Coord(3, 3), RadColor.GREEN)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, self.layer_buildings, DesacDomeShape.CORNER, Coord(3, 6), RadColor.GREEN)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, self.layer_buildings, DesacDomeShape.TSHAPE, Coord(3, 9), RadColor.GREEN)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, self.layer_buildings, DesacDomeShape.FULL, Coord(0, 0), RadColor.YELLOW)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, self.layer_buildings, DesacDomeShape.BORDER, Coord(0, 3), RadColor.YELLOW)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, self.layer_buildings, DesacDomeShape.CORNER, Coord(0, 6), RadColor.YELLOW)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, self.layer_buildings, DesacDomeShape.TSHAPE, Coord(0, 9), RadColor.YELLOW)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, self.layer_buildings, DesacDomeShape.FULL, Coord(6, 0), RadColor.PURPLE)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, self.layer_buildings, DesacDomeShape.BORDER, Coord(6, 3), RadColor.PURPLE)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, self.layer_buildings, DesacDomeShape.CORNER, Coord(6, 6), RadColor.PURPLE)
        self.desac_dome_manager.desac_domes.append(desac_dome)
        desac_dome = DesacDome(self, self.layer_buildings, DesacDomeShape.TSHAPE, Coord(6, 9), RadColor.PURPLE)
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
            # TODO WIP booo !!
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
            # TODO : fonction dans desac_dome pour renvoyer le fixed desac dome courant
            fixed_desac_dome = desac_result.desac_dome.dome_rotations[
                desac_result.desac_dome.rot_index_cur
            ]
            fixed_desac_dome.gobj_dome.add_transition(
                squarity.TransitionSteps(
                    "coord",
                    ((500, desac_result.coord_dest_dome), )
                )
            )
            desac_result.desac_dome.gobj_dome_color.add_transition(
                squarity.TransitionSteps(
                    "coord",
                    ((500, desac_result.coord_desac), )
                )
            )
            delay_ms = 800
            desac_result.anim_step += 1

        elif desac_result.anim_step == 2:
            #  TODO : animation avec une explosion dans le dôme. Boum !!!
            self.deradioactivize(desac_result.coord_desac)
            delay_ms = 300
            desac_result.anim_step += 1

        elif desac_result.anim_step == 3:
            # TODO : fonction dans desac_dome pour renvoyer le fixed desac dome courant
            fixed_desac_dome = desac_result.desac_dome.dome_rotations[
                desac_result.desac_dome.rot_index_cur
            ]
            fixed_desac_dome.gobj_dome.add_transition(
                squarity.TransitionSteps(
                    "coord",
                    ((500, desac_result.coord_return_dome), )
                )
            )
            # TODO : on pourrait precalc cette coord et la laisser dans le desac_dome.
            coord_return_color = desac_result.desac_dome.pos_upleft.clone()
            coord_return_color.move_by_vect(x=1, y=1)
            desac_result.desac_dome.gobj_dome_color.add_transition(
                squarity.TransitionSteps(
                    "coord",
                    ((500, coord_return_color), )
                )
            )
            delay_ms = 500
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

    def on_click(self, coord):

        if self.ended_game:
            print(self.end_game_phrase)
            return

        elif self.desac_dome_manager.process_dome_click(coord):
            return

        # TODO : fonction spécifique pour chacun de ces trucs, parce que c'est les gestions des clicks.
        if self.desac_dome_manager.selected_dome is None:

            if self.layer_radact.get_tile(coord).barrel_strength:
                self.ended_game = True
                self.end_game_phrase = "Fail !!! Cliquez sur Exécutez pour recommencer une partie."
                for c in squarity.RectIterator(self.rect):
                    self.layer_block.remove_at_coord(c)
                print(self.end_game_phrase)
                print(f"score: {self.score}")
            else:
                self.layer_block.remove_at_coord(coord)

        else:

            desac_result = self.desac_dome_manager.process_desac_try(coord)
            fails = self.desac_dome_manager.fails_with_red_cross
            if desac_result.desac_res in fails:
                #print("need to remove red crosses.")
                ev = squarity.EventResult()
                ev.add_delayed_callback(
                    squarity.DelayedCallBack(
                        700,
                        self.desac_dome_manager.remove_red_crosses
                    )
                )
                return ev
            elif desac_result.desac_res in (DesacRes.SUCCESS, DesacRes.SUCCESS_WITH_ROTATION):
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

    def on_button_direction(self, direction):
        pass

    def on_button_action(self, action_name):
        pass


