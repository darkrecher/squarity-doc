# https://i.postimg.cc/155hbHMf/unstable-isotope.png

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
Qu'est-ce qu'on va bien pouvoir faire avec ça ?

un jeu genre Aqua Splash (sur KadoKado). Le truc avec les boules d'eau. Sauf que ce sera des isotopes instables.
"""

import random

GAME_SIZE_W = 7
GAME_SIZE_H = 7

DIR_INT_FROM_STR = {
    "U": 0,
    "R": 2,
    "D": 4,
    "L": 6,
}


class MovingNeutron:
    def __init__(self, direction, step):
        self.direction = direction
        self.step = step
        self.has_moved = False

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
        # TODO : test à l'arrache :
        if y == 3:
            if x == 2:
                self.nb_neutron = 2
                self.moving_neutrons.append(MovingNeutron(0, 2))
                self.moving_neutrons.append(MovingNeutron(2, 2))
                self.moving_neutrons.append(MovingNeutron(4, 2))
                self.moving_neutrons.append(MovingNeutron(6, 2))

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
                isot = random.randint(0, 3)
                new_tile = Tile(x, y, isot)
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

        self.told_msg_no_iso = False

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

    def move_neutrons(self):
        # C'est moche parce que je fais deux fois de suite
        # la triple-boucle pour parcourir tous les neutrons,
        # mais osef.
        for line in self.tiles:
            for tile in line:
                for neutron in tile.moving_neutrons:
                    neutron.has_moved = False

        for line in self.tiles:
            for tile in line:
                copy_neutrons = list(tile.moving_neutrons)
                for neutron in copy_neutrons:
                    self.handle_neutron_move(tile, neutron)

    def export_all_tiles(self):
        tiles_to_export = []
        for y in range(self.h):
            line_to_export = [tile.get_gamobjs() for tile in self.tiles[y]]
            tiles_to_export.append(line_to_export)

        x_cursor = self.tile_cursor.x
        y_cursor = self.tile_cursor.y
        gamobjs_cursor = tiles_to_export[y_cursor][x_cursor]
        gamobjs_cursor.append(self.gamobj_cursor)
        return tiles_to_export

    def on_game_event(self, event_name):

        move_dir = DIR_INT_FROM_STR.get(event_name)
        if move_dir is not None:
            new_tile_cursor = self.tile_cursor.adjacencies[move_dir]
            if new_tile_cursor is None:
                return
            if self.taking_isotope:
                if new_tile_cursor.nb_neutron:
                    if new_tile_cursor.nb_neutron > 3:
                        return
                    self.taking_isotope = False
                    self.gamobj_cursor = "cursor_normal"
                nb_iso_to_move = self.tile_cursor.nb_neutron
                self.tile_cursor.nb_neutron = 0
                new_tile_cursor.nb_neutron += nb_iso_to_move
            self.tile_cursor = new_tile_cursor
            return

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
            return

        # TODO test
        if event_name == "action_2":
            self.move_neutrons()
