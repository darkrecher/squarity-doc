"""
Jeu de soko-ban.

Dirigez votre personnage et poussez les caisses pour les amener sur les cibles jaunes.
Vous passez au niveau suivant lorsque toutes les caisses sont sur des cibles.

Appuyez deux fois sur le bouton "1" pour réinitialiser le niveau en cours.

Ce jeu est le résultat final du tutoriel :
https://github.com/darkrecher/squarity-doc/blob/master/user_manual/tutoriel_sokoban.md

Il y a des commentaires un peu partout dans le code, pour expliquer tout un tas de choses.
"""

# Cette variable contient la définition de tous les niveaux.
# Il s'agit d'un tuple, contenant autant d'éléments que vous voulez.
# Chaque élément correspond à un niveau.
# Ses éléments sont des sous-tuples, de deux éléments chacun.
#  - Le premier élément est une chaîne de caractère, décrivant le niveau.
#    Elle s'affiche dans le log, lorsque la personne qui joue arrive à ce niveau.
#  - Le second élément est une sous-sous-tuple de 14 chaînes de caractères,
#    correspondant au plan du niveau.
#    Chaque caractère correspond à une tile dans le jeu, et décrit les game objects
#    à placer dans cette tile.
#    Pour chaque niveau, ces chaînes de caractères doivent contenir un et un seul
#    personnage. C'est à dire un seul caractère "@", ou bien un seul caractère "+".
#    Et pas les deux en même temps.
#
# La correspondance entre un caractère et ses game objects se trouve plus bas,
# dans la variable "corresp_game_objects_a_partir_char"
PLANS_DES_NIVEAUX_ET_DESCRIPTIONS = (
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
        "Origine : https://alonso-delarte.medium.com/the-basics-of-sokoban-level-formats-for-designing-your-own-sokoban-levels-51882a7a36f0",
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

# Les correspondances entre un caractère écrit dans les plans du niveau,
# et la liste de game objects qu'il faut placer sur la tile.
corresp_game_objects_a_partir_char = {
    " ": ["herbe"],
    "#": ["herbe", "mur"],
    "@": ["herbe", "personnage"],
    "$": ["herbe", "caisse"],
    ".": ["herbe", "cible"],
    "+": ["herbe", "cible", "personnage"],
    "*": ["herbe", "cible", "caisse"],
}

class BoardModel():

    def debuter_niveau(self):
        """
        Cette fonction est appelée à chaque fois qu'on change de niveau. C'est à dire :
         - au tout début du jeu, pour initialiser le premier niveau.
         - lorsque vous gagnez et que vous passez au niveau suivant.
         - lorsque vous appuyez deux fois sur l'action "1" pour réinitialiser le niveau.
        """

        # Récupération de la description à afficher et du plan du niveau,
        # en fonction du numéro de niveau actuel,
        # stocké dans la variable self.numero_niveau
        description, plan_du_niveau = PLANS_DES_NIVEAUX_ET_DESCRIPTIONS[self.numero_niveau]
        # Affichage de la description.
        print(description)
        print()
        # Cette variable contient le tableau en deux dimensions,
        # avec tous les game objects.
        # Sa structure et son utilisation sont expliqués en détail dans le tutoriel.
        self.tiles = []

        # On fait deux boucles imbriquées, pour parcourir
        # toutes les lignes de l'aire de jeu, et pour chaque ligne, on parcourt
        # toutes ses cases.
        # Les variables de boucle x et y indiquent les coordonnées de la tile
        # sur laquelle on se trouve actuellement.
        # Le but de ces deux boucles imbriquées est de remplir la variable self.tiles,
        # et d'initialiser les deux variables self.personnage_x et self.personnage_y,
        # qui contiennent les coordonnées du personnage.
        for y in range(self.h):
            # Récupération d'une ligne du plan du niveau, à partir de la variable
            # définie tout au début du code.
            # Cette ligne est une chaîne de caractère avec 20 caractères.
            ligne_plan_du_niveau = plan_du_niveau[y]
            ligne = []
            for x in range(self.w):
                # Récupération du caractère courant, depuis le plan du niveau.
                char_carte = ligne_plan_du_niveau[x]
                # Déduction, à partir de ce caractère, des game objects à placer
                # dans la tile courante.
                game_objects = corresp_game_objects_a_partir_char[char_carte]
                # On recopie la liste de game objects, sinon on aura des références
                # une seule et même liste, et ça donnera n'importe quoi quand on
                # modifiera son contenu.
                # Chaque tile doit avoir sa propre liste de game objects, qui sont
                # indépendantes les unes des autres.
                game_objects = list(game_objects)
                # On a trouvé un game object de personnage !
                # On définit les coordonnées du personnage avec les coordonnées courantes
                # de la boucle.
                # Le code ne gère pas le cas où il n'y a aucun game object personnage
                # dans l'aire de jeu. Le jeu plantera après, lorsque vous appuierez
                # sur une des flèches de direction.
                # Il ne gère pas non plus le cas où il y a plusieurs personnage.
                # Les variables seront remises à jour à chaque fois.
                # Dans les deux cas : c'est pas notre problème. On part du postulat
                # que chaque niveau contient un et un seul personnage.
                # Si ce n'est pas le cas, c'est le problème de la personne qui a créé
                # les niveaux.
                if "personnage" in game_objects:
                    self.personnage_x = x
                    self.personnage_y = y
                # Fin d'une itération de la boucle imbriquée.
                # On ajoute la case courante dans la ligne courante.
                ligne.append(game_objects)
            # Fin d'une itération de la boucle principale. On ajoute la ligne courante dans
            # self.tiles qui contiendra toute l'aire de jeu.
            self.tiles.append(ligne)

    def __init__(self):
        """
        Fonction d'initialisaton, à définir obligatoirement, quel que soit votre jeu.
        Celle-ci ne fait pas grand chose, juste définir quelques variables dont on a besoin un peu partout,
        et déclencher la fonction debuter_niveau (voir plus haut).
        """
        self.w = 20
        self.h = 14
        self.numero_niveau = 0
        self.debuter_niveau()
        self.niveau_reussi = False
        self.confirm_reset_level = False

    def get_size(self):
        return self.w, self.h

    def export_all_tiles(self):
        return self.tiles

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def coord_mouvement(self, x, y, direction):
        if direction == "R":
            x += 1
        elif direction == "L":
            x -= 1
        if direction == "D":
            y += 1
        if direction == "U":
            y -= 1
        return (x, y)

    def verifier_mouvement(self, dest_x, dest_y):
        if not (0 <= dest_x < self.w and 0 <= dest_y < self.h):
            return False
        if "mur" in self.get_tile(dest_x, dest_y):
            return False
        return True

    def on_game_event(self, event_name):

        if event_name == "action_1":
            if self.confirm_reset_level:
                self.debuter_niveau()
                self.confirm_reset_level = False
                print("réinitialisation niveau")
            else:
                self.confirm_reset_level = True
                print("Appuyez à nouveau sur le bouton '1'")
                print("pour confirmer la réinitialisation du niveau.")
            return

        self.confirm_reset_level = False

        if self.niveau_reussi:
            self.numero_niveau += 1
            self.debuter_niveau()
            self.niveau_reussi = False
            return

        personnage_dest_x, personnage_dest_y = self.coord_mouvement(
            self.personnage_x,
            self.personnage_y,
            event_name
        )
        if not self.verifier_mouvement(personnage_dest_x, personnage_dest_y):
            return

        tile_depart_perso = self.get_tile(self.personnage_x, self.personnage_y)
        tile_dest_perso = self.get_tile(personnage_dest_x, personnage_dest_y)

        if "caisse" in tile_dest_perso:
            caisse_dest_x, caisse_dest_y = self.coord_mouvement(
                personnage_dest_x,
                personnage_dest_y,
                event_name
            )
            if not self.verifier_mouvement(caisse_dest_x, caisse_dest_y):
                return
            tile_dest_caisse = self.get_tile(caisse_dest_x, caisse_dest_y)
            if "caisse" in tile_dest_caisse:
                return

            tile_dest_perso.remove("caisse")
            tile_dest_caisse.append("caisse")
            if self.verifier_caisses_sur_cible():
                print("Bravo, vous avez gagné !")
                print("Appuyez sur un bouton pour passer au niveau suivant")
                print("")
                self.niveau_reussi = True

        tile_depart_perso.remove("personnage")
        tile_dest_perso.append("personnage")
        self.personnage_x = personnage_dest_x
        self.personnage_y = personnage_dest_y

    def verifier_caisses_sur_cible(self):
        for y in range(self.h):
            for x in range(self.w):
                current_tile = self.get_tile(x, y)
                if "caisse" in current_tile and "cible" not in current_tile:
                    return False
        return True
