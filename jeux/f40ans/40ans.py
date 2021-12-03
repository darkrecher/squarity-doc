# https://i.postimg.cc/3r98fXXH/sprites.png
# https://i.ibb.co/qNzWPMz/sprites.png
# https://i.ibb.co/jZqwWMX/sprites.png


"""
{
  "game_area": {
    "nb_tile_width": 8,
    "nb_tile_height": 7
  },
  "tile_size": 64,

  "img_coords": {
    "pote_head": [0, 0],
    "pote_torso": [0, 64],
    "pote_legs": [0, 128],

    "me_head": [288, 0],
    "me_torso": [288, 64],
    "me_legs": [288, 128],

    "bg_outside_00_00": [369, 1],
    "bg_outside_00_01": [369, 65],
    "bg_outside_00_02": [369, 129],
    "bg_outside_00_03": [369, 193],
    "bg_outside_00_04": [369, 257],
    "bg_outside_00_05": [369, 321],
    "bg_outside_00_06": [369, 385],
    "bg_outside_01_00": [433, 1],
    "bg_outside_01_01": [433, 65],
    "bg_outside_01_02": [433, 129],
    "bg_outside_01_03": [433, 193],
    "bg_outside_01_04": [433, 257],
    "bg_outside_01_05": [433, 321],
    "bg_outside_01_06": [433, 385],
    "bg_outside_02_00": [497, 1],
    "bg_outside_02_01": [497, 65],
    "bg_outside_02_02": [497, 129],
    "bg_outside_02_03": [497, 193],
    "bg_outside_02_04": [497, 257],
    "bg_outside_02_05": [497, 321],
    "bg_outside_02_06": [497, 385],
    "bg_outside_03_00": [561, 1],
    "bg_outside_03_01": [561, 65],
    "bg_outside_03_02": [561, 129],
    "bg_outside_03_03": [561, 193],
    "bg_outside_03_04": [561, 257],
    "bg_outside_03_05": [561, 321],
    "bg_outside_03_06": [561, 385],
    "bg_outside_04_00": [625, 1],
    "bg_outside_04_01": [625, 65],
    "bg_outside_04_02": [625, 129],
    "bg_outside_04_03": [625, 193],
    "bg_outside_04_04": [625, 257],
    "bg_outside_04_05": [625, 321],
    "bg_outside_04_06": [625, 385],
    "bg_outside_05_00": [689, 1],
    "bg_outside_05_01": [689, 65],
    "bg_outside_05_02": [689, 129],
    "bg_outside_05_03": [689, 193],
    "bg_outside_05_04": [689, 257],
    "bg_outside_05_05": [689, 321],
    "bg_outside_05_06": [689, 385],
    "bg_outside_06_00": [753, 1],
    "bg_outside_06_01": [753, 65],
    "bg_outside_06_02": [753, 129],
    "bg_outside_06_03": [753, 193],
    "bg_outside_06_04": [753, 257],
    "bg_outside_06_05": [753, 321],
    "bg_outside_06_06": [753, 385],
    "bg_outside_07_00": [817, 1],
    "bg_outside_07_01": [817, 65],
    "bg_outside_07_02": [817, 129],
    "bg_outside_07_03": [817, 193],
    "bg_outside_07_04": [817, 257],
    "bg_outside_07_05": [817, 321],
    "bg_outside_07_06": [817, 385],

    "osef": [0, 0]
  }
}
"""

SCENE_WIDTH = 8
SCENE_HEIGHT = 7


class SceneObject:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.visible = True

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def draw(self, func_get_tile):
        raise NotImplemented


class Scene:
    def __init__(self, name):
        self.name = name
        self.ordered_scene_objects = []
        self.indexed_scene_objects = {}

    def add_object(self, scene_object):
        self.ordered_scene_objects.append(scene_object)
        name_obj = scene_object.name
        if name_obj in self.indexed_scene_objects:
            raise Exception(
                f"Ajout de plusieurs scene objets ayant le même nom, not supposed to happen. {name_obj}"
            )
        self.indexed_scene_objects[name_obj] = scene_object


class Background(SceneObject):
    def __init__(self, name):
        super().__init__(0, 0, name)
        self.array_gamobjs = []
        for y in range(SCENE_HEIGHT):
            line_gamobjs = []
            for x in range(SCENE_WIDTH):
                line_gamobjs.append(f"bg_{self.name}_{x:02}_{y:02}")
            self.array_gamobjs.append(line_gamobjs)

    def draw(self, func_get_tile):
        for y in range(SCENE_HEIGHT):
            for x in range(SCENE_WIDTH):
                func_get_tile(x, y).append(self.array_gamobjs[y][x])


class CharacterMe(SceneObject):

    GAMOBJS_NORMAL = (
        ("me_head", 0, -2),
        ("me_torso", 0, -1),
        ("me_legs", 0, 0),
    )

    def __init__(self, x, y):
        super().__init__(x, y, "me")
        self.current_gamobjs = CharacterMe.GAMOBJS_NORMAL

    def draw(self, func_get_tile):
        # TODO : check pour vérifier que x et y sont dans les bornes de l'aire de jeu.
        for gamobj, offset_x, offset_y in self.current_gamobjs:
            func_get_tile(self.x + offset_x, self.y + offset_y).append(gamobj)


class GameModel:
    def get_tile(self, map_x, map_y):
        return self.tiles[map_y][map_x]

    def __init__(self):

        self.w = SCENE_WIDTH
        self.h = SCENE_HEIGHT

        self.tiles = []
        for map_y in range(self.h):
            line = []
            for map_x in range(self.w):
                line.append([])
            self.tiles.append(line)

        self.scene_outside = Scene("outside")
        self.scene_outside.add_object(Background("outside"))
        self.scene_outside.add_object(CharacterMe(4, 5))
        self.current_scene = self.scene_outside

    def export_all_tiles(self):

        # TODO : factorize this, ou bien c'est de la daube.
        self.tiles = []
        for map_y in range(self.h):
            line = []
            for map_x in range(self.w):
                line.append([])
            self.tiles.append(line)

        for scene_obj in self.current_scene.ordered_scene_objects:
            if scene_obj.visible:
                scene_obj.draw(self.get_tile)

        return self.tiles

    def on_game_event(self, event_name):
        # Toute la gestion de la game logic est en dur là dedans, à l'arrache.
        # Pas le temps de faire mieux.
        move_coords = squarity.MOVE_FROM_DIR.get(event_name)
        if move_coords is not None:
            self.current_scene.indexed_scene_objects["me"].move(*move_coords)
