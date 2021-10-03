# https://i.postimg.cc/155hbHMf/unstable-isotope.png

# https://github.com/darkrecher/squarity-doc/blob/master/jeux/ludum_unstable/unstable_isotopes.py

"""
{
  "game_area": {
    "nb_tile_width": 7,
    "nb_tile_height": 7
  },
  "tile_size": 64,

  "img_coords": {
    "cursor_normal": [0, 0],
    "cursor_select_01": [64, 0],
    "cursor_select_02": [64, 0],
    "cursor_select_03": [64, 0],
    "background": [128, 0],
    "isot_01": [0, 64],
    "isot_02": [64, 64],
    "isot_03": [128, 64],
    "isot_04": [192, 64],
    "isot_05": [256, 64],
    "isot_06": [0, 128],

    "neutron_up_00": [192, 201],
    "neutron_up_01": [192, 227],
    "neutron_up_02": [192, 242],
    "neutron_right_00": [44, 192],
    "neutron_right_01": [28, 192],
    "neutron_right_02": [12, 192],
    "neutron_down_00": [256, 242],
    "neutron_down_01": [256, 227],
    "neutron_down_02": [256, 201],
    "neutron_left_00": [12, 256],
    "neutron_left_01": [28, 256],
    "neutron_left_02": [44, 256],


    "blorp": [0, 0]
  }
}
"""

"""
Le thème c'est "Unstable".

un jeu genre Aqua Splash (sur KadoKado). Le truc avec les boules d'eau. Sauf que ce sera des isotopes instables.

Gestion de l'énergie.
Un déplacement d'un neutron coûte un point d'énergie, puis 2, puis 3, etc.
L'accumulation se remet à zéro lorsqu'on casse un isotope de 4 neutrons.

Ça s'applique aussi pour les déplacements d'isotope ayant plusieurs neutrons.
Par exemple, je déplace un isotope de 3 neutrons d'une seule case. Ça me coûte 1+2+3 = 6 énergies.
Je le redéplace d'une autre case, ça me coûte 4+5+6 = 15 énergies supplémentaires.

On gagne de l'énergie avec les réactions en chaînes. La première explosion d'un isotope rapporte 1, la suivante 2, etc.

Lorsqu'on termine un niveau, on gagne autant d'énergie que le numéro du niveau. +1 au niveau 1, +2 au niveau 2, etc.

Et un bonus de +10 énergies lorsqu'on finit vide complètement un niveau.
"""

START_ENERGY = 20

import random
import json

GAME_SIZE_W = 7
GAME_SIZE_H = 7

DIR_INT_FROM_STR = {
    "U": 0,
    "R": 2,
    "D": 4,
    "L": 6,
}


class MovingNeutron:
    def __init__(self, direction, step, has_moved):
        self.direction = direction
        self.step = step
        self.has_moved = has_moved

    def __str__(self):
        str_dirs = {
            0: "up",
            2: "right",
            4: "down",
            6: "left",
        }
        my_dir = str_dirs[self.direction]
        return f"neutron_{my_dir}_0{self.step}"


class Tile:
    def __init__(self, x, y, nb_neutron):
        self.x = x
        self.y = y
        self.nb_neutron = nb_neutron
        self.moving_neutrons = []
        self.adjacencies = None

    def get_gamobjs(self):
        if self.nb_neutron > 6:
            raise Exception(f"Trop d'isotope. Tile : {self.x}, {self.y}")
        result_gamobjs = ["background"]
        if self.nb_neutron:
            result_gamobjs.append(f"isot_0{self.nb_neutron}")
        result_gamobjs += [str(neutron) for neutron in self.moving_neutrons]
        return result_gamobjs


class GameModel:
    def __init__(self):
        self.w = GAME_SIZE_W
        self.h = GAME_SIZE_H
        self.tiles = []
        for y in range(self.h):
            line = []
            for x in range(self.w):
                new_tile = Tile(x, y, 0)
                line.append(new_tile)
            self.tiles.append(line)

        for y in range(self.h):
            for x in range(self.w):
                self.tiles[y][x].adjacencies = self._make_adjacencies(x, y)

        x_cursor = 0
        y_cursor = 0
        self.tile_cursor = self.tiles[y_cursor][x_cursor]
        self.taking_isotope = False
        self.gamobj_cursor = "cursor_normal"
        self.doing_chain_reaction = False
        self.chain_reaction_duration = 0
        self.told_msg_no_iso = False
        self.level = 0
        self.energy = START_ENERGY
        self.cumulative_cost = 0
        self.cumulative_isotope_break = 0
        self.spawn_isotopes()

    def _make_adjacencies(self, x, y):
        """
        Renvoie les tiles adjacentes à la tile située aux coordonnées x, y.
        On renvoie toujours une liste de 8 éléments (les 8 directions), mais certains éléments
        peuvent être None, si les coordonnées x, y sont sur un bord de l'aire de jeu.
        """
        adjacencies = (
            self.tiles[y - 1][x] if 0 <= y - 1 else None,
            self.tiles[y - 1][x + 1] if 0 <= y - 1 and x + 1 < self.w else None,
            self.tiles[y][x + 1] if x + 1 < self.w else None,
            self.tiles[y + 1][x + 1] if y + 1 < self.h and x + 1 < self.w else None,
            self.tiles[y + 1][x] if y + 1 < self.h else None,
            self.tiles[y + 1][x - 1] if y + 1 < self.h and 0 <= x - 1 else None,
            self.tiles[y][x - 1] if 0 <= x - 1 else None,
            self.tiles[y - 1][x - 1] if 0 <= y - 1 and 0 <= x - 1 else None,
        )
        return adjacencies

    def compute_delayed_action_chain_react(self):
        # On diminue progressivement le delay. Sinon c'est relou d'attendre que les neutrons se déplacent et etc.
        delay_ms = 150 - self.chain_reaction_duration * 5
        delay_ms = max(delay_ms, 80)
        delayed_action_chain_reaction = {
            "delayed_actions": [{"name": "chain_reaction", "delay_ms": delay_ms}]
        }
        return json.dumps(delayed_action_chain_reaction)

    def handle_neutron_move(self, initial_tile, neutron):
        if neutron.has_moved:
            return
        neutron.has_moved = True

        # Si le neutron arrive sur un isotope possédant
        # plus de 5 neutrons, il va passer au travers.
        # Mais c'est pas censé arriver, parce que dès que c'est 4 ou plus ça éclate.
        if neutron.step == 0 and 0 < initial_tile.nb_neutron <= 5:
            # Le neutron se colle à l'isotope sur lequel il se trouve.
            initial_tile.moving_neutrons.remove(neutron)
            initial_tile.nb_neutron += 1
            return

        if neutron.step < 2:
            neutron.step += 1
            return

        initial_tile.moving_neutrons.remove(neutron)
        neutron.step = 0
        next_tile = initial_tile.adjacencies[neutron.direction]
        if next_tile is None:
            # Le neutron sort par un bord de l'aire de jeu.
            return
        # Le neutron avance d'une tile dans sa direction.
        next_tile.moving_neutrons.append(neutron)

    def process_chain_reaction(self):

        did_something = False

        # C'est moche parce que je fais deux fois de suite
        # la triple-boucle pour parcourir tous les neutrons,
        # mais osef.
        for line in self.tiles:
            for tile in line:
                for neutron in tile.moving_neutrons:
                    neutron.has_moved = False

        # Séparation des isotopes ayant 4 neutrons ou plus.
        for line in self.tiles:
            for tile in line:
                if tile.nb_neutron >= 4:
                    tile.nb_neutron -= 4
                    new_neutrons = [
                        MovingNeutron(0, 2, True),
                        MovingNeutron(2, 2, True),
                        MovingNeutron(4, 2, True),
                        MovingNeutron(6, 2, True),
                    ]
                    tile.moving_neutrons.extend(new_neutrons)
                    self.cumulative_isotope_break += 1
                    self.energy += int(self.cumulative_isotope_break ** 0.25)
                    # print("TODO paf", self.energy, self.cumulative_isotope_break, )
                    did_something = True

        for line in self.tiles:
            for tile in line:
                copy_neutrons = list(tile.moving_neutrons)
                for neutron in copy_neutrons:
                    self.handle_neutron_move(tile, neutron)
                    did_something = True

        return did_something

    def spawn_isotopes(self):
        """
        Rajoute des isotopes dans l'aire de jeu, en fonction de self.level.
        Plus le niveau est bas, plus c'est facile, plus on ajoute des isotopes ayant déjà 3 neutrons.
        Plus le niveau est haut, plus on ajoute des isotopes n'ayant que 1 neutron.
        """
        nb_total_tiles = self.w * self.h
        nb_tile_iso_3 = nb_total_tiles // 3 - self.level * 4
        nb_tile_iso_3 = max(1, nb_tile_iso_3)
        nb_tile_iso_2 = nb_total_tiles // 3 - self.level * 2
        nb_tile_iso_2 = max(2, nb_tile_iso_2)
        nb_tile_iso_1 = min(self.level, nb_total_tiles // 3)

        nb_tile_iso_3 += random.randint(0, 6)
        nb_tile_iso_2 += random.randint(0, 4)
        nb_tile_iso_1 += random.randint(0, 2)
        choices_isotopes = (
            [3] * nb_tile_iso_3 + [2] * nb_tile_iso_2 + [1] * nb_tile_iso_1
        )
        random.shuffle(choices_isotopes)
        all_tiles = []
        for line in self.tiles:
            all_tiles.extend(line)
        random.shuffle(all_tiles)

        for tile, iso_type in zip(all_tiles, choices_isotopes):
            # Il peut y avoir déjà des neutrons sur la tile.
            # Par exemple, lorsqu'il en reste des niveaux précédents.
            # Dans ce cas, on passe simplement cette tile. Ça ajoute un petit peu plus d'aléatoiritude au spawnage des isotopes.
            if not tile.nb_neutron:
                tile.nb_neutron = iso_type

    def count_neutrons(self):
        total_neutrons = 0
        for line in self.tiles:
            for tile in line:
                total_neutrons += tile.nb_neutron
        return total_neutrons

    def export_all_tiles(self):
        tiles_to_export = []
        for y in range(self.h):
            line_to_export = [tile.get_gamobjs() for tile in self.tiles[y]]
            tiles_to_export.append(line_to_export)

        if not self.doing_chain_reaction:
            x_cursor = self.tile_cursor.x
            y_cursor = self.tile_cursor.y
            gamobjs_cursor = tiles_to_export[y_cursor][x_cursor]
            gamobjs_cursor.append(self.gamobj_cursor)
        return tiles_to_export

    def pay_energy(self, nb_neutron_to_move):
        if nb_neutron_to_move == 0:
            return True

        cumul_add = 1
        cost = self.cumulative_cost + cumul_add
        if nb_neutron_to_move > 1:
            cumul_add += 1
            cost += self.cumulative_cost + cumul_add
        if nb_neutron_to_move > 2:
            cumul_add += 1
            cost += self.cumulative_cost + cumul_add

        if self.energy >= cost:
            self.energy -= cost
            self.cumulative_cost += cumul_add
            return True
        else:
            # TODO : checker si d'autres mouvements sont possibles.
            # Si non, terminer le jeu.
            print("Not enough energy")
            return False

    def on_game_event(self, event_name):

        if event_name == "chain_reaction":
            continue_chain = self.process_chain_reaction()
            if continue_chain:
                self.chain_reaction_duration += 1
                return self.compute_delayed_action_chain_react()
            else:
                self.doing_chain_reaction = False
                self.chain_reaction_duration = 0
                self.cumulative_isotope_break = 0
                nb_neutron = self.count_neutrons()
                if nb_neutron < 4:
                    self.level += 1
                    print(f"Next level : {self.level}")
                    self.energy += self.level
                    if nb_neutron == 0:
                        # Bonus de 10 si on nettoie complètement l'aire de jeu.
                        self.energy += 10
                    self.spawn_isotopes()
                print("TODO energy :", self.energy)
                return None

        if self.doing_chain_reaction:
            # Il y a une réaction en chaîne en cours.
            # On ne prend en compte aucun input de boutons.
            return None

        move_dir = DIR_INT_FROM_STR.get(event_name)
        if move_dir is not None:
            new_tile_cursor = self.tile_cursor.adjacencies[move_dir]
            if new_tile_cursor is None:
                return None

            if self.taking_isotope:
                if new_tile_cursor.nb_neutron:
                    if new_tile_cursor.nb_neutron > 3:
                        return None
                    self.taking_isotope = False
                    self.gamobj_cursor = "cursor_normal"
                nb_neutron_to_move = self.tile_cursor.nb_neutron
                if not self.pay_energy(nb_neutron_to_move):
                    return None
                self.tile_cursor.nb_neutron = 0
                new_tile_cursor.nb_neutron += nb_neutron_to_move
                if new_tile_cursor.nb_neutron >= 4:
                    self.doing_chain_reaction = True
                    self.cumulative_cost = 0
                print("TODO. energy :", self.energy)
            self.tile_cursor = new_tile_cursor
            if self.doing_chain_reaction:
                return self.compute_delayed_action_chain_react()
            else:
                return None

        if event_name == "action_1":
            if self.taking_isotope:
                self.taking_isotope = False
                self.gamobj_cursor = "cursor_normal"
            else:
                iso_on_cursor = self.tile_cursor.nb_neutron
                if 0 < iso_on_cursor <= 3:
                    self.taking_isotope = True
                    self.gamobj_cursor = f"cursor_select_0{iso_on_cursor}"
                else:
                    if not iso_on_cursor and not self.told_msg_no_iso:
                        print("You must be on a tile containing some isotopes.")
                        self.told_msg_no_iso = True
            return None
