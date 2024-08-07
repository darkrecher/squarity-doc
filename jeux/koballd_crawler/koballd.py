# https://i.ibb.co/VjVQnxQ/koballd-tileset.png
# https://gist.githubusercontent.com/darkrecher/24d6471c87d1065064ca830646709fea/raw/34a6a8059adba985d219f228c96bb9405c3a633b/koballd-crawler.txt
# http://squarity.fr/#fetchez_githubgist_darkrecher/24d6471c87d1065064ca830646709fea/raw/koballd-crawler.txt

"""

  {
    "name": "Koballd Crawler",
    "version": "1.0.0",
    "game_area": {
        "nb_tile_width": 21,
        "nb_tile_height": 21
    },
    "tile_size": 32,
    "img_coords": {
        "dark": [0, 0],
        "kob_right_up": [32, 0],
        "kob_right_down": [32, 32],
        "kob_down_left": [64, 0],
        "kob_down_right": [96, 0],
        "kob_up_left": [64, 32],
        "kob_up_right": [96, 32],
        "kob_left_up": [128, 0],
        "kob_left_down": [128, 32],
        "selection": [64, 64],
        "wall": [0, 64],
        "ground": [0, 32],
        "cake": [32, 64],

        "osef": [0, 0]
    }
  }

"""

"""
Koballd Crawler

My contribution to Ludum Dare 55.

Select one of the eight green balls, then click on a border of the map to launch it.
The ball goes to its primary direction, to the opposite border of the map.
When blocked by a wall, it goes to its secondary direction, indicated by the yellow arrow.
The ball stops when the two directions are blocked.

To restart a level, click twice on the button 1.

Try to get the cake.

I knew I would have very little time for this Ludum edition, so, it's not that bad.

This is why I called my game “Koballd Crawler”.
If I don't have time, the sprites would stay as green balls, like in “koBALLd”.
If I had time, I would have drawn kobolds instead, like in KOballD.

Looks like we sticked to green balls.

Happy crawling!
"""

LEVEL_ONE = (
    "#...............#",
    ".................",
    ".................",
    ".................",
    ".................",
    ".................",
    ".................",
    ".......#...#.....",
    ".......#.C.#.....",
    ".......#...#.....",
    ".......#####.....",
    ".................",
    ".................",
    ".................",
    ".................",
    ".................",
    "#...............#",
)


LEVEL_TWO = (
    "#...............#",
    "...####..........",
    ".................",
    ".................",
    ".................",
    "...........#.#...",
    "...........#.#...",
    "........####.#...",
    ".............#...",
    ".............#...",
    "........#..#.....",
    "........#..#####.",
    "........#.....C#.",
    "........########.",
    "...#.............",
    "..#.#............",
    "#.#.#...........#",
)

LEVEL_THREE = (
    "#...............#",
    ".................",
    ".....###....##...",
    ".....#C#..#..#...",
    "....##.####..#...",
    "....#........#...",
    "..#.#######..#...",
    "..#.......#..#...",
    "..#..#....#..#...",
    "..#....#.........",
    "..#....#.........",
    "..#.####.........",
    "..#.#.##.........",
    ".................",
    ".................",
    ".....######......",
    "#...............#",
)

LEVELS = (LEVEL_ONE, LEVEL_TWO, LEVEL_THREE)

OFFSET_FROM_DIR_STR = {
    "up": (0, -1),
    "right": (+1, 0),
    "down": (0, +1),
    "left": (-1, 0),
}

OFFSET_SCREEN_TO_MAP = (2, 2)


class MapTile:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.adjacencies = None
        self.game_objects = []

    def is_passable(self):
        if "wall" in self.game_objects:
            return False
        for gobj in self.game_objects:
            if gobj.startswith("kob"):
                return False
        return True

    def change_selection(self, selected):
        if selected:
            self.game_objects.append("selection")
        else:
            if "selection" in self.game_objects:
                self.game_objects.remove("selection")

    def render(self):
        return self.game_objects


class KoballdLauncher:

    def __init__(self, x, y, direction, subdirection):
        self.x = x
        self.y = y
        self.direction = direction
        self.subdirection = subdirection
        self.selected = False
        self.kob_game_object = "kob_" + self.direction + "_" + self.subdirection

    # useless, mais on sait jamais.
    def set_neighbor_launcher(self, neighbor):
        self.neighbor = neighbor

    def change_selection(self, selected):
        self.selected = selected

    def render(self):
        if self.selected:
            return ["dark", self.kob_game_object, "selection"]
        else:
            return ["dark", self.kob_game_object]


class WalkingKoballd:

    def __init__(self, x, y, koballd_launcher, owner):
        self.x = x
        self.y = y
        self.direction = koballd_launcher.direction
        self.subdirection = koballd_launcher.subdirection
        self.gobj_name = koballd_launcher.kob_game_object
        self.owner = owner
        self.is_blocked = False
        self.is_outside = False
        self.found_cake = False

    def _try_move(self, selected_direction):
        offset = OFFSET_FROM_DIR_STR[selected_direction]
        dest_x = self.x + offset[0]
        dest_y = self.y + offset[1]

        # J'aurais dû utiliser les adjacencies. Tant pis.
        # C'est la faute de Copilot qui m'a grillé le cerveau.
        if not (0 <= dest_x < self.owner.map_w and 0 <= dest_y < self.owner.map_h):
            self.is_outside = True
            return False
        dest_tile = self.owner.get_map_tile(dest_x, dest_y)
        if not dest_tile.is_passable():
            self.is_blocked = True
            return False
        if "cake" in dest_tile.game_objects:
            self.found_cake = True
            return False
        self.x = dest_x
        self.y = dest_y
        return True

    def walk(self):
        if self._try_move(self.direction):
            return True
        if self.is_blocked:
            # Ouh, ça c'est dégueu.
            self.is_blocked = False
            return self._try_move(self.subdirection)


class GameModel():

    EVENT_RESULT_WALK = """
        { "delayed_actions": [ {"name": "walk_koballd", "delay_ms": 100} ], "player_locks": ["walk_koballd"] }
    """
    EVENT_RESULT_WALK_END = """
        { "player_unlocks": ["walk_koballd"] }
    """

    EVENT_RESULT_TUTO_BLINK = """
        { "delayed_actions": [ {"name": "tuto_blink", "delay_ms": 100} ], "player_locks": ["tuto_blink"] }
    """

    EVENT_RESULT_TUTO_BLINK_END = """
        { "player_unlocks": ["tuto_blink"] }
    """


    def __init__(self):
        self.w = 21
        self.h = 21
        ofs_x, ofs_y = OFFSET_SCREEN_TO_MAP
        self.map_w = self.w - 2*ofs_x
        self.map_h = self.h - 2*ofs_y
        self.rendered_tiles = [
            [
                [] for x in range(self.w)
            ]
            for y in range(self.h)
        ]

        self.map_tiles = [
            [
                MapTile(x, y) for x in range(self.map_w)
            ]
            for y in range(self.map_h)
        ]
        for y in range(self.map_h):
            for x in range(self.map_w):
                self.get_map_tile(x, y).adjacencies = self._make_adjacencies(x, y)

        KOBALLD_LAUNCHER_DEFINITIONS = (
            (self.w // 2 - 2, 0, "down", "left"),
            (self.w // 2 + 2, 0, "down", "right"),
            (self.w // 2 - 2, self.h - 1, "up", "left"),
            (self.w // 2 + 2, self.h - 1, "up", "right"),
            (0, self.h // 2 - 2, "right", "up"),
            (0, self.h // 2 + 2, "right", "down"),
            (self.w - 1, self.h // 2 - 2, "left", "up"),
            (self.w - 1, self.h // 2 + 2, "left", "down"),
        )
        self.koblaus = []
        self.koblaus_from_coord = {}
        for x, y, direction, subdirection in KOBALLD_LAUNCHER_DEFINITIONS:
            koballd_launcher = KoballdLauncher(x, y, direction, subdirection)
            self.koblaus.append(koballd_launcher)
            self.koblaus_from_coord[(x, y)] = koballd_launcher
        # useless neighboring.
        #for idx_kob in range(0, 8, 2):
        #    self.koblaus[idx_kob].set_neighbor_launcher(self.koblaus[idx_kob + 1])
        #    self.koblaus[idx_kob + 1].set_neighbor_launcher(self.koblaus[idx_kob])
        self.koblaus[0].selected = True
        self.walking_koballd = None
        self.explained_selection = False
        self.explained_border = False
        self.blink_selection = 0
        self.can_pass_level = False
        self.reset_level = False
        self.current_level = 0
        self.tiles_to_blink = []
        self.init_ihm()
        self.init_level(LEVELS[self.current_level])

    def _make_adjacencies(self, x, y):
        """
        Renvoie les tiles adjacentes à la tile située aux coordonnées x, y.
        On renvoie toujours une liste de 8 éléments (les 8 directions), mais certains éléments
        peuvent être None, si les coordonnées x, y sont sur un bord de l'aire de jeu.
        """
        adjacencies = (
            self.map_tiles[y - 1][x] if 0 <= y - 1 else None,
            self.map_tiles[y - 1][x + 1] if 0 <= y - 1 and x + 1 < self.map_w else None,
            self.map_tiles[y][x + 1] if x + 1 < self.map_w else None,
            self.map_tiles[y + 1][x + 1] if y + 1 < self.map_h and x + 1 < self.map_w else None,
            self.map_tiles[y + 1][x] if y + 1 < self.map_h else None,
            self.map_tiles[y + 1][x - 1] if y + 1 < self.map_h and 0 <= x - 1 else None,
            self.map_tiles[y][x - 1] if 0 <= x - 1 else None,
            self.map_tiles[y - 1][x - 1] if 0 <= y - 1 and 0 <= x - 1 else None,
        )
        return adjacencies

    def get_map_tile(self, x, y):
        return self.map_tiles[y][x]

    def init_ihm(self):
        ofs_x, ofs_y = OFFSET_SCREEN_TO_MAP
        for x in range(self.w):
            for y in range(ofs_y):
                self.rendered_tiles[y][x] = ["dark"]
            for y in range(self.h - ofs_y, self.h):
                self.rendered_tiles[y][x] = ["dark"]
        for y in range(self.h):
            for x in range(ofs_x):
                self.rendered_tiles[y][x] = ["dark"]
            for x in range(self.w - ofs_x, self.w):
                self.rendered_tiles[y][x] = ["dark"]
        self.render_koballd_launcher()

    def render_koballd_launcher(self):
        for koballd_launcher in self.koblaus:
            self.rendered_tiles[koballd_launcher.y][koballd_launcher.x] = list(koballd_launcher.render())

    def init_level(self, level_definition):
        self.can_pass_level = False
        CORRESP = {
            ".": ["ground"],
            "#": ["wall"],
            "C": ["ground", "cake"],
        }
        for y, line in enumerate(level_definition):
            for x, char in enumerate(line):
                self.get_map_tile(x, y).game_objects[:] = CORRESP[char]

    def export_all_tiles(self):
        ofs_x, ofs_y = OFFSET_SCREEN_TO_MAP
        for y in range(self.map_h):
            for x in range(self.map_w):
                tile = self.get_map_tile(x, y)
                self.rendered_tiles[y + ofs_y][x + ofs_x] = list(tile.render())
        if self.walking_koballd:
            self.rendered_tiles[self.walking_koballd.y + ofs_y][self.walking_koballd.x + ofs_x].append(self.walking_koballd.gobj_name)

        return self.rendered_tiles

    def get_selected_koballd_launcher(self, direction):
        for koballd_launcher in self.koblaus:
            if koballd_launcher.direction == direction and koballd_launcher.selected:
                return koballd_launcher
        return None

    def on_game_event(self, event_name):

        if event_name == "action_1":
            if self.reset_level:
                self.init_level(LEVELS[self.current_level])
                self.reset_level = False
            else:
                print("")
                print("Click again on the button 1 to restart the level.")
                self.reset_level = True

        elif event_name == "walk_koballd":
            if self.walking_koballd:
                if self.walking_koballd.walk():
                    return GameModel.EVENT_RESULT_WALK
                else:
                    if self.walking_koballd.is_blocked:
                        self.get_map_tile(self.walking_koballd.x, self.walking_koballd.y).game_objects.append(
                            self.walking_koballd.gobj_name
                        )
                    elif self.walking_koballd.found_cake:
                        self.get_map_tile(self.walking_koballd.x, self.walking_koballd.y).game_objects.append(
                            self.walking_koballd.gobj_name
                        )
                        self.current_level += 1
                        if self.current_level == len(LEVELS):
                            print("")
                            print("That was the last level.")
                            print("Didn't have time to put more, sorry.")
                            print("Let's restart everything!")
                            self.current_level = 0
                        else:
                            print("")
                            print("You found the cake!")
                            print("Click anywhere to go to the next level.")
                        self.can_pass_level = True
                    self.walking_koballd = None
                    return GameModel.EVENT_RESULT_WALK_END
            else:
                # not supposed to happen.
                return GameModel.EVENT_RESULT_WALK_END

        elif event_name == "tuto_blink":
            self.blink_selection -= 1
            show_select = self.blink_selection % 2
            for koballd_launcher in self.tiles_to_blink:
                koballd_launcher.change_selection(show_select)
            self.render_koballd_launcher()
            if self.blink_selection:
                return GameModel.EVENT_RESULT_TUTO_BLINK
            else:
                self.tiles_to_blink = []
                return GameModel.EVENT_RESULT_TUTO_BLINK_END

        else:
            print("Select a green ball, then click on a border of the map to launch it.")

    def on_click(self, x, y):

        if self.can_pass_level:
            self.init_level(LEVELS[self.current_level])
            return None

        selected_koballd_launcher = None
        for koballd_launcher in self.koblaus:
            if koballd_launcher.x == x and koballd_launcher.y == y:
                selected_koballd_launcher = koballd_launcher
                break
        if selected_koballd_launcher:
            for koballd_launcher in self.koblaus:
                koballd_launcher.change_selection(False)
            selected_koballd_launcher.change_selection(True)
            self.render_koballd_launcher()
            return None

        map_x = x - OFFSET_SCREEN_TO_MAP[0]
        map_y = y - OFFSET_SCREEN_TO_MAP[1]

        if not (0 <= map_x < self.map_w and 0 <= map_y < self.map_h):
            return None
        if not self.get_map_tile(map_x, map_y).is_passable():
            return None

        direction = None
        selected_koballd_launcher = None
        if map_x == 0:
            if 0 < map_y < self.map_h - 1:
                direction = "right"
        if map_x == self.map_w - 1:
            if 0 < map_y < self.map_h - 1:
                direction = "left"
        if map_y == 0:
            if 0 < map_x < self.map_w - 1:
                direction = "down"
        if map_y == self.map_h - 1:
            if 0 < map_x < self.map_w - 1:
                direction = "up"

        if not direction:
            self.tiles_to_blink = []
            for x in range(1, self.map_w - 1):
                self.tiles_to_blink.append(self.get_map_tile(x, 0))
                self.tiles_to_blink.append(self.get_map_tile(x, self.map_h - 1))
            for y in range(1, self.map_h - 1):
                self.tiles_to_blink.append(self.get_map_tile(0, y))
                self.tiles_to_blink.append(self.get_map_tile(self.map_w - 1, y))
            for koballd_launcher in self.tiles_to_blink:
                koballd_launcher.change_selection(True)
            if not self.explained_border:
                self.explained_border = True
                print("You must click on a border of the map to launch the selected green ball.")
            self.blink_selection = 11
            return GameModel.EVENT_RESULT_TUTO_BLINK

        selected_koballd_launcher = self.get_selected_koballd_launcher(direction)
        if selected_koballd_launcher:
            self.walking_koballd = WalkingKoballd(
                map_x,
                map_y,
                selected_koballd_launcher,
                self
            )
            return GameModel.EVENT_RESULT_WALK
        else:
            self.tiles_to_blink = []
            for koballd_launcher in self.koblaus:
                if koballd_launcher.direction == direction:
                    self.tiles_to_blink.append(koballd_launcher)
            for koballd_launcher in self.tiles_to_blink:
                koballd_launcher.change_selection(True)
            self.render_koballd_launcher()
            if not self.explained_selection:
                self.explained_selection = True
                print("You must first select a green ball near the map border where you want to launch it.")
            self.blink_selection = 11
            return GameModel.EVENT_RESULT_TUTO_BLINK


