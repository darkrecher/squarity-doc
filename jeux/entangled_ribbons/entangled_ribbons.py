# https://i.ibb.co/G30yFzv/ent-rib-tileset.png

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
      "rib_red_horiz_below": [320, 32],
      "rib_red_vertic_below": [352, 32],
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
      "rib_yel_horiz_below": [320, 128],
      "rib_yel_vertic_below": [352, 128],
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
      "rib_grn_horiz_below": [320, 64],
      "rib_grn_vertic_below": [352, 64],
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
      "rib_blu_horiz_below": [320, 96],
      "rib_blu_vertic_below": [352, 96],

      "rib_glow_horiz": [0, 160],
      "rib_glow_vertic": [32, 160],
      "rib_glow_turn_06": [64, 160],
      "rib_glow_turn_02": [96, 160],
      "rib_glow_turn_24": [128, 160],
      "rib_glow_turn_46": [160, 160],
      "rib_glow_extr_6": [192, 160],
      "rib_glow_extr_0": [224, 160],
      "rib_glow_extr_4": [256, 160],
      "rib_glow_extr_2": [288, 160],

      "icon_grab": [32, 0],
      "icon_swap": [64, 0],
      "hero": [96, 0],
      "black": [128, 0],
      "background": [0, 0]
    }
  }
"""

"""
tuto:

click anywhere in the game,
then click on the red ribbon next to me to grab it.

(You must click on a ribbon extremity)

Great! Now click the hand icon on the upper left corner
to activate the swap mode.

Click the green ribbon, then the yellow ribbon
to swap and un-entangle them.

(I can swap ribbons only if they cross just after
the two extremities you clicked)

(I can't reach that extremity)

Click the upper left icon to go back to grab mode
and remove the two ribbons.

[story dialogues]

I learned laser eyes, I can now see very far!
You can scroll the game area, with arrow keys or arrow icons.

I learned telekinesis! I can now swap ribbons
even if I can't reach them.

I learned levitation!
I can now grab a ribbon if it is above the others.
Try it with the blue ribbon next to me.

I learned planar shift! Click on a ribbon cross to magically
reverse it. It will help to put any ribbon above.

"""


"""
Bug dans le moteur, avec cette version du code du jeu.

Au moins, c'est reproductible:
aller tout à droite jusqu'à enlever le héros, puis refaire un dernier petit coup à droite.
Cliquer en haut à droite. (ça marche).
Aller tout à gauche au maximum. Puis cliquer en bas à gauche.
On réessaye une dernière fois.
Oui c'est ça. (Et il y a sûrement des moyens plus simple de reproduire.
Mais au moins il y a ça).
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
        self.gobjs_highlight = []
        self.highlight_index = None
        self.highlight_step = None
        self.highlighting = False

    def hard_code_path_1(self):
        self.gobjs = [
            GameObject(Coord(18, 17), "rib_red_extr_4"),
            GameObject(Coord(18, 18), "rib_red_vertic"),
            GameObject(Coord(18, 19), "rib_red_vertic"),
            GameObject(Coord(18, 20), "rib_red_turn_02"),
            GameObject(Coord(19, 20), "rib_red_horiz"),
            GameObject(Coord(20, 20), "rib_red_horiz_below"),
            GameObject(Coord(21, 20), "rib_red_extr_6"),
        ]
        for gobj_rib in self.gobjs:
            gobj_rib.owner_ribbon = self
            self.ribbons_world.add_game_object(gobj_rib)

    def hard_code_path_2(self):
        self.gobjs = [
            GameObject(Coord(23, 16), "rib_yel_extr_6"),
            GameObject(Coord(22, 16), "rib_yel_horiz"),
            GameObject(Coord(21, 16), "rib_yel_horiz"),
            GameObject(Coord(20, 16), "rib_yel_turn_24"),
            GameObject(Coord(20, 17), "rib_yel_vertic"),
            GameObject(Coord(20, 18), "rib_yel_vertic_below"),
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
            GameObject(Coord(18, 18), "rib_grn_horiz_below"),
            GameObject(Coord(19, 18), "rib_grn_horiz"),
            GameObject(Coord(20, 18), "rib_grn_horiz"),
            GameObject(Coord(21, 18), "rib_grn_horiz"),
            GameObject(Coord(22, 18), "rib_grn_horiz"),
            GameObject(Coord(23, 18), "rib_grn_extr_6"),
        ]
        for gobj_rib in self.gobjs:
            gobj_rib.owner_ribbon = self
            self.ribbons_world.add_game_object(gobj_rib)

    def hard_code_path_4(self):
        self.gobjs = [
            GameObject(Coord(16, 26), "rib_blu_extr_2"),
            GameObject(Coord(17, 26), "rib_blu_horiz"),
            GameObject(Coord(18, 26), "rib_blu_horiz"),
            GameObject(Coord(19, 26), "rib_blu_turn_46"),
            GameObject(Coord(19, 27), "rib_blu_turn_06"),
            GameObject(Coord(18, 27), "rib_blu_horiz"),
            GameObject(Coord(17, 27), "rib_blu_turn_02"),
            GameObject(Coord(17, 26), "rib_blu_vertic_below"),
            GameObject(Coord(17, 25), "rib_blu_vertic"),
            GameObject(Coord(17, 24), "rib_blu_extr_4"),
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

    def remove_gobjs(self, gobjs_to_remove=None):
        if gobjs_to_remove is None:
            gobjs_to_remove = self.gobjs
            self.gobjs = []
        else:
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

    def check_can_be_grabbed(self, ribbons_world, with_levitate):
        for gobj_rib in self.gobjs:
            gobj_ribs_cur = ribbons_world.get_game_objects(gobj_rib._coord)
            if len(gobj_ribs_cur) == 2 and "turn" not in gobj_rib.sprite_name:
                if with_levitate:
                    if "below" in gobj_rib.sprite_name:
                        return False
                else:
                    return False
        return True

    def start_highlight(self, which_extremity):
        self.highlight_step = which_extremity
        self.highlighting = True
        if self.highlight_step == 1:
            self.highlight_index = 0
        elif self.highlight_step == -1:
            self.highlight_index = len(self.gobjs) - 1
        else:
            raise Exception("Not supposed to happen.")

    def highlight_next_gobjs(self, view_rect):
        """
        Renvoie None, ou un nouveau game object, qui devra être ajouté dans l'UI.
        """
        if not (0 <= self.highlight_index < len(self.gobjs)):
            self.highlighting = False
            return None
        gobj = self.gobjs[self.highlight_index]
        highlight_sprite_name = "rib_glow" + gobj.sprite_name[7:]
        if highlight_sprite_name.endswith("below"):
            highlight_sprite_name = highlight_sprite_name[:-6]
        coord_in_view = gobj.get_coord().move_by_vect(x=-view_rect.x, y=-view_rect.y)
        gobj_highlight = GameObject(coord_in_view, highlight_sprite_name)
        self.gobjs_highlight.append(gobj_highlight)
        self.highlight_index += self.highlight_step
        return gobj_highlight

    def unhighlight_next_gobjs(self):
        """
        Renvoie None, ou un tuple de deux éléments:
         - un game object existant, qui devra être enlevé de l'UI.
         - None, ou bien les coordonnée d'un un autre game object existant,
           dont le sprite aura été modifié.
        """
        if not self.gobjs_highlight:
            return None
        if len(self.gobjs_highlight) <= 2:
            gobj = self.gobjs_highlight.pop()
            return gobj, None
        gobj_0 = self.gobjs_highlight.pop()
        gobj_1 = self.gobjs_highlight[-1]
        coord_1 = gobj_1._coord
        coord_2 = self.gobjs_highlight[-2]._coord
        vector_1_to_2 = (coord_2.x - coord_1.x, coord_2.y - coord_1.y)
        for direc in squarity.dirs.as_list[::2]:
            if direc.vector == vector_1_to_2:
                if int(direc) in (0, 2, 4, 6):
                    gobj_1.sprite_name = "rib_glow_extr_" + str(int(direc))
                    return gobj_0, coord_1
        return gobj_0, None


class RibbonWorldManager():

    def __init__(self, ribbons_world):
        self.ribbons_world = ribbons_world
        self.ribbons = []
        self.reset_all_swap()

    def reset_all_swap(self):
        self.hide_temp_coord_swap = False
        self.coord_swap_1 = None
        self.ribbon_swap_1 = None
        self.extr_swap_1 = None
        self.coord_swap_2 = None
        self.ribbon_swap_2 = None
        self.extr_swap_2 = None

    def add_ribbon(self, ribbon):
        self.ribbons.append(ribbon)

    def get_coord_swap_for_ui(self, view_rect):
        if self.coord_swap_1 is None:
            return None
        if self.hide_temp_coord_swap:
            return None
        if not view_rect.in_bounds(self.coord_swap_1):
            return None
        if view_rect.on_border(self.coord_swap_1):
            return None
        return self.coord_swap_1

    def get_ribbon_and_extremity(self, coord):
        gobj_ribs = self.ribbons_world.get_game_objects(coord)
        if len(gobj_ribs) != 1:
            return None
        gobj_rib = gobj_ribs[0]
        ribbon = gobj_rib.owner_ribbon
        extremity = ribbon.which_extremity(gobj_rib)
        if extremity is None:
            return None
        return ribbon, extremity

    def remove_ribbon(self, ribbon):
        self.ribbons.remove(ribbon)

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

        rib_and_extr = self.get_ribbon_and_extremity(coord_swap)
        if rib_and_extr is None:
            return False
        ribbon, extr_swap = rib_and_extr

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
                self.hide_temp_coord_swap = True
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
        if gobj_rib_cross_1 == gobj_rib_cross_2:
            return False
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
        self.layer_hero.add_game_object(self.gobj_hero)
        self.gobj_hero.plock_transi = squarity.PlayerLockTransi.LOCK
        self.coord_hero_world = Coord(24, 23)

    def render_hero(self):
        view_corner = coord_upleft_from_rect(self.view_rect)
        # TODO LIB: reverse a coord, you dumb!
        view_corner.x = -view_corner.x
        view_corner.y = -view_corner.y
        if self.view_rect.in_bounds(self.coord_hero_world):
            new_coord_hero = self.coord_hero_world.clone().move_by_vect(view_corner)
        else:
            new_coord_hero = Coord(0, 0)
        self.gobj_hero.move_to(new_coord_hero, transition_delay=0)

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

    def record_transitions_in_view(self, path):
        coords_in_view = []
        cur_delay = 50
        total_delay = 0
        for world_coord in path[::-1]:
            if self.view_rect.in_bounds(world_coord):
                coords_in_view.append(world_coord)
            else:
                cur_delay = 0
                break
        if not self.view_rect.in_bounds(self.coord_hero_world):
            cur_delay = 0

        if not coords_in_view:
            return
        coords_in_view = coords_in_view[::-1]

        path_steps = []
        for world_coord in coords_in_view:
            view_coord = Coord(
                world_coord.x - self.view_rect.x,
                world_coord.y - self.view_rect.y
            )
            path_steps.append((cur_delay, view_coord))
            total_delay += cur_delay
            cur_delay = 50
        self.gobj_hero.add_transition(
            squarity.TransitionSteps("coord", path_steps)
        )
        return total_delay


class Powers():
    SWAP_EVERYWHERE = 1
    SCROLL = 2
    GRAB_EVERYWHERE = 3
    GRAB_ABOVE = 4
    SWAP_CROSS = 5

    def __init__(self):
        self.power_availability = {
            pow_id: False for pow_id in range(6)
        }

    def grant_power(self, pow_id):
        self.power_availability[pow_id] = True

    def has_power(self, pow_id):
        return self.power_availability[pow_id]


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
        rib_4 = Ribbon(self.ribbons_world, "blu")
        rib_4.hard_code_path_4()
        self.ribbon_world_manager.add_ribbon(rib_4)

        self.layer_hero = squarity.Layer(self, self.w, self.h)
        self.layers.append(self.layer_hero)
        self.hero = Hero(self.layer_hero, self.view_rect, self.ribbons_world)
        self.interaction_mode = "swap"
        self.layer_ui = squarity.Layer(self, self.w, self.h, False)
        # TODO lib. iterateur sur les bords d'un squarity.Rect. (ça itère des Coord).
        for x in range(self.w):
            self.layer_ui.add_game_object(
                GameObject(Coord(x, 0), "black")
            )
            self.layer_ui.add_game_object(
                GameObject(Coord(x, self.h - 1), "black")
            )
        for y in range(1, self.h - 1):
            self.layer_ui.add_game_object(
                GameObject(Coord(0, y), "black")
            )
            self.layer_ui.add_game_object(
                GameObject(Coord(self.w - 1, y), "black")
            )
        self.ui_gobj_swap = GameObject(Coord(0, 0), "icon_swap")
        self.layers.append(self.layer_ui)
        self.ribbon_grabbing = None

        self.powers = Powers()
        # self.powers.grant_power(Powers.SWAP_EVERYWHERE)
        # self.powers.grant_power(Powers.GRAB_EVERYWHERE)
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

        ui_coord_swap = self.ribbon_world_manager.get_coord_swap_for_ui(self.view_rect)
        if ui_coord_swap is None:
            if self.ui_gobj_swap.layer_owner is not None:
                self.layer_ui.remove_game_object(self.ui_gobj_swap)
        else:
            coord_swap_view = Coord(
                ui_coord_swap.x - self.view_rect.x,
                ui_coord_swap.y - self.view_rect.y,
            )
            self.ui_gobj_swap.move_to(coord_swap_view)
            if self.ui_gobj_swap.layer_owner is None:
                self.layer_ui.add_game_object(self.ui_gobj_swap)

    def on_button_direction(self, direction):
        # TODO LIB : appliquer un vecteur sur un rect pour bouger son corner upleft.
        temp_view_corner = coord_upleft_from_rect(self.view_rect)
        temp_view_corner.move_dir(direction)
        if all(
            (
                temp_view_corner.x >= 0,
                temp_view_corner.y >= 0,
                temp_view_corner.x + self.view_rect.w < WORLD_WIDTH,
                temp_view_corner.y + self.view_rect.h < WORLD_HEIGHT,
            )
        ):
            self.view_rect.x = temp_view_corner.x
            self.view_rect.y = temp_view_corner.y
            self.render_world()
        else:
            print("You are at the world limits.")

    def on_button_action(self, action_name):
        # TODO : si on a les 2 pouvoirs "EVERYWHERE",
        # et que l'on clique sur un ruban grabbable, alors ça le grab tout de suite,
        # même si on est en mode swap.
        # C'est un pouvoir supplémentaire: l'auto-grab. "le pouvoir de prescience".
        if self.interaction_mode == "swap":
            self.interaction_mode = "grab"
        else:
            self.interaction_mode = "swap"
        print(self.interaction_mode)

    def on_click(self, coord):
        if self.rect.on_border(coord):
            return

        # TODO : fonctions spécifiques world <-> view
        world_coord = Coord(
            self.view_rect.x + coord.x,
            self.view_rect.y + coord.y
        )
        if not self.ribbon_world_manager.ribbons_world.get_game_objects(world_coord):
            return self.on_click_move(world_coord)
        if self.interaction_mode == "swap":
            return self.on_click_swap(world_coord)
        elif self.interaction_mode == "grab":
            return self.on_click_grab(world_coord)

    def on_click_move(self, world_coord):
        path_to_dest = self.hero.find_path(world_coord)
        if path_to_dest is None:
            print("I can't reach this place.")
            return
        if len(path_to_dest) > 1:
            total_delay = self.hero.record_transitions_in_view(path_to_dest[1:])
            self.hero.coord_hero_world = path_to_dest[-1]
            event_res = squarity.EventResult()
            event_res.plocks_custom.append("move_anim")
            event_res.add_delayed_callback(
                squarity.DelayedCallBack(total_delay, self.callback_hero_arrived)
            )
            return event_res

    def callback_hero_arrived(self):
        event_res = squarity.EventResult()
        event_res.punlocks_custom.append("move_anim")
        return event_res

    def on_click_grab(self, world_coord):

        if self.powers.has_power(Powers.GRAB_EVERYWHERE):
            self.hero.coord_to_grab = world_coord
            return self.callback_hero_try_grab()

        path_to_grab = self.hero.find_path(world_coord)
        if path_to_grab is None:
            print("I can't reach this ribbon extremity.")
            return
        if len(path_to_grab) > 2:
            total_delay = self.hero.record_transitions_in_view(path_to_grab[1:-1])
            self.hero.coord_hero_world = path_to_grab[-2]
            self.hero.coord_to_grab = world_coord
            event_res = squarity.EventResult()
            event_res.plocks_custom.append("grab_anim")
            event_res.add_delayed_callback(
                squarity.DelayedCallBack(total_delay, self.callback_hero_try_grab)
            )
            return event_res
        else:
            self.hero.coord_to_grab = world_coord
            return self.callback_hero_try_grab()

    def callback_hero_try_grab(self):
        world_coord = self.hero.coord_to_grab
        rib_and_extr = self.ribbon_world_manager.get_ribbon_and_extremity(world_coord)
        if rib_and_extr is None:
            # Raaaah. J'ai ce truc là partout. C'est vraiment horrible ce code.
            event_res = squarity.EventResult()
            event_res.punlocks_custom.append("grab_anim")
            return event_res
        ribbon, extremity = rib_and_extr
        if not ribbon.check_can_be_grabbed(self.ribbons_world, False):
            print("This ribbon can't be grabbed.")
            event_res = squarity.EventResult()
            event_res.punlocks_custom.append("grab_anim")
            return event_res

        self.ribbon_grabbing = ribbon
        self.ribbon_grabbing.start_highlight(extremity)
        event_res = squarity.EventResult()
        event_res.plocks_custom.append("grab_anim")
        event_res.add_delayed_callback(
            squarity.DelayedCallBack(50, self.callback_grabbing_ribbon)
        )
        return event_res

    def callback_grabbing_ribbon(self):

        if self.ribbon_grabbing.highlighting:
            gobj_to_add = self.ribbon_grabbing.highlight_next_gobjs(self.view_rect)
            if gobj_to_add is None:
                self.ribbon_grabbing.remove_gobjs()
                self.render_world()
                event_res = squarity.EventResult()
                event_res.add_delayed_callback(
                    squarity.DelayedCallBack(50, self.callback_grabbing_ribbon)
                )
                return event_res
            else:
                if self.rect.in_bounds(gobj_to_add._coord) and not self.rect.on_border(gobj_to_add._coord):
                    self.layer_ui.add_game_object(gobj_to_add)
                    delay = 50
                else:
                    delay = 5
                event_res = squarity.EventResult()
                event_res.add_delayed_callback(
                    squarity.DelayedCallBack(delay, self.callback_grabbing_ribbon)
                )
                return event_res

        else:

            unhighlight_result = self.ribbon_grabbing.unhighlight_next_gobjs()
            if unhighlight_result is None:
                self.ribbon_world_manager.remove_ribbon(self.ribbon_grabbing)
                self.ribbon_grabbing = None
                self.render_world()
                event_res = squarity.EventResult()
                event_res.punlocks_custom.append("grab_anim")
                return event_res
            else:
                gobj_to_remove, coord_change = unhighlight_result
                delay = 5
                if gobj_to_remove.layer_owner is not None:
                    delay = 50
                    self.layer_ui.remove_game_object(gobj_to_remove)
                if coord_change is not None:
                    if self.rect.in_bounds(coord_change):
                        delay = 50
                event_res = squarity.EventResult()
                event_res.add_delayed_callback(
                    squarity.DelayedCallBack(delay, self.callback_grabbing_ribbon)
                )
                return event_res

    def on_click_swap(self, world_coord):

        if self.powers.has_power(Powers.SWAP_EVERYWHERE):
            can_swap = self.ribbon_world_manager.select_coord_swap(world_coord)
            if can_swap:
                self.ribbon_world_manager.make_swap()
                self.ribbon_world_manager.reset_all_swap()
            self.render_world()
            return

        path_to_swap = self.hero.find_path(world_coord)
        if path_to_swap is None:
            print("I can't reach this ribbon extremity.")
            return
        if len(path_to_swap) > 2:
            total_delay = self.hero.record_transitions_in_view(path_to_swap[1:-1])
            self.hero.coord_hero_world = path_to_swap[-2]
            self.hero.coord_to_swap = world_coord
            # Ça c'est dégueux, mais osef:
            if self.ribbon_world_manager.coord_swap_1 is not None:
                total_delay += 200
            # TODO LIB : callback when all the current transitions, or all the blocking transitions, are finished.
            event_res = squarity.EventResult()
            event_res.plocks_custom.append("swap_anim")
            event_res.add_delayed_callback(
                squarity.DelayedCallBack(total_delay, self.callback_hero_try_swap)
            )
            return event_res
        else:
            self.hero.coord_to_swap = world_coord
            return self.callback_hero_try_swap()

    def callback_hero_try_swap(self):
        print("hero arrived")
        # TODO: bug if we select two extremities of the same ribbon, with a single cross in the middle.
        can_swap = self.ribbon_world_manager.select_coord_swap(self.hero.coord_to_swap)
        self.render_world()
        if can_swap:
            event_res = squarity.EventResult()
            event_res.plocks_custom.append("swap_anim")
            event_res.add_delayed_callback(
                squarity.DelayedCallBack(200, self.callback_make_swap)
            )
            return event_res
        else:
            event_res = squarity.EventResult()
            event_res.punlocks_custom.append("swap_anim")
            return event_res

    def callback_make_swap(self):
        self.ribbon_world_manager.make_swap()
        self.ribbon_world_manager.reset_all_swap()
        self.render_world()
        event_res = squarity.EventResult()
        event_res.punlocks_custom.append("swap_anim")
        return event_res

