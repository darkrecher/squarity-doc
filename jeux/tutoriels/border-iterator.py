# /gamedata/tutorials/tutorial_tileset.png

"""
{
  "name": "Test des itérateurs Rect et Boder",
  "version": "2.1.0",
  "game_area": {
    "nb_tile_width": 35,
    "nb_tile_height": 25
  },
  "tile_size": 32,
  "img_coords": {
    "head_green": [96, 0],
    "hat_violet": [0, 32]
  }
}
"""

"""
Petit test rapide des itérateurs RectIterator et BorderIterator

Cliquez dans l'aire de jeu pour définir le premier coin du rectangle.
Cliquez une seconde fois pour l'autre coin.

Des têtes vertes seront crées sur toutes les cases du rectangle.
Des chapeaux violets seront ajoutés sur les bords du rectangle.

Pour activer/désactiver l'ajout de chapeaux violets
dans les coins du rectangle: cliquez sur le bouton d'action "1"

Pour passer en mode suppression d'objets:
cliquez sur le bouton d'action "2"
"""


import squarity


class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.coord_first_corner = None
        self.include_corners = True
        self.add_gobj = True


    def on_click(self, coord):

        if self.coord_first_corner is None:
            self.coord_first_corner = coord.clone()
            print("Premier coin du rectangle:", coord)
            return

        rect = squarity.Rect.from_coords(self.coord_first_corner, coord)
        self.coord_first_corner = None

        if self.add_gobj:

            for coord in squarity.RectIterator(rect):
                gobj = squarity.GameObject(coord, "head_green")
                self.layer_main.add_game_object(gobj)
            print("-" * 5 + " border coords " + "-" * 5)
            for coord in squarity.BorderIterator(rect, self.include_corners):
                gobj = squarity.GameObject(coord, "hat_violet")
                self.layer_main.add_game_object(gobj)
                print(coord)

        else:

            for coord in squarity.RectIterator(rect):
                self.layer_main.remove_at_coord(coord)


    def on_button_direction(self, direction):
        print("Les boutons de directions ne servent à rien dans ce test.")

    def on_button_action(self, action_name):
        if action_name == "action_1":
            self.add_gobj = True
            self.include_corners = not self.include_corners
            print(
                "Ajout des chapeaux dans les coins du rectangle :",
                self.include_corners
            )
        elif action_name == "action_2":
            self.add_gobj = not self.add_gobj
            if self.add_gobj:
                print("Mode 'ajout d'objets'.")
            else:
                print("Mode 'suppression d'objets'.")

