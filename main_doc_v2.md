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
      "my_sprite": [0, 0],
      "my_other_sprite": [32, 0]
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

Un Game Object (ou gobj) est un élément du jeu, qui s'affiche dans l'aire de jeu. Un Game Object possède des coordonnées (un objet `Coord`) et un nom de sprite (`sprite_name`). Le nom de sprite correspond à un nom référencé dans le dictionnaire `img_coords` de la config JSON.

Pour que le Game Object s'affiche, il doit être placé dans un `Layer`. Un Game Object peut être transféré d'un Layer à un autre, il peut également n'appartenir à aucun Layer. Mais il n'est pas censé être placé dans plusieurs Layers en même temps.

La coordonnée et le nom de sprite doivent être spécifiés dès l'instanciation du Game Object. L'ajout dans le Layer peut être effectué juste après (voir plus loin, la classe Layer).

```
gobj = squarity.GameObject(
    squarity.Coord(5, 2),
    "my_sprite"
)
print(gobj)
# Le texte "<Gobj (5,2) my_sprite>" s'affiche dans la console.
```

Il existe d'autres paramètres facultatifs que l'on peut transmettre lors de l'instanciation. Ils sont détaillés plus loin dans cette documentation.

### Nom du sprite

L'aspect visuel du Game Object peut être directement changé en modifiant la variable membre `sprite_name`. La nouvelle image s'affichera, en fonction du tileset et de la config JSON.

Attention, il n'y a pas de vérification sur le nom du sprite. Si vous indiquez un nom qui n'est pas référencé dans `config.img_coords`, le jeu va planter sans aucun message. (On améliorera ça dans les versions à venir).

### Coordonnées (accès et modification)

Le Game Object possède une variable membre interne appelée `_coord`. **Vous n'êtes pas censé y accéder directement**, sinon ça risque de désordonner l'indexation des Game Objects dans les Layers.

Pour lire la coordonnée, utilisez la méthode `coord_clone = gobj.get_coord()`. Vous pouvez ensuite faire ce que vous voulez avec votre variable `coord_clone`, y compris la modifier. Mais les modifications ne seront pas reportés dans le Game Object.

Pour déplacer un Game Object, utilisez les méthodes `move_xxx`. Il s'agit des méthodes suivantes :

 - `move_to_xy` : déplace l'objet sur une case de destination, spécifiée par les paramètres X et Y (`int`).
 - `move_to` : déplace l'objet sur une case de destination, spécifiée par le paramètre `dest_coord` (`Coord`).
 - `move` : déplace l'objet de manière relative, selon un vecteur de déplacement spécifié par le paramètre `coord_offset` (`Coord`).
 - `move_dir` : déplace l'objet de manière relative, spécifié par le paramètre `direction` (`Direction`) et le paramètre facultatif `distance` (`int`).

```
gobj = squarity.GameObject(
    squarity.Coord(5, 2),
    "my_sprite"
)
gobj.move_to_xy(15, 9)
print(gobj)
# Le texte "<Gobj (15,9) my_sprite>" s'affiche dans la console.
gobj.move_to(squarity.Coord(7, 4))
print(gobj)
# Le texte "<Gobj (7,4) my_sprite>" s'affiche dans la console.
gobj.move(squarity.Coord(1, -1))
print(gobj)
# Le texte "<Gobj (8,3) my_sprite>" s'affiche dans la console.
gobj.move_dir(squarity.dirs.Right, 4)
print(gobj)
# Le texte "<Gobj (12,3) my_sprite>" s'affiche dans la console.
```

Ces 4 fonctions laissent le Game Object dans le même Layer. Voir la documentation de la classe Layer pour transférer un Game Object d'un Layer à un autre.

### Transitions ajoutées automatiquement.

Lorsque vous déplacez un Game Object, un déplacement de transition est automatiquement affichée. Durant 200 millisecondes, le Game Object se déplace progressivement (pixel par pixel) depuis sa case initiale vers sa case de destination.

Ce déplacement de transition automatique est effectué en une seule ligne droite. Par exemple, si vous déplacez un objet des coordonnées (5, 3) vers les coordonnées 8, 2, la ligne de déplacement sera oblique.

Si vous changez plusieurs fois les coordonnées dans le même tour de jeu, les valeurs intermédiaires ne seront pas prises en compte pour la transition. Les deux seules valeurs prises en compte sont celles avant l'exécution du code et celles après.

Vous pouvez déclencher plusieurs transitions sur plusieurs Game Objects, en modifiant les coordonnées de chacun d'entre eux.

Il est possible de définir des déplacements avec des étapes intermédiaires. Par exemple, un déplacement horizontal de x=5 vers x=8, puis un vertical de y=3 vers y=2. Voir plus loin (TODO : chapitres Transitions).

Le temps de la transition peut être redéfini individuellement pour chaque Game Object, avec la fonction `gobj.set_transition_delay(transition_delay)`. Le paramètre `transition_delay` est un `int` indiquant le temps en millisecondes. Toutes les futures transitions dues à un changement de coordonnées utiliseront ce nouveau temps.

Les 4 fonctions `move_xxx` possèdent un paramètre facultatif `transition_delay`, qui permet de définir un temps différent uniquement pour la prochaine transition.

Vous pouvez définir un transition delay à 0 si vous voulez que votre objet se déplace instantanément.

### Callback de fin de transition

Il est possible d'indiquer a un Game Object une "callback de fin de transition". Il s'agit d'une fonction python qui sera automatiquement exécutée chaque fois que le Game Object aura fini toutes ses transitions en cours. Utilisez la méthode `gobj.set_callback_end_transi(callback_end_transi)`.

Les callbacks ne peuvent pas avoir de paramètre, mais vous pouvez indiquer une fonction ou une méthode d'un objet spécifique.

Pour enlever une callback, exécutez `set_callback_end_transi` en indiquant le paramètre `None`.

Les 4 fonctions `move_xxx` possèdent un paramètre facultatif `callback`, qui permet de définir une callback différente uniquement pour la prochaine transition.

```
def my_callback():
    print("coucou")

gobj = squarity.GameObject(
    squarity.Coord(5, 2),
    "my_sprite"
)
gobj.set_callback_end_transi(my_callback)
# (Cette exemple n'affiche rien dans la console, désolé)
```


## class Layer

Un layer est un tableau en 2 dimensions, contenant des Game Objects. Votre aire de jeu peut contenir plusieurs Layers, qui seront affiché dans un ordre déterminé. Vous pouvez donc avoir un Layer pour vos objets du décor de fond, un pour les personnages et les bonus, un pour afficher des éléments d'interface, etc.

L'ordre d'affichage des objets au sein d'un Layer n'est pas déterminé. Concrètement, c'est l'ordre d'ajout des Game Object dans le Layer, mais il s'agit d'un détail d'implémentation et ce comportement n'est pas garanti pour les versions ultérieures. Si vous souhaitez être sûr de l'ordre d'affichage de vos objets, utilisez plusieurs Layers.

Si l'ordre importe peu pour votre jeu, vous pouvez utiliser le Layer créé par défaut : la variable membre `layer_main` dans le `GameModel`. Vous pouvez placer tous vos objets dans le `layer_main`.

### Ajouter et retirer des Game Objects

La méthode `layer.add_game_object(gobj)` permet d'ajouter un Game Object dans un Layer. (Les coordonnées du Game Object doivent être définies).

La méthode `layer.remove_game_object(gobj)` permet d'enlever un Game Object d'un Layer. Une exception sera levée si vous tentez d'enlever un Game Object n'appartenant pas au Layer.

La méthode `layer.remove_at_coord(coord)` permet d'enlever tous les Game Objects situés sur la coordonnée indiquée en paramètre.

Après avoir été enlevé, le Game Object existe toujours, vous pouvez le réutiliser et le placer dans un autre Layer.

Ci-dessous, un exemple de game code minimal, affichant un seul objet immobile. Pour l'exécuter, sélectionner le jeu d'exemple du diamant vert, supprimer tout le game code, puis copier-coller ce texte à la place.

```
import squarity

class GameModel(squarity.GameModelBase):
    def on_start(self):
        self.gobj = squarity.GameObject(squarity.Coord(5, 2), "gem_green")
        self.layer_main.add_game_object(self.gobj)
```

### Récupérer des Tiles et des Game Objects

Chaque élément du tableau 2D d'un Layer est une `Tile`. Ces `Tile` sont utiles pour se déplacer de case en case dans un Layer, grâce à la variable `adjacencies`. Il s'agit d'une liste de 8 éléments, contenant les Tiles adjacentes (certains éléments peuvent être None pour les Tiles qui sont au bord).

Les Game Objects d'une Tile sont stockés dans la variable membre `game_objects` (`list`).

Les méthodes `layer.get_tile(coord)` et `layer.get_tile_xy(x, y)` permettent de récupérer une Tile.

```
        tile = self.layer_main.get_tile_xy(5, 1)
        tile_down = tile.adjacencies[int(squarity.dirs.Down)]
        print("Nombre d'objets sur la tile :", len(tile_down.game_objects))
        print(tile_down.game_objects)
```

La méthode `layer.get_game_objects(coord)` permet de récupérer directement la liste de tous les Game Objects sur les coordonnées indiquées.

La méthode `layer.iter_all_game_objects()` permet d'itérer sur tous les Game Objects d'un Layer.

```
        for gobj in self.layer_main.iter_all_game_objects():
            print(gobj)
```

### Créer des layers et les ajouter dans le jeu

(avec ou sans transitions)

### LayerSparse


## class GameModel

(Pour faire fonctionner l'exemple ci-dessous, effacer tout le game code existant d'un jeu d'exemple, et ajouter un nom de sprite "my_sprite" dans la config).

```
import squarity

def my_callback():
    print("coucou")

class GameModel(squarity.GameModelBase):
    def on_start(self):
        self.gobj = squarity.GameObject(
            squarity.Coord(5, 2),
            "my_sprite"
        )
        self.layer_main.add_game_object(self.gobj)
        self.gobj.set_callback_end_transi(my_callback)

    def on_click(self, coord):
        self.gobj.move_to_xy(1, 1)

# Exécutez le jeu, puis cliquez n'importe où dans l'aire de jeu.
# L'objet se déplacera et le texte "coucou" s'affichera
# dans la console à la fin du déplacement.
```

## class EventResult

### class DelayedCallBack

### plock custom

### no redraw

TODO: je l'ai toujours ce truc ou pas ?

## Transitions

Pour l'instant, on peut pas définir de vitesse. Seulement le temps.

### transition time

### plock transi

### TransitionSteps

## Info supplémentaires dans la config

## ComponentImageModifier

## ComponentBackCaller

## Itérer sur les GameObjects

## Créer un lien direct vers votre jeu


