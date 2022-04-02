# https://i.ibb.co/Qnz8ZVZ/cat-frag.png
# https://i.ibb.co/tYWZf8Y/cat-frag.png

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
    def __init__(self, image_prefix, w, h, x, y=0):
        self.image_prefix = image_prefix
        self.w = w
        self.h = h
        self.x = x
        self.y = y

    def get_gamobj_name(self, x, y):
        return f"{self.image_prefix}_{y:02d}_{x:02d}"

    def draw_on_tiles(self, tiles):
        for cur_y in range(self.h):
            for cur_x in range(self.w):
                gamobj = self.get_gamobj_name(cur_x, cur_y)
                tiles[cur_y + self.y][cur_x + self.x].append(gamobj)


class LayedCats:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.tiles = [[[] for x in range(self.w)] for y in range(self.h)]

    def get_tile(self, x, y):
        return self.tiles[y][x]


class Gravitator:
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
        print("y_dest", y_dest)

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
            self.cat_images = [
                cat_img for cat_img in self.cat_images if cat_img not in cats_to_lay
            ]


class GameModel:
    def __init__(self):
        self.w = 12
        self.h = 20
        self.ship_coords = (4, 3)
        # Les cat_image de la liste doivent être ordonnée par leur y_bottom.
        # La première cat_image est celle qui a la plus grande valeur de (cat_img.y+cat_img.h)
        self.cat_images = [CatImage("cat_B", 3, 3, 1, 5), CatImage("cat_A", 4, 2, 3, 3)]
        self.layed_cats = LayedCats(self.w, self.h)
        self.gravitator = Gravitator(self.layed_cats, self.cat_images)

    def export_all_tiles(self):
        exported_tiles = []
        for y in range(self.h):
            line = []
            for x in range(self.w):
                line.append(["background"])
            exported_tiles.append(line)
        ship_x, ship_y = self.ship_coords
        exported_tiles[ship_y][ship_x].append("ship_00")
        exported_tiles[ship_y][ship_x + 1].append("ship_01")

        for cat_img in self.cat_images:
            cat_img.draw_on_tiles(exported_tiles)

        return exported_tiles

    def on_game_event(self, event_name):
        if event_name == "action_1":
            self.gravitator.apply_gravity()


"""

Le sixième son (alert) :

Le son d'un monstre réveillé qui est proche du héros.

zombie : son A
mancubus : son A

imp : son B
chien des enfers : son C
crâne volant : son C
2ème œil volant : son C
minotaure : son C
1er œil volant : son C

etc : son C

squelette lance-missile : son D

mini-araignée : son E

boss araignée : son C
boss minotaure : son C



"""
