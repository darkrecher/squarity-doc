# https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/sokoban_tileset.png

# TODO : message d'erreur quand l'url de l'image ne permet pas de récupérer une image.

"""
{
    "version": "2.0.0",
    "tile_size": 32,
    "game_area": {
      "nb_tile_width": 20,
      "nb_tile_height": 14
    },
    "img_coords": {
        "herb": [0, 0],
        "wall": [32, 0],
        "crate": [64, 0],
        "avatar": [0, 32],
        "target": [32, 32]
    }
}
"""

import squarity
Coord = squarity.Coord

LEVELS_AND_DESCRIPTIONS = (
    (
        "Origine de ce niveau : http://www.sokobano.de/wiki/index.php?title=Optimizer",
        (
            "                    ",
            "          ####      ",
            "         ##. ##     ",
            "     ##### .  #     ",
            "     #   #  # #     ",
            "     # $ #  # #     ",
            "     # $      #     ",
            "     ######  ##     ",
            "          # ##      ",
            "          # #       ",
            "          # #       ",
            "         ## ##      ",
            "         # @ #      ",
            "         #   #      ",
        )
    ),
    (
        "Origine : https://www.mathsisfun.com/games/sokoban.html (un peu transformé)",
        (
            "    #####           ",
            "    #   #      ###  ",
            "    #$  #      #.#  ",
            "  ###  $###    # #  ",
            "  #  $  $ #   ## ###",
            "### # ### #   #   .#",
            "#   # ### #####  ###",
            "# $  $           ..#",
            "########### ###  ###",
            "          # # #   .#",
            "          # # ## ###",
            "          # #  # #  ",
            "          # #  #.#  ",
            "          #@#  ###  ",
        )
    ),
    (
        "Origine : https://www.mathsisfun.com/games/sokoban.html",
        (
            "                    ",
            "                    ",
            "                    ",
            "         #####      ",
            "##########   #      ",
            " @      . $  #      ",
            "########## $.#      ",
            "       #.##$ #      ",
            "       # # . ##     ",
            "       #$ *$$.#     ",
            "       #   .  #     ",
            "       ## #####     ",
            "        # #         ",
            "        # #         ",
        )
    ),
    (
        "Origine : https://alonso-delarte.medium.com/the-basics-of-sokoban-level-formats-"
        "for-designing-your-own-sokoban-levels-51882a7a36f0",
        (
            "       #####        ",
            "   #####   #####    ",
            "   #           #    ",
            "   #  ### ###  #    ",
            " #### #     # ####  ",
            "##    #  *  #    #  ",
            "   $  # *+*      #  ",
            "##    #  *  #    #  ",
            " #### #     # ####  ",
            "   #  ### ###  #    ",
            "   #           #    ",
            "   #####   #####    ",
            "       #####        ",
            "                    ",
        ),
    ),
    (
        "Bravo, vous avez réussi tous les niveaux. Pourquoi ne pas en profiter pour créer les vôtres ?",
        (
            "         @          ",
            "#  #  ### #   #  #  ",
            "#  #  #    # #   #  ",
            "####  ##    #    #  ",
            "#  #  #     #       ",
            "#  #  ###   #    #  ",
            "                    ",
            "        ####        ",
            "       #    #       ",
            "      # .  . #      ",
            "      #      #      ",
            "      #  ..  #      ",
            "       #    #       ",
            "        ####        ",
        ),
    ),
)

ELEMS_FROM_CHAR = {
    " ": ["herb"],
    "#": ["herb", "wall"],
    "@": ["herb", "avatar"],
    "$": ["herb", "crate"],
    ".": ["herb", "target"],
    "+": ["herb", "target", "avatar"],
    "*": ["herb", "target", "crate"],
}


# TODO : récupère le premier gamobj ayant un sprite_name spécifique,
# sur une tile spécifique.
# faudrait mettre ça dans la lib squarity, je sais pas où.
def get_gobj_with_sprite_name(tile, sprite_name):
    for gobj in tile.game_objects:
        if gobj.sprite_name == sprite_name:
            return gobj
    return None


class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.transition_delay = 70
        self.layer_background = squarity.Layer(self, self.w, self.h, False)
        self.layers.insert(0, self.layer_background)

        self.gobj_avatar = squarity.GameObject(Coord(0, 0), "avatar")
        self.gobj_avatar.plock_transi = squarity.PlayerLockTransi.INVISIBLE
        self.main_layer.add_game_object(self.gobj_avatar)
        self.delay_avatar = None
        self.current_level = 0
        self.initiate_level()
        self.victory = False
        self.restart_level = False

    def initiate_level(self):
        descrip, level_map = LEVELS_AND_DESCRIPTIONS[self.current_level]
        print(descrip)
        layer_from_elem = {
            "herb": self.layer_background,
            "wall": self.layer_background,
            "crate": self.main_layer,
            "target": self.layer_background,
        }
        # TODO : itération à la con, of course.
        for y in range(self.h):
            for x in range(self.w):

                coord = Coord(x, y)
                self.layer_background.get_tile(coord).game_objects = []
                # TODO : C'est pas pratique du tout ça.
                for gobj in self.main_layer.get_tile(coord).game_objects:
                    if gobj.sprite_name == "crate":
                        # TODO : la fonction Layer.remove_game_object est buggée !
                        #self.main_layer.remove_game_object(gobj)
                        gobj.layer_owner = None
                        self.main_layer.get_tile(coord).game_objects.remove(gobj)

                char_def = level_map[y][x]
                elems_to_add = ELEMS_FROM_CHAR[char_def]
                for elem in elems_to_add:
                    if elem == "avatar":
                        self.gobj_avatar.move_to(coord, self.delay_avatar)
                    else:
                        layer = layer_from_elem[elem]
                        layer.add_game_object(squarity.GameObject(coord, elem))
        self.delay_avatar = 0

    # TODO : generic tool
    def in_bounds(self, coord):
        if not (0 <= coord.x < self.w):
            return False
        if not (0 <= coord.y < self.h):
            return False
        return True

    def on_button_direction(self, direction):
        if self.victory:
            self.victory = False
            self.current_level += 1
            if self.current_level >= len(LEVELS_AND_DESCRIPTIONS):
                self.current_level = 0
            self.initiate_level()
            return

        self.restart_level = False
        # TODO : homogénéité move_to_dir et move_dir.
        coord_avatar_dest = self.gobj_avatar.get_coord()
        coord_avatar_dest.move_to_dir(direction)
        if not self.in_bounds(coord_avatar_dest):
            return
        tile_av_dest_bg = self.layer_background.get_tile(coord_avatar_dest)
        if get_gobj_with_sprite_name(tile_av_dest_bg, "wall") is not None:
            return
        tile_av_dest_main = self.main_layer.get_tile(coord_avatar_dest)

        crate_to_push = get_gobj_with_sprite_name(tile_av_dest_main, "crate")
        if crate_to_push is not None:
            coord_crate_dest = Coord(coord=coord_avatar_dest)
            coord_crate_dest.move_to_dir(direction)
            if not self.in_bounds(coord_crate_dest):
                return
            tile_cr_dest_bg = self.layer_background.get_tile(coord_crate_dest)
            if get_gobj_with_sprite_name(tile_cr_dest_bg, "wall") is not None:
                return
            tile_cr_dest_main = self.main_layer.get_tile(coord_crate_dest)
            if get_gobj_with_sprite_name(tile_cr_dest_main, "crate") is not None:
                return
            crate_to_push.move_dir(direction)

        self.gobj_avatar.move_dir(direction)
        self.check_crate_on_target()

    def check_crate_on_target(self):

        all_crate_on_target = True
        # TODO : re itération à la con, of course.
        for y in range(self.h):
            for x in range(self.w):
                coord = Coord(x, y)
                tile_background = self.layer_background.get_tile(coord)
                tile_main = self.main_layer.get_tile(coord)
                has_target = get_gobj_with_sprite_name(tile_background, "target") is not None
                has_crate = get_gobj_with_sprite_name(tile_main, "crate") is not None
                if has_target ^ has_crate:
                    all_crate_on_target = False

        if all_crate_on_target:
            print("Victoire !")
            print("Appuyez sur un bouton pour passer au niveau suivant.")
            self.victory = True

    def on_button_action(self, action_name):
        if action_name == "action_1":
            if self.restart_level:
                self.initiate_level()
                self.restart_level = False
            else:
                print("Appuyez une seconde fois sur le bouton '1' pour redémarrer le niveau.")
                self.restart_level = True

