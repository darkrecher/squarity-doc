# Documentation de référence de Squarity V1

[Squarity](http://squarity.fr) est un espace de création et de partage de jeux vidéo jouables en ligne.

Ce manuel suppose que vous ayez déjà un minimum de connaissance en informatique (langage python, format JSON, ...). Pour les personnes qui débutent, vous pouvez lire [le tutoriel soko-ban](https://github.com/darkrecher/squarity-doc/blob/master/user_manual/tutoriel_sokoban.md), plus long mais plus détaillé.

Les jeux sont en 2D "case par case", (comme les dames, le démineur, ...). L'aire de jeu est une grille composée de carrés, sur lesquels sont placés des éléments.

La "game logic" (le fonctionnement et les règles du jeu) est définie par du code en python.

Un jeu est défini par trois composants :

 - tileset,
 - configuration,
 - "game_code".


## Le tileset

Il s'agit d'une image au format jpg, png ou autre, contenant les éléments de votre jeu (décors, personnages, objets). Voici quelques exemples :

![Le tileset original (et moche) de H2O](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/jeux/h2o/h2o_tileset.png)

![Le tileset utilisé dans les mini exemples de tutoriels](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/jeux/tutoriels/tutorial_tileset.png)

Chaque élément de jeu est contenu dans un carré, qui ont tous la même taille en pixels.

Les pixels transparents, dans le format png, sont pris en compte.

Pour que votre tileset soit accessible dans Squarity, il doit être publié sur internet. Utilisez des sites d'hébergement d'images comme imgur ou imgbb. Récupérez le lien direct de votre fichier et indiquez-le dans le champ "Url de l'image".

Si l'image n'est pas trop grande, vous pouvez également la convertir en url-data, avec un service en ligne comme [ezgif](https://ezgif.com/image-to-datauri).


## La configuration

Il s'agit d'un texte, au format JSON. Voici un exemple :

```
{
    "version": "1.0.0",
    "tile_size": 32,
    "img_coords": {
        "X": [0, 0],
        ".": [32, 0],
        "H": [64, 0],
        "C": [96, 0],
        "water_right": [0, 32],
        "water_down": [32, 32],
        "water_left": [64, 32],
        "water_up": [96, 32],
        "O": [0, 256],
        "wet_grid": [32, 256],
        "S": [64, 256]
    }
}
```

Cette configuration est un dictionnaire (une "correspondance"), contenant deux éléments :

 - le premier a pour clé `tile_size` et pour valeur un nombre. Il définit la taille, en pixels, de chacun des éléments du jeu, tel que vous les avez dessinés dans votre tileset.
 - le suivant a pour clé `img_coords` et pour valeur un sous-dictionnaire :
     - chacun de ses sous-éléments a pour clé un texte (de un ou plusieurs caractères), définissant un nom d'objet dans votre jeu. La valeur correspondante est une liste de deux nombres, indiquant les coordonnées du coin supérieur gauche, dans votre tileset, de l'image de cet objet du jeu.

Par défaut, l'aire de jeu a une largeur de 20 cases et une hauteur de 14 cases. Vous pouvez changer cette taille en ajoutant un élément dans la configuration :

```
    "game_area": {
        "nb_tile_width": 22,
        "nb_tile_height": 15
    }
```


## Le game_code

Il s'agit d'un texte écrit en langage python.

Ce code doit décrire le contenu de l'aire de jeu (quels objets se trouvent sur quelle case) et ce qui se passe lorsque la personne qui joue appuie sur une touche de direction ou d'action.

Voici la structure minimale du code :

```
class GameModel():

    def __init__(self):
        self.w = 20 # width (largeur) : 20 cases
        self.h = 14 # height (hauteur) : 14 cases
        self.tiles = [
            [
                [] for x in range(self.w)
            ]
            for y in range(self.h)
        ]

    def export_all_tiles(self):
        return self.tiles

    def on_game_event(self, event_name):
        pass
```

Ce code définit une classe `GameModel`, contenant la fonction `__init__` et deux callbacks, c'est à dire des fonctions appelées automatiquement par le système de jeu.

Vous pouvez bien entendu ajouter d'autres classes, d'autres fonctions, d'autres variables membres dans `GameModel`, etc.

### Fonction GameModel.\_\_init\_\_(self)

Cette fonction est exécutée une seule fois, au début du jeu.

Ce n'est pas obligé d'initialiser une variable membre `self.tiles`, mais c'est une bonne pratique.

Cette variable membre est constituée d'un tableau de 20*14 cases, chacune contenant une liste vide. Si vous avez défini une autre taille dans la configuration, vous devez changer les variables `self.w` et `self.h`.

Vous pouvez ensuite remplir ce tableau, en ajoutant une ou plusieurs strings dans les listes vides. Ces strings correspondent aux noms des objets définis dans la partie `img_coords` de la configuration.

### Fonction GameModel.export_all_tiles(self)

Cette fonction est appelée à chaque rendu (dessin à l'écran) de l'aire de jeu.

Il faut renvoyer un tableau 2D dont chaque case contient une liste de strings. Il faut donc renvoyer "une liste de liste de liste de strings".

L'ordre des noms dans chacune des listes définit l'ordre de dessin des objets sur la case.

Cette fonction peut effectuer des traitements spécifiques, par exemple construire le nom d'un objet complexe et le placer dans une des cases. Le comportement le plus commun est de renvoyer directement `self.tiles`.

Cette fonction pourra, dans le futur, renvoyer d'autres informations sur la situation du jeu.

### Fonction GameModel.on_game_event(self, event_name)

Cette fonction est appelée à chaque événement du jeu : une action de la personne qui joue, ou bien une action différée qui a été préalablement enregistrée.

Le paramètre `event_name` indique le type d'action. Il peut prendre les valeurs suivantes :

 - "U" (up) : le bouton "haut" a été appuyé
 - "D" (down) : bouton "bas"
 - "L" (left) : bouton "gauche"
 - "R" (right) : bouton "droit"
 - "action_1" : bouton "1"
 - "action_2" : bouton "2"

Ces événements sont également déclenchés par des appuis de touches sur le clavier (flèches de direction, touches "1" et "2"). Pour cela, le focus doit être sur l'aire de jeu ou sur les boutons (il faut avoir cliqué dessus).

Le paramètre `event_name` peut prendre d'autres valeurs, dans le cas des actions différées. Cette fonctionnalité n'est pas documentée pour l'instant.

La fonction `on_game_event` a pour charge de modifier la situation du jeu, c'est à dire le contenu de `self.tiles`, en fonction de l'événement. Elle implémente la plus grande partie de la "game logic".

Un rendu complet de l'aire de jeu est déclenché après chaque appel de cette fonction. Sauf si on indique explicitement qu'on ne le veut pas (fonctionnement non documenté pour l'instant).


## Données renvoyées par on_game_event

La fonction `on_game_event` peut renvoyer une chaîne de caractère JSON, contenant différentes indications que le moteur de Squarity interprétera. Ce n'est pas obligatoire, la fonction peut ne contenir aucune instruction `return`, dans ce cas elle renverra `None` et le moteur ne fera rien de plus.

Vous trouverez des exemples de ces JSON dans [le jeu du sorcier](https://squarity.pythonanywhere.com/game/#fetchez_example_magician).

### Action différée

Ce JSON peut contenir une clé `delayed_actions`. La valeur doit être une liste de sous-dictionnaire, avec une clé `name` et une clé `delay_ms`.

Exemple de ligne de code renvoyant un JSON avec une action différée:

`return """ { "delayed_actions": [ {"name": "my_action", "delay_ms": 500} ] } """`

Avec ce JSON, le moteur exécutera à nouveau la fonction `GameModel.on_game_event`, 500 millisecondes plus tard. Le paramètre `event_name` aura la valeur `"my_action"`.

Lors de cet exécution différée de `on_game_event`, il est tout à fait possible de renvoyer un autre JSON avec une (ou plusieurs) autres actions différées, et ainsi de suite.

### Blocage/déblocage de l'interface

Le JSON peut contenir une clé `player_locks` et/ou une clé `player_unlocks`. Les valeurs doivent être des listes de chaînes de caractères.

Chaque chaîne correspond à une "raison" de bloquer l'interface de la personne qui joue.

L'interface est entièrement bloquée tant qu'il y a au moins une raison en cours : les boutons de directions et d'actions apparaissent en grisé, les touches de clavier et les clics de souris n'ont aucun effet dans le jeu.

Lorsque vous bloquez l'interface, il est fortement conseillé de prévoir en même temps un enchaînement d'action différée, qui finira par débloquer l'interface.

Ces blocages d'interface peuvent être utile pour montrer des animations prédéfinies, à regarder sans jouer.

Petit exemple :

 - Vous renvoyez le JSON `""" { "delayed_actions": [ {"name": "play_anim", "delay_ms": 500} ], "player_locks": ["anim"] } """`, pour bloquer l'interface tout en planifiant l'action différée `"play_anim"`.
 - Cette action différée déclenchera éventuellement d'autres actions différées.
 - Au bout d'un moment, l'une de ces actions renvoie le JSON `""" { "player_unlocks": ["anim"] } """` pour débloquer l'interface.

Si vous avez bloqué l'interface avec plusieurs raisons différentes et que vous ne savez plus trop lesquelles, vous pouvez renvoyer le déblocague `*` pour supprimer en une fois toutes les raisons en cours. Exemple : `""" { "player_unlocks": ["*"] } """`

### Annulation du rendu

Si la fonction `on_game_event` ne change pas la disposition des game objects, vous pouvez indiquer au moteur de Squarity que ce n'est pas la peine de redessiner l'aire de jeu. Ça permet d'optimiser l'exécution de votre jeu.

Le JSON peut contenir une clé `redraw`, qui vaut 1 par défaut. Si vous la définissez à 0, le rendu n'est pas effectué pour cette fois.

Exemple : `"""{ "redraw": 0 }"""`

Il est bien entendu possible d'avoir plusieurs clés en même temps, et plusieurs éléments dans les listes, le tout dans un même JSON. Vous pourriez, en une seule fois, planifier 10 actions différées, bloquer l'interface pour 15 raisons différentes, la débloquer pour 20 autres raisons, le tout en annulant le rendu.


## Démarrer le jeu

Cliquez sur le bouton "Exécuter" au milieu de la page. Le jeu est entièrement réinitialisé, la classe `GameModel` est reconstruite à partir du nouveau game_code.

Si l'url du tileset a changée, l'image est rechargée. Si vous avez modifié votre tileset mais que l'url est restée la même, vous devez changer l'url, exécuter le jeu, puis remettre l'ancienne url. Ce petit désagrément sera corrigé dès que possible.

Pour l'instant, il n'est pas possible de sauvegarder la partie en cours. Le jeu recommence au début à chaque exécution et à chaque rechargement de la page.


## Quelques détails techniques

Le game_code doit être codé en python version 3.7.4, il est exécuté par votre navigateur web, grâce à [Pyodide](https://github.com/iodide-project/pyodide). Ça fonctionne plus ou moins bien sur les smartphones, selon leur type et beaucoup d'autres choses.

Lorsque votre code python comporte des erreurs, celles-ci apparaissent dans la zone de texte en bas de la page.

Lorsque vous appelez la fonction `print("message")`, le texte s'affiche également dans cette zone de texte. Vous pouvez utiliser cette fonctionnalité pour debugger et pour le jeu lui-même.

Évitez de déclencher des prints trop fréquents, car cela ralentit l'exécution. Chaque print modifie le DOM (la structure interne de la page web) et prend donc un peu de temps.

Une bonne pratique serait d'avoir une fonction `debug(message)`, exécutant un print uniquement si un booléen global `debug_mode` est mis à True. Avant la distribution de votre jeu, mettez ce booléen à False.

