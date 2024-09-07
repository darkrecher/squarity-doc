# Documentation de référence de Squarity V2

Squarity est un espace de création et de partage de jeux vidéo jouables dans un navigateur web. Les jeux se déroulent sur une grille en 2D composée de carrés. La "game logic" (le fonctionnement et les règles du jeu) est définie par du code en python.

Ce document décrit les fonctionnalités de la version 2.1.0 du moteur de Squarity. Il suppose que vous avez déjà un minimum de connaissance en python. Si ce n'est pas le cas, vous pouvez les acquérir avec ce tutoriel en français : https://python.doctor/

Un jeu est défini par trois informations :

 - le tileset,
 - la configuration,
 - le "game code".

Pour l'instant, Squarity ne gère pas de comptes ni de profil personnel. Vous devez sauvegardez vos jeux par vous-même, sur votre disque dur ou ailleurs. Vous pouvez les publier sur un gist github (voir plus loin : TODO).


## Le tileset

Le tileset est comme un atlas : c'est une image regroupant toutes les "sous-images" des éléments de votre jeu (décor, personnages, bonus, ...).

Pour que votre tileset soit accessible dans Squarity, il doit être publié sur internet : dans un repository github, sur site d'hébergement d'images, etc.

Dans l'interface de Squarity, indiquez le lien direct vers votre fichier image dans le champ "Url de l'image".


## Configuration json

Exemple :

```
{
    "name": "Mon super jeu",
    "version": "2.1.0",
    "tile_size": 32,
    "game_area": {
      "nb_tile_width": 20,
      "nb_tile_height": 14
    },
    "img_coords": {
      "a_game_object": [0, 0],
      "another_game_object": [32, 0]
    }
}
```

Dans l'interface, indiquez cette configuration dans la zone de texte "Config du jeu".

### Informations génériques

`name` (chaîne de caractère) : le nom de votre jeu. Il est écrit dans le "title" de la page web, précédé du texte "Squarity - ".

`version` (chaîne de caractère) : version du moteur du jeu, indiquez "2.1.0". Voir plus loin : TODO.

`tile_size` (nombre entier) : la taille par défaut, en pixels dans le tileset, des images représentant les éléments de votre jeu.

`game_area` (sous-dictionnaire contenant deux nombres entiers) : largeur et hauteur de l'aire de jeu, en nombre de cases (tiles).

### Définition des images

Il s'agit des images représentant les éléments de votre jeu (les "Game Objects"). Elles sont définies dans un sous-dictionnaire, identifié par la clé `img_coords`.

Chaque clé de ce sous-dictionnaire est une chaîne de caractère que vous pourrez utiliser dans votre code python, pour identifier une image de Game Object.

Chaque valeur de ce sous-dictionnaire est une liste de 2 entiers. Ils représentent les coordonnées x et y, en pixels dans le tileset, du coin supérieur gauche de l'image.

Il est possible d'ajouter d'autres valeurs après les deux entiers de la liste. Voir plus loin : TODO.

### Versions du moteur Squarity

La seule information utile de la clé `version` est le premier nombre, situé avant le premier point.

Si ce nombre est "1", la version utilisée sera "1.0.0".

Si ce nombre est "2", la version utilisée sera la version 2.x.y la plus récente (actuellement : "2.1.0"). Vous n'avez donc pas accès aux précédentes versions 2.x.y, mais elles sont censées être rétro-compatibles.


## Notions de base du "game code"

Il s'agit du programme définissant la logique de votre jeu, il est écrit en langage python.

Dans l'interface, placez ce programme dans la zone de texte "Le code du jeu".

Ce programme doit contenir une classe intitulée `GameModel`, qui hérite de la classe `squarity.GameModelBase`.

Cette classe sera instanciée automatiquement par le moteur Squarity. Elle contient des fonctions de callback, que vous aurez éventuellement redéfinie. Ces fonctions sont appelées automatiquement sur certains événements (appui sur un bouton du jeu, clic de souris, etc.)

Votre `GameModel` contient des objets de type `squarity.Layer`, ordonnés dans une liste. Chacun de ces layers contient un tableau de "tiles". Ce tableau est en 2 dimensions, la largeur et la hauteur correspondent à celles de l'aire de jeu (les valeurs `nb_tile_width` et `nb_tile_height` indiquées dans la config JSON).

Une tile représente une case de l'aire de jeu. Chaque tile peut contenir des `squarity.GameObject`, représentant des objets de votre jeu. Un GameObject est toujours placé sur une seule tile de seul layer. Un GameObject possède des coordonnées (x, y) indiquant la tile d'appartenance dans le layer. Un GameObject possède une variable membre `sprite_name`, de type chaîne de caractère. Cette variable doit avoir pour valeur l'un des noms définis dans le dictionnaire `img_coords` de la configuration JSON.

La suite de cette documentation contient des exemples de code. Vous pouvez les copier-coller dans Squarity puis cliquer sur le bouton "Executer". Vous devriez voir des informations apparaître dans la console (la fenêtre de texte en bas de l'aire de jeu). Pour les exemples un peu plus complexes, il faut trouver le bon endroit où placer le code, mais vous êtes très fort et vous allez y arriver.


## Schéma d'affichage, calculs des tailles

TODO.

Vous ne pouvez pas définir la taille en pixel des cases réellement affichées. Cette-ci dépend de la taille de la fenêtre du navigateur affichant Squarity, qui est définie par la personne qui joue.

Le calcul est effectué comme suit:

 - calcul de la largeur possible et de la hauteur possible des tiles (en pixel, à l'écran) :
   - `largeur_possible = largeur_fenêtre_du_jeu / config.nb_tile_width`
   - `hauteur_possible = hauteur_fenêtre_du_jeu / config.nb_tile_height`
 - détermination de la taille réelle des tiles, en prenant la plus petite :
   - `taille_tile_ecran = min(largeur_possible, hauteur_possible)`
 - application de cette taille pour la largeur et la hauteur à l'écran :
   - `largeur_tile_ecran = taille_tile_ecran`
   - `hauteur_tile_ecran = taille_tile_ecran`

Ensuite, une mise à l'échelle est effectuée, pour afficher les images ayant une taille égale à `config.tile_size` (en pixel dans le tileset), vers des images ayant une taille égale à `taille_tile_ecran` (en pixel à l'écran).

La mise à l'échelle est effectuée selon l'algorithme "proche voisin", sans aucun traitement ni anti-aliasing. C'est à dire que des gros pixels carrés seront visibles si vos images de tileset sont petites et que la personne qui joue a choisi une grande fenêtre de jeu.


## class Direction

### Liste des directions

Il s'agit d'une classe dont il n'existe que 8 instances, 4 pour les directions de base (haut, droite, bas, gauche) et 4 autres pour les diagonales. Ces 8 instances sont stockées dans l'objet `squarity.dirs`.

Les instances peuvent être comparées entre elles, par exemple : `my_dir == dirs.Up`. Elles peuvent être converties en entier et en string. Elles possèdent une variable `vector` qui est un tuple de deux éléments, indiquant respectivement son déplacement en X et son déplacement en Y.

Tableau récapitulatif des directions et de leurs caractéristiques :

| `d = `           | `int(d)` | `str(d)`       | `d.vector[0]` | `d.vector[1]` |
|------------------|----------|----------------|---------------|---------------|
| `dirs.Up`        |    0     | `"up"`         |     0         |    -1         |
| `dirs.UpRight`   |    1     | `"up_right"`   |    +1         |    -1         |
| `dirs.Right`     |    2     | `"right"`      |    +1         |     0         |
| `dirs.DownRight` |    3     | `"down_right"` |    +1         |    +1         |
| `dirs.Down`      |    4     | `"down"`       |     0         |    +1         |
| `dirs.DownLeft`  |    5     | `"down_left"`  |    -1         |    +1         |
| `dirs.Left`      |    6     | `"left"`       |    -1         |     0         |
| `dirs.UpLeft`    |    7     | `"up_left"`    |    -1         |    -1         |

### Rotations

Les méthodes `turn_cw` et `turn_ccw` renvoient une direction tournée, respectivement dans le sens des aiguilles d'une montre et dans le sens inverse. L'angle de rotation par défaut est de 90 degrés.

```
d = squarity.dirs.Right
print(d.turn_cw())
# La valeur 'down' s'affiche dans la console.
```

Le second paramètre permet de préciser l'angle de rotation. C'est un entier indiquant le nombre de pas de 45 degrés.

```
d = squarity.dirs.UpRight
print(d.turn_ccw(3))
# La valeur 'left' s'affiche dans la console.
```

## class Coord

Cette classe sert à identifier une case dans l'aire de jeu ou dans un layer. Elle possède deux variables membres `x` et `y`, de type `int`.

### Instanciation

La classe peut être créée en indiquant un X et un Y, ou à partir d'une autre `Coord`. Les `Coord` peuvent être comparées entre elles.

```
coord_1 = squarity.Coord(5, 2)
coord_2 = squarity.Coord(coord=coord_1)
print(coord_1 == coord_2)
# La valeur 'True' s'affiche dans la console
```

### Fonctions de base

Les `Coord` peuvent être utilisées comme clés dans un dictionnaire. Elles ont une représentation textuelle, ce qui permet de les écrire avec un `print`. Elles peuvent être dupliquées avec la méthode `clone`.

```
coord_1 = squarity.Coord(5, 2)
coord_2 = coord_1.clone()
print(coord_2)
# Le texte "<Coord 5, 2 >" s'affiche dans la console
```

### Fonctions de modification

La méthode `move_dir` permet de modifier les coordonnées en la décalant dans une direction donnée, sur une distance donnée (avec un `int`). La distance par défaut est 1.

```
coord_1 = squarity.Coord(5, 2)
coord_1.move_dir(squarity.dirs.Right, 2)
print(coord_1)
# "<Coord 7, 2 >"
```

La méthode `move_by_vect` permet de modifier les coordonnées en lui appliquant un décalage. Le décalage est spécifié par une `Coord` dans le paramètre `vector`, ou bien directement par les coordonnées `x` et `y`.

Attention, il n'y a pas de blocage sur les bords. Les mouvements peuvent amener une coordonnée dans des zones négatives, ou en dehors de l'aire de jeu.

```
coord_1 = squarity.Coord(5, 2)
coord_vect = squarity.Coord(0, -3)
coord_1.move_by_vect(vector=coord_vect)
coord_1.move_by_vect(x=1, y=-3)
print(coord_1)
# "<Coord 6, -4 >"
```


## class Rect

Définit un rectangle, à partir de 4 paramètres de type `int` : le X et le Y du coin supérieur droit, la largeur la hauteur.

Les coordonnées dans le rectangle s'étendent depuis X jusqu'à (X+largeur-1) en abscisse, et depuis Y jusqu'à (Y+hauteur-1) en ordonnée.

### Fonction in_bounds

Indique si une coordonnée se trouve à l'intérieur du rectangle.

```
rect = squarity.Rect(5, 2, 3, 5)
# Les coordonnées dont le X vaut (5, 6 ou 7) et dont le Y vaut (2, 3, 4, 5 ou 6)
# sont comprises dans le rectangle.
print(rect.in_bounds(squarity.Coord(0, 0)))
# La valeur False s'affichera dans la console.
```

### Fonction on_borders

Indique si une coordonnée se trouve sur un bord du rectangle.

```
rect = squarity.Rect(5, 2, 3, 5)
for x in range(4, 10):
    coord_1 = squarity.Coord(x, 3)
    border = rect.on_border(coord_1)
    print(coord_1, "est-elle au bord ?", border)
# Les informations suivantes vont s'afficher:
# <Coord 4, 3 > est-elle au bord ? False
# <Coord 5, 3 > est-elle au bord ? True
# <Coord 6, 3 > est-elle au bord ? False
# <Coord 7, 3 > est-elle au bord ? True
# <Coord 8, 3 > est-elle au bord ? False
# <Coord 9, 3 > est-elle au bord ? False
```


## class GameObject

transition par défaut quand on change des coordonnées.

## class Layer

## class GameModel

## class EventResult

### class DelayedCallBack

### plock custom

### no redraw

TODO: je l'ai toujours ce truc ou pas ?

## Transitions

### transition time

### plock transi

### TransitionSteps

## Info supplémentaires dans la config

## ComponentImageModifier

## ComponentBackCaller

## Itérer sur les GameObjects

## Créer un lien direct vers votre jeu


