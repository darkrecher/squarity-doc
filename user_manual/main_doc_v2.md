# Documentation de référence de Squarity V2

Squarity est un espace de création et de partage de jeux vidéo jouables dans un navigateur web. Les jeux se déroulent sur une grille en 2D composée de carrés. La "game logic" (le fonctionnement et les règles du jeu) est définie par du code en python.

Ce document décrit les fonctionnalités de la version 2.1.0 du moteur de Squarity. Il suppose que vous avez déjà un minimum de connaissance en python. Si ce n'est pas le cas, vous pouvez les acquérir avec ce tutoriel en français : https://python.doctor/

Un jeu est défini par trois informations :

 - le tileset,
 - la configuration,
 - le "game code".

Pour l'instant, Squarity ne gère pas de comptes ni de profil personnel. Vous devez sauvegardez vos jeux par vous-même, sur votre disque dur ou ailleurs. Vous pouvez [les publier sur un gist github](https://github.com/darkrecher/squarity-doc/blob/master/user_manual/main_page.md#partager-un-jeu).


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

`version` (chaîne de caractère) : version du moteur du jeu, indiquez "2.1.0". ([Voir chapitre "Versions"](https://github.com/darkrecher/squarity-doc/blob/master/user_manual/main_doc_v2.md#versions-du-moteur-squarity)).

`tile_size` (nombre entier) : la taille par défaut, en pixels dans le tileset, des images représentant les éléments de votre jeu.

`game_area` (sous-dictionnaire contenant deux nombres entiers) : largeur et hauteur de l'aire de jeu, en nombre de cases (tiles).

### Définition des images

Il s'agit des images représentant les éléments de votre jeu (les "Game Objects"). Elles sont définies dans un sous-dictionnaire, identifié par la clé `img_coords`.

Chaque clé de ce sous-dictionnaire est une chaîne de caractère que vous pourrez utiliser dans votre code python, pour identifier une image de Game Object.

Chaque valeur de ce sous-dictionnaire est une liste de 2 entiers. Ils représentent les coordonnées x et y, en pixels dans le tileset, du coin supérieur gauche de l'image.

Il est possible d'ajouter d'autres valeurs après les deux entiers de la liste. [Voir chapitre "Info supplémentaires pour les sprites"](#info-suppl%C3%A9mentaires-pour-les-sprites).

### Versions du moteur Squarity

La seule information utile de la clé `version` est le premier nombre, situé avant le premier point.

Si ce nombre est "1", la version utilisée sera "1.0.0".

Si ce nombre est "2", la version utilisée sera la version 2.x.y la plus récente (actuellement : "2.1.0"). Vous n'avez donc pas accès aux précédentes versions 2.x.y, mais elles sont censées être rétro-compatibles.


## Notions de base du "game code"

Il s'agit du programme définissant la logique de votre jeu, il est écrit en langage python.

Dans l'interface, placez ce programme dans la zone de texte "Le code du jeu".

Ce programme doit contenir une classe intitulée `GameModel`, qui hérite de la classe `squarity.GameModelBase`.

Cette classe sera instanciée automatiquement par le moteur Squarity. Elle contient des fonctions de callback, que vous aurez éventuellement redéfinie. Ces fonctions sont appelées automatiquement sur certains événements (appui sur un bouton du jeu, clic de souris, etc.)

Votre `GameModel` contient des objets de type `squarity.Layer`, ordonnés dans une liste. Chacun de ces layers contient un tableau de "tiles". Ce tableau est en 2 dimensions, la largeur et la hauteur correspondent à celles de l'aire de jeu (les valeurs `nb_tile_width` et `nb_tile_height` indiquées dans la config JSON).

Une tile représente une case de l'aire de jeu. Chaque tile peut contenir des `squarity.GameObject`, représentant des objets de votre jeu. Un GameObject est toujours placé sur une seule tile de seul layer. Un GameObject possède des coordonnées (x, y) indiquant la tile d'appartenance dans le layer. Un GameObject possède une variable membre `sprite_name`, de type chaîne de caractère. Cette variable doit avoir pour valeur l'un des noms définis dans le dictionnaire `img_coords` de la configuration JSON.

La suite de cette documentation contient des exemples de code. Vous pouvez les copier-coller dans Squarity puis cliquer sur le bouton "Executer". Vous devriez voir des informations apparaître dans la console (la fenêtre de texte en bas de l'aire de jeu). Pour les exemples un peu plus complexes, il faut trouver le bon endroit où placer le code, mais vous êtes très fort et vous allez y arriver.


## Schéma d'affichage, calculs des tailles

TODO.

Vous ne pouvez pas définir la taille en pixel des cases réellement affichées. Cette-ci dépend de la taille de la fenêtre du navigateur affichant Squarity, qui est définie par la personne qui joue.

Le calcul est effectué comme suit:

 - calcul de la largeur possible et de la hauteur possible des tiles (en pixel, à l'écran) :
   - `largeur_case_temp = largeur_affichage // config.game_area.nb_tile_width`
   - `hauteur_case_temp = hauteur_affichage // config.game_area.nb_tile_height`
 - détermination de la taille réelle des tiles, en prenant la plus petite :
   - `taille_case_affichage = min(largeur_case_temp, hauteur_case_temp)`
 - application de cette taille pour la largeur et la hauteur à l'écran :
   - `largeur_case_affichage = taille_case_affichage`
   - `hauteur_case_affichage = taille_case_affichage`

Ensuite, une mise à l'échelle est effectuée, pour afficher les images ayant une taille égale à `config.tile_size` (en pixel dans le tileset), vers des images ayant une taille égale à `taille_case_ecran` (en pixel à l'écran).

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

Il est possible de définir des déplacements avec des étapes intermédiaires. Par exemple, un déplacement horizontal de x=5 vers x=8, puis un vertical de y=3 vers y=2. [Voir chapitres "Transitions"](#transitions).

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

Une transition représente la modification progressive d'une variable d'un Game Object, sur une période de temps définie. Il est possible d'appliquer une transition sur les coordonnées. L'objet se déplacera "pixel par pixel" de sa case de destination vers sa case d'arrivée. Visuellement, les coordonnées de votre objet deviennent des valeurs décimales, pour le placer entre deux cases. Dans votre code python, les coordonnées restent des nombres entiers, et passent directement de la valeur de départ à la valeur d'arrivée.

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

Dans le futur, on changera l'ordre des paramèter. D'abord le sprite_name, puis le temps. Ce sera plus logique à comprendre.

Si votre Game Object a une callback de fin de transition, définie à l'aide de la fonction `game_object.set_callback_end_transi`, cellec-ci sera déclenchée à la fin de la liste des transitions.

### Gestion des transitions

Vous pouvez ajouter des transitions via la méthode `add_transition`, même si des anciennes transitions sont encore en cours. Celles-ci vont s'ajouter après les transitions existantes.

La prise en compte des transitions par le moteur est effectuée à la fin de l'exécution du code en cours (`on_click`, `on_button_xxx`, une callback, ...). Si vous ajoutez plusieurs transitions dans le même code, elles seront déclenchées au même moment et seront exécutées en même temps. Cela permet, d'avoir un objet qui se déplace tout en changeant de sprites.

Dans votre Game Object, les variables membres `coord` et `sprite_name` changent automatiquement, au fur et à mesure de l'enchaînement des transitions. Ce changement n'est pas progressif, il est appliqué au début de chaque transition. Cela permet de garder des nombres entiers dans les coordonnées, même si visuellement l'objet s'affiche entre les deux.

Le moteur essaye, autant que faire se peut, d'avoir le même type de gestion pour les transitions ajoutées suite à une modification d'une variable et les transitions ajoutées avec `add_transition` :

 - Durant une transition provenant d'une modification de variable, la variable contient la valeur finale. C'est normal, c'est vous même qui l'avez définie avec votre code python.
 - Si vous remodifiez la variable pendant une transition, celle-ci va s'enchaîner après les transitions existantes. Dans tous les cas, votre code utilise toujours la valeur finale de tout l'enchaînement de transitions. Ça reste cohérent, c'est juste la représentation visuelle qui a du retard par rapport au code, le temps de dérouler les transitions.
 - Durant les transitions provenant de `add_transition`, c'est le moteur du jeu qui modifie automatiquement la variable transitionnée. Cette modification se fait au début de chaque transition (comme si c'était votre code qui le changeait manuellement, à chaque fois que la transition précédente se termine).

**Attention** : il est fortement déconseillé d'avoir, sur un même Game Object, à la fois des transitions provenant de la modification d'une variable et à la fois des transitions provenant de `add_transition`. C'est une situation ambigüe, dans laquelle on ne pourrait pas déterminer les valeurs des variables. Le moteur essaiera de le gérer comme il peut, c'est à dire pas très bien. Vous devez donc vous assurer des transitions en cours et de leurs origines, avant d'effectuer des actions qui vont en ajouter de nouvelles.

Si vous avez des doutes, le plus simple est de s'assurer qu'il n'y a aucune transition en cours sur un Game Object avant d'exécuter `add_transition`, ou une fonction `move_xxx`, ou une modification de `sprite_name`.

La méthode `game_object.get_nb_undone_transitions()` renvoie le nombre de transitions d'un Game Object qui ne sont pas encore terminées ou pas commencées. Si cette fonction renvoie 0, vous pouvez ajouter des transitions en toute sécurité.

Dans l'exemple ci-dessous, lorsque vous appuyez sur un bouton de direction, le diamant se déplace tout en clignotant (jaune-vert-jaune-vert). Lorsque vous cliquez dans le jeu, la console affiche l'état actuel du diamant : coordonnées, nom du sprite et nombres de transitions restantes. Appuyez plusieurs fois sur un bouton, puis cliquez à fond dans le jeu pour avoir une démonstration de la manière dont sont gérées les transitions.

```
import squarity

class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.gobj = squarity.GameObject(squarity.Coord(5, 2), "gem_green")
        self.layer_main.add_game_object(self.gobj)

    def on_button_direction(self, direction):
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
        self.gobj.add_transition(
            squarity.TransitionSteps(
                "sprite_name",
                (
                    (400, "gem_yellow"),
                    (400, "gem_green"),
                    (400, "gem_yellow"),
                    (0, "gem_green"),
                )
            )
        )

    def on_click(self, coord):
        print("Coordonnées:", self.gobj.get_coord())
        print("Nom du sprite:", self.gobj.sprite_name)
        print("Transitions restantes:", self.gobj.get_nb_undone_transitions())
```

### Blocage de l'interface (Player Lock Transi)

Si la personne qui joue reste appuyé sur une touche, la fonction `on_button_direction` ou `on_button_action` sera exécutée plusieurs fois très vite. Selon le code que vous avez écrit, cela peut poser problème.

Il est possible de bloquer automatiquement toute l'interface du jeu (clics et boutons) tant qu'un Game Object a au moins une transition en cours. Ça peut être utile si votre jeu comporte un élément principal (héros/héroïne/avatar/etc.) dirigé par la personne qui joue. Si un bouton est appuyé durant le mouvement de cet élément, ce ne sera pas pris en compte.

Modifiez la variable membre `plock_transi` de votre Game Object. Celle-ci peut prendre 3 valeurs:

 - `PlayerLockTransi.NO_LOCK` : pas le blocage (valeur par défaut).
 - `PlayerLockTransi.INVISIBLE` : blocage invisible. Les boutons ne changent pas d'apparence, mais rien ne se passe si on clique dessus.
 - `PlayerLockTransi.LOCK` : blockage visible. Les boutons s'affichent en grisé.

```
self.gobj = squarity.GameObject(squarity.Coord(5, 2), "gem_green")
self.gobj.plock_transi = squarity.PlayerLockTransi.INVISIBLE
```

En général, cette fonctionnalité déclenche des micro-blocage successifs, durant les mouvements de l'élément principal. Si les boutons d'interface sont grisés/dégrisés à chaque fois, c'est dérangeant pour la personne qui joue. C'est pourquoi il vaut mieux indiquer un blocage invisible. Les deux types de blocages ont exactement le même effet dans le fonctionnement du jeu, la différence est seulement visuelle.

Les blocages visibles sont utiles pour les animations narratives (les "cut-scenes"). Ils permettent d'indiquer explicitement que ce n'est pas le moment de jouer, mais le moment de regarder (voire admirer) ce qu'il se passe dans le jeu.

Ce type de blocage est appliqué pour tous les types de transitions, aussi bien celles provenant d'une modification de variable que celles ajoutées avec `add_transition`.

Vous pouvez avoir plusieurs Game Object configurés pour bloquer l'interface. Dans ce cas, l'interface est utilisable lorsque tous ces objets n'ont aucune transition en cours.

Vous pouvez ajouter des transitions à un objet bloqueur même s'il a déjà des transitions en cours.

Ce type de blocage permet de simplifier la gestion des transitions, et le fait qu'il faille éviter d'avoir plusieurs types de transition en même temps sur un même Game Object.

### Annuler les transitions en cours

La méthode `game_object.clear_transitions_to_record()` permet de supprimer les transitions que vous auriez ajoutées via des méthodes `add_transition`, AVANT qu'elles aient été prises en compte par le moteur du jeu.

La méthode `game_object.clear_all_transitions()` permet d'annuler toutes les transitions prises en compte. Dans le code, vous pouvez à la fois exécuter cette fonction, puis exécuter des `add_transition`. Dans ce cas, les transitions précédentes seront toutes annulées, puis celles que vous avez ajoutées seront prises en compte.

Attention, si vous avez ajouté un enchaînement de transition et que vous l'annulez, la transition actuellement en cours est immédiatement terminée (l'objet se déplace instantanément à la destination de la transition). Les transitions qui n'étaient pas commencées sont entièrement annulées.

Pour essayer, remettez le code du chapitre "Gestion des transitions", puis ajoutez ce code à la fin:

```
    def on_button_action(self, action_name):
        self.gobj.clear_all_transitions()
```

Cliquez sur un bouton de direction, et immédiatement après cliquez sur un bouton d'action (le "1" ou le "2").

Selon le moment où vous avez cliqué, le diamant s'arrêtera à un endroit différent, et il sera jaune ou vert.


## Info supplémentaires pour les sprites

Chaque valeur du dictionnaire `img_coords` est une liste contenant au moins deux nombres entiers. D'autres valeurs facultatives peuvent être ajoutées après.

Voici la liste complète (incluant les 2 premiers nombres obligatoires)

 - 2 nombres entiers. Coordonnées x et y du coin supérieur gauche de l'image, dans le tileset. L'unité est le pixel de tileset.

 - 2 nombres entiers, par défaut : config.tile_size. Taille (largeur, hauteur) de l'image prise dans l'atlas. L'unité est le pixel de tileset. Ces deux tailles ont également une influence sur la taille de l'image affichée dans l'aire de jeu. Par exemple, si on indique une largeur qui vaut un tiers de config.tile_size, l'image affichée aura une largeur de un tiers de case dans l'aire de jeu. La méthode de positionnement du sprite dans l'aire de jeu, par rapport à la taille de l'image d'atlas, est définie juste après.

 - chaines de caractères : "center" ou "corner_upleft", par défaut : "corner_upleft". Indique où ancrer l'image du tileset par rapport à la case de l'aire de jeu, en particulier quand l'image et la case n'ont pas la même taille. Avec "corner_upleft", le coin haut gauche de l'image reste fixé sur le coin haut gauche de la case. Donc si on agrandit l'image, elle va dépasser vers le bas et vers la droite. Avec "center", le centre de l'image reste fixé sur le centre de la case. Si on agrandit l'image, elle va dépasser par les 4 côtés.

TODO : faire un schéma pour ça aussi.

## ComponentImageModifier

### Initialisation

Cette classe doit être placée dans un Game Object, au moment de sa création. Elle permet de modifier la manière dont l'image du Game Object est affichée dans l'aire de jeu.

Si le `ComponentImageModifier` est indiqué après la création du Game Object, il ne sera pas pris en compte. Il faut donc instancier votre Game Object comme ceci :

```
gobj = squarity.GameObject(
    Coord(0, 0),
    "gem_green",
    image_modifier=squarity.ComponentImageModifier()
)
```

### Variables membres

Toutes les variables commençant par `img_` ont pour unité le nombre de pixels dans l'image de tileset. Ce sont des nombres entiers, positifs ou négatifs.

Toutes les variables commençant par `area_` ont pour unité le nombre de cases dans l'aire de jeu. Ce sont des nombres décimaux, positifs ou négatifs. Il est donc possible d'indiquer des fractions de cases.

`img_offset_x`, `img_offset_y` : décalage, dans le tileset, de l'image à afficher. Modifier ces valeurs revient à modifier, temporairement et pour un seul Game Object, les 2 premières valeurs du sprite name, dans `config.img_coords`.

`img_size_x`, `img_size_y` : taille, dans le tileset, de l'image à afficher. Modifier ces valeurs revient à modifier, temporairement et pour un seul Game Object, les 3ème et 4ème valeurs du sprite name, dans `config.img_coords`. Par défaut, ces valeurs sont initialisées à `config.tile_size`.

`area_offset_x`, `area_offset_y` : décalage, dans l'aire de jeu, de l'objet affiché. Ces variables permettent d'afficher un objet entre deux cases (même si, dans la logique du jeu, l'objet restera toujours contenu dans une seule case). Par exemple, si `area_offset_x = -1.25`, l'objet sera décalé vers la gauche, sur une distance de une case un quart. Il est possible d'afficher un objet partiellement en dehors de l'aire de jeu. Par défaut, ces deux valeurs valent 0.0.

`area_scale_x`, `area_scale_y` : facteur d'échelle de l'image affichée dans l'aire de jeu. Par exemple, si `area_scale_x = 2.5`, l'image sera affichée 2,5 fois plus large que sa taille normale. Le positionnement de l'image retaillée est déterminée à l'aide de l'anchor (la valeur "center"/"corner_upleft" définie dans la configuration). Par défaut, ces deux valeurs valent 1.0.

Ces 8 valeurs peuvent être définies lors de la création du `ComponentImageModifier` et peuvent ensuite être modifiées pendant le jeu. Le component se trouve dans la variable membre `image_modifier` du Game Object.

Dans cet exemple, le diamant vert est affiché de manière écrasée. Appuyez sur la flèche de gauche ou de droite pour l'écraser encore plus, appuyez sur la flèche du haut ou du bas pour l'étirer.

```
import squarity

d = squarity.dirs

class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.gobj = squarity.GameObject(
            squarity.Coord(5, 2),
            "gem_green",
            image_modifier=squarity.ComponentImageModifier(
                area_scale_x=2.0,
                area_scale_y=0.8,
            )
        )
        self.gobj.set_transition_delay(50)
        self.layer_main.add_game_object(self.gobj)

    def on_button_direction(self, direction):
        if direction in (d.Up, d.Down):
            if self.gobj.image_modifier.area_scale_x > 0.1:
                self.gobj.image_modifier.area_scale_x -= 0.1
                self.gobj.image_modifier.area_scale_y += 0.1
        else:
            if self.gobj.image_modifier.area_scale_y > 0.1:
                self.gobj.image_modifier.area_scale_y -= 0.1
                self.gobj.image_modifier.area_scale_x += 0.1
```


### Transitions de l'ImageModifier

Les 8 valeurs de l'ImageModifier fonctionnent de la même manière que les coordonnées au niveau des transitions:

 - Une simple modification de l'une de ces valeurs déclenche une transition entre la valeur courante et la valeur finale, sur une durée définie via `set_transition_delay`.
 - Selon la valeur de `gobj.plock_transi`, l'interface peut être lockée durant une transition de l'ImageModifier.
 - La fonction de callback de fin de transition sera appelée, si elle est définie.
 - Il est possible d'ajouter et d'enchaîner des séquences de transition avec la fonction `gobj.image_modifier.add_transitions`.

L'exemple ci-dessous reproduit la petite animation lorsque les deux diamants se rencontre, mais cette fois-ci il n'y a que le diamant vert. Cliquez dans l'aire de jeu pour déclencher l'animation.

```
import squarity

class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.gobj = squarity.GameObject(
            squarity.Coord(5, 2),
            "gem_green",
            image_modifier=squarity.ComponentImageModifier()
        )
        self.layer_main.add_game_object(self.gobj)

    def on_click(self, coord):

        TRANSI_SCALE = (
            (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5),
            (150, 0.5), (150, 1.5), (150, 0.5), (150, 1.5),
            (150, 0.5), (150, 1.5),
            (150, 0.5), (75, 1),
        )
        self.gobj.image_modifier.add_transition(
            squarity.TransitionSteps(
                "area_scale_x",
                TRANSI_SCALE
            )
        )
        self.gobj.image_modifier.add_transition(
            squarity.TransitionSteps(
                "area_scale_y",
                TRANSI_SCALE
            )
        )

        self.gobj.image_modifier.add_transition(
            squarity.TransitionSteps(
                "area_offset_x",
                ((200, -1), (400, -1), (400, 1), (400, 1), (400, -1), (200, 0))
            )
        )
        self.gobj.image_modifier.add_transition(
            squarity.TransitionSteps(
                "area_offset_y",
                ((200, 1), (400, -1), (400, -1), (400, 1), (400, 1), (200, 0))
            )
        )
```


## ComponentBackCaller

Cette classe doit être placée dans un Game Object, au moment de sa création. Elle permet d'exécuter des callbacks au bout d'un temps défini. C'est le même principe que les callbacks dans les `EventResult`, mais elles sont associées à un Game Object.

Si le Game Object est supprimé, ou s'il est retiré de son Layer, les callbacks prévues ne sont pas exécutées.

Utilisez le paramètre optionnel `back_caller` lors de la création du Game Object. Puis, utiliser la fonction `back_caller.add_callback(delayed_callback)` pour ajouter une callback.

Contrairement aux transitions sur les coordonnées, l'image modifier, etc., lorsqu'il n'y a plus de callback à exécuter, cela ne déclenche pas la callback de fin des transitions.

En revanche, les callbacks ajoutées et qui n'ont pas encore été exécutées sont comptées comme des transitions non réalisées par la fonction `get_nb_undone_transitions`. (Note: et c'est bizarre et on devrait avoir une fonction spéciale pour renvoyer le nombre de callback restantes).

Dans le code ci-dessous, le diamant vert ajoute deux callbacks dès le lancement du jeu. L'une sera lancée au bout de 2 secondes, l'autre au bout de 4 secondes. Lorsque vous cliquez dans le jeu, le nombre de transitions restantes s'affiche dans la console. Ce nombre passera de 2 vers 1, puis vers 0.

```
import squarity

def my_callback():
    print("coucou de my_callback")

class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.gobj = squarity.GameObject(
            squarity.Coord(5, 2),
            "gem_green",
            back_caller=squarity.ComponentBackCaller()
        )
        self.layer_main.add_game_object(self.gobj)
        self.gobj.back_caller.add_callback(
            squarity.DelayedCallBack(2000, my_callback)
        )
        self.gobj.back_caller.add_callback(
            squarity.DelayedCallBack(4000, my_callback)
        )

    def on_click(self, coord):
        print("Transitions restantes:", self.gobj.get_nb_undone_transitions())
```


## Itérer sur les GameObjects

Il est très souvent nécessaire de parcourir tout ou une partie de l'aire de jeu, pour rechercher des Game Object spécifiques.

La classe `Sequencer` est un outil permettant d'effectuer les itérations les plus communes.

Cette classe contient uniquement des fonctions statiques (vous n'avez pas besoin de l'instancier).

La fonction `Sequencer.seq_iter` renvoie un itérateur. Les paramètres de cette fonction sont des "mini-itérateurs" mis bout à bout. Selon ces paramètres, votre séquenceur renverra des coordonnées, des Game Objects ou des listes de Game Objects.

Les mini-itérateurs sont créés à l'aide d'autres fonctions statiques du séquenceur.

### Itérer sur des coordonnées

Le séquenceur permet d'éviter deux itérations imbriquées sur x et sur y. Il nécessite un seul paramètre, renvoyé par `Sequencer.iter_on_rect(rect, instanciate_coord=False)`.

`rect` doit être un objet `Rect`, `instanciate_coord` est un booléen, lorsqu'il vaut True, l'itérateur recrée un nouvel objet `Coord` à chaque itération. Il est nécessaire de le mettre à True uniquement dans des situations très particulières, où vous auriez besoin de modifier temporairement les coordonnées sur lesquelles vous itérez.

L'exemple ci-dessous remplit l'aire de jeu avec une alternance de diamant vert et de diamant jaune, pour créer une sorte d'échiquier.

```
import squarity
S = squarity.Sequencer

class GameModel(squarity.GameModelBase):

    def on_start(self):
        color = "gem_green"
        seq = S.seq_iter(S.iter_on_rect(self.rect))
        for coord in seq:
            if coord.x:
                color = "gem_green" if color == "gem_yellow" else "gem_yellow"
            self.gobj = squarity.GameObject(coord, color)
            self.layer_main.add_game_object(self.gobj)
```

### Itérer sur des Game Objects

Avec un deuxième paramètre, le séquenceur permet d'itérer sur les Game Objects d'un ou plusieurs layers.

`Sequencer.gobj_on_layers(layers)` renverra les Game Objects les un après les autres. Le paramètre `layers` est la liste de Layer dans laquelle on recherche les Game Objects. L'itération est effectuée sur le Rect spécifié par `iter_on_rect`.

`Sequencer.gobj_on_layers_by_coords(layers)` renverra des listes de Game Objects, en les groupant par coordonnées. Les coordonnées n'ayant aucun Game Objects généreront des listes vides.

Le troisième paramètre du séquenceur permet de filtrer sur des noms de sprites spécifique: `Sequencer.filter_sprites(sprite_names, skip_empty_lists=False)`. Le paramètre `sprite_names` doit être une liste de strings. Le paramètre `skip_empty_lists` est utile lorsqu'on utilise la fonction `gobj_on_layers_by_coords`, il permet de passer les cases ne contenant aucun Game Objects.

L'exemple ci-dessous place un diamant vert sur une case, et deux diamants verts + un diamant jaune sur une autre. Chaque bouton de direction effectue une itération spécifique et logge les infos dans la console.

 - La flèche du haut itère sur tous les Game Objects.
 - La flèche du bas itère sur les listes de Game Objects (le log est moche mais c'est pas grave).
 - La flèche de gauche itère sur les diamants vert.
 - La flèche de gauche itère sur les listes de diamant verts, en passant les cases qui n'en contiennent pas.

```
import squarity
S = squarity.Sequencer

class GameModel(squarity.GameModelBase):

    def on_start(self):
        self.layer_other = squarity.Layer(self, self.w, self.h)
        self.layers.append(self.layer_other)
        self.layer_main.add_game_object(
            squarity.GameObject(squarity.Coord(5, 2), "gem_green")
        )
        self.layer_main.add_game_object(
            squarity.GameObject(squarity.Coord(2, 4), "gem_yellow")
        )
        self.layer_other.add_game_object(
            squarity.GameObject(squarity.Coord(2, 4), "gem_green")
        )
        self.layer_other.add_game_object(
            squarity.GameObject(squarity.Coord(2, 4), "gem_green")
        )

    def on_button_direction(self, direction):
        print("#" * 20)
        if direction == squarity.dirs.Up:
            for gobj in S.seq_iter(
                S.iter_on_rect(self.rect),
                S.gobj_on_layers(self.layers)
            ):
                print(gobj)
        elif direction == squarity.dirs.Down:
            print(*S.seq_iter(
                S.iter_on_rect(self.rect),
                S.gobj_on_layers_by_coords(self.layers)
            ))
        elif direction == squarity.dirs.Left:
            for gobj in S.seq_iter(
                S.iter_on_rect(self.rect),
                S.gobj_on_layers(self.layers),
                S.filter_sprites(["gem_green"])
            ):
                print(gobj)
        elif direction == squarity.dirs.Right:
            for game_objects in S.seq_iter(
                S.iter_on_rect(self.rect),
                S.gobj_on_layers_by_coords(self.layers),
                S.filter_sprites(["gem_green"], True)
            ):
               print(*game_objects)
```

### Récupérer le premier Game Object

Il est possible de récupérer directement le premier élément renvoyé par un séquenceur, au lieu d'itérer avec. Pour cela, utilisez la fonction `Sequencer.seq_first` à la place de `Sequencer.seq_iter`. Le fonctionnement des paramètres est exactement le même. La fonction `seq_first` va itérer une seule fois sur la séquence que vous avez fournie et renverra le premier élément. Si l'itération ne peut pas du tout être effectuée, la fonction renvoie None.

Pour information, la fonction `GameModel.get_first_gobj` utilise un séquenceur en interne.


## Exemple bonus : afficher tous les sprites existants

Attention, cet exemple n'utilise pas le jeu des diamants. Vous devez sélectionner le jeu d'exemple H2O. C'est plus amusant ainsi, car H2O contient beaucoup d'images.

Dans la config, modifier l'information `version` de "1.0.0" vers "2.1.0".

Ensuite, supprimez le code existant et remplacez-le par celui-ci:
```
import json
import squarity

class GameModel(squarity.GameModelBase):

    def on_start(self):
        game_conf = json.loads(self.str_game_conf_json)

        seq = squarity.Sequencer.seq_iter(
            squarity.Sequencer.iter_on_rect(self.rect)
        )
        for coord, sprite_name in zip(seq, game_conf["img_coords"].keys()):
            self.layer_main.add_game_object(
                squarity.GameObject(coord, sprite_name)
            )
```

Vous verrez tous les sprites du jeu affiché les uns après les autres dans l'aire de jeu.

Cet exemple de code fonctionne avec tous les jeux (à condition de les mettre en version 2). Il peut être utile, par exemple si vous voulez vérifier que vous avez bien défini toutes les coordonnées de tous les noms de sprites.


## Créer un lien direct vers votre jeu

Le fonctionnement est le même que pour la version 1.

Les explications sont ici : https://github.com/darkrecher/squarity-doc/blob/master/user_manual/main_page.md#partager-un-jeu

