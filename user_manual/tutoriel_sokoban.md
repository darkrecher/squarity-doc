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

Dans le champ en-dessous *"Config du jeu (en JSON)"*, copier-collez la configuration suivante :

```
{
    "tile_size": 32,
    "tile_coords": {
        "herbe": [0, 0]
    }
}
```

Et dans le dernier champ : *"Le code du jeu (en python)"*, copier-collez le code suivant :

```
class BoardModel():

    def __init__(self):

        self.w = 20
        self.h = 14
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


## Quelques explications concernant tout ce code

Le champ *"config du jeu (en JSON)"* ne contient pas votre programme, mais des informations structurées.

La ligne avec le mot `tile_size` définit la taille des images (en pixels) dans le tileset. On gardera 32 pour ce tileset, sinon ça fait n'importe quoi.

Les informations dans `tile_coords` définissent tous les types d'objets que vous utilisez dans votre jeu. Pour l'instant, il n'y en a qu'un seul, qui s'appelle "herbe".

Les deux valeurs entre crochets correspondent aux coordonnées, dans le tileset, de la portion d'image de ce type d'objet. Il s'agit des coordonnées du coin supérieur gauche. On rajoutera très vite les autres types d'objets.

Le champ *"code du jeu (en python)"* contient votre programme. Ce programme doit définir une classe intitulée `BoardModel`.

Tout le code écrit après définit trois fonctions dans cette classe :

 - la fonction `__init__`, c'est la plus longue.
 - la fonction `get_size`, elle ne contient qu'une seule ligne de code.
 - la fonction `export_all_tiles`, qui ne contient elle aussi qu'une seule ligne de code.

Dans un environnement python plus classique, vous devez "instancier votre classe" pour l'utiliser après. Mais vous n'avez pas besoin de faire ça avec la classe `BoardModel`. Le système de Squarity s'occupe de l'instancier et d'appeler les bonnes fonctions aux bons moments.

Cependant, rien ne vous empêche de créer vos propres classes et de les instancier quand vous en avez besoin.

Dans le code, les noms de variables commençant par `self.` signifient qu'elles appartiennent à la classe. Elles sont accessible en lecture et en écriture depuis toutes les fonctions de la classe. Leur valeur est conservée entre deux "tours" de jeu.

Les variables ne commençant pas par `self.`, par exemple `line` ou `game_objects` ne sont pas conservées. Vous les définissez et les utilisez dans une fonction, ensuite elles sont effacées.

Les variables `self.w` et `self.h` définissent la taille de l'aire de jeu, en nombre de case. w = width = largeur = 20 cases, h = height = hauteur = 14 cases.

La variable `self.tiles` est importante. Elle contient tous les objets à afficher dans le jeu. C'est un tableau en deux dimensions. Chaque case de ce tableau peut contenir plusieurs objets. Un objet est identifié par une chaîne de caractère, correspondant à son nom.

Dans notre programme, nous avons ajouté un seul objet dans une seule case de ce tableau. Cet objet a pour nom : "herbe".

Selon ce que vous avez bidouillé dans le chapitre précédent, vous avez peut-être ajouté un objet dans plusieurs cases du tableau.

(TODO : re screenshot en indiquant où sont tous les trucs dont je viens de parler).


## Plein d'herbe

Dans le code du jeu, remplacez la ligne

`game_objects = []`

par

`game_objects = ["herbe"]`

Exécutez votre jeu. Vous devriez voir de l'herbe partout.

La ligne que vous venez de modifier se trouve dans une boucle (pour être exact : dans une boucle de boucle). Elle est exécutée pour chaque case de l'aire de jeu, ce qui ajoute de l'herbe partout.

La ligne `self.tiles[3][5].append("herbe")` n'est plus utile, mais on va la laisser pour l'instant.


## Attention à l'indentation

Vous avez peut-être un peu de mal à comprendre entièrement le code du jeu. Ne vous inquiétez pas, ça n'empêche pas de terminer ce tutoriel, et vous pouvez aussi lire un cours sur le python après.

Il y a cependant un point très important à prendre en compte avec ce langage de programmation : l'indentation est significative. Autrement dit : faites attention aux espaces qui se trouvent au début de chaque ligne, ils servent à indiquer la manière dont les blocs de code sont imbriquées.

Pour une explication plus détaillée, consultez [cette page](https://python.developpez.com/cours/DiveIntoPython/php/frdiveintopython/getting_to_know_python/indenting_code.php)


## Un deuxième type d'objet

L'herbe c'est bien, mais un peu monotone. Nous allons ajouter un nouveau type.

Remplacez la configuration du jeu par ceci :

```
{
    "tile_size": 32,
    "tile_coords": {
        "herbe": [0, 0],
        "mur": [32, 0]
    }
}
```

La configuration définit maintenant deux types d'objets, l'herbe et le mur. N'oubliez pas la virgule entre les deux, sinon ça ne marchera pas.

Puis, dans la ligne `self.tiles[3][5].append("herbe")`, remplacer le mot `"herbe"` par `"mur"`. Attention de bien garder les guillemets.

L'aire de jeu devrait afficher de l'herbe, et un seul objet de type mur.


## Vocabulaire spécifique au jeu

Une image utilisée pour afficher un élément dans l'aire de jeu s'appellent **image de tile**. Autres appellations : **image de tuile**, **tile_image**, ou tout simplement **image**.

La grande image contenant toutes les images de tile s'appelle le **tileset**. Autres appellations : **tilesheet**, **image set**, **image atlas**, **atlas**. On utilise le mot "atlas" pour représenter le fait que c'est un ensemble d'image exhaustif. Comme les atlas de cartes géographiques.

Une case dans l'aire de jeu s'appelle une **tile**. Autres appellations : **tuile**, **case**. Ces tiles sont organisées sous forme d'un tableau en deux dimensions, appellé **tiles** (au pluriel). Dans notre programme, ce tableau est enregistré dans la variable `self.tiles`. Ce tableau a une largeur de 20 tiles et une hauteur de 14 tiles.

Pour repérer une tile dans le tableau, on utilise les coordonnées x et y.

X augmente lorsqu'on va vers la droite. Les tiles tout à gauche ont pour coordonnée x = 0. Les tiles tout à droite ont pour coordonnée x = 19.

Y augmente lorsqu'on va vers le bas. Les tiles tout en haut ont pour coordonnée y = 0. Les tiles tout en bas ont pour coordonnée y = 13.

Les graphiques que l'on dessine en cours de maths ont la coordonnée Y dans l'autre sens (Y augmente lorsqu'on va vers le haut). En programmation, on préfère avoir un Y qui augmente lorsqu'on va vers le bas. C'est plus logique car ça correspond au sens de lecture, au sens des pixels sur l'écran, etc.

Les coordonnées sont comptées à partir de zéro, et non pas à partir de un, parce que c'est comme ça qu'on fait en informatique, et c'est plus logique ainsi.

Un élément placé dans une tile s'appelle un **objet de jeu**. Autres appellations : **game object**, **gamobj**, **gobject**, **gobj**. Il peut y avoir plusieurs game object sur une même tile. Ils seront dessinés les uns par-dessus des autres, au même endroit.

Chaque game object possède un **type de game object**. Autre appellation : **game object type**. Dans notre programme, les mots "herbe" et "mur" sont des types de game object.

Dans la documentation de Squarity, et dans les noms de variables des programmes, il faut essayer au maximum d'utiliser ce vocabulaire, pour qu'il devienne commun à toutes les personnes utilisant Squarity.

On évitera d'utiliser les noms "objet" et "type" tout seul, car ce sont des termes trop génériques, et qui sont déjà beaucoup utilisés en programmation.

On peut se permettre d'utiliser les noms anglais ("game object", "tile", ...) dans un texte français, puisque la langue française possède déjà des anglicismes. Vous pouvez aussi faire le contraire, puisque la langue française possède des francicismes.

Dans notre programme, nous avons commencé par placer dans toutes les tiles un seul game object, de type "herbe". Puis, pour une tile spécifique, celle qui est aux coordonnées x=5, y=3, nous avons ajouté un second game object, de type "mur".

(TODO : schéma avec le tableau des tiles)

Dans la tile x=5, y=3, on ne voit pas le game object "herbe", car le game object "mur" est dessiné par dessus, et la recouvre entièrement. Mais cette tile possède bien deux game objects.


## Quelques règles du fonctionnement de Squarity

 - On peut créer, supprimer, déplacer les game objects dans les tiles, et d'une tile vers une autre.
 - Une tile peut contenir autant de game objects que l'on veut.
 - Une tile peut posséder plusieurs game objects de même type.
 - L'ordre des game object dans une tile est important, car il définit l'ordre dans lequel ils seront affichés.
 - On ne peut pas déplacer, ajouter ou supprimer des tiles. Ce sont les cases du tableau, et le tableau ne change pas.
 - Pour l'instant, on ne peut pas changer la largeur ou la hauteur du tableau. C'est forcément largeur = 20, hauteur = 14. Mais ce sera amélioré dans des versions futures de Squarity.
 - On ne peut pas placer un game object sur plusieurs tiles en même temps. (Mais on peut créer plusieurs game object de même type et les placer chacun sur une tile)
 - **On ne peut pas placer un game object à cheval sur plusieurs tiles**. Les coordonnées sont forcément des nombres entiers. Vous ne pourrez donc jamais avoir un personnage qui se déplace légèrement et se retrouve entre deux tiles, comme dans le premier Zelda ou comme dans les jeux Bomberman. C'est un choix de conception dans Squarity, qui permet de simplifier la création des jeux.

Dans la configuration du jeu, la donnée `tile_coords` permet de lister tous les types de game object de votre jeu, et de faire la correspondance avec leurs images respectives.

Au passage, le nom `tile_coords` est un peu illogique, et je le renommerais en `img_coords` dès que possible.


## Une liste de liste de liste

La notion de "tableau" n'existe pas vraiment en python, on ne peut créer que des listes.

Mais on peut créer une liste, dont chaque élément est une sous-liste.

 - La variable `self.tiles` est une liste de 14 éléments, représentant les 14 lignes de l'aire de jeu,
   - chacun de ces éléments est une sous-liste de 20 éléments, représentant les 20 cases d'une ligne de l'aire de jeu,
     - chacun de ces éléments est une sous-sous-liste ayant un nombre variable d'éléments, représentant les game objects de la case de l'aire de jeu,
       - chacun de ces éléments est un nom, correspondant à un type de game object.





