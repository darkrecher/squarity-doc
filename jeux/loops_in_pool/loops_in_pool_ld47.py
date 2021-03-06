"""
********************************
***       LOOPS IN POOL      ***
********************************
You are a magigardener. The Countess du Swagging asked you to clean
her swimming-pool, which has been invaded by mud and vines.

Select two tiles with the "1" button (numpad or keyboard)
to exchange their vines.

Make some closed vine loops to remove the mud inside it.
The clear fountain water propagates where there is no mud.

You can not exchange the vines when the tile is not completely
covered by mud or by water, because LOOPS STUCKS !!

The "2" button is a special power :
 - on a tile covered by water, it spins the vines.
 - on a tile with mud, it adds a vine between two mud triangles.

Each action costs Pool mana (totally unrelated to Mana pool !) :

 - exchange : 1
 - spin vines : 4
 - add a vine on mud : 10

Use the "1" button on the upper left fountain
to know you current Pool mana.
You regain some by propagating water.

Try to reach the goal on the lower right.

Good luck, magigardener !

"""

# The text below is the game source code, you are not obliged to read it.

# https://raw.githubusercontent.com/darkrecher/squarity-doc/master/jeux/loops_in_pool

# v = Vine. m = Mud.

# Ouais, désolé. On peut pas encore importer la standard lib de python dans Squarity.
# Du coup on est obligé d'avoir un recours dégueulasse au javascript pour faire du random.
# J'essayerais d'arranger ça très vite. Promis.
from javascript import Math

def randrange(a, b=None):
    if b is None:
        low = 0
        high = a
    else:
        low = a
        high = b

    return Math.floor(Math.random() * (high - low)) + low

VINES = ["v0", "v1", "v2", "v3", "v4", "v5", "v6", "v7"]
VINES_LEN = len(VINES)
VINES_SET = set(VINES)

VINE_CONNECTIONS_ADJACENT = {
    "v0": (( 0, -1, "v4"), ),
    "v1": ((+1, -1, "v5"), (0, -1, "v3"), (+1, 0, "v7"), ),
    "v2": ((+1,  0, "v6"), ),
    "v3": ((+1, +1, "v7"), (0, +1, "v1"), (+1, 0, "v5"), ),
    "v4": (( 0, +1, "v0"), ),
    "v5": ((-1, +1, "v1"), (0, +1, "v7"), (-1, 0, "v3"), ),
    "v6": ((-1,  0, "v2"), ),
    "v7": ((-1, -1, "v3"), (0, -1, "v5"), (-1, 0, "v1"), ),
}

VINE_CONNECTIONS_SAME_SQUARE = tuple(
    (0, 0, vine) for vine in VINES
)

VINE_CONNECTIONS = {}

for vine_start, adj_connections in VINE_CONNECTIONS_ADJACENT.items():
    complete_connections = tuple(adj_connections + VINE_CONNECTIONS_SAME_SQUARE)
    VINE_CONNECTIONS[vine_start] = complete_connections

TRIANGLES = ["t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7"]

TRI_CONNECTIONS = {
    "t0": ((0, 0, "t1", "v1"), (0, 0, "t7", "v0"), ( 0, -1, "t3", None)),
    "t1": ((0, 0, "t2", "v2"), (0, 0, "t0", "v1"), (+1,  0, "t6", None)),
    "t2": ((0, 0, "t3", "v3"), (0, 0, "t1", "v2"), (+1,  0, "t5", None)),
    "t3": ((0, 0, "t4", "v4"), (0, 0, "t2", "v3"), ( 0, +1, "t0", None)),
    "t4": ((0, 0, "t5", "v5"), (0, 0, "t3", "v4"), ( 0, +1, "t7", None)),
    "t5": ((0, 0, "t6", "v6"), (0, 0, "t4", "v5"), (-1,  0, "t2", None)),
    "t6": ((0, 0, "t7", "v7"), (0, 0, "t5", "v6"), (-1,  0, "t1", None)),
    "t7": ((0, 0, "t0", "v0"), (0, 0, "t6", "v7"), ( 0, -1, "t4", None)),
}

VINES_FROM_TRIANGLE = {
    key: (val[0][3], val[1][3])
    for key, val in TRI_CONNECTIONS.items()
}
# print("VINES_FROM_TRIANGLE", VINES_FROM_TRIANGLE)

TRIANGLES_FROM_VINE = {
    "v0": ("t7", "t0"),
    "v1": ("t0", "t1"),
    "v2": ("t1", "t2"),
    "v3": ("t2", "t3"),
    "v4": ("t3", "t4"),
    "v5": ("t4", "t5"),
    "v6": ("t5", "t6"),
    "v7": ("t6", "t7"),
}

ALL_MUD = [ "m" ] * 8
ALL_WATER = [ "l" ] * 8

# elem 1 et 2 : index de triangle adjacents, sur une même case.
# elem 3 : index de la vine qui se trouve entre ces deux triangles adjacents.
VINES_INTER_TRI = (
    (0, 1, 1),
    (1, 2, 2),
    (2, 3, 3),
    (3, 4, 4),
    (4, 5, 5),
    (5, 6, 6),
    (6, 7, 7),
    (7, 0, 0),
)

MANA_START = 50
MANA_COST_EXCHANGE = 1
MANA_COST_ADD_VINE = 10
MANA_COST_SPIN = 4

class Tile():

    def __init__(self):
        self.triangle_types = [ "" ] * 8
        self.vine_types = [ 0 ] * 8
        self.triangle_tmp_data = [ 0 ] * 8
        self.tile_tmp_data = 0
        self.put_random_vines()

    def put_random_vines(self):
        quantity = randrange(2, 5)
        for _ in range(quantity):
            idx_vine = randrange(8)
            self.vine_types[idx_vine] = 1

    def mudify_borders(self, border):
        tri_borders = {
            "U": (7, 0),
            "R": (1, 2),
            "D": (3, 4),
            "L": (5, 6),
        }
        for idx_tri in tri_borders[border]:
            self.triangle_types[idx_tri] = "m"

    def spin(self):
        first_vine = self.vine_types[0]
        for idx_vine in range(7):
            self.vine_types[idx_vine] = self.vine_types[idx_vine + 1]
        self.vine_types[7] = first_vine

class BoardModel():

    def __init__(self):
        # print(VINE_CONNECTIONS)
        self.w = 20 # width (largeur) : 20 cases
        self.h = 14 # height (hauteur) : 14 cases
        self.text_outing = 0

        self.tiles = [
            [
                Tile() for x in range(self.w)
            ]
            for y in range(self.h)
        ]
        self.cursor_coords = [4, 5]
        for x in range(self.w):
            self.tiles[0][x].mudify_borders("U")
            self.tiles[self.h-1][x].mudify_borders("D")
        for y in range(self.h):
            self.tiles[y][0].mudify_borders("L")
            self.tiles[y][self.w-1].mudify_borders("R")

        self.tiles[0][0].triangle_types = [""] * 8
        self.tiles[0][0].vine_types = [0] * 8
        for idx_tri in (7, 6, 5, 4):
            self.tiles[0][1].triangle_types[idx_tri] = ""
        for idx_tri in (6, 7, 0, 1):
            self.tiles[1][0].triangle_types[idx_tri] = ""
        for idx_tri in (6, 7):
            self.tiles[1][1].triangle_types[idx_tri] = ""
        self.tiles[0][1].vine_types[0] = 1
        self.tiles[0][1].vine_types[4] = 1
        self.tiles[1][0].vine_types[6] = 1
        self.tiles[1][0].vine_types[2] = 1
        self.tiles[1][1].vine_types[6] = 1
        self.tiles[1][1].vine_types[0] = 1

        self.tiles[self.h-1][self.w-1].triangle_types = [""] * 8
        self.tiles[self.h-1][self.w-1].vine_types = [0] * 8
        for idx_tri in (5, 4, 3, 2):
            self.tiles[self.h-2][self.w-1].triangle_types[idx_tri] = ""
        for idx_tri in (0, 1, 2, 3):
            self.tiles[self.h-1][self.w-2].triangle_types[idx_tri] = ""
        for idx_tri in (3, 2):
            self.tiles[self.h-2][self.w-2].triangle_types[idx_tri] = ""
        self.tiles[self.h-2][self.w-1].vine_types[6] = 1
        self.tiles[self.h-2][self.w-1].vine_types[2] = 1
        self.tiles[self.h-1][self.w-2].vine_types[4] = 1
        self.tiles[self.h-1][self.w-2].vine_types[0] = 1
        self.tiles[self.h-2][self.w-2].vine_types[4] = 1
        self.tiles[self.h-2][self.w-2].vine_types[2] = 1


        #self.propagate_some_mud()
        self.must_start_mud = True
        self.finished_init = False
        self.coord_tile_to_exchange = None
        self.tile_coords_not_watered = []
        for x in range(self.w):
            for y in range(self.h):
                self.tile_coords_not_watered.append((x, y))
        self.pool_mana = MANA_START

    def story(self, text):
        print(text)
        self.text_outing = 5

    def get_size(self):
        return self.w, self.h

    def get_tile_gamobjs(self, x, y):
        return self.tiles[y][x]

    def export_all_tiles(self):
        rendered_tiles = []
        for y in range(self.h):
            line = []
            for x in range(self.w):
                gamobjs = ["ground"]
                the_tile = self.tiles[y][x]
                for idx_tri in range(8):
                    tri_type = the_tile.triangle_types[idx_tri]
                    if tri_type:
                        gamobjs.append(tri_type + str(idx_tri))
                for idx_vi in range(8):
                    vi_type = the_tile.vine_types[idx_vi]
                    if vi_type == 1:
                        gamobjs.append("v" + str(idx_vi))
                    elif vi_type == 2:
                        gamobjs.append("v" + str(idx_vi) + "_lit")
                line.append(gamobjs)
            rendered_tiles.append(line)

        rendered_tiles[self.h-1][self.w-1].insert(1, "goal")
        if self.coord_tile_to_exchange is not None:
            c_exch_x, c_exch_y = self.coord_tile_to_exchange
            rendered_tiles[c_exch_y][c_exch_x].append("selection")
        c_cursor_x, c_cursor_y = self.cursor_coords
        rendered_tiles[c_cursor_y][c_cursor_x].append("cursor")

        rendered_tiles[0][0].append("fountain")
        if self.pool_mana < 100:
            nb_fountain_darking = (100 - self.pool_mana) // 5
            rendered_tiles[0][0] += ["darkfountain"] * nb_fountain_darking

        return rendered_tiles

    def clean_tri_tmp_data(self):
        for y in range(self.h):
            for x in range(self.w):
                the_tile = self.tiles[y][x]
                for idx_tri in range(8):
                    the_tile.triangle_tmp_data[idx_tri] = 0

    def get_tri_next_to_mud_one_tile(self, x, y):
        triangles_next_to_mud = []
        the_tile = self.tiles[y][x]
        if the_tile.triangle_types == ALL_MUD:
            the_tile.tile_tmp_data = 1
            return triangles_next_to_mud
        for idx_tri in range(8):
            if the_tile.triangle_types[idx_tri] == "":
                for offset_x, offset_y, tri_type_adj, blocking_vine in TRI_CONNECTIONS["t" + str(idx_tri)]:
                    target_x = x + offset_x
                    target_y = y + offset_y
                    blocked_by_vine = False
                    if blocking_vine is not None:
                        vine_type = the_tile.vine_types[int(blocking_vine[1])]
                        blocked_by_vine = bool(vine_type)
                    if 0 <= target_x < self.w and 0 <= target_y < self.h and not blocked_by_vine:
                        tri_adj_value = self.tiles[target_y][target_x].triangle_types[int(tri_type_adj[1])]
                        if tri_adj_value == "m":
                            triangles_next_to_mud.append((x, y, idx_tri))
                            break
        # print("get tri", triangles_next_to_mud)
        return triangles_next_to_mud

    def get_tri_next_to_mud(self):
        tri_nexts = []
        y_up = 0
        y_down = self.h-1
        triangles_next_to_mud = set()
        while y_up <= y_down:
            for x in range(self.w):
                if self.tiles[y_up][x].tile_tmp_data == 0:
                    triangles_next_to_mud = triangles_next_to_mud.union(set(self.get_tri_next_to_mud_one_tile(x, y_up)))
                if y_up != y_down:
                    if self.tiles[y_down][x].tile_tmp_data == 0:
                        triangles_next_to_mud = triangles_next_to_mud.union(set(self.get_tri_next_to_mud_one_tile(x, y_down)))
            y_up += 1
            y_down -= 1
            if len(triangles_next_to_mud) >= 40:
                return triangles_next_to_mud
        return triangles_next_to_mud

    def propagate_some_mud(self):
        # print("propagate_mud")
        triangles_next_to_mud = self.get_tri_next_to_mud()

        if not triangles_next_to_mud:
            # print("no more triangles")
            self.finished_init = True
            for x in range(self.w):
                for y in range(self.h):
                    self.tiles[y][x].tile_tmp_data = 0
                    return

        for x, y, idx_tri in triangles_next_to_mud:
            self.tiles[y][x].triangle_types[idx_tri] = "m"
        return """{ "delayed_actions": [ {"name": "propagate_mud", "delay_ms": 100} ] }"""

    def get_tri_next_to_water_one_tile(self, x, y):
        triangles_next_to_water = []
        the_tile = self.tiles[y][x]
        for idx_tri in range(8):
            if the_tile.triangle_types[idx_tri] == "":
                for offset_x, offset_y, tri_type_adj, blocking_vine in TRI_CONNECTIONS["t" + str(idx_tri)]:
                    target_x = x + offset_x
                    target_y = y + offset_y
                    if 0 <= target_x < self.w and 0 <= target_y < self.h:
                        tri_adj_value = self.tiles[target_y][target_x].triangle_types[int(tri_type_adj[1])]
                        if tri_adj_value == "l":
                            triangles_next_to_water.append((x, y, idx_tri))
                            break
        # print("get tri", triangles_next_to_water)
        return triangles_next_to_water

    def propagate_some_water(self):
        triangles_next_to_water = set()
        coord_to_remove = []
        for coord in self.tile_coords_not_watered:
            x, y = coord
            if self.tiles[y][x].triangle_types == ALL_WATER:
                # print("fully watered", x, y)
                coord_to_remove.append(coord)
            else:
                triangles_next_to_water = triangles_next_to_water.union(self.get_tri_next_to_water_one_tile(*coord))
                if len(triangles_next_to_water) >= 5:
                    break

        if coord_to_remove:
            for coord in coord_to_remove:
                self.tile_coords_not_watered.remove(coord)

        if not triangles_next_to_water:
            # print("tile_coords_not_watered")
            # print(self.tile_coords_not_watered)
            if self.tiles[self.h-1][self.w-1].triangle_types == ALL_WATER:
                self.story("*" * 30)
                self.story("YOU WON !!")
                self.story("Your final score is : " + str(self.pool_mana))
                self.story("*" * 30)
                self.text_outing = 0
            return

        for x, y, idx_tri in triangles_next_to_water:
            self.tiles[y][x].triangle_types[idx_tri] = "l"
        self.pool_mana += len(triangles_next_to_water)
        return """{ "delayed_actions": [ {"name": "propagate_some_water", "delay_ms": 400} ] }"""

    def get_inside_triangles_from_tile(self, coords):
        coord_x, coord_y = coords
        out_x1 = -1
        out_x2 = self.w #self.world_w
        out_y1 = -1
        out_y2 = self.h #self.world_h
        self.tmp_datas_out = []
        self.tmp_datas_inside = []
        tmp_data_cur = 0

        for idx_tri in range(8):

            if self.tiles[coord_y][coord_x].triangle_tmp_data[idx_tri]:
                # already processed
                continue

            if self.tiles[coord_y][coord_x].triangle_types[idx_tri] != "m":
                # Not a mud triangle. No need to process.
                continue

            localised_tri = (coord_x, coord_y, idx_tri)
            current_triangle_pack = [localised_tri]
            tmp_data_cur += 1
            #current_triangle_pack_validated = []
            #is_pack_out = False
            # print("start prop", localised_tri)
            is_pack_out = False

            while current_triangle_pack:
                cur_tri_propag = current_triangle_pack.pop(0)
                # print("cur_tri_propag", cur_tri_propag)
                cur_tri_propag_x, cur_tri_propag_y, cur_tri_propag_idx_tri = cur_tri_propag
                if cur_tri_propag_x in (out_x1, out_x2) or cur_tri_propag_y in (out_y1, out_y2):
                    self.tmp_datas_out.append(tmp_data_cur)
                    is_pack_out = True
                    # print("out because limits")
                    break

                cur_tri_tmp_data = self.tiles[cur_tri_propag_y][cur_tri_propag_x].triangle_tmp_data[cur_tri_propag_idx_tri]
                if tmp_data_cur == cur_tri_tmp_data:
                    # print("already processed")
                    continue
                if cur_tri_tmp_data in self.tmp_datas_out:
                    self.tmp_datas_out.append(tmp_data_cur)
                    is_pack_out = True
                    # print("out because reached tri already out")
                    break

                #print("add in current prop")
                self.tiles[cur_tri_propag_y][cur_tri_propag_x].triangle_tmp_data[cur_tri_propag_idx_tri] = tmp_data_cur

                for offset_x, offset_y, tri_type_adj, blocking_vine in TRI_CONNECTIONS["t" + str(cur_tri_propag_idx_tri)]:
                    blocked_by_vine = False
                    if blocking_vine is not None:
                        if self.tiles[cur_tri_propag_y][cur_tri_propag_x].vine_types[int(blocking_vine[1])]:
                            blocked_by_vine = True
                    if not blocked_by_vine:
                        current_triangle_pack.append(
                            (cur_tri_propag_x + offset_x, cur_tri_propag_y + offset_y, int(tri_type_adj[1]))
                        )

            # print("tris out or not", is_pack_out, current_triangle_pack_validated)
            if not is_pack_out:
                self.tmp_datas_inside.append(tmp_data_cur)
                # TODO : insides.append(current_triangle_pack_validated)

        # print("fini big loop")
        # print("self.tmp_datas_inside", self.tmp_datas_inside)
        insides = []
        if self.tmp_datas_inside:
            insides = [ [] for _ in range(tmp_data_cur + 1) ]
            for y in range(self.h):
                for x in range(self.w):
                    the_tile = self.tiles[y][x]
                    for idx_tri in range(8):
                        tmp_data = the_tile.triangle_tmp_data[idx_tri]
                        if tmp_data in self.tmp_datas_inside:
                            insides[tmp_data].append(
                                (x, y, idx_tri)
                            )

        return [ inside_list for inside_list in insides if inside_list ]

    def remove_inside_mud(self, coords):
        insides = self.get_inside_triangles_from_tile(coords)
        # print("insides", insides)

        for tri_pack_inside in insides:
            for tri_x, tri_y, idx_tri in tri_pack_inside:
                self.tiles[tri_y][tri_x].triangle_types[idx_tri] = ""

        return bool(insides)

    def on_game_event(self, event_name):
        # print(event_name)

        if self.text_outing and event_name != "propagate_some_water":
            print("")
            self.text_outing -= 1

        if self.must_start_mud:
            self.must_start_mud = False
            return self.propagate_some_mud()

        if event_name == "propagate_mud":
            still_mud = self.propagate_some_mud()
            if still_mud:
                return still_mud
            else:
                self.tiles[0][0].triangle_types[7] = "l"
                return """{ "delayed_actions": [ {"name": "propagate_some_water", "delay_ms": 400} ] }"""

        if event_name == "propagate_some_water":
            return self.propagate_some_water()


        if event_name == "action_1":
            if not self.finished_init:
                self.story("Please wait while propagating mud")
                return

            x, y = self.cursor_coords

            if x == 0 and y == 0:
                self.story("Your current Pool mana is : " + str(self.pool_mana))
                return

            if self.tiles[y][x].triangle_types != ALL_MUD and self.tiles[y][x].triangle_types != ALL_WATER:
                self.story("You can not exchange two tiles if ")
                self.story("they are not totally covered with mud,")
                self.story("or not totally covered with water.")
                return

            if self.coord_tile_to_exchange is None:
                self.coord_tile_to_exchange = list(self.cursor_coords)
                return

            if self.coord_tile_to_exchange is not None and self.coord_tile_to_exchange == self.cursor_coords:
                # print("canceling selection")
                self.coord_tile_to_exchange = None
                return

            if self.pool_mana < MANA_COST_EXCHANGE:
                self.story("You do not have enough mana to use the exchange power")
                self.story("It seems you have lost...")
                return

            self.pool_mana -= MANA_COST_EXCHANGE
            cursor_x, cursor_y = self.cursor_coords
            exch_x, exch_y = self.coord_tile_to_exchange
            vines_tmp = self.tiles[cursor_y][cursor_x].vine_types
            self.tiles[cursor_y][cursor_x].vine_types = list(self.tiles[exch_y][exch_x].vine_types)
            self.tiles[exch_y][exch_x].vine_types = list(vines_tmp)

            removed_mud = False
            try:
                self.clean_tri_tmp_data()
                self.tmp_datas_inside = []
                self.tmp_datas_out = []
                if self.remove_inside_mud(self.cursor_coords):
                    removed_mud = True
                self.clean_tri_tmp_data()
                self.tmp_datas_inside = []
                self.tmp_datas_out = []
                if self.remove_inside_mud(self.coord_tile_to_exchange):
                    removed_mud = True
            except Exception as blarg:
                print("The game failed. Not supposed to happen. Sorry")
                # print(blarg)
                # print(type(blarg))
                # print(blarg.__traceback__)
                # print(dir(blarg))

            self.coord_tile_to_exchange = None

            if removed_mud:
                return """{ "delayed_actions": [ {"name": "propagate_some_water", "delay_ms": 400} ] }"""
            else:
                return

        if event_name == "action_2":
            if not self.finished_init:
                self.story("Please wait while propagating mud")
                return

            x, y = self.cursor_coords

            if x == 0 and y == 0:
                self.story("Your current Pool mana is : " + str(self.pool_mana))
                return

            the_tile = self.tiles[y][x]

            if the_tile.triangle_types == ALL_WATER:
                if self.pool_mana < MANA_COST_SPIN:
                    self.story("You do not have enough mana to use the spin power.")
                else:
                    self.pool_mana -= MANA_COST_SPIN
                    the_tile.spin()
                return

            potential_vines = []
            for idx_tri_1, idx_tri_2, idx_vine in VINES_INTER_TRI:
                if the_tile.triangle_types[idx_tri_1] == "m" and the_tile.triangle_types[idx_tri_2] == "m" and not the_tile.vine_types[idx_vine]:
                    potential_vines.append(idx_vine)

            if not potential_vines:
                self.story("You can use your special power only on")
                self.story("a tile where there is not enough vines,")
                self.story("or on a tile fully covered with water.")
                return

            if self.pool_mana < MANA_COST_ADD_VINE:
                self.story("You do not have enough mana to use the add-vine power.")
                return

            self.pool_mana -= MANA_COST_ADD_VINE
            selected_vine_idx_idx = randrange(len(potential_vines))
            selected_vine_idx = potential_vines[selected_vine_idx_idx]
            the_tile.vine_types[selected_vine_idx] = 1
            self.clean_tri_tmp_data()
            self.tmp_datas_inside = []
            self.tmp_datas_out = []
            if self.remove_inside_mud(self.cursor_coords):
                return """{ "delayed_actions": [ {"name": "propagate_some_water", "delay_ms": 400} ] }"""
            else:
                return

        move_offset = squarity.MOVE_FROM_DIR.get(event_name)
        if move_offset is not None:

            # weird bug that happened only once...
            if self.coord_tile_to_exchange is not None:
                x, y = self.coord_tile_to_exchange
                if self.tiles[y][x].triangle_types != ALL_MUD and self.tiles[y][x].triangle_types != ALL_WATER:
                    self.coord_tile_to_exchange = None
                    print("WEIRD BUG !!")

            self.cursor_coords = [
                self.cursor_coords[0] + move_offset[0],
                self.cursor_coords[1] + move_offset[1]
            ]
            self.cursor_coords[0] = min((self.cursor_coords[0], self.w - 1))
            self.cursor_coords[0] = max((self.cursor_coords[0], 0))
            self.cursor_coords[1] = min((self.cursor_coords[1], self.h - 1))
            self.cursor_coords[1] = max((self.cursor_coords[1], 0))
