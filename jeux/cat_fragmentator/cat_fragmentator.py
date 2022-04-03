# https://i.ibb.co/Qnz8ZVZ/cat-frag.png
# https://i.ibb.co/tYWZf8Y/cat-frag.png
# https://i.postimg.cc/zDL4VgK3/cat-frag.png

"""


{
    "game_area": {
        "nb_tile_width": 12,
        "nb_tile_height": 20
},
    "tile_size": 32,
    "img_coords": {

        "background": [128, 32],

        "ship_00": [128, 0],
        "ship_01": [160, 0],

        "cut_left": [96, 64],
        "cut_right": [128, 64],

        "cat_A_00_00": [0, 0],
        "cat_A_00_01": [32, 0],
        "cat_A_00_02": [64, 0],
        "cat_A_00_03": [96, 0],
        "cat_A_01_00": [0, 32],
        "cat_A_01_01": [32, 32],
        "cat_A_01_02": [64, 32],
        "cat_A_01_03": [96, 32],

        "cat_B_00_00": [0, 64],
        "cat_B_00_01": [32, 64],
        "cat_B_00_02": [64, 64],
        "cat_B_01_00": [0, 96],
        "cat_B_01_01": [32, 96],
        "cat_B_01_02": [64, 96],
        "cat_B_02_00": [0, 128],
        "cat_B_02_01": [32, 128],
        "cat_B_02_02": [64, 128],

        "blorp": [0, 0]
    }
}

"""


class CatImage:
    def __init__(
        self, image_prefix, gamobjs, w, h, x, y=0, cut_left=False, cut_right=False
    ):
        self.image_prefix = image_prefix
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.cut_left = cut_left
        self.cut_right = cut_right

        if image_prefix:
            self.gamobjs = {}
            for offset_y in range(self.h):
                for offset_x in range(self.w):
                    gamobj = self._build_gamobj_name(offset_x, offset_y)
                    self.gamobjs[(offset_x, offset_y)] = gamobj
        else:
            self.gamobjs = gamobjs

    def _build_gamobj_name(self, x, y):
        return f"{self.image_prefix}_{y:02d}_{x:02d}"

    def get_gamobj_name(self, x, y):
        return self.gamobjs[(x, y)]

    def must_be_cut(self, area_x_cut, area_y_cut):
        # Et c'est bien deux signes "inférieurs stricts".
        return (self.x < area_x_cut < self.x + self.w) and self.y <= area_y_cut

    def get_gamobjs_after_cut(self, area_x_cut, is_cut_on_left):
        """
        La coordonnée area_x_cut correspond à une coordonnée dans l'aire de jeu.
        Et non pas un offset dans les éléments de l'image du chat.
        """
        gamobjs_after_cut = {}
        for offset_coord, gamobj in self.gamobjs.items():
            offset_x, offset_y = offset_coord
            if is_cut_on_left:
                if offset_x + self.x < area_x_cut:
                    gamobjs_after_cut[(offset_x, offset_y)] = gamobj
            else:
                if offset_x + self.x >= area_x_cut:
                    gamobjs_after_cut[
                        (offset_x + self.x - area_x_cut, offset_y)
                    ] = gamobj
        return gamobjs_after_cut

    def draw_on_tiles(self, tiles):
        for offset_coord, gamobj in self.gamobjs.items():
            offset_x, offset_y = offset_coord
            tiles[offset_y + self.y][offset_x + self.x].append(gamobj)

        if self.cut_left:
            for cur_y in range(self.h):
                tiles[cur_y + self.y][self.x].append("cut_left")
        if self.cut_right:
            for cur_y in range(self.h):
                tiles[cur_y + self.y][self.x + self.w - 1].append("cut_right")


class LayedCats:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.tiles = [[[] for x in range(self.w)] for y in range(self.h)]

    def get_tile(self, x, y):
        return self.tiles[y][x]


class CatImgManager:
    def __init__(self, layed_cats, cat_images):
        self.layed_cats = layed_cats
        self.cat_images = cat_images
        self.w = self.layed_cats.w
        self.h = self.layed_cats.h

    def _lay_cat(self, cat_img):
        for y in range(cat_img.h):
            for x in range(cat_img.w):
                gamobj_cat = cat_img.get_gamobj_name(x, y)
                self.layed_cats.get_tile(cat_img.x + x, cat_img.y + y).append(
                    gamobj_cat
                )

    def _apply_gravity_on_cat(self, cat_img):
        y_dest = cat_img.y + cat_img.h

        if y_dest == self.h:
            print("bottom", cat_img.y, cat_img.h, y_dest)
            # l'image de chat doit poser ses éléments dans layed_cats
            return False

        coords_dest = [(x, y_dest) for x in range(cat_img.x, cat_img.x + cat_img.w)]
        gravity_ok = all([not self.layed_cats.get_tile(x, y) for x, y in coords_dest])

        if not gravity_ok:
            print("bumped a layed cat")
            # l'image de chat doit poser ses éléments dans layed_cats
            return False

        cat_img.y += 1
        return True

    def apply_gravity(self):
        cats_to_lay = []
        for cat_img in self.cat_images:
            must_lay_cat = not self._apply_gravity_on_cat(cat_img)
            if must_lay_cat:
                cats_to_lay.append(cat_img)
                self._lay_cat(cat_img)

        if cats_to_lay:
            self.cat_images[:] = [
                cat_img for cat_img in self.cat_images if cat_img not in cats_to_lay
            ]

    def cut_cats(self, area_x_cut, area_y_cut):
        processed_cat_images = []
        for cat_img in self.cat_images:
            if cat_img.must_be_cut(area_x_cut, area_y_cut):
                print("on cutte !")
                gamobjs_cut_left = cat_img.get_gamobjs_after_cut(area_x_cut, True)
                cat_img_cut_1 = CatImage(
                    None,
                    gamobjs_cut_left,
                    area_x_cut - cat_img.x,
                    cat_img.h,
                    cat_img.x,
                    cat_img.y,
                    cat_img.cut_left,
                    True,
                )
                gamobjs_cut_right = cat_img.get_gamobjs_after_cut(area_x_cut, False)
                cat_img_cut_2 = CatImage(
                    None,
                    gamobjs_cut_right,
                    cat_img.w - area_x_cut + cat_img.x,
                    cat_img.h,
                    area_x_cut,
                    cat_img.y,
                    True,
                    cat_img.cut_right,
                )
                processed_cat_images.append(cat_img_cut_1)
                processed_cat_images.append(cat_img_cut_2)
            else:
                print("on cutte pô.")
                processed_cat_images.append(cat_img)
        self.cat_images[:] = processed_cat_images


class GameModel:
    def __init__(self):
        self.w = 12
        self.h = 20
        self.area_w = 12
        self.area_h = 20
        self.ship_coords = [4, 17]
        # Les cat_image de la liste doivent être ordonnée par leur y_bottom.
        # La première cat_image est celle qui a la plus grande valeur de (cat_img.y+cat_img.h)

        cat_test = CatImage("cat_A", {}, 4, 2, 3, 3)
        self.cat_images = [
            CatImage("cat_B", {}, 3, 3, 2, 5),
            cat_test,
        ]
        self.layed_cats = LayedCats(self.w, self.h)
        self.cat_img_manager = CatImgManager(self.layed_cats, self.cat_images)

    def export_all_tiles(self):
        exported_tiles = []
        for y in range(self.h):
            line = []
            for x in range(self.w):
                gamobjs = ["background"]
                gamobjs.extend(self.layed_cats.get_tile(x, y))
                line.append(gamobjs)
            exported_tiles.append(line)
        ship_x, ship_y = self.ship_coords
        exported_tiles[ship_y][ship_x].append("ship_00")
        exported_tiles[ship_y][ship_x + 1].append("ship_01")

        for cat_img in self.cat_images:
            cat_img.draw_on_tiles(exported_tiles)

        return exported_tiles

    def on_game_event(self, event_name):
        # TODO : faudra faire une vraie classe pour le ship. Parce que là c'est à l'arrache.
        if event_name == "L" and self.ship_coords[0] > 0:
            self.ship_coords[0] -= 1
        # -2 parce que le ship a une largeur de 2.
        elif event_name == "R" and self.ship_coords[0] < self.area_w - 2:
            self.ship_coords[0] += 1
        elif event_name == "action_1":
            self.cat_img_manager.cut_cats(self.ship_coords[0] + 1, self.ship_coords[1])
        elif event_name == "action_2":
            self.cat_img_manager.apply_gravity()
