# https://squarity.fr/game/#fetchez_githubgist_darkrecher/6ac1768472ecd954d4818ef1dbd59d6c/raw/radioactivesweeper.txt
# https://tinyurl.com/radswp123
# https://raw.githubusercontent.com/darkrecher/squarity-doc/refs/heads/master/jeux/radioactive_sweeper/radioactive_tileset.png
# taille de l'aire de jeu : 30, 20 ??
"""
{
  "name": "Radioactive Sweeper",
  "version": "2.1.0",
  "game_area": {
    "nb_tile_width": 15,
    "nb_tile_height": 20
  },
  "tile_size": 32,
  "img_coords": {
    "rad_01": [32, 0],
    "rad_02": [64, 0],
    "rad_03": [96, 0],
    "rad_04": [128, 0],
    "rad_05": [160, 0],
    "rad_06": [192, 0],
    "rad_07": [224, 0],
    "rad_08": [256, 0],
    "rad_09": [288, 0],
    "rad_10": [0, 32],
    "rad_11": [32, 32],
    "rad_12": [64, 32],
    "rad_13": [96, 32],
    "rad_14": [128, 32],
    "rad_15": [160, 32],
    "rad_16": [192, 32],
    "rad_17": [224, 32],
    "rad_18": [256, 32],
    "rad_19": [288, 32],

    "block": [0, 64],
    "rad_ylw_source": [32, 64],
    "rad_ylw_barrel": [64, 64],
    "red_cross": [0, 96],
    "dome_ground_base": [0, 160, 96, 96],
    "dome_full": [96, 64, 96, 96],
    "dome_border_0": [448, 0, 96, 64],

    "background": [0, 0]
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

PATTERN_RAD_YELLOW_1 = (
    (0, -1, 6), (1, -1, 6), (1, 0, 6), (1, 1, 6),
    (0, 1, 6), (-1, 1, 6), (-1, 0, 6), (-1, -1, 6),
    (0, -2, 4), (2, 0, 4), (0, 2, 4), (-2, 0, 4),
    (0, -3, 2), (3, 0, 2), (0, 3, 2), (-3, 0, 2),
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

        if self.barrel_color == RadColor.YELLOW:
            if self.barrel_strength == 1:
                # TODO LIB : ça fait du yo-yo. On devrait avoir une fonction dans Tile,
                # pour ajouter/supprimer des game objects directement dedans.
                gobj_source = GameObject(self._coord, "rad_ylw_source")
                self.layer_owner.add_game_object(gobj_source)
            gobj_barrel = GameObject(self._coord, "rad_ylw_barrel")
            self.layer_owner.add_game_object(gobj_barrel)

        sum_strength = min(19, sum(self.rad_strengths))
        if self.barrel_color is not None:
            sum_strength = 0
        #print("WIP", self._coord, sum_strength)
        if sum_strength:
            if sum_strength > 19:
                raise Exception("TODO : Pas de sprite de radioactivité après 19 !!!")
            gobj_rad_indic = GameObject(self._coord, f"rad_{sum_strength:02d}")
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
        if rad_color != RadColor.YELLOW:
            raise Exception("TODO Rad !!")
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
            if tile_barrel.barrel_color == RadColor.YELLOW and tile_barrel.barrel_strength == 1:
                pattern = PATTERN_RAD_YELLOW_1
                rad_color_index = RadColor.YELLOW
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
    ]
}


class FixedDesacDome():
    """
    "Fixed desactivation dome", c'est à dire une rotation spécifique
    d'une shape spécifique d'un dôme.
    """

    def __init__(self, shape, rot_index, pos_upleft):
        dome_conf = DESAC_DOME_CONFIGS[shape][rot_index]
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
    - refusé, car la tile principale est déjà révélée (red cross positions, une seule)
    - refusé car tout n'est pas révélé, ou alors c'est au bord (red cross positions).
    - le dôme casse sur une tile vide.
    - le dôme casse sur une tile avec un baril n'ayant pas la bonne couleur.
    - ok
    - ok, mais faudrait tourner le dôme. (index de rotation)
    """

    def __init__(self, desac_res, failed_coords=[], rot_index=None):
        self.desac_res = desac_res
        self.failed_coords = failed_coords
        self.rot_index = rot_index


class DesacDome():
    """
    Un dôme spécifique, placé dans l'aire de jeu.
    Gère les rotations et la validation d'une désactivation.
    """

    def __init__(self, game, layer_owner, shape, pos_upleft):
        # TODO : est-ce une bonne idée de prendre tout ça?
        # On pourrait juste garder la ref vers "game".
        self.layer_radact = game.layer_radact
        self.is_revealed = game.is_revealed
        self.rect = game.rect
        self.layer_owner = layer_owner
        self.pos_upleft = Coord(coord=pos_upleft)
        # Au max, on a 4 instances de DesacDome, indiquant les différentes positions du dôme.
        # Quand c'est le dôme circulaire, on a une seule instance.
        self.dome_rotations = [
            FixedDesacDome(shape, 0, self.pos_upleft)
        ]
        self.rot_index = 0
        self.rad_color = RadColor.YELLOW
        self.selected = False
        self.gobj_ground_base = GameObject(pos_upleft, "dome_ground_base")
        self.layer_owner.add_game_object(self.gobj_ground_base)
        self.selection_rect = squarity.Rect(
            self.pos_upleft.x, self.pos_upleft.y, 3, 3
        )
        # TODO : gérer le game object indiquant la couleur du dôme. Dans un autre layer, du coup. Argh.

    def select(self):
        self.selected = True
        for gobj in self.dome_rotations[self.rot_index].gobjs_show_selection:
            self.layer_owner.add_game_object(gobj)

    def unselect(self):
        self.selected = False
        for gobj in self.dome_rotations[self.rot_index].gobjs_show_selection:
            self.layer_owner.remove_game_object(gobj)

    def show_current_dome(self):
        gobj_dome_current = self.dome_rotations[self.rot_index].gobj_dome
        self.layer_owner.add_game_object(gobj_dome_current)

    def check_desactivation(self, coord_desac):

        if self.is_revealed(coord_desac):
            return DesactivationResult(
                DesacRes.FAIL_MAIN_TILE_REVEALED,
                failed_coords=[coord_desac]
            )

        # TODO : on teste d'abord la rotation actuelle, puis les autres.
        rot_index_ok = None
        for rot_index_try, dome_rotation in enumerate(self.dome_rotations):
            offsets = dome_rotation.offset_positions_to_check
            all_around_ok = True
            for offset in offsets:
                coord_to_check = coord_desac.clone().move_by_vect(offset)
                if not self.rect.in_bounds(coord_to_check):
                    print("coord_to_check out of bounds", coord_to_check, self.rect)
                    all_around_ok = False
                    break
                if not self.is_revealed(coord_to_check):
                    print("coord_to_check fails", coord_to_check)
                    all_around_ok = False
                    break
            if all_around_ok:
                rot_index_ok = rot_index_try
                break
        if rot_index_ok is None:
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
            return DesactivationResult(DesacRes.FAIL_BREAK_COLOR_MISMATCH)

        if rot_index_ok == self.rot_index:
            return DesactivationResult(DesacRes.SUCCESS)
        else:
            return DesactivationResult(
                DesacRes.SUCCESS_WITH_ROTATION,
                rot_index=rot_index_ok
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

    def add_dome(self, desac_dome):
        self.desac_domes.append(desac_dome)
        desac_dome.show_current_dome()

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
        elif desac_result.desac_res == DesacRes.SUCCESS:
            self.selected_dome.unselect()
            fixed_desac_dome = self.selected_dome.dome_rotations[
                self.selected_dome.rot_index
            ]
            coord_dest = coord_desac.clone().move_by_vect(
                fixed_desac_dome.offset_sprite_pos
            ).move_by_vect(
                x=-1, y=-1
            )
            coord_return = self.selected_dome.pos_upleft.clone().move_by_vect(
                fixed_desac_dome.offset_sprite_pos
            )

            fixed_desac_dome.gobj_dome.add_transition(
                squarity.TransitionSteps(
                    "coord",
                    (
                        (500, coord_dest),
                        (600, coord_dest),
                        (500, coord_return)
                    )
                )
            )
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
        self.layer_ihm = squarity.Layer(self, self.w, self.h, False)
        self.layers.append(self.layer_ihm)
        self.gobjs_red_crosses = []
        self.ended_game = False
        self.end_game_phrase = ""

        rect_dome_zone = squarity.Rect(0, 3, 3, 6)
        for c in squarity.RectIterator(self.rect):
            gobj = GameObject(c, "block")
            if not rect_dome_zone.in_bounds(c):
                self.layer_block.add_game_object(gobj)

        self.desac_dome_manager = DesacDomeManager(self.layer_ihm)
        desac_dome = DesacDome(self, self.layer_buildings, DesacDomeShape.FULL, Coord(0, 3))
        self.desac_dome_manager.add_dome(desac_dome)
        desac_dome = DesacDome(self, self.layer_buildings, DesacDomeShape.BORDER, Coord(0, 6))
        self.desac_dome_manager.add_dome(desac_dome)

        if INDEX_LEVEL == 1:
            self.put_barrels_level_1()
        else:
            self.put_barrels_level_2()

        self.layer_radact.compute_rad_indicators()

    def put_barrels_level_1(self):
        forbidden_rect_1 = squarity.Rect(0, 0, 4, 6)
        forbidden_rect_2 = squarity.Rect(0, 0, 6, 3)
        for _ in range(7):
            coord_barrel = Coord(
                random.randrange(1, self.w - 1),
                random.randrange(1, self.h - 1)
            )
            # TODO WIP booo !!
            if _ == 0:
                coord_barrel = Coord(6, 3)
            if not forbidden_rect_1.in_bounds(coord_barrel) and not forbidden_rect_2.in_bounds(coord_barrel):
                tile_radact = self.layer_radact.get_tile(coord_barrel)
                no_barrel_around = all(
                    (tile_adj is None) or not tile_adj.barrel_strength
                    for tile_adj in tile_radact.adjacencies
                )
                if no_barrel_around:
                    self.layer_radact.add_barrel(coord_barrel, RadColor.YELLOW)

    def put_barrels_level_2(self):
        for _ in range(14):
            coord_barrel = Coord(
                random.randrange(0, self.w),
                random.randrange(0, self.h)
            )
            if coord_barrel.x >= 4 or coord_barrel.y >= 4:
                self.layer_radact.add_barrel(coord_barrel, RadColor.YELLOW)

    def is_revealed(self, coord):
        return not bool(self.layer_block.get_game_objects(coord))

    def deradioactivize(self, coord):
        tile_to_deradact = self.layer_radact.get_tile(coord)
        tile_to_deradact.deradioactivize()
        self.layer_block.remove_at_coord(coord)
        self.layer_radact.compute_rad_indicators()
        if self.layer_radact.no_more_barrels():
            self.ended_game = True
            if INDEX_LEVEL == 1:
                self.end_game_phrase = "Bravo !!! Augmentez de 1 la valeur de INDEX_LEVEL au début du code source, puis, relancez une partie"
            else:
                self.end_game_phrase = "Bravo !!! Vous avez gagné ! Bientôt, de nouvelles versions de ce jeu seront créées."
            print(self.end_game_phrase)

    def on_click(self, coord):

        if self.ended_game:
            print(self.end_game_phrase)
            return

        elif self.desac_dome_manager.process_dome_click(coord):
            return

        else:

            if self.desac_dome_manager.selected_dome is None:

                if self.layer_radact.get_tile(coord).barrel_strength:
                    self.ended_game = True
                    self.end_game_phrase = "Fail !!! Cliquez sur Exécutez pour recommencer une partie."
                    for c in squarity.RectIterator(self.rect):
                        self.layer_block.remove_at_coord(c)
                    print(self.end_game_phrase)
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
                else:
                    ev = squarity.EventResult()
                    ev.add_delayed_callback(
                        squarity.DelayedCallBack(
                            800,
                            lambda: self.deradioactivize(coord)
                        )
                    )
                    return ev

    def on_button_direction(self, direction):
        pass

    def on_button_action(self, action_name):
        pass

