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

Ci-dessous, un exemple de game code minimal, affichant un seul objet immobile. Pour l'exécuter, sélectionnez le jeu d'exemple du diamant vert, supprimez tout le game code, puis copier-collez ce texte à la place.

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

Les Layers doivent être placés dans la liste `layers` du `GameModel`, cette liste contient initialement le `layer_main`.

L'ordre dans la liste `layers` est important, car il détermine l'ordre d'affichage des Layers. Le premier Layer de la liste est dessiné en premier, et apparaîtra donc en-dessous de tous les autres layers, et ainsi de suite.

Vous pouvez ajouter, enlever et réordonner les Layers dans la liste à tout moment. Ce sera immédiatement pris en compte dans l'affichage de l'aire de jeu.

Lors de l'instanciation, un Layer a besoin d'avoir une référence vers le `GameModel` dans lequel il est placé. Il faut également spécifier une largeur et une hauteur, en nombre de cases.

```
class GameModel(squarity.GameModelBase):
    def on_start(self):
        layer_second = Layer(self, self.w, self.h)
        self.layers.append(layer_second)
```

Tous les Layers que vous placez dans `layers` doivent avoir les mêmes largeur et hauteur que votre aire de jeu. Ces dimensions sont déjà initialisés dans le `GameModel`, variables membres `game_model.w` et `game_model.h`

Pour gérer la logique interne de votre jeu, vous pouvez utiliser des Layers de n'importe quelles dimensions, que vous ne placerez pas dans `layers`. Ils ne seront pas affichés.

La fonction `Layer.__init__` possède un paramètre facultatif `show_transitions`, défini à True par défaut. Lorsqu'il est défini à False, le Layer ne gère aucune transition, ni pour les déplacements d'objets, ni pour les modifications graphiques (scaling, décalage, ...). Lorsque vous changez les coordonnées d'un objet dans un Layer sans transition, il sera instantanément déplacé vers sa case de destination.

Les Layers sans transition sont gérés de manière optimisée par le moteur Squarity, et permettent d'effectuer des mouvements massifs et fréquents. Ils peuvent aussi être utiles pour afficher le décor de fond de votre jeu, qui change d'un seul coup en passant d'un niveau à un autre.

Le choix d'avoir un Layer avec ou sans transition peut uniquement être effectué lors de son instanciation. Si vous modifiez la variable `layer.show_transitions` après avoir créé le Layer, ce ne sera pas pris en compte par le moteur. (Ce serait trop compliqué à gérer, on ne saurait pas quoi faire avec les transitions en cours, etc.)

### LayerSparse

Il s'agit d'une classe ayant le même fonctionnement que `Layer` (les deux héritent de la classe `LayerBase`). Les Game Objects qu'il contient sont stockés différemment. Au lieu d'être indexés dans un tableau en deux dimensions, ils sont placés dans une liste unique.

Selon les actions que vous effectuez, elles peuvent s'exécuter un peu plus rapidement sur un `LayerSparse`: l'ajout, la suppression et le parcours de tous les objets s'exécutent plus rapidement, mais la récupération d'objets à une coordonnée spécifique est plus lent.

Si vous créez des jeux n'ayant pas de gros besoins en performance, vous n'avez pas besoin de vous soucier de ces détails et vous pouvez utiliser uniquement des `Layer`.

Liste des méthodes communes aux `Layer` et aux `LayerSparse` :

 - `get_game_objects`
 - `iter_all_game_objects`
 - `add_game_object`
 - `remove_game_object`
 - `remove_at_coord`
 - `move_game_object`
 - `move_game_object_xy`

Les méthodes `get_tile` et `get_tile_xy` ne sont pas présentes dans un `LayerSparse`, puisqu'il n'y a pas de tableau en 2 dimensions contenant des objets `Tile`.


## class GameModel

La classe principale définissant la logique de votre jeu. Elle hérite de `GameModelBase`. Vous devez la définir, mais pas l'instancier, car c'est fait automatiquement par le moteur.

Dans votre GameModel, vous pouvez définir des fonctions de callback spécifiques, qui seront automatiquement appelées sur certains événements dans le jeu.

### Liste des fonctions de callback

`on_start(self)` : cette fonction est appelée une seule fois au début du jeu. Il est conseillé de mettre votre code d'initialisation dans cette fonction, plutôt que dans la fonction `__init__`, car la fonction `on_start` permet de renvoyer un objet `EventResult` qui sera pris en compte. (TODO : voir plus loin).

`on_click(self, coord)` : cette fonction est appelée chaque fois que la personne qui joue clique dans l'aire de jeu. Vous pouvez consulter le paramètre `coord` pour savoir sur quelle case le clic a eu lieu. Vous ne pouvez pas savoir précisément quel Game Object a été cliqué, ni la position exacte du clic dans la case, car le but du moteur de jeu Squarity est de rester simple, et de se spécialiser uniquement dans les jeux en 2D sur un quadrillage.

Dans l'exemple ci-dessous, un diamant s'ajoute sur chaque case que vous cliquez. Pour l'exécuter, sélectionnez le jeu d'exemple du diamant vert, supprimez tout le game code et copier-collez ce texte à la place.

```
import squarity

class GameModel(squarity.GameModelBase):
    def on_click(self, coord):
        if not self.layer_main.get_game_objects(coord):
            self.gobj = squarity.GameObject(coord, "gem_yellow")
            self.layer_main.add_game_object(self.gobj)
```

`on_button_direction(self, direction)` : cette fonction est appelée lorsque l'un des 4 boutons de direction est cliqué, ou que l'une des 4 touches de direction du clavier est appuyée. Le paramètre `direction` est un objet de type `Direction`, il indique quel bouton a été appuyé.

Dans l'exemple ci-dessous, l'aire de jeu affiche un seul diamant. Celui-ci se déplace lorsque vous cliquez sur un bouton de direction, et reste bloqué dans les limites de l'aire de jeu.

```
import squarity

class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.gobj = squarity.GameObject(squarity.Coord(5, 2), "gem_green")
        self.layer_main.add_game_object(self.gobj)

    def on_button_direction(self, direction):
        coord_dest = self.gobj.get_coord().move_dir(direction)
        if self.rect.in_bounds(coord_dest):
            self.gobj.move_to(coord_dest)
```

`on_button_action(self, action_name)` : cette fonction est appelée lorsque l'un des boutons d'actions "1" ou "2" est cliqué, ou lorsque l'une des touches du clavier "1" ou "2" est appuyée (Les "1" et "2" au-dessus des lettres, ainsi que ceux du pavé numérique).

### Autres méthodes et variables de GameModel

Ces variables membres sont initialisées dès le départ. Il est fortement conseillé de les utiliser sans les modifier, car cela pourrait modifier le comportement de certaines fonctions.

 - `self.w` : largeur de l'aire de jeu, en nombre de case. (Correspond à `nb_tile_width` dans la config json)
 - `self.h` : hauteur de l'aire de jeu, en nombre de case. (Correspond à `nb_tile_height` dans la config json)
 - `self.str_game_conf_json` : chaîne de caractère contenant la configuration json complète.
 - `self.rect` : objet `Rect` ayant les dimensions de l'aire de jeu, c'est à dire `Rect(0, 0, self.w, self.h)`.

La méthode `game_model.get_first_gobj(coord, sprite_names, layer)` permet de récupérer le premier Game Object présent dans l'aire de jeu, selon différents critères cumulables. Les 3 paramètres sont facultatifs. Si aucun objet n'est trouvé, la méthode renvoie None.

 - paramètre `coord` : par défaut, l'objet est cherché sur tout l'aire de jeu. Sinon, ce paramètre peut être un `Rect` ou une `Coord`, indiquant dans quelle zone ou dans quelle coordonnée on cherche l'objet.
 - paramètre `sprite_names` : par défaut, pas de filtre sur le nom de sprite. Sinon, ce paramètre doit être une liste de strings, indiquant le ou les noms de sprite recherché.
 - paramètre `layer` : par défaut, on cherche dans tous les Layers placés dans la liste `game_model.layers`. Sinon, ce paramètre doit être un unique `Layer`, dans lequel on cherche l'objet.

La variable membre `self.transition_delay` définit le temps par défaut (en millisecondes) de toutes les transitions effectuées suite à un changement de coordonnées d'un Game Object. Contrairement aux autres variables membres, celle-ci peut être modifiée. (TODO : voir plus loin).


## class EventResult

Cette classe regroupe des informations générales que vous pouvez communiquer au moteur de jeu, après l'exécution de n'importe quelle fonction de callback (provenant du Game Model, d'un Game Object ou de n'importe quoi d'autres).

Par défaut, les fonctions de callback ne renvoient rien (pas de `return` dans la fonction). Dans ce cas, la valeur réellement renvoyée est `None`, ce qui est accepté par le moteur du jeu.

### Callback différée

Vous pouvez indiquer au moteur d'exécuter plus tard une de vos fonctions (une callback).

Instanciez une classe `DelayedCallBack`, en indiquant dans les paramètres le délai d'exécution en millisecondes, et la callback. Vous pouvez indiquer une fonction définie directement dans votre code, une méthode de votre Game Model (`self.my_callback`), une méthode d'un Game Object spécifique, etc. La callback ne peut pas avoir de paramètres.

Ajoutez ensuite votre objet `DelayedCallBack` dans le Event Result, avec la fonction `event_result.add_delayed_callback`.

Le code ci-dessous n'affiche rien dans l'aire de jeu, mais écrit "coucou" dans la console après un temps d'attente de 500 millisecondes.

```
import squarity

def my_callback():
    print("coucou")

class GameModel(squarity.GameModelBase):
    def on_start(self):
        event_result = squarity.EventResult()
        event_result.add_delayed_callback(
            squarity.DelayedCallBack(500, my_callback)
        )
        return event_result
```

C'est un peu verbeux, on raccourcira le code dans une version ultérieure de Squarity.

Vous ne pouvez pas annuler les callbacks. Lorsque vous avez renvoyé un Event Result contenant une callback, celle-ci sera forcément appelée. C'est à vous de gérer cela dans votre code.

Il y a un bug : si vous redémarrez votre jeu, ou même si vous lancez un autre jeu, les callbacks du jeu précédent restent en mémoire et sont tout de même exécutées. On corrigera ça au plus vite.

### Player Lock (plock) Custom

Votre jeu aura peut-être besoin d'afficher des "cut scene" ou des petites animations courtes, durant lesquelles la personne qui joue n'est pas censé agir. Il est possible d'appliquer un "Player Lock", c'est à dire de bloquer temporairement les boutons et les clics.

Il y a deux types de Player Locks:

 - custom : c'est à vous d'indiquer explicitement, via le code, à quel moments ça locke et ça délocke.
 - transition : les locks/delocks sont effectués automatiquement d'après les transitions de certains Game Object (TODO : voir plus loin).

Pour les Locks Custom, le blocage est toujours montré dans l'interface : les boutons d'actions apparaissent grisé.

Il est possible de locker/delocker avec plusieurs mots-clés (chaque mot-clé peut-être vue comme une raison pour locker). L'interface se délocke lorsqu'il n'y a plus aucun mot-clé de lock en cours.

Pour locker, instancier un `EventResult` et ajouter une ou plusieurs strings dans la liste `event_result.plocks_custom`, représentant les mot-clés de lock. Pour délocker, utiliser la liste `event_result.punlocks_custom`.

Attention, l'interface est entièrement bloquée dès le premier mot-clé. Cela signifie qu'il faut obligatoirement prévoir les delocks dans des fonctions de callbacks, qui sont, en général, déclarées au même moment que l'on ajoute un lock. Si ce n'est pas fait, la personne qui joue restera bloquée indéfiniment (au pire des cas, le bouton "exécuter le jeu" enlève systématiquement tous les locks, mais cela réinitialise aussi tout le jeu).

Il est possible de delocker tous les mots-clés d'un seul coup en mettant une string `"*"` dans `punlocks_custom`.

Le code ci-dessous n'affiche rien, il locke l'interface pendant 2 secondes à chaque fois que l'on clique dans l'aire de jeu.

```
import squarity

def callback_unlock():
    print("unlock")
    event_result = squarity.EventResult()
    event_result.punlocks_custom.append("*")
    return event_result

class GameModel(squarity.GameModelBase):
    def on_click(self, coord):
        print("lock")
        event_result = squarity.EventResult()
        event_result.plocks_custom.append("lock_a")
        event_result.plocks_custom.append("lock_b")
        event_result.add_delayed_callback(
            squarity.DelayedCallBack(2000, callback_unlock)
        )
        return event_result
```

### Annuler le rendu de l'aire de jeu

Certaines actions de votre jeu (en particulier, les fonctions de callback contenant peu de code) peuvent ne pas modifier la disposition ou l'état des Game Objects. Dans ce cas, vous pouvez indiquer au moteur qu'il n'est pas nécessaire de redessiner l'aire de jeu après la fonction callback.

Instancier un `EventResult`, et définissez la variable `redraw` à False. N'oubliez pas de le renvoyer.

```
event_result = squarity.EventResult()
event_result.redraw = False
```

À noter que s'il y a des transitions en cours, l'aire de jeu est régulièrement redessinée pour les afficher. Donc même si vous renvoyez un Event Result qui annule le rendu, il peut quand même y en avoir.

Vous pouvez cumuler plusieurs éléments dans le même Event Result. Par exemple, vous pouvez déclarer plusieurs callbacks, tout en lockant l'interface avec 3 mot-clés et en délockant 4 autres mot-clés, le tout en annulant le rendu.


## Transitions

Une transition représente la modification progressive d'une variable d'un Game Object, sur une période de temps définie. Il est possible d'appliquer une transition sur les coordonnées. L'objet se déplacera "pixel par pixel" de sa case de destination vers sa case d'arrivée. Visuellement, les coordonnées de votre objet deviennent des valeurs décimales, pour le placer entre deux cases. Dans votre code python, les coordonnées restent des nombres entiers, et passent directement de la valeur de départ à la valeur d'arriver.

D'autres variables d'un Game Object peuvent également avoir des transitions, par exemple `area_scale_x` et `area_scale_y` dans le `ComponentImageModifier`. Ces variables permettent de grossir/rétrécir l'objet (TODO : voir plus loin).

Le sprite name peut également avoir des transitions, mais elles ne sont pas progressives. L'image change d'un seul coup. L'intérêt étant de pouvoir enchaîner ces transitions : une première image pendant 100 millisecondes, une deuxième pendant les 100 millisecondes suivantes, etc.

Il existe deux moyens pour déclencher une transition : modifier directement une variable transitionnable ou exécuter la fonction `add_transition`.

### Temps de transition

Les transitions ajoutées suite à une modification de variable doivent déterminer automatiquement le temps de transition. Ce temps est pris, par ordre de priorité :

 - Le paramètre optionnel `transition_delay` d'une fonction `move_to_xxx`, si celui-ci a été défini.
 - Le temps spécifique au Game Object, si celui-ci a été défini via la fonction `game_object.set_transition_delay(transition_delay)`.
 - Le temps global de votre jeu, c'est à dire la variable membre `game_model.transition_delay` (initialisée à 200 millisecondes, que vous pouvez modifier).

### Ajout d'une séquence de transitions

La fonction `game_object.add_transition` nécessite deux paramètres :

 - un nom de variable membre (`coord` ou `sprite_name`),
 - une liste contenant des tuples de temps de délais et de valeurs.

Avec `"coord"`, les valeurs doivent être des `Coord`. Le Game Object se déplacera vers ces coordonnées, les unes après les autres.

Dans l'exemple ci-dessous, lorsqu'on clique dans l'aire de jeu, le diamant vert se déplace vers la coordonnée (3, 1), puis il se déplace très rapidement vers (7, 1), puis il revient plus lentement à son point de départ.

```
import squarity

class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.gobj = squarity.GameObject(squarity.Coord(5, 2), "gem_green")
        self.layer_main.add_game_object(self.gobj)

    def on_click(self, coord):
        self.gobj.add_transition(
            squarity.TransitionSteps(
                "coord",
                (
                    (500, squarity.Coord(3, 1)),
                    (200, squarity.Coord(7, 1)),
                    (900, squarity.Coord(5, 2)),
                )
            )
        )
```

Vous ne pouvez définir que le temps de déplacement, mais pas une vitesse générique. Par exemple, si vous souhaitez que votre Game Object se déplace toujours à la même vitesse, mais parfois à une case de distance et parfois à deux cases, vous allez devoir coder vous-même le calcul des temps de déplacement. (On fera mieux à la prochaine version).

Lorsque le premier paramètre de `TransitionSteps` est `"sprite_name"`, les valeurs doivent être des strings correspondant à des noms de sprites. Le Game Object changera successivement d'apparence.

Attention, le principe d'une transition est d'être appliquée dans le jeu dès qu'elle est démarrée, puis d'être affichée progressivement. Pour les coordonnées, c'est logique. Pour les noms de sprite, c'est un peu particulier, car ça ne peut pas être progressif. Le sprite change dès le début de la transition et reste tel quel durant le temps indiqué. Ce qui signifie que pour une transition sur un nom de sprite, le dernier temps n'est pas très utile et peut être zéro.

Si votre Game Object a une callback de fin de transition, définie à l'aide de la fonction `game_object.set_callback_end_transi`, cellec-ci sera déclenchée à la fin de la liste des transitions.

### Gestion des transitions

Vous pouvez ajouter des transitions via la méthode `add_transition`, même si des anciennes transitions sont encore en cours. Celles-ci vont s'ajouter après les transitions existantes.

La prise en compte des transitions par le moteur est effectuée à la fin de l'exécution du code en cours (`on_click`, `on_button_xxx`, une callback, ...). Si vous ajoutez plusieurs transitions dans le même code, elles seront déclenchées au même moment et seront exécutées en même temps. Cela permet, d'avoir un objet qui se déplace tout en changeant de sprites.

Dans votre Game Object, les variables membres `coord` et `sprite_name` changent automatiquement, au fur et à mesure de l'enchaînement des transitions. Ce changement n'est pas progressif, il est appliqué au début de chaque transition. Cela permet de garder des nombres entiers dans les coordonnées, même si visuellement l'objet s'affiche entre les deux.

**Attention** : il est fortement déconseillé d'avoir, sur un même Game Object, à la fois des transitions ajoutées automatiquement suite à la modification d'une variable, et à la fois des transitions ajoutées avec `add_transition`. C'est une situation ambigüe, dans laquelle on ne pourrait pas déterminer les valeurs des variables. Le moteur essaiera de le gérer comme il peut, c'est à dire pas très bien. Vous devez donc vous assurer des transitions en cours et de leurs origines, avant d'effectuer des actions qui vont en ajouter de nouvelles.

Si vous n'êtes pas sûr de vous dans la gestion des transitions, le plus simple est de s'assurer qu'il n'y en a aucune en cours sur un Game Object, avant d'exécuter `add_transition`, une fonction `move_xxx` ou une modification de `sprite_name`.

la variable qui dit combien qu'on en a en cours.

paf, le gros exemple.

### Blocage de l'interface

ça permet de faciliter la vérif des transitions en cours.

 plock transi


## Info supplémentaires dans la config

(dans img_coords)

## ComponentImageModifier

## ComponentBackCaller

## Itérer sur les GameObjects

un bout de code qui place tous les sprites existants dans l'aire de jeu.

## Créer un lien direct vers votre jeu


