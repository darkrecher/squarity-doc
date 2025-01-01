# Manuel utilisateur de Squarity

[Squarity](http://squarity.fr) est un espace de création et de partage de jeux vidéo jouables en ligne.

Ce manuel suppose que vous avez déjà un minimum de connaissance en informatique (langage python, format JSON, ...). Si vous n'êtes pas sûr de vous, vous pouvez lire [le tutoriel soko-ban](https://github.com/darkrecher/squarity-doc/blob/master/user_manual/tutoriel_sokoban.md), plus long mais plus détaillé.

Les jeux sont en 2D "case par case", (comme les dames, le démineur, ...). L'aire de jeu est une grille composée de carrés, sur lesquels sont placés des éléments.

La "game logic" (le fonctionnement et les règles du jeu) est définie par du code en python.

Un jeu est défini par trois composants :

 - tileset,
 - configuration,
 - "game_code".


## Le tileset

Il s'agit d'une image au format jpg, png ou autre, contenant les éléments de votre jeu (décors, personnages, objets). Voici quelques exemples :

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/jeux/h2o/h2o_tileset.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/jeux/h2o/h2o_tileset.png)

![https://opengameart.org/sites/default/files/HighContrastRoguelikeCastle.png](https://opengameart.org/sites/default/files/HighContrastRoguelikeCastle.png)

Chaque élément de jeu est contenu dans un carré, qui ont tous la même taille en pixels.

Les pixels transparents, dans le format png, sont pris en compte.

Pour que votre tileset soit accessible dans Squarity, il doit être publié sur internet. Utilisez des sites d'hébergement d'images comme imgur ou imgbb. Récupérez le lien direct de votre fichier et indiquez-le dans le champ "Url de l'image".

Si l'image n'est pas trop grande, vous pouvez également la convertir en url-data, avec un service en ligne comme [ezgif](https://ezgif.com/image-to-datauri).


## La configuration

Il s'agit d'un texte, au format JSON. Voici un exemple :

```
{
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

### Fonction facultative get_tile_gamobjs(self, x, y)

Elle doit être définie dans la classe `GameModel`.

Elle renvoie la liste des objets d'une seule case. C'est une fonction d'aide que vous pouvez utiliser pour ajouter/enlever des objets dans `self.tiles`.

Le jeu fonctionnera même si vous ne la définissez pas.

```
    def get_tile_gamobjs(self, x, y):
        return self.tiles[y][x]
```

### Actions différées, actions bloquantes, annulation du rendu

Non documentés pour l'instant. Ce sera fait "dès que possible". Consultez l'exemple du jeu du magicien pour (essayer de) déterminer à quoi ça sert et comment ça fonctionne.

Ce sont les strings json renvoyées par `on_game_event`, permettant de montrer le déplacement progressif des boules de feu et les étapes intermédiaires lorsque le personnage passe une porte.


## Démarrer le jeu

Cliquez sur le bouton "Exécuter" au milieu de la page. Le jeu est entièrement réinitialisé, la classe `GameModel` est reconstruite à partir du nouveau game_code.

Si l'url du tileset a changée, l'image est rechargée. Si vous avez modifié votre tileset mais que l'url est restée la même, vous devez changer l'url, exécuter le jeu, puis remettre l'ancienne url. Ce petit désagrément sera corrigé dès que possible.

Pour l'instant, il n'est pas possible de sauvegarder la partie en cours. Le jeu recommence au début à chaque exécution et à chaque rechargement de la page.


## Quelques détails techniques

Le game_code doit être codé en python version 3.8, il est exécuté par votre navigateur web, grâce à [Pyodide](https://github.com/iodide-project/pyodide). Ça fonctionne plus ou moins bien sur les smartphones, selon leur type et beaucoup d'autres choses.

Lorsque votre code python comporte des erreurs, celles-ci apparaissent dans la zone de texte en bas de la page.

Lorsque vous appelez la fonction `print("message")`, le texte s'affiche également dans cette zone de texte. Vous pouvez utiliser cette fonctionnalité pour debugger et pour le jeu lui-même.

Évitez de déclencher des prints trop fréquents, car cela ralentit l'exécution. Chaque print modifie le DOM (la structure interne de la page web) et prend donc un peu de temps.

Une bonne pratique serait d'avoir une fonction `debug(message)`, exécutant un print uniquement si un booléen global `debug_mode` est mis à True. Avant la distribution de votre jeu, mettez ce booléen à False.


## Partager un jeu

Il est possible d'enregistrer vos jeux et de les partager avec d'autres personnes par un simple lien, si vous avez un compte [github](https://github.com).

Connectez-vous sur github, cliquez sur votre avatar en haut à droite et sélectionnez "Your gists".

Cliquez sur le bouton "+" en haut à droite pour créer un nouveau gist (un texte que vous rendez public).

Choisissez un nom pour votre texte, **attention, pas d'underscore dans le nom du fichier, uniquement des caractères alphanumériques et des tirets "-"**.

Dans le contenu du texte, mettez les informations suivantes les unes à la suite des autres :

 - L'url de votre tileset.
 - À la ligne en-dessous, un séparateur. Le plus simple est de mettre 8 tirets : `------`. Attention, pas d'espace au début de la ligne.
 - Votre configuration json.
 - Le même séparateur que précédemment. Attention, il faut exactement les mêmes caractères (les 8 tirets).
 - Votre game_code.

En bas à droite, cliquez sur la flèche du bouton pour sélectionner "Create public gist", puis cliquez sur le bouton.

Lorsque votre gist est sauvegardé, cliquez sur le bouton "Raw" à droite du fichier texte.

L'url affichée dans votre navigateur devrait avoir cette forme :

`https://gist.githubusercontent.com/votre-nom/xxx123/raw/yyy456/super-jeu.txt`

Les parties "xxx123" et "yyy456" sont de longues suites de caractères alphanumériques, permettant d'identifier votre gist de manière unique.

Supprimez la partie `yyy456/` et rechargez la page. Vérifiez que le texte brut de votre jeu s'affiche toujours.

Garder la fin de cette url, à partir de votre nom de compte github. C'est à dire : `votre-nom/xxx123/raw/super-jeu.txt`.

Ajoutez au début l'url de squarity et le préfixe `/#fetchez_githubgist_` :

`squarity.fr/#fetchez_githubgist_votre-nom/xxx123/raw/super-jeu.txt`.

Attention, si vous indiquez le protocole, mettez `http://`, et non pas `https://`. Pour l'instant le site n'est pas en HTTPS. Ce n'est pas grave, les infos qu'il contient sont publiques et non critiques.

Cette url reconstruite est le lien vers votre jeu. Vérifiez qu'il fonctionne bien, puis distribuez-le à vos ami(e)s et devenez une star de la scène vidéoludique indépendante !

Vous pouvez ensuite modifier votre gist pour améliorer ou corriger votre jeu, le lien restera le même. Attention, la mise à jour par github n'est pas instantanée. Vous devrez donc [attendre un peu](https://stackoverflow.com/questions/47066049/github-gist-raw-permalink-wont-update) avant de revérifier votre lien.

À titre d'exemple, voici un pacman créé par une gentille personne du nom de 10kbis.

Lien vers le gist : https://gist.githubusercontent.com/darkrecher/b5240940356e3bb7e59c8a2522c279d9/raw/pacman-10kbis.txt

Lien pour jouer directement : [http://squarity.fr#fetchez_githubgist_darkrecher/b5240940356e3bb7e59c8a2522c279d9/raw/pacman-10kbis.txt](http://squarity.fr#fetchez_githubgist_darkrecher/b5240940356e3bb7e59c8a2522c279d9/raw/pacman-10kbis.txt)


## Améliorations prévues

Délais de réalisation indéterminés.

 - roadmap : https://squarity.pythonanywhere.com/roadmap
 - liste des tâches en cours, publiée sur Trello : https://trello.com/b/bt91FVOH/squarity


## Contacter l'admin de Squarity

Moi c'est Réchèr. Je développe Squarity pendant mon temps libre, pour faire foisonner la créativité vidéoludique de l'humanité.

Je n'ai prévu aucun moyen "officiel" pour me contacter. Il vous reste ceux que vous connaissez éventuellement déjà (réseau social, en vrai, etc.). En dernier recours, postez une petite issue dans github. J'essayerais de les consulter fréquemment.

Amusez-vous bien !
