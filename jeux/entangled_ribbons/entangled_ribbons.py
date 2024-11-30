# https://ibb.co/rHsfXWK
# https://i.ibb.co/GRT3rhf/ent-rib-tileset.png
# https://i.ibb.co/m9HwNJG/ent-rib-tileset.png

"""
  {
    "name": "Entangled ribbon",
    "version": "2.1.0",
    "game_area": {
      "nb_tile_width": 20,
      "nb_tile_height": 20
    },
    "tile_size": 32,
    "img_coords": {
      "rib_red_horiz": [0, 32],
      "rib_red_vertic": [32, 32],
      "rib_red_turn_06": [64, 32],
      "rib_red_turn_02": [96, 32],
      "rib_red_turn_24": [128, 32],
      "rib_red_turn_46": [160, 32],
      "rib_red_extr_6": [192, 32],
      "rib_red_extr_0": [224, 32],
      "rib_red_extr_4": [256, 32],
      "rib_red_extr_2": [288, 32],
      "rib_yel_horiz": [0, 128],
      "rib_yel_vertic": [32, 128],
      "rib_yel_turn_06": [64, 128],
      "rib_yel_turn_02": [96, 128],
      "rib_yel_turn_24": [128, 128],
      "rib_yel_turn_46": [160, 128],
      "rib_yel_extr_6": [192, 128],
      "rib_yel_extr_0": [224, 128],
      "rib_yel_extr_4": [256, 128],
      "rib_yel_extr_2": [288, 128],
      "rib_grn_horiz": [0, 64],
      "rib_grn_vertic": [32, 64],
      "rib_grn_turn_06": [64, 64],
      "rib_grn_turn_02": [96, 64],
      "rib_grn_turn_24": [128, 64],
      "rib_grn_turn_46": [160, 64],
      "rib_grn_extr_6": [192, 64],
      "rib_grn_extr_0": [224, 64],
      "rib_grn_extr_4": [256, 64],
      "rib_grn_extr_2": [288, 64],
      "rib_blu_horiz": [0, 96],
      "rib_blu_vertic": [32, 96],
      "rib_blu_turn_06": [64, 96],
      "rib_blu_turn_02": [96, 96],
      "rib_blu_turn_24": [128, 96],
      "rib_blu_turn_46": [160, 96],
      "rib_blu_extr_6": [192, 96],
      "rib_blu_extr_0": [224, 96],
      "rib_blu_extr_4": [256, 96],
      "rib_blu_extr_2": [288, 96],

      "icon_grap": [32, 0],
      "icon_swap": [64, 0],
      "hero": [96, 0],
      "background": [0, 0]
    }
  }
"""

import squarity
Coord = squarity.Coord
GameObject = squarity.GameObject

WORLD_WIDTH = 100
WORLD_HEIGHT = 100

class Ribbon():

    def __init__(self, ribbons_world, color):
        self.gobjs = []
        self.color = color
        self.ribbons_world = ribbons_world

    def hard_code_path_1(self):
        self.gobjs = [
            GameObject(Coord(18, 17), "rib_red_extr_4"),
            GameObject(Coord(18, 18), "rib_red_vertic"),
            GameObject(Coord(18, 19), "rib_red_vertic"),
            GameObject(Coord(18, 20), "rib_red_turn_02"),
            GameObject(Coord(19, 20), "rib_red_horiz"),
            GameObject(Coord(20, 20), "rib_red_horiz"),
            GameObject(Coord(21, 20), "rib_red_extr_6"),
        ]
        for gobj_rib in self.gobjs:
            gobj_rib.owner_ribbon = self
            self.ribbons_world.add_game_object(gobj_rib)

    def hard_code_path_2(self):
        self.gobjs = [
            GameObject(Coord(20, 17), "rib_yel_extr_4"),
            GameObject(Coord(20, 18), "rib_yel_vertic"),
            GameObject(Coord(20, 19), "rib_yel_vertic"),
            GameObject(Coord(20, 20), "rib_yel_vertic"),
            GameObject(Coord(20, 21), "rib_yel_vertic"),
            GameObject(Coord(20, 22), "rib_yel_vertic"),
            GameObject(Coord(20, 23), "rib_yel_vertic"),
            GameObject(Coord(20, 24), "rib_yel_extr_0"),
        ]
        for gobj_rib in self.gobjs:
            gobj_rib.owner_ribbon = self
            self.ribbons_world.add_game_object(gobj_rib)

    def hard_code_path_3(self):
        self.gobjs = [
            GameObject(Coord(16, 18), "rib_grn_extr_2"),
            GameObject(Coord(17, 18), "rib_grn_horiz"),
            GameObject(Coord(18, 18), "rib_grn_horiz"),
            GameObject(Coord(19, 18), "rib_grn_horiz"),
            GameObject(Coord(20, 18), "rib_grn_horiz"),
            GameObject(Coord(21, 18), "rib_grn_horiz"),
            GameObject(Coord(22, 18), "rib_grn_horiz"),
            GameObject(Coord(23, 18), "rib_grn_extr_6"),
        ]
        for gobj_rib in self.gobjs:
            gobj_rib.owner_ribbon = self
            self.ribbons_world.add_game_object(gobj_rib)

    def which_extremity(self, gobj_rib):
        """
        Si c'est l'extremité du début, renvoie 1.
        Si c'est celle de la fin, renvoie -1.
        Sinon, renvoie None
        """
        if self.gobjs[0] == gobj_rib:
            return 1
        if self.gobjs[-1] == gobj_rib:
            return -1
        return None

    def iter_follow_ribbon(self, which_extr):
        if which_extr == 1:
            return iter(self.gobjs)
        if which_extr == -1:
            return iter(self.gobjs[::-1])
        return None

    def remove_gobjs(self, gobjs_to_remove):
        self.gobjs = [g for g in self.gobjs if g not in gobjs_to_remove]
        for gobj in gobjs_to_remove:
            self.ribbons_world.remove_game_object(gobj)

    def add_gobjs(self, gobjs_to_add, extremity):
        for gobj in gobjs_to_add:
            sprite_name = "rib_" + self.color + gobj.sprite_name[7:]
            gobj_me = GameObject(gobj.get_coord(), sprite_name)
            gobj_me.owner_ribbon = self
            self.ribbons_world.add_game_object(gobj_me)
            if extremity == 1:
                self.gobjs.insert(0, gobj_me)
            if extremity == -1:
                self.gobjs.append(gobj_me)

    def add_turning_gobj(self, coord, coord_adj_1, coord_adj_2, extremity):
        four_dirs = (
            squarity.dirs.Up,
            squarity.dirs.Right,
            squarity.dirs.Down,
            squarity.dirs.Left,
        )
        adj_dirs = []
        for direction in four_dirs:
            adj_test = coord.clone().move_dir(direction)
            if adj_test == coord_adj_1 or  adj_test == coord_adj_2:
                adj_dirs.append(direction.int_dir)
        adj_dirs.sort()
        sprite_name = f"rib_{self.color}_turn_{adj_dirs[0]}{adj_dirs[1]}"
        print(sprite_name)
        gobj_new = GameObject(coord.clone(), sprite_name)
        gobj_new.owner_ribbon = self
        self.ribbons_world.add_game_object(gobj_new)
        if extremity == 1:
            self.gobjs.insert(0, gobj_new)
        if extremity == -1:
            self.gobjs.append(gobj_new)


class RibbonWorldManager():

    def __init__(self, ribbons_world):
        self.ribbons_world = ribbons_world
        self.ribbons = []
        self.reset_all_swap()

    def reset_all_swap(self):
        self.coord_swap_1 = None
        self.ribbon_swap_1 = None
        self.extr_swap_1 = None
        self.coord_swap_2 = None
        self.ribbon_swap_2 = None
        self.extr_swap_2 = None

    def add_ribbon(self, ribbon):
        self.ribbons.append(ribbon)

    def select_coord_swap(self, coord_swap):
        """
        Renvoie True si il faut effectuer un swap. Sinon renvoie False.
        Pour savoir ce qui est éventuellement sélectionné,
        consultez les variables self.coord_swap_x.
        """
        # TODO LIB: ajouter des hasattr dans le coord.__eq__.
        if self.coord_swap_1 is not None and self.coord_swap_1 == coord_swap:
            # Déselection d'une coordonnée sélectionnée.
            self.reset_all_swap()
            return False
        gobj_ribs = self.ribbons_world.get_game_objects(coord_swap)
        if len(gobj_ribs) != 1:
            return False
        gobj_rib = gobj_ribs[0]
        ribbon = gobj_rib.owner_ribbon
        extr_swap = ribbon.which_extremity(gobj_rib)
        if extr_swap is None:
            return False

        if self.coord_swap_1 is None:
            self.coord_swap_1 = coord_swap.clone()
            self.ribbon_swap_1 = ribbon
            self.extr_swap_1 = extr_swap
            print("Selected a first ribbon extremity.")
            return False
        else:
            self.coord_swap_2 = coord_swap.clone()
            self.ribbon_swap_2 = ribbon
            self.extr_swap_2 = extr_swap
            if self.check_can_swap():
                print("We can swap")
                self.make_swap()
                self.reset_all_swap()
                return True
            else:
                print("We can not swap")
                self.coord_swap_2 = None
                self.ribbon_swap_2 = None
                self.extr_swap_2 = None
                return False

    def _find_first_cross(self, ribbon, extremity):
        gobjs_until_cross = []
        for gobj_rib in ribbon.iter_follow_ribbon(extremity):
            gobjs_until_cross.append(gobj_rib)
            gobj_ribs_cur = self.ribbons_world.get_game_objects(gobj_rib._coord)
            if len(gobj_ribs_cur) == 2 and "turn" not in gobj_rib.sprite_name:
                return gobj_rib, gobjs_until_cross
        return None

    def check_can_swap(self):
        find_result = self._find_first_cross(self.ribbon_swap_1, self.extr_swap_1)
        if find_result is None:
            return False
        gobj_rib_cross_1, gobjs_until_cross_1 = find_result
        find_result = self._find_first_cross(self.ribbon_swap_2, self.extr_swap_2)
        if find_result is None:
            return False

        gobj_rib_cross_2, gobjs_until_cross_2 = find_result
        if gobj_rib_cross_1._coord == gobj_rib_cross_2._coord:
            self.gobjs_until_cross_1 = gobjs_until_cross_1
            self.gobjs_until_cross_2 = gobjs_until_cross_2
            return True
        else:
            return False

    def _compute_new_adj_coords(self, coord_cross, gobjs_until_cross_me, gobjs_until_cross_other):
        sprite_name = gobjs_until_cross_me[-1].sprite_name
        print(sprite_name)
        rib_vertic = "vertic" in sprite_name
        rib_horiz = "horiz" in sprite_name
        if not (rib_vertic ^ rib_horiz):
            raise Exception("Not supposed to happen")
        if rib_horiz:
            coord_rib_adj_1 = coord_cross.clone().move_dir(squarity.dirs.Left)
            if coord_rib_adj_1 == gobjs_until_cross_me[-2]._coord:
                # C'est pas celle là. On prend l'autre.
                coord_rib_adj_1 = coord_cross.clone().move_dir(squarity.dirs.Right)
        if rib_vertic:
            coord_rib_adj_1 = coord_cross.clone().move_dir(squarity.dirs.Up)
            if coord_rib_adj_1 == gobjs_until_cross_me[-2]._coord:
                # C'est pas celle là. On prend l'autre.
                coord_rib_adj_1 = coord_cross.clone().move_dir(squarity.dirs.Down)
        coord_rib_adj_2 = gobjs_until_cross_other[-2].get_coord()
        return coord_rib_adj_1, coord_rib_adj_2

    def make_swap(self):
        # algo: ribbon_1, si vertic: prendre la coord en haut et en bas, puis enlever la 2ème coord du ribbon 1 (car on ne l'a plus)
        #       se rajouter la 2ème coord du ribbon 2 (c'est la nôtre maintenant)
        # etc.
        coord_cross = self.gobjs_until_cross_1[-1].get_coord()
        coord_rib_1_adj_1, coord_rib_1_adj_2 = self._compute_new_adj_coords(
            coord_cross, self.gobjs_until_cross_1, self.gobjs_until_cross_2
        )
        coord_rib_2_adj_1, coord_rib_2_adj_2 = self._compute_new_adj_coords(
            coord_cross, self.gobjs_until_cross_2, self.gobjs_until_cross_1
        )
        print("swap 1", self.ribbon_swap_1.color, coord_rib_1_adj_1, coord_rib_1_adj_2)
        print("swap 2", self.ribbon_swap_2.color, coord_rib_2_adj_1, coord_rib_2_adj_2)
        self.ribbon_swap_1.remove_gobjs(self.gobjs_until_cross_1)
        self.ribbon_swap_2.remove_gobjs(self.gobjs_until_cross_2)
        self.ribbon_swap_1.add_turning_gobj(coord_cross, coord_rib_1_adj_1, coord_rib_1_adj_2, self.extr_swap_1)
        self.ribbon_swap_2.add_turning_gobj(coord_cross, coord_rib_2_adj_1, coord_rib_2_adj_2, self.extr_swap_2)
        # On ajoute les morceaux de ribbon en prenant la liste à l'envers,
        # et on ne prend pas le dernier objet de la liste, qui correspond à la cross.
        self.ribbon_swap_1.add_gobjs(self.gobjs_until_cross_2[-2::-1], self.extr_swap_1)
        self.ribbon_swap_2.add_gobjs(self.gobjs_until_cross_1[-2::-1], self.extr_swap_2)


# TODO LIB
def coord_upleft_from_rect(rect):
    return Coord(rect.x, rect.y)


class Hero():

    def __init__(self, layer_hero, view_rect, ribbons_world):
        self.layer_hero = layer_hero
        self.view_rect = view_rect
        self.ribbons_world = ribbons_world
        self.gobj_hero = GameObject(Coord(0, 0), "hero")
        self.coord_hero_world = Coord(24, 23)

    def render_hero(self):
        view_corner = coord_upleft_from_rect(self.view_rect)
        # TODO LIB: reverse a coord, you dumb!
        view_corner.x = -view_corner.x
        view_corner.y = -view_corner.y
        if self.view_rect.in_bounds(self.coord_hero_world):
            new_coord_hero = self.coord_hero_world.clone().move_by_vect(view_corner)
            self.gobj_hero.move_to(new_coord_hero, transition_delay=0)
            if not self.gobj_hero.layer_owner:
                self.layer_hero.add_game_object(self.gobj_hero)
        else:
            if self.gobj_hero.layer_owner:
                self.layer_hero.remove_game_object(self.gobj_hero)

    def find_path(self, dest):
        """Good old pathfinding"""
        distances = {}
        nexts = [(self.coord_hero_world, 0)]
        while nexts and dest not in distances:
            cur_coord, cur_dist = nexts.pop(0)
            if cur_coord not in distances:
                cur_tile = self.ribbons_world.get_tile(cur_coord)
                if not cur_tile.game_objects or cur_coord == dest:
                    distances[cur_coord] = cur_dist
                    for adj_tile in cur_tile.adjacencies[::2]:
                        if adj_tile is not None:
                            nexts.append((adj_tile._coord, cur_dist + 1))

        if dest not in distances:
            return None
        path = [dest]
        cur_coord = dest
        cur_dist = distances[dest]
        while cur_dist:
            cur_tile = self.ribbons_world.get_tile(cur_coord)
            for adj_tile in cur_tile.adjacencies[::2]:
                if adj_tile is not None and distances.get(adj_tile._coord) == cur_dist - 1:
                    cur_coord = adj_tile._coord
                    cur_dist -= 1
                    path.append(cur_coord)
                    break
        return path[::-1]


class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.ribbons_world = squarity.Layer(self, WORLD_WIDTH, WORLD_HEIGHT)
        self.ribbons_view = squarity.Layer(self, self.w, self.h)
        self.layers.append(self.ribbons_view)
        self.ribbon_world_manager = RibbonWorldManager(self.ribbons_world)
        self.view_rect = squarity.Rect(14, 14, self.w, self.h)

        rect_background = squarity.Rect(1, 1, self.w-2, self.h-2)
        for c in squarity.Sequencer.iter_on_rect(rect_background):
            self.layer_main.add_game_object(GameObject(c, "background"))

        rib_1 = Ribbon(self.ribbons_world, "red")
        rib_1.hard_code_path_1()
        self.ribbon_world_manager.add_ribbon(rib_1)
        rib_2 = Ribbon(self.ribbons_world, "yel")
        rib_2.hard_code_path_2()
        self.ribbon_world_manager.add_ribbon(rib_2)
        rib_3 = Ribbon(self.ribbons_world, "grn")
        rib_3.hard_code_path_3()
        self.ribbon_world_manager.add_ribbon(rib_3)

        self.layer_hero = squarity.Layer(self, self.w, self.h)
        self.layers.append(self.layer_hero)
        self.hero = Hero(self.layer_hero, self.view_rect, self.ribbons_world)
        self.layer_ui = squarity.Layer(self, self.w, self.h, False)
        self.layers.append(self.layer_ui)

        self.render_world()

    def render_world(self):
        view_corner_x = self.view_rect.x
        view_corner_y = self.view_rect.y
        c_view = Coord(0, 0)
        for c_world in squarity.Sequencer.iter_on_rect(self.view_rect):
            c_view.x = c_world.x - view_corner_x
            c_view.y = c_world.y - view_corner_y
            self.ribbons_view.remove_at_coord(c_view)
            for gobj_world in self.ribbons_world.get_game_objects(c_world):
                gobj_view = GameObject(c_view, gobj_world.sprite_name)
                self.ribbons_view.add_game_object(gobj_view)
        self.hero.render_hero()

    def on_button_direction(self, direction):
        # TODO LIB : appliquer un vecteur sur un rect pour bouger son corner upleft.
        dx, dy = direction.vector
        self.view_rect.x += dx
        self.view_rect.y += dy
        self.render_world()

    def on_click(self, coord):
        # TODO : fonctions spécifiques world <-> view
        world_coord = Coord(
            self.view_rect.x + coord.x,
            self.view_rect.y + coord.y
        )
        if self.ribbon_world_manager.select_coord_swap(world_coord):
            self.render_world()
        # TODO debug test
        else:
            print(self.hero.find_path(world_coord))


