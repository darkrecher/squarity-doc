# Tutoriel Squarity

Ce tutoriel vous montrera comment créer un petit jeu simple avec Squarity. Il s'agit d'un jeu de type [soko-ban](https://fr.wikipedia.org/wiki/Sokoban), dans lequel un personnage doit pousser des caisses pour les ranger dans des emplacements spécifiques.

Il n'est pas nécessaire de beaucoup connaître le langage python pour effectuer ce tutoriel, mais ça peut aider.

Certaines notions seront utilisées sans être expliquées en détail, par exemple : le format JSON, la programmation objet, etc. À vous d'approfondir ces sujets par vous-mêmes, si vous le souhaitez.

Le tutoriel est un peu long, mais rassurez-vous, il est décomposé en plusieurs étapes, et vous êtes récomponsé par un résultat à chacune d'elle.

À l'issu du tutoriel (TODO : quand j'aurais fini de l'écrire), vous devriez avoir un petit jeu simple qui fonctionne avec l'outil Squarity.


## Le tileset

Pour commencer, il faudrait dessiner un "tileset", c'est à dire une image contenant tous les éléments qui s'affichent dans votre jeu.

En voici un déjà prêt :

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/sokoban_tileset.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/sokoban_tileset.png)

Il comporte 5 images d'objets :

 - un sol avec de l'herbe
 - un mur
 - une caisse
 - le personnage
 - une cible, représentant un endroit où il faut placer une caisse.

Ce tileset comporte des pixels transparents. Si vous créez vos propres tilesets, vous aurez peut-être besoin d'un logiciel de dessin capable de gérer la transparence (donc, quelque chose de mieux que Paint).

Pour pouvoir être utilisé dans un jeu, le tileset doit être publié sur internet, et vous devez connaître son url. Vous pouvez utiliser pour cela des sites d'hébergement d'images, comme https://imgbb.com/ .

Pour ce tutoriel, le tileset est déjà publié, son url est : https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/sokoban_tileset.png


## Un peu d'herbe

Nous allons créer un premier programme qui fonctionne dans Squarity, même s'il ne constitue pas un vrai jeu.

Dans le champ "Url de l'image tileset", copier-collez l'url de notre tileset :

`https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/sokoban_tileset.png`

Dans le champ en-dessous "Config du jeu (en JSON)", copier-collez la configuration suivante :

```
{
    "tile_size": 32,
    "tile_coords": {
        "herbe": [0, 0]
    }
}
```

Et dans le dernier champ : "Le code du jeu (en python)", copier-collez le code suivant :

```
class BoardModel():

    def __init__(self):

        self.w = 20 # width (largeur) : 20 cases
        self.h = 14 # height (hauteur) : 14 cases
        self.tiles = []

        for y in range(self.h):
            line = []
            for x in range(self.w):
                game_objects = []
                line.append(game_objects)
            self.tiles.append(line)

        self.tiles[3][5].append("herbe")

    def get_size(self):
        return self.w, self.h

    def export_all_tiles(self):
        return self.tiles
```

Puis cliquez sur le bouton tout en bas "<<< Exécutez le jeu"

Vous devriez voir un petit morceau d'herbe apparaître dans l'aire de jeu. Oh comme c'est impressionnant !

Votre écran devrait ressembler à ceci (certains boutons ont été supprimés pour simplifier l'image) :

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_01.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_01.png)


## Bidouillons un peu

Nous allons effectuer quelques petites modifications dans le code, pour essayer de comprendre ce que font certaines parties.

À chaque modification, vous devez recliquer sur le bouton "<<< Exécutez le jeu". Pour aller plus vite, vous pouvez utiliser le raccourci clavier Ctrl+Entrée.

Si vous faites une modification incorrecte, un message d'erreur apparaîtra en bas à gauche, que vous ne comprendrez pas forcément. Le plus simple est alors de revenir à une version du jeu qui fonctionne : faite des Ctrl-Z, ou au pire refaites les copié-collés du chapitre précédent.

Dans la configuration du jeu, modifiez la ligne `"herbe": [0, 0]`. Remplacez un zéro, ou les deux zéros, par d'autres nombres, entre 1 et 50, et regardez le résultat. Essayez de comprendre ce que ces nombres représentent. Pour vous aidez, vous pouvez réafficher dans un autre onglet de navigateur l'image du tileset que nous avons vu dans le premier chapitre.

Toujours dans la configuration du jeu, modifiez la ligne `"tile_size": 32,`. Remplacez le "32" par un autre nombre, entre 1 et 100. Essayez de comprendre ce que ce nombre représente.

Dans le code du jeu, modifiez la ligne `self.tiles[3][5].append("herbe")`. Modifiez le 3, le 5, ou les deux valeurs par d'autres nombres, entre 0 et 13. Essayez de comprendre ce que ces nombres représentent. Lequel définit l'abscisse (X) du carré d'herbe ? Lequel définit son ordonnée (Y) ?

Dupliquez la ligne `self.tiles[3][5].append("herbe")` (attention à l'indentation, il faut aussi dupliquer les espaces au début). Dans cette deuxième ligne, modifiez le 3 et le 5. Que voyez-vous dans l'aire de jeu ?

Vous pouvez re-dupliquer la ligne plusieurs fois si vous le souhaitez.

Ne vous embêtez pas à la dupliquer des dizaines de fois pour remplir d'herbe tout l'aire de jeu. Il y a une méthode plus simple que nous verrons juste après.

Pour finir, appuyez sur les boutons du jeu : les flèches, ou les actions 1 et 2. Votre jeu va planter et affichera un message d'erreur. C'est normal, nous réglerons ça dans une étape ultérieure.


## Qu'est-ce donc que tout ce code ?

Le champ "config du jeu (en JSON)" ne contient pas votre programme, mais des informations structurées.

La ligne avec le mot `tile_size` définit la taille des images dans le tileset. On gardera 32, cela correspond aux tailles (en pixels) de chaque élément dans l'image de tileset.

Les informations dans `tile_coords` définissent tous les types d'objets que vous utilisez dans votre jeu. Pour l'instant, il n'y en a qu'un seul, qui s'appelle "herbe". Les deux valeurs indiquées entre crochets correspondent aux coordonnées, dans le tileset, de la portion d'image de ce type d'objet. Il s'agit des coordonnées du coin supérieur gauche. On rajoutera très vite les autres types d'objets.

Le champ "code du jeu (en python)" contient votre programme. Ce programme doit définir une classe intitulée `BoardModel`.

Tout le code écrit après définit trois fonctions dans cette classe :

 - la fonction `__init__`, c'est la plus longue.
 - la fonction `get_size`, elle ne contient qu'une seule ligne de code.
 - la fonction `export_all_tiles`, qui ne contient elle aussi qu'une seule ligne de code.

Dans un environnement python plus classique, vous devez "instancier votre classe" pour l'utiliser après. Vous n'avez pas besoin de faire ça avec la classe `BoardModel`. Le système de Squarity s'occupe de l'instancier, et d'appeler les bonnes fonctions aux bons moments. Cependant, rien ne vous empêche de créer vos propres classes et de les instancier quand vous en avez besoin.

Dans le code, les noms de variables commençant par `self.` signifient qu'ils appartiennent à la classe. Elles sont accessible en lecture et en écriture depuis toutes les fonctions de la classe. Leur valeur est conservée entre deux "tours" de jeu.

Les variables `self.w` et `self.h` définissent la taille de l'aire de jeu, en nombre de case (w = width = largeur) (h = height = hauteur).


## Brouillon

Indentation du code :

https://python.developpez.com/cours/DiveIntoPython/php/frdiveintopython/getting_to_know_python/indenting_code.php

