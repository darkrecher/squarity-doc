# https://i.ibb.co/FJYCn5n/loops-in-pool-ld47.png

# Attention, l'hébergeur imgbb s'amuse à changer la taille des images.
# Il faut lui dire explicitement de pas le faire.
# https://i.ibb.co/Scr4ymr/loops-in-pools-ld47.png
# https://i.ibb.co/bKYLQ0F/loops-in-pools-ld47.png
# https://i.ibb.co/PMbKkk1/loops-in-pools-ld47.png
# https://i.ibb.co/g6wW1vG/loops-in-pools-ld47.png
# https://i.ibb.co/687v3CM/loops-in-pools-ld47.png
# https://i.ibb.co/n3v36pk/loops-in-pools-ld47.png
# https://i.ibb.co/n3v36pk/loops-in-pools-ld47.png
# https://raw.githubusercontent.com/darkrecher/squarity-doc/master/jeux/loops_in_pool/loops_in_pool_ld47.png

# v = Vine. m = Mud.

CONF_JSON = """
  {
    "tile_size": 32,
    "tile_coords": {
      "ground": [0, 0],
      "cursor": [32, 0],
      "selection": [64, 0],
      "v0": [0, 32],
      "v1": [32, 32],
      "v2": [64, 32],
      "v3": [96, 32],
      "v4": [128, 32],
      "v5": [160, 32],
      "v6": [192, 32],
      "v7": [224, 32],
      "v0_lit": [0, 64],
      "v1_lit": [32, 64],
      "v2_lit": [64, 64],
      "v3_lit": [96, 64],
      "v4_lit": [128, 64],
      "v5_lit": [160, 64],
      "v6_lit": [192, 64],
      "v7_lit": [224, 64],
      "m0": [0, 96],
      "m1": [32, 96],
      "m2": [64, 96],
      "m3": [96, 96],
      "m4": [128, 96],
      "m5": [160, 96],
      "m6": [192, 96],
      "m7": [224, 96],
      "l0": [0, 128],
      "l1": [32, 128],
      "l2": [64, 128],
      "l3": [96, 128],
      "l4": [128, 128],
      "l5": [160, 128],
      "l6": [192, 128],
      "l7": [224, 128]
    }
  }
"""

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

class BoardModel():

    def __init__(self):
        # print(VINE_CONNECTIONS)
        self.w = 10 # 20 # width (largeur) : 20 cases
        self.h = 7 # 14 # height (hauteur) : 14 cases
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

        self.tiles[0][0].triangle_types = ["l"] * 8
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

        #self.propagate_some_mud()
        self.must_start_mud = True
        self.finished_init = False
        self.coord_tile_to_exchange = None
        self.tile_coords_not_watered = []
        for x in range(self.w):
            for y in range(self.h):
                self.tile_coords_not_watered.append((x, y))

    def story(self, text):
        print(text)
        self.text_outing = 5

    def get_size(self):
        return self.w, self.h

    def get_tile_gamobjs(self, x, y):
        return self.tiles[y][x]

    def export_tile(self, x, y):
        the_tile = self.tiles[y][x]
        gamobjs = []

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

        if self.coord_tile_to_exchange is not None and self.coord_tile_to_exchange == [x, y]:
            gamobjs.append("selection")
        if self.cursor_coords == [x, y]:
            gamobjs.append("cursor")
        return gamobjs

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
            return

        for x, y, idx_tri in triangles_next_to_water:
            self.tiles[y][x].triangle_types[idx_tri] = "l"
        return """{ "delayed_actions": [ {"name": "propagate_some_water", "delay_ms": 400} ] }"""

    def get_vines(self, x, y):
        return list(VINES_SET.intersection(set(self.get_tile_gamobjs(x, y))))

    def get_inside_triangles(self, connected_vines):
        xs = [ vine[0] for vine in connected_vines ]
        ys = [ vine[1] for vine in connected_vines ]
        bounding_x1 = min(xs)
        bounding_x2 = max(xs)
        bounding_y1 = min(ys)
        bounding_y2 = max(ys)
        out_x1 = bounding_x1 - 1
        out_x2 = bounding_x2 + 1
        out_y1 = bounding_y1 - 1
        out_y2 = bounding_y2 + 1
        # print("bounds", bounding_x1, bounding_y1, ";", bounding_x2, bounding_y2)
        insides = []
        out_triangles = set()

        for vine in connected_vines:
            for tri_type_cur in TRIANGLES_FROM_VINE[vine[2]]:

                localised_tri = (vine[0], vine[1], tri_type_cur)
                already_processed = False
                for inside_triangle_pack in insides:
                    if localised_tri in inside_triangle_pack:
                        already_processed = True
                        break
                if already_processed:
                    continue

                current_triangle_pack = [localised_tri]
                current_triangle_pack_validated = []
                is_pack_out = False
                # print("start prop", localised_tri)

                while current_triangle_pack:
                    cur_tri_propagate = current_triangle_pack.pop(0)
                    # print("cur_tri_propagate", cur_tri_propagate)
                    if cur_tri_propagate in current_triangle_pack_validated:
                        # print("already in")
                        continue
                    if cur_tri_propagate in out_triangles:
                        is_pack_out = True
                        # print("out because already out")
                        break
                    if cur_tri_propagate[0] in (out_x1, out_x2) or cur_tri_propagate[1] in (out_y1, out_y2):
                        is_pack_out = True
                        # print("out because limits")
                        break
                    # print("add in current prop")
                    current_triangle_pack_validated.append(cur_tri_propagate)
                    for offset_x, offset_y, tri_type_adj, blocking_vine in TRI_CONNECTIONS[cur_tri_propagate[2]]:
                        blocked_by_vine = False
                        if blocking_vine is not None:
                            localised_blocking_vine = (cur_tri_propagate[0], cur_tri_propagate[1], blocking_vine)
                            if localised_blocking_vine in connected_vines:
                                blocked_by_vine = True
                        if not blocked_by_vine:
                            current_triangle_pack.append(
                                (cur_tri_propagate[0] + offset_x, cur_tri_propagate[1] + offset_y, tri_type_adj)
                            )

                # print("tris out or not", is_pack_out, current_triangle_pack_validated)
                if is_pack_out:
                    out_triangles.union(current_triangle_pack_validated)
                else:
                    insides.append(current_triangle_pack_validated)

        return insides


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

        if self.text_outing:
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
                return """{ "delayed_actions": [ {"name": "propagate_some_water", "delay_ms": 400} ] }"""

        if event_name == "propagate_some_water":
            return self.propagate_some_water()


        if event_name == "action_1":
            if not self.finished_init:
                self.story("Please wait while propagating mud")
                return

            x, y = self.cursor_coords
            if self.tiles[y][x].triangle_types != ALL_MUD:
                self.story("You can not exchange two tiles if they are not covered with mud")
                return

            if self.coord_tile_to_exchange is None:
                self.coord_tile_to_exchange = list(self.cursor_coords)
                return

            if self.coord_tile_to_exchange is not None and self.coord_tile_to_exchange == self.cursor_coords:
                # print("canceling selection")
                self.coord_tile_to_exchange = None
                return

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
            the_tile = self.tiles[y][x]
            potential_vines = []
            for idx_tri_1, idx_tri_2, idx_vine in VINES_INTER_TRI:
                if the_tile.triangle_types[idx_tri_1] == "m" and the_tile.triangle_types[idx_tri_2] == "m" and not the_tile.vine_types[idx_vine]:
                    potential_vines.append(idx_vine)

            if not potential_vines:
                self.story("You can use your special power only on")
                self.story("a tile where there is not enough vines,")
                self.story("or on a tile fully covered with water.")
                return

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

        move_offset = board_model.MOVE_FROM_DIR.get(event_name)
        if move_offset is not None:

            # weird bug that happened only once...
            if self.coord_tile_to_exchange is not None:
                x, y = self.coord_tile_to_exchange
                if self.tiles[y][x].triangle_types != ALL_MUD:
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

