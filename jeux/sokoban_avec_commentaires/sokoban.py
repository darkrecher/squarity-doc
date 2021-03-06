"""
Jeu de soko-ban.

Dirigez votre personnage et poussez les caisses pour les amener sur les cibles jaunes.
Vous passez au niveau suivant lorsque toutes les caisses sont sur des cibles.

Appuyez deux fois sur le bouton "1" pour réinitialiser le niveau en cours.

Ce jeu est le résultat final du tutoriel :
https://github.com/darkrecher/squarity-doc/blob/master/user_manual/tutoriel_sokoban.md

Il y a des commentaires un peu partout dans le code, pour expliquer tout un tas de choses.
"""

# url : https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/sokoban_tileset.png
TILESET = """
{
    "tile_size": 32,
    "tile_coords": {
        "herbe": [0, 0],
        "mur": [32, 0],
        "caisse": [64, 0],
        "personnage": [0, 32],
        "cible": [32, 32]
    }
}
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
        Pour ce jeu en particulier, elle ne fait pas grand chose, juste définir quelques
        variables dont on a besoin un peu partout,
        et déclencher la fonction debuter_niveau (voir plus haut).
        """
        # Longueur et largeur de l'aire de jeu. À définir obligatoirement, mais on ne peut pas
        # les changer. (Le moteur de jeu Squarity ne sait pas gérer d'autres tailles)
        self.w = 20
        self.h = 14
        # Le numéro actuel du niveau. On commence au niveau 0. À chaque niveau gagné,
        # cette variable augmente de un.
        # !!!! Si vous voulez tricher à ce jeu, modifiez cette variable !!!!!
        # Mais attention, si vous mettez une valeur trop grande (supérieure au nombre total
        # de niveau dans le jeu), ça va planter.
        self.numero_niveau = 0
        # Initialisation du tout premier niveau.
        self.debuter_niveau()
        # Cette variable permet de savoir si on vient de réussir le niveau courant, ou pas.
        # Lorsqu'on réussit le niveau courant, on ne passe pas tout de suite au suivant.
        # Il faut effectuer une action (flèches de direction, action 1, ou action 2) pour
        # passer au niveau suivant. Ça permet de vous laisser le temps de réaliser
        # que vous venez de gagner, et qu'on va passer au niveau suivant.
        # Et il faut une variable pour gérer cet état intermédiaire.
        self.niveau_reussi = False
        # Cette variable permet de représenter le fait qu'il faut appuyer deux fois
        # sur le bouton action_1 pour réinitialiser le niveau.
        # Une première fois pour demander la réinitialisation (la variable devient True).
        # Une seconde fois pour confirmer la réinitialisation (le niveau se réinitialise
        # et la variable se remet à False).
        self.confirm_reset_level = False

    def get_size(self):
        """
        Fonction qui renvoie la taille de l'aire de jeu.
        C'est obligé de la créer, c'est obligé de renvoyer un tuple de deux éléments,
        avec la largeur et la hauteur (en nombre de case) de l'aire de jeu.
        Et dans le fonctionnement actuel de Squarity, la taille de l'aire de jeu
        est obligatoirement (20, 14).
        Donc pour l'instant, cette fonction ne sert à rien, mais plus tard, ça servira.
        """
        return self.w, self.h

    def export_all_tiles(self):
        """
        Fonction qui renvoie le contenu de l'aire de jeu.
        Il faut renvoyer un tableau à 2 dimensions, dont chaque élément est une liste,
        contenant des chaînes de caractères, correspondant à des game objects.
        Ça mérite des explications beaucoup plus détaillées qu'une simple phrase. Ces
        explications sont dans le tutoriel, dont le lien est mentionné tout en haut.
        Autre petite info : on n'est pas obligé d'utiliser la variable self.tiles.
        Ce qui est important, c'est que cette fonction renvoie un tableau à 2 dimensions.
        Si vous construisez ce tableau d'une autre manière qu'en utilisant self.tiles,
        c'est tout à fait possible.
        C'est vous qui voyez.
        """
        return self.tiles

    def get_tile(self, x, y):
        """
        La fonction qui renvoie une tile de l'aire de jeu.
        On peut ensuite ajouter, supprimer, ou vérifier la présence de game objects
        dans cette tile. La présence de cette fonction est facultative.
        Mais c'est plus simple de s'en servir, et ça fait un code plus clair.
        """
        return self.tiles[y][x]

    def coord_mouvement(self, x, y, direction):
        """
        Cette fonction renvoie un tuple contenant deux coordonnées (x, y).
        Celles-ci sont définies à partir des deux coordonnées passées dans les
        deux premiers paramètres, auxquelles on applique un mouvement, de une seule case.
        La direction du mouvement est indiquée par le troisième paramètre :
        R: Right, L: Left, D: Down, U: Up.
        """
        # On modifie l'une des deux coordonnées (x ou y), de +1 ou -1, selon la direction,
        # définie par le troisième paramètre de la fonction.
        if direction == "R":
            x += 1
        elif direction == "L":
            x -= 1
        if direction == "D":
            y += 1
        if direction == "U":
            y -= 1
        # Après modification, on renvoie le tuple de coordonnées.
        return (x, y)

    def verifier_mouvement(self, dest_x, dest_y):
        """
        Vérifie qu'il est possible de déplacer un game object vers la destination indiquée
        par les coordonnées en paramètre.
        La fonction vérifie que les coordonnées se situent bien dans l'aire de jeu
        (c'est à dire qu'on n'est pas sorti par l'un des bords),
        et elle vérifie également que la tile de destination ne contient pas
        un game object de type "mur". (On ne peut rien déplacer sur une tile ayant un mur).

        Attention, c'est une vérification de base. On ne vérifie rien concernant
        la présence de caisses. C'est pour ça que dans la fonction on_game_event,
        il y a une vérification supplémentaire, dans le cas d'une caisse qui peut
        se déplacer (ou pas), sur une tile ne contenant pas de caisse (ou si).
        """
        # Vérification que les coordonnées sont dans l'aire de jeu.
        if not (0 <= dest_x < self.w and 0 <= dest_y < self.h):
            return False
        # Vérification que la case de destination ne contient pas un mur.
        if "mur" in self.get_tile(dest_x, dest_y):
            return False
        # C'est bon, on a fait toutes les vérifs de base. Si on est arrivée jusqu'ici dans
        # le code, ça veut dire qu'on peut faire le mouvement. On renvoie True.
        return True

    def verifier_caisses_sur_cible(self):
        """
        Cette fonction renvoie un booléen, qui vaut True si toutes les caisses du niveau
        sont placées sur une cible.
        La fonction ne considère pas les cibles sur lesquelles aucune caisse n'est posée.
        Cela signifie qu'il peut y avoir des niveaux contenant plus ce cibles que de caisses,
        il est quand même possible de les gagner.
        Par contre, on ne peut pas gagner les niveaux ayant moins de cibles que de caisses.

        Cette fonction renverrait systématiquement True dans le cas d'un niveau
        n'ayant aucune caisse (car concrètement, il n'y aurait aucune caisse qui
        n'est pas sur une cible).
        Mais lorsqu'on est dans ce cas, cette fonction n'est pas appelée
        (voir le code de game_event)
        """
        # On parcourt toutes les tiles de l'aire de jeu.
        # Il faut une boucle dans une boucle pour cela.
        # La première boucle parcourt les lignes de l'aire de jeu,
        # la seconde parcourt, pour chaque ligne, les tiles qui la composent.
        for y in range(self.h):
            for x in range(self.w):
                # Récupération des game objects de la tile courante.
                current_tile = self.get_tile(x, y)
                # Si il y a une caisse, mais pas de cible, alors on renvoie tout
                # de suite False. Pas la peine de regarder les autres tiles.
                # Vous n'avez pas (encore) gagné.
                if "caisse" in current_tile and "cible" not in current_tile:
                    return False
        # Lorsqu'on arrive à cet endroit du code, on a parcouru toute l'aire de jeu,
        # mais on n'a trouvé aucune caisse qui n'est pas sur une cible. Cela signifie
        # que toutes les caisses (quel que soit leur nombre) ont été bien placé.
        # On renvoie True pour indiquer que vous avez gagné le niveau.
        return True

    def on_game_event(self, event_name):
        """
        La fonction la plus importante de tout le jeu. Elle est appelée automatiquement
        par le système de Squarity, lorsque vous appuyez sur une des touches du jeu :
        l'une des flèches de direction, ou bien l'un des deux boutons d'action.
        Le paramètre event_name est une chaîne de caractère.
        Il indique quelle bouton vous avez appuyé.

        Cette fonction fait tout un tas de trucs. Pour le détail, consultez
        les commentaires dans le code.
        """

        # --- Gestion du passage au niveau suivant ---
        if self.niveau_reussi:
            # Si on est arrivé à cet endroit du code, cela signifie que vous venez
            # de réussir un niveau, et que le message indiquant cette réussite a été
            # écrit dans le log.
            # Dans ce cas, on ne regarde pas la variable event_name. Quel que soit le
            # bouton d'action que vous avez appuyé, on passe au niveau suivant.

            # Augmentation de la variable indiquant à quel niveau vous vous trouvez actuellement.
            # Attention, il n'y a aucune vérification sur cette variable, concernant le nombre
            # de niveau. Par exemple, si le jeu comporte 4 niveau (numéroté de 0 à 3),
            # rien n'empêce cette variable d'arriver jusqu'à 4. Et dans ce cas, ça va planter,
            # car au moment d'initialiser le niveau d'index 4, on ne peut pas y accéder
            # car il n'existe pas.
            # Pour éviter un message d'erreur, il faut faire en sorte que le dernier niveau
            # de votre jeu ne puisse pas être gagné. C'est ce que j'ai fait, car le dernier
            # niveau ne comporte aucune caisse. (Voir un peu plus loin pourquoi les
            # niveaux sans caisse ne peuvent être gagnés).
            self.numero_niveau += 1
            # Réinitialisation du niveau. Comme on vient d'augmenter la variable numero_niveau,
            # ça va réinitialiser le contenu de self.tiles, mais avec le plan du niveau suivant.
            self.debuter_niveau()
            # On remet cette variable à zéro, car le passage au niveau suivant vient
            # d'être effectué. Cette variable se remettra à True lorsque vous gagnerez
            # le prochain niveau.
            self.niveau_reussi = False
            return

        # --- Gestion du bouton d'action numéro 1 ---
        if event_name == "action_1":
            if self.confirm_reset_level:
                # Lorsqu'on arrive à cet endroit du code, cela signifie que
                # c'est la deuxième fois à la suite que vous appuyez sur le bouton d'action "1".
                # Il faut réinitialiser le niveau.
                # On re-appelle la fonction "debuter_niveau", comme on l'a fait au début.
                # Ça remodifie entièrement tout le contenu de self.tiles, en replaçant les caisses
                # et le personnage tel qu'ils sont au début du niveau.
                self.debuter_niveau()
                # Et on remet à zéro la confirmation de réinitialisation du niveau.
                self.confirm_reset_level = False
                print("réinitialisation niveau")
            else:
                # Lorsqu'on arrive à cet endroit du code, cela signifie que c'est
                # la première fois que vous appuyez sur le bouton d'action "1".
                # On met à True la variable confirm_reset_level, pour retenir le fait que vous
                # venez d'appuyez sur ce bouton. Et on écrit un petit message pour avertir
                # que vous pouvez réinitialiser le niveau.
                # Mais on ne fait rien de plus.
                self.confirm_reset_level = True
                print("Appuyez à nouveau sur le bouton '1'")
                print("pour confirmer la réinitialisation du niveau.")
            # Il n'y a rien de plus à faire dans le cas
            # où vous venez d'appuyer sur le bouton d'action "1".
            # On s'en va de la fonction.
            return

        # Il n'y a pas de gestion du bouton d'action numéro 2.
        # Ce bouton ne fait rien de spécial dans ce jeu.

        # Remise à zéro de la confirmation de la réinitialisation.
        # Ainsi, si vous avez préalablement appuyé sur le bouton "1", mais que ensuite
        # vous appuyez sur un autre bouton, le niveau ne sera pas réinitialisé.
        # La confirmation est systématiquement remise à zéro. Même lorsque ce n'est pas nécessaire
        # Par exemple, si vous appuyez plusieurs fois sur des boutons de direction, on remet
        # à chaque fois la confirmation à zéro. C'est un peu idiot, car ce n'est pas la peine.
        # Mais c'est plus simple de faire comme ça, que de vérifier si c'est nécessaire
        # puis de remettre à zéro dans ce cas. (Ça rajouterai juste du code en plus,
        # qui n'est pas nécessaire). Ce n'est pas grave de modifier plusieurs fois de suite
        # une simple variable.
        self.confirm_reset_level = False

        # --- Gestion des boutons de directions ---

        # Détermination des coordonnées de destination du personnage, en fonction de ces
        # coordonnées actuelles et de la direction du mouvement.
        # Les variables personnage_dest_x, personnage_dest_y contiennent les coordonnées
        # sur laquelle il faudrait placer le personnage, si jamais le mouvement est possible.
        # (Ce qu'on n'a pas encore vérifié, mais ça vient après).
        personnage_dest_x, personnage_dest_y = self.coord_mouvement(
            self.personnage_x,
            self.personnage_y,
            event_name
        )

        # Vous allez rire. Dans le cas où vous avez appuyé sur le bouton d'action "2",
        # on reste dans le code. On ne quitte pas la fonction, alors que ça aurait été plus
        # logique de le faire.
        # La fonction coord_mouvement a renvoyé des coordonnées de destination égale aux
        # coordonnées initiale. La suite du code s'exécute avec cette situation.
        # On vérifie un mouvement qui n'en est pas un.
        # On enlève le game object du personnage pour ensuite le remettre sur la même tile.
        # Mais tout fonctionne bien comme il faut. Rigolo, non ?

        # Revenons aux choses sérieuses. Dans le cas où vous avez vraiment appuyé sur
        # un bouton de direction.
        # On vérifie si le mouvement à faire est possible. Si non, on quitte directement la fonction,
        # il n'y a rien de plus à effectuer.
        if not self.verifier_mouvement(personnage_dest_x, personnage_dest_y):
            return

        # Maintenant qu'on a les coordonnées de départ et d'arrivée du personnage,
        # on peut récupérer les tiles de départ et d'arrivée, et leurs game objects.
        tile_depart_perso = self.get_tile(self.personnage_x, self.personnage_y)
        tile_dest_perso = self.get_tile(personnage_dest_x, personnage_dest_y)

        # --- Gestion du cas où le mouvement du personnage pousserait une caisse ---
        if "caisse" in tile_dest_perso:
            # Détermination des coordonnées d'arrivée de la caisse.
            # On prend la même direction de mouvement que précédemment, et on
            # l'applique, non pas sur les coordonnées initiales du personnage,
            # mais sur ces coordonnées d'arrivée. C'est à dire là où se trouve
            # actuellement la caisse.
            caisse_dest_x, caisse_dest_y = self.coord_mouvement(
                personnage_dest_x,
                personnage_dest_y,
                event_name
            )
            # On vérifie que les coordonnées d'arrivée de la caisse sont valides.
            # Sinon, on ne fait pas du tout de mouvement, ni du personnage, ni d'une caisse.
            # Ce cas arriverait lorsque vous essayeriez de pousser une caisse contre
            # un mur, ou contre un bord de l'écran.
            if not self.verifier_mouvement(caisse_dest_x, caisse_dest_y):
                return
            # On récupère la tile d'arrivée de la caisse avec ses game objects.
            # On a déjà consulté le contenu de cette tile, lorsqu'on a appelé
            # la fonction verifier_mouvement juste avant. Mais on doit la re-récupérer
            # pour faire une dernière verif, et aussi pour déplacer la caisse
            # si c'est possible.
            tile_dest_caisse = self.get_tile(caisse_dest_x, caisse_dest_y)
            # On vérifie qu'il n'y a pas déjà une caisse sur la tile où on veut
            # pousser la caisse. Sinon, pas de mouvement possible.
            if "caisse" in tile_dest_caisse:
                return

            # Si on est arrivée jusqu'ici, ça veut dire que le mouvement que vous
            # voulez faire à votre personnage est possible (on a tout vérifié)
            # et que en plus ce mouvement va aussi provoquer un poussage de caisse.
            # Dans cette partie du code, on s'occupe uniquement du poussage de caisse.
            # Le mouvement du personnage se fait juste après.

            # C'est tout simple, on enlève le game object "caisse" de sa tile de départ,
            # et on le rajoute sur sa tile d'arrivée.
            tile_dest_perso.remove("caisse")
            tile_dest_caisse.append("caisse")
            # On vient de pousser une caisse. Il faut vérifier si la nouvelle position des
            # caisses correspond à une situation de réussite du niveau.
            # À noter que si un niveau ne comporte aucune caisse, alors on ne pousse jamais
            # aucune caisse, donc on n'arrive jamais à cet endroit du code, et donc on
            # n'appelle jamais cette fonction, et donc le niveau n'est jamais gagné.
            # C'est cette astuce qui est utilisée pour le dernier niveau de ce jeu.
            # On ne peut pas aller plus loin, car il ne comporte aucune caisse.
            # Si on permettait d'aller plus loin, ça planterait, car on ne fait pas de
            # vérification sur le nombre de niveau.
            if self.verifier_caisses_sur_cible():
                # Toutes les caisses sont chacune sur un game object cible. Youpi !!
                # Un petit message de félicitations.
                print("Bravo, vous avez gagné !")
                print("Appuyez sur un bouton pour passer au niveau suivant")
                print("")
                # On se contente de définir cette variable à True. On ne fait rien d'autre.
                # Le prochain niveau sera affiché lors de votre prochain appui
                # sur un bouton d'action. Cela vous permet d'admirer le niveau que vous
                # venez de réussir, avant de passer au suivant.
                self.niveau_reussi = True

        # Arrivé à cet endroit du code, on a fait un mouvement de caisse, ou pas.
        # Dans tous les cas, le mouvement du personnage a été validé, et il faut maintenant
        # l'effectuer.
        # Comme pour une caisse, on enlève le game object de type personnage de la tile
        # où il se trouve actuellement, et on l'ajoute sur la tile où il doit être après
        # le mouvement.
        tile_depart_perso.remove("personnage")
        tile_dest_perso.append("personnage")
        # Et pour finir, on met à jour les coordonnées du personnage. On en a besoin pour
        # réaliser les prochaines actions. Et ça permet de ne pas reparcourir toute l'aire
        # de jeu à chaque fois, pour retrouver où est placé le personnage.
        self.personnage_x = personnage_dest_x
        self.personnage_y = personnage_dest_y

        # Et voilà. Si vous avez tout lu jusqu'ici, bravo !
        # Si vous avez tout lu et tout compris, super-bravo, vous êtes totalement
        # capable de programmer vos propres jeux. Amusez-vous bien !
