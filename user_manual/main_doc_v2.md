# Documentation de référence de Squarity V2

Squarity est un espace de création et de partage de jeux vidéo jouables dans un navigateur web. Les jeux se déroulent sur une grille en 2D composée de carrés. Le fonctionnement et les règles du jeu sont définis par du code en python.

Ce document décrit les fonctionnalités de la version 2.1.0 du moteur de Squarity. Il suppose que vous avez déjà un minimum de connaissance en python. Si ce n'est pas le cas, vous pouvez les acquérir avec la doc ["dive into python" en français](https://diveintopython.org/fr/learn).

Un jeu est défini par trois informations :

 - le tileset,
 - la configuration,
 - le "game code".

Pour l'instant, Squarity ne gère pas de comptes ni de profil personnel. Vous devez sauvegarder vos jeux par vous-même. Vous pouvez les distribuer en [les publiant sur un gist github](https://squarity.pythonanywhere.com/create/share-your-game).


## Le tileset

Le tileset est comme un atlas : c'est une image regroupant toutes les "sous-images" des éléments de votre jeu (décor, personnages, bonus, ...).

Pour que votre tileset soit accessible dans Squarity, il doit être publié sur internet : dans un repository github, sur un site d'hébergement d'images, etc.

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

Dans l'interface, cette configuration doit être écrite dans la zone de texte "Config du jeu".

### Informations générales de la config

`name` (chaîne de caractère) : le nom de votre jeu. Il sera écrit dans le titre de la page web, précédé du texte "Squarity - ".

`version` (chaîne de caractère) : version du moteur du jeu, indiquez "2.1.0". ([Voir Version"](#version-du-moteur-squarity)).

`tile_size` (nombre entier) : la taille par défaut, en pixels dans le tileset, des images représentant les éléments de votre jeu.

`game_area` (sous-dictionnaire contenant deux nombres entiers) : largeur et hauteur de l'aire de jeu, en nombre de cases (tiles).

### Définition des images

Il s'agit des images représentant les éléments de votre jeu (les "Game Objects"). Elles sont définies par un sous-dictionnaire, situé dans `img_coords`.

Chaque clé de ce sous-dictionnaire est une chaîne de caractère que vous pourrez utiliser dans votre code python, pour spécifier l'image d'un Game Object.

Chaque valeur de ce sous-dictionnaire est une liste de 2 entiers, représentant les coordonnées x et y, en pixels dans le tileset, du coin supérieur gauche de l'image.

Il est possible d'ajouter d'autres valeurs après ces deux entiers. [Voir "Info supplémentaires pour les sprites"](#info-suppl%C3%A9mentaires-pour-les-sprites).

### Version du moteur Squarity

La seule information utile de la clé `version` est le premier nombre.

Si ce nombre est "1", la version utilisée sera "1.0.0".

Si ce nombre est "2", la version utilisée sera la version 2.x.y la plus récente (actuellement : "2.1.0"). Vous n'avez pas accès aux précédentes versions 2.x.y, mais elles sont censées être rétro-compatibles.

### Descriptions et notes de bas de page

Pas encore documenté. Ça viendra bientôt. Mais c'est assez simple à comprendre.

Il s'agit des clés suivantes :

 - `show_code_at_start`
 - `appendices`
   - `descrip_text`
   - `descrip_img`
   - `show_descrip_at_start`
   - `footnotes`

Il y a des exemples de ces clés dans le jeu "Tiny Skweek plays breakout" et dans le tutoriel soko-ban.

## Notions de base du "game code"

Il s'agit du programme définissant la logique de votre jeu, il est écrit en langage python.

Dans l'interface, placez ce programme dans la zone de texte intitulée "Le code du jeu".

Ce programme doit contenir une classe intitulée `GameModel`, qui hérite de la classe `squarity.GameModelBase`.

Cette classe sera instanciée par le moteur Squarity. Elle contient des fonctions de callback qui seront automatiquement appelées sur certains événements (appui sur un bouton du jeu, clic de souris, etc.)

Votre `GameModel` contient des objets de type `squarity.Layer`, ordonnés dans une liste. Chacun de ces layers contient un tableau en 2 dimensions avec des "tiles". La largeur et la hauteur correspondent à celles de l'aire de jeu (c'est à dire les valeurs `nb_tile_width` et `nb_tile_height` indiquées dans la config JSON).

Une tile représente une case de l'aire de jeu. Chaque tile peut contenir plusieurs `squarity.GameObject`, représentant des objets de votre jeu.

 - Un GameObject est toujours placé sur une seule tile de un seul layer.
 - Un GameObject possède des coordonnées (x, y) indiquant la tile d'appartenance dans le layer.
 - Un GameObject possède une variable membre `sprite_name`, de type chaîne de caractère. Cette variable doit avoir pour valeur l'un des noms définis dans le dictionnaire `img_coords` de la configuration JSON.

La suite de cette documentation contient des exemples de code. Pour les essayer :

 - chargez le jeu de l'émeraude verte (qui fonctionne en version 2.1.0),
 - copier-collez le code d'exemple dans la fenêtre du code,
 - cliquez sur le bouton "Exécuter".

Vous devriez voir des informations apparaître dans la fenêtre de texte en bas de l'aire de jeu.

Les exemples de code qui ne commencent pas par la ligne `import squarity` doivent être **ajoutés** dans le code existant, juste après la ligne `import squarity` déjà présente.

Les exemples de code commençant par `import squarity` sont plus complets, ils doivent **remplacer** tout le code existant.


## Schéma d'affichage, calculs des tailles

Vous ne pouvez pas définir la taille en pixel des cases réellement affichées, car cette taille s'adapte automatiquement à la fenêtre du navigateur affichant Squarity.

Le calcul est effectué comme suit :

 - détermination des plus grandes valeurs possibles pour la largeur et la hauteur des tiles (en pixel, à l'écran) :
   - `largeur_case_temp = largeur_affichage // config.game_area.nb_tile_width`
   - `hauteur_case_temp = hauteur_affichage // config.game_area.nb_tile_height`
 - détermination de la taille réelle des tiles, en prenant la plus petite :
   - `taille_case_affichage = min(largeur_case_temp, hauteur_case_temp)`
 - application de cette taille pour la largeur et la hauteur à l'écran :
   - `largeur_case_affichage = taille_case_affichage`
   - `hauteur_case_affichage = taille_case_affichage`

Ensuite, une mise à l'échelle des images est effectuée. On part de la taille définie par `config.tile_size` (en pixel de tileset), pour arriver à des images ayant une taille égale à `taille_case_affichage` (en pixel d'écran).

La mise à l'échelle est effectuée selon l'algorithme "proche voisin", sans traitement ni anti-aliasing. Vous verrez donc des gros pixels carrés si vos images de tileset sont petites et que vous jouez dans une grande fenêtre.

![Schéma décrivant les tailles de case et d'aire de jeu](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/schema_game_sizes.png)


## class Direction

Il s'agit d'une classe python dont il n'existe que 8 instances : 4 pour les directions de base (haut, droite, bas, gauche) et 4 pour les diagonales. Ces 8 instances sont stockées dans l'objet `squarity.dirs`.

### Liste des directions

Les instances peuvent être comparées entre elles, par exemple : `my_dir == dirs.Up`. Elles peuvent être converties en entier et en string. Elles possèdent une variable `vector` : un tuple de deux éléments indiquant respectivement le déplacement en X et le déplacement en Y.

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

Les directions sont "hashables", vous pouvez donc les utiliser comme clé de dictionnaire. Par exemple: `dist_to_bonus = {dirs.Up: 4, dirs.UpRight: 7}` ...

### Rotations

La méthode `turn_cw` renvoie une direction tournée dans le sens des aiguilles d'une montre. La méthode `turn_ccw` renvoie une direction tournée dans le sens inverse. L'angle de rotation par défaut est de 90 degrés.

```
d = squarity.dirs.Right
print(d.turn_cw())
# La valeur 'down' s'affiche dans la console.
```

Un paramètre optionnel (nombre entier) permet de préciser l'angle de rotation, en multiple de 45 degrés.

```
d = squarity.dirs.UpRight
print(d.turn_ccw(3))
# La valeur 'left' s'affiche dans la console.
```


## class Coord

Cette classe sert à identifier une case dans l'aire de jeu ou dans un layer. Elle possède deux variables membres `x` et `y`, de type `int`.

### Instanciation

La classe peut être instanciée en indiquant un X et un Y, ou une autre `Coord`. Les objets `Coord` peuvent être comparés entre eux.

```
coord_a = squarity.Coord(5, 2)
coord_b = squarity.Coord(coord=coord_a)
print(coord_a == coord_b)
# La valeur 'True' s'affiche dans la console
```

### Méthodes de base

Les `Coord` peuvent être utilisées comme clés dans un dictionnaire. Elles ont une représentation textuelle, ce qui permet de les écrire avec un `print`. Elles peuvent être dupliquées avec la méthode `clone`.

```
coord_a = squarity.Coord(5, 2)
coord_b = coord_a.clone()
print(coord_b)
# Le texte "<Coord 5, 2 >" s'affiche dans la console
```

### Méthodes de modification

La méthode `move_dir` permet de se déplacer dans une direction donnée, sur une distance donnée (indiquée par un `int`). La distance par défaut est 1.

```
coord_a = squarity.Coord(5, 2)
coord_a.move_dir(squarity.dirs.Right, 2)
print(coord_a)
# Affichage de "<Coord 7, 2 >"
```

La méthode `move_by_vect` permet d'appliquer un déplacement, spécifié par le paramètre `vector` (de type `Coord`), ou spécifié par les paramètres `x` et `y`.

Attention, il n'y a pas de blocage sur les bords. Les mouvements peuvent amener une coordonnée en négatif ou en dehors de l'aire de jeu.

```
coord_a = squarity.Coord(5, 2)
coord_vect = squarity.Coord(0, -3)
coord_a.move_by_vect(vector=coord_vect)
coord_a.move_by_vect(x=1, y=-3)
print(coord_a)
# Affichage de "<Coord 6, -4 >"
```

La méthode `scale` permet de multiplier les coordonnées par un facteur.

La méthode `reverse` change `x` et `y` en leurs opposés.

Toutes ces méthodes modifient les coordonnées "en place", elles ne créent pas un nouvel objet `Coord`. Il est possible de les enchaîner.

```
coord_a = squarity.Coord(0, 0)
coord_a.move_by_vect(x=1, y=3).scale(2).reverse()
print(coord_a)
# Affichage de "<Coord -2, -6 >"
```


## class Rect

Définit un rectangle à partir de 4 paramètres de type `int` :

 - coordonnée X du coin supérieur droit,
 - coordonnée Y du coin supérieur droit,
 - largeur,
 - hauteur.

Les coordonnées dans le rectangle s'étendent de X jusqu'à (X+largeur-1) en abscisse, et de Y jusqu'à (Y+hauteur-1) en ordonnée. C'est le même principe que la fonction python `range`.

### Création d'un Rect

En plus de l'instanciation classique, il est possible de créer un `Rect` avec la méthode statique `from_coords`. Les paramètres spécifient deux coins du rectangle.

Pour respecter le principe précédent, la colonne de droite et la ligne du bas ne sont pas incluses dans le rectangle.

```
rect = squarity.Rect.from_coords(
    squarity.Coord(10, 20),
    squarity.Coord(12, 25),
)
print(rect)
# Le texte "<Rect(10, 20, 2, 5)>" s'affichera dans la console.
```

### Méthode coord_upleft

Renvoie une `Coord` contenant les coordonnées du coin supérieur gauche du rectangle.

### Méthode in_bounds

Indique si la `Coord` passée en paramètre se trouve à l'intérieur du rectangle.

```
rect = squarity.Rect(5, 2, 3, 5)
print(rect.in_bounds(squarity.Coord(0, 0)))
# La valeur False s'affichera dans la console.
print(rect.in_bounds(squarity.Coord(5, 4)))
# La valeur True s'affichera dans la console.
```

### Méthode on_borders

Indique si la `Coord` se trouve sur un bord du rectangle.

```
rect = squarity.Rect(5, 2, 3, 5)
for x in range(4, 10):
    coord_a = squarity.Coord(x, 3)
    border = rect.on_border(coord_a)
    print(coord_a, "est-elle au bord ?", border)
# Les informations suivantes vont s'afficher:
# <Coord 4, 3 > est-elle au bord ? False
# <Coord 5, 3 > est-elle au bord ? True
# <Coord 6, 3 > est-elle au bord ? False
# <Coord 7, 3 > est-elle au bord ? True
# <Coord 8, 3 > est-elle au bord ? False
# <Coord 9, 3 > est-elle au bord ? False
```

### Méthodes move_dir et move_by_vect

Ces méthodes déplacent le rectangle selon une direction ou un vecteur. Elles fonctionnent de la même manière que celles de la classe `Coord`.


## class GameObject

Un "game object" (ou gobj) est un élément qui s'affiche dans l'aire de jeu. Un game object possède des coordonnées et un nom de sprite (`sprite_name`). Le nom de sprite correspond à un nom référencé dans le dictionnaire `img_coords` de la config JSON.

Pour que le game object s'affiche, il doit être placé dans un `squarity.Layer`. Un game object peut être transféré d'un layer à un autre. Il peut également n'appartenir à aucun layer.

Les coordonnées et le nom de sprite doivent être spécifiés dès l'instanciation du game object. L'ajout dans le layer peut être effectué juste après (voir [la classe squarity.Layer](#class-layer)).

```
gobj = squarity.GameObject(squarity.Coord(5, 2), "my_sprite")
print(gobj)
# Le texte "<Gobj (5,2) my_sprite>" s'affiche dans la console.
```

L'instanciation possède d'autres paramètres facultatifs. Ils sont détaillés plus loin dans cette doc.

### Nom du sprite

L'aspect visuel du game object peut être directement changé en modifiant la variable membre `sprite_name`. La nouvelle image s'affichera en fonction du tileset et de la config JSON.

Attention, il n'y a pas de vérification sur le nom du sprite. Si vous indiquez un nom qui n'est pas référencé dans `config.img_coords`, le jeu va planter sans aucun message. (On améliorera ça dans les versions à venir).

### Coordonnées (accès et modification)

Le game object possède une variable membre interne appelée `_coord`. **Vous n'êtes pas censé y accéder directement**, au risque de désordonner l'indexation des game objects dans les layers.

Pour lire les coordonnées, utilisez la méthode `coord_clone = gobj.get_coord()`. Si vous changez le contenu de la variable `coord_clone`, vos modifications ne seront pas reportées dans le game object.

Pour déplacer un game object, utilisez les méthodes `move_xxx` :

 - `move_to_xy` : déplace l'objet sur une case de destination, spécifiée par les paramètres X et Y (`int`).
 - `move_to` : déplace l'objet sur une case de destination, spécifiée par le paramètre `dest_coord` (`Coord`).
 - `move` : déplace l'objet de manière relative, selon un vecteur de déplacement spécifié par le paramètre `vector` (`Coord`).
 - `move_dir` : déplace l'objet de manière relative, selon le paramètre `direction` (`Direction`) et le paramètre facultatif `distance` (`int`).

```
gobj = squarity.GameObject(squarity.Coord(5, 2), "my_sprite")
gobj.move_to_xy(15, 9)
print(gobj)
# Affichage de "<Gobj (15,9) my_sprite>".
gobj.move_to(squarity.Coord(7, 4))
print(gobj)
#   --------->        (7,4)
gobj.move(squarity.Coord(1, -1))
print(gobj)
#   --------->        (8,3)
gobj.move_dir(squarity.dirs.Right, 4)
print(gobj)
#   --------->        (12,3)
```

Ces 4 fonctions laissent le game object dans le même layer. Voir la documentation de la classe layer pour transférer un game object d'un layer à un autre.

### Transitions ajoutées automatiquement.

Lorsque vous déplacez un game object, une "transition" est automatiquement affichée. Durant 200 millisecondes, le game object se déplace progressivement (pixel par pixel) depuis sa case initiale vers sa case de destination.

Ce déplacement automatique est effectué en une seule ligne droite. Par exemple, si vous déplacez un objet des coordonnées (5, 3) vers les coordonnées (8, 2), la ligne de déplacement sera oblique.

Si vous changez plusieurs fois les coordonnées dans un même tour de jeu, la transition n'utilisera pas les valeurs intermédiaires. Les deux seules valeurs prises en compte sont celles avant et après l'exécution du code.

Vous pouvez déclencher des transitions simultanées sur plusieurs game objects, en modifiant les coordonnées de chacun d'entre eux.

Il est possible de définir des déplacements avec des étapes intermédiaires. Par exemple, un déplacement horizontal de x=5 vers x=8, puis un vertical de y=3 vers y=2. [Voir "Transitions"](#transitions).

Le temps de la transition peut être redéfini individuellement pour chaque game object, avec la fonction `gobj.set_transition_delay(transition_delay)`. Le paramètre `transition_delay` est un `int`, en millisecondes. Toutes les futures transitions dues à un changement de coordonnées utiliseront ce nouveau temps.

Les 4 fonctions `move_xxx` possèdent un paramètre facultatif `transition_delay`, permettant de définir un temps spécifique uniquement pour la prochaine transition.

Si transition_delay est défini à 0, l'objet se déplacera instantanément.

### Callback de fin de transition

Il s'agit d'une fonction python que vous définissez et que vous associez à un game object. Elle sera automatiquement exécutée chaque fois que le game object aura fini toutes ses transitions en cours. Pour associer une callback, utilisez la méthode `gobj.set_callback_end_transi(callback_end_transi)`.

Les callbacks ne peuvent pas avoir de paramètre, mais vous pouvez indiquer une fonction ou une méthode d'un objet spécifique.

Pour enlever une callback, exécutez `set_callback_end_transi` avec le paramètre `None`.

Les 4 fonctions `move_xxx` possèdent un paramètre facultatif `callback`, permettant de définir une callback différente uniquement pour la prochaine transition.

```
def my_callback():
    print("coucou")

gobj = squarity.GameObject(squarity.Coord(5, 2), "my_sprite")
gobj.set_callback_end_transi(my_callback)
# (Cette exemple n'affiche rien dans la console, désolé)
```


## class Layer

Un layer est un tableau en 2 dimensions, contenant des game objects. Votre aire de jeu peut contenir plusieurs layers, affichés dans un ordre déterminé. Vous pouvez donc avoir un layer pour le décor de fond, un pour les personnages et les bonus, un pour les éléments d'interface, etc.

L'ordre d'affichage des objets au sein d'un layer n'est pas déterminé. Pour être sûr de l'ordre, vous devez utiliser plusieurs layers.

Si l'ordre importe peu, vous pouvez placer tous vos objets dans l'unique layer créé par défaut : la variable membre `layer_main`, dans le `GameModel`.

### Ajouter et retirer des game objects

La méthode `layer.add_game_object(gobj)` permet d'ajouter un game object dans un layer. Les coordonnées du game object doivent être définies.

La méthode `layer.remove_game_object(gobj)` permet d'enlever un game object d'un layer. Une exception sera levée si vous tentez d'enlever un game object n'appartenant pas au layer.

La méthode `layer.remove_at_coord(coord)` permet d'enlever tous les game objects situés aux coordonnées indiquées en paramètre.

Après avoir été enlevé, le game object existe toujours. Vous pouvez le réutiliser et le placer dans un autre layer.

Ci-dessous, un exemple de code minimal affichant un seul objet immobile. Pour l'exécuter, sélectionnez le jeu d'exemple de l'émeraude verte, supprimez tout le game code, puis copier-collez ce texte à la place.

```
import squarity

class GameModel(squarity.GameModelBase):
    def on_start(self):
        self.gobj = squarity.GameObject(squarity.Coord(5, 2), "gem_green")
        self.layer_main.add_game_object(self.gobj)
```

### Récupérer des tiles et des game objects

Chaque élément du tableau 2D d'un layer est un objet `squarity.Tile`, ils sont utiles pour se déplacer dans un layer, grâce à la variable `adjacencies`. Il s'agit d'une liste de 8 éléments, contenant les tiles adjacentes. Certains de ces éléments peuvent être `None`, pour les tiles qui sont au bord.

Les game objects d'une tile sont stockés dans la variable membre `game_objects` (de type `list`).

Les méthodes `layer.get_tile(coord)` et `layer.get_tile_xy(x, y)` permettent de récupérer une tile.

Ajoutez ce code après le code d'exemple précédent pour tester une récupération de game object.

```
        tile = self.layer_main.get_tile_xy(5, 1)
        tile_down = tile.adjacencies[int(squarity.dirs.Down)]
        print("Nombre d'objets sur la tile :", len(tile_down.game_objects))
        print(tile_down.game_objects)
```

La méthode `layer.get_game_objects(coord)` permet de récupérer directement tous les game objects situés sur `coord`.

La méthode `layer.iter_all_game_objects()` permet d'itérer sur tous les game objects d'un layer.

```
        for gobj in self.layer_main.iter_all_game_objects():
            print(gobj)
```

### Créer des layers et les ajouter dans le jeu

Les layers doivent être placés dans la liste `layers` du `GameModel`, cette liste contient initialement le `layer_main`.

L'ordre dans `layers` détermine l'ordre d'affichage. Le premier layer de la liste est dessiné en premier et apparaîtra donc en-dessous de tous les autres layers. Le dernier layer de la liste apparaîtra au-dessus de tous les autres.

Vous pouvez ajouter, enlever et réordonner les layers dans la liste à tout moment. Ce sera immédiatement pris en compte dans l'affichage de l'aire de jeu.

Lors de l'instanciation, un layer a besoin d'avoir une référence vers le `GameModel` dans lequel il est placé. Il faut également spécifier une largeur et une hauteur, en nombre de cases.

```
class GameModel(squarity.GameModelBase):
    def on_start(self):
        layer_second = Layer(self, self.w, self.h)
        self.layers.append(layer_second)
```

Tous les layers que vous placez dans `layers` doivent avoir les mêmes largeur et hauteur que votre aire de jeu. Ces dimensions sont déjà initialisés dans le `GameModel`, variables membres `game_model.w` et `game_model.h`

Pour gérer la logique interne de votre jeu, vous pouvez utiliser des layers de n'importe quelles dimensions, que vous ne placerez pas dans `layers`. Ils ne seront pas affichés.

La fonction `Layer.__init__` possède un paramètre facultatif `show_transitions`, défini à True par défaut. Lorsqu'il est défini à False, le layer ne gère aucune transition, ni pour les déplacements d'objets ni pour les modifications graphiques (scaling, décalage, ...). Lorsque vous changez les coordonnées d'un objet dans un layer sans transition, il sera instantanément déplacé vers sa case de destination.

Les layers sans transition sont gérés de manière optimisée par le moteur Squarity, ils permettent des mouvements massifs et fréquents. Ils peuvent être utiles, par exemple, pour afficher le décor de fond de votre jeu, si ce décor change d'un seul coup d'un niveau à un autre.

Le choix d'avoir ou pas des transitions peut être effectué uniquement à l'instanciation du layer. Si vous modifiez la variable `layer.show_transitions` après l'avoir créé, ce ne sera pas pris en compte par le moteur.

### class LayerSparse

Il s'agit d'une classe ayant le même fonctionnement que la classe `Layer` (les deux héritent de `LayerBase`). Les game objects contenus dans un `LayerSparse` ne sont pas indexés dans un tableau en deux dimensions, mais placés dans une liste unique.

L'ajout, la suppression et le parcours d'objets sont plus rapides avec un `LayerSparse`, mais la récupération d'objets à une coordonnée spécifique est plus lent.

Si vous créez des jeux n'ayant pas de gros besoins en performance, vous n'avez pas besoin de vous soucier de ces détails. Vous pouvez utiliser uniquement des classes `Layer`, avec gestion des transitions.

Liste des méthodes communes aux classes `Layer` et `LayerSparse` :

 - `get_game_objects`
 - `iter_all_game_objects`
 - `add_game_object`
 - `remove_game_object`
 - `remove_at_coord`
 - `move_game_object`
 - `move_game_object_xy`

Les méthodes `get_tile` et `get_tile_xy` ne sont pas présentes dans un `LayerSparse`, puisqu'il n'y a pas de tableau en 2 dimensions contenant des tiles.


## class GameModel

Il s'agit de la classe principale définissant la logique de votre jeu. Elle hérite de `GameModelBase`. Vous devez la définir, mais pas l'instancier, c'est fait automatiquement par le moteur.

Le game model sert à définir des fonctions de callback, qui seront automatiquement appelées sur certains événements dans le jeu.

### Liste des callbacks

`on_start(self)` : cette fonction est appelée une seule fois au début du jeu. Il est conseillé de mettre votre code d'initialisation dans cette fonction plutôt que dans `__init__`, car `on_start` permet de renvoyer un objet `EventResult`. [Voir la classe "EventResult"](#class-eventresult)

`on_click(self, coord)` : cette fonction est appelée à chaque clic de souris dans l'aire de jeu. Le paramètre `coord` indique la case où le clic a eu lieu. Vous ne pouvez pas savoir précisément quel Game Object a été cliqué, ni la position exacte du clic au pixel près, car le but de Squarity est de rester simple et de se spécialiser dans les jeux en 2D sur un quadrillage.

Dans l'exemple ci-dessous, un diamant s'ajoute sur chaque case que vous cliquez.

```
import squarity

class GameModel(squarity.GameModelBase):
    def on_click(self, coord):
        if not self.layer_main.get_game_objects(coord):
            self.gobj = squarity.GameObject(coord, "gem_yellow")
            self.layer_main.add_game_object(self.gobj)
```

`on_button_direction(self, direction)` : cette fonction est appelée lorsque l'un des 4 boutons de direction est cliqué ou que l'une des 4 touches de direction du clavier est appuyée. Le paramètre `direction` est un objet de type `Direction`.

Dans l'exemple ci-dessous, l'aire de jeu affiche un diamant qui se déplace en fonction des actions de la personne qui joue.

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

`on_button_action(self, action_name)` : cette fonction est appelée lorsque la personne qui joue déclenche l'action "1" ou "2", c'est à dire dans l'un des cas suivants :

 - un des boutons "1" ou "2" à côté des flèches de direction a été cliqué.
 - l'une des touches du clavier "1" ou "2" au-dessus des lettres a été appuyée.
 - l'une tes touches "1" ou "2" du pavé numérique a été appuyée.

### Variables membres de GameModel

Elles sont initialisées dès le départ. Vous pouvez les lire mais vous ne devriez pas les modifier, car elles sont utilisées dans la librairie squarity.

 - `self.w` : largeur de l'aire de jeu, en nombre de case. (Correspond à `nb_tile_width` dans la config json)
 - `self.h` : hauteur de l'aire de jeu, en nombre de case. (Correspond à `nb_tile_height` dans la config json)
 - `self.str_game_conf_json` : chaîne de caractère contenant la configuration json complète.
 - `self.rect` : objet `Rect` ayant les dimensions de l'aire de jeu, c'est à dire `Rect(0, 0, self.w, self.h)`.
 - `self.transition_delay` : définit le temps par défaut (en millisecondes) de toutes les transitions effectuées suite à un changement de coordonnées d'un game object. Contrairement aux autres variables, celle-ci peut être modifiée. [Voir "Transitions"](#transitions)

### Méthode get_first_gobj

La méthode `self.get_first_gobj(coord, sprite_names, layer)` permet de récupérer le premier game object présent dans l'aire de jeu, selon différents critères cumulables. Les 3 paramètres sont facultatifs. Si aucun objet n'est trouvé, la méthode renvoie None.

 - paramètre `coord` : par défaut, l'objet est cherché sur toute l'aire de jeu. Sinon, ce paramètre peut être un `Rect` ou une `Coord`, indiquant dans quelle zone ou sur quelles coordonnées on cherche l'objet.
 - paramètre `sprite_names` : par défaut, pas de filtre sur le nom de sprite. Sinon, ce paramètre doit être une liste de strings, indiquant le ou les noms de sprite recherchés.
 - paramètre `layer` : par défaut, l'objet est cherché dans tous les Layers de la liste `self.layers`. Sinon, ce paramètre doit être un unique `Layer`.


## class EventResult

Cette classe regroupe des informations générales que vous pouvez communiquer au moteur du jeu, après l'exécution de n'importe quelle fonction de callback (provenant du game model, d'un game object ou de n'importe quoi d'autres).

Par défaut, ces fonctions de callback ne renvoient rien (elles n'ont pas d'instruction `return`). Dans ce cas, la valeur réellement renvoyée est `None`, mais vous pouvez renvoyer un objet `EventResult` à la place.

### Callback différée

Vous pouvez indiquer dans un `EventResult` que le moteur doit exécuter une de vos fonctions (une autre callback), après un délai spécifié.

Instanciez une classe `DelayedCallBack`, en indiquant le délai d'exécution en millisecondes et la callback. Vous pouvez indiquer une fonction de votre code, une méthode de votre game model (`self.my_callback`), une méthode d'un game object spécifique, etc. La callback ne peut pas avoir de paramètres.

Ajoutez ensuite cet objet `DelayedCallBack` dans votre event result, avec la fonction `event_result.add_delayed_callback`.

Le code ci-dessous écrit "coucou" dans la console après un temps d'attente de 500 millisecondes.

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

C'est un peu verbeux, on raccourcira ce code dans une version ultérieure de Squarity.

Vous ne pouvez pas annuler une callback après l'avoir renvoyée via un event result. C'est à vous de le gérer dans votre code.

Il y a un bug : si vous redémarrez votre jeu, ou même si vous lancez un autre jeu, les callbacks du jeu précédent restent en mémoire et sont tout de même exécutées. Ce sera corrigé au plus vite.

### Player Lock (plock) Custom

Votre jeu aura peut-être besoin d'afficher des petites animations courtes, durant lesquelles la personne qui joue n'est pas censée agir. Il est possible d'appliquer un "Player Lock", c'est à dire de bloquer temporairement les boutons et les clics.

Il y a deux types de Player Locks :

 - custom : vous indiquez explicitement, dans votre code, à quel moments se passent les locks et unlocks.
 - transition : les locks/unlocks sont effectués automatiquement d'après les transitions de certains game objects ([Voir "Player Lock Transi"](#blocage-de-linterface-player-lock-transi)).

Pour les locks custom, le blocage est toujours montré dans l'interface : les boutons d'actions apparaissent grisé.

Il est possible de locker/delocker avec plusieurs mots-clés (chacun étant considéré comme une raison pour locker). L'interface redevient active lorsqu'il n'y a plus aucun mot-clé de lock en cours.

Pour locker : instanciez un `EventResult` et ajoutez des strings dans la liste `event_result.plocks_custom`, représentant les mot-clés de lock. Pour enlever des locks : utilisez la liste `event_result.punlocks_custom`.

Attention, l'interface est entièrement bloquée dès le premier mot-clé. Il faut donc obligatoirement prévoir les unlocks en renvoyant des fonctions de callbacks en même temps. Si ce n'est pas fait, la personne qui joue restera bloquée. Le bouton "Exécuter le jeu" enlève tous les locks, mais il réinitialise tout le jeu au début.

Il est possible d'enlever tous les mots-clés de lock d'un seul coup, en ajoutant le caractère `"*"` dans `punlocks_custom`.

Le code ci-dessous locke l'interface pendant 2 secondes à chaque fois que l'on clique dans l'aire de jeu.

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

Certaines actions de votre jeu (en particulier, les fonctions de callback contenant peu de code) ne modifient pas forcément la disposition ou l'état des game objects. Dans ce cas, vous pouvez indiquer au moteur qu'il n'est pas nécessaire de redessiner l'aire de jeu.

Instancier un `EventResult`, définissez la variable `redraw` à False, puis renvoyez-le avec un `return`.

```
        event_result = squarity.EventResult()
        event_result.redraw = False
        return event_result
```

À noter que s'il y a des transitions en cours, l'aire de jeu est régulièrement redessinée pour les afficher. Le fait de renvoyer un event result annulant le rendu n'empêche pas les autres événements de faire leurs rendus à eux.

Vous pouvez cumuler plusieurs éléments dans le même event result. Par exemple, vous pouvez déclarer plusieurs callbacks, locker l'interface avec 3 mot-clés, enlever 4 autres mot-clés de locks, le tout en annulant le rendu.


## Transitions

Une transition représente la modification progressive d'une variable d'un game object, sur une période de temps définie.

Les coordonnées sont des variables transitionnables. L'objet se déplacera pixel par pixel de sa case de destination vers sa case d'arrivée. Visuellement, les coordonnées de votre game object deviennent des valeurs décimales, afin de le placer entre deux cases. Dans votre code python, les coordonnées restent des nombres entiers et passent directement de la valeur de départ à la valeur d'arrivée.

Les variables permettant de décaler et agrandir l'image d'un game object sont elles aussi transitionnables, [voir la classe ComponentImageModifier](#class-componentimagemodifier).

Le sprite name peut avoir des transitions, mais elles ne sont pas progressives. L'image change d'un seul coup. Il est possible d'enchaîner ces changements : une première image pendant 100 millisecondes, une deuxième pendant les 100 millisecondes suivantes, etc.

Il existe deux moyens pour déclencher une transition : modifier directement une variable transitionnable ou exécuter la fonction `game_object.add_transition`.

### Modification d'une variable transitionnable

#### Pour les coordonnées

Il faut appeler une fonction `move_to_xxx`. Le temps de la transition sera déterminé automatiquement. Il prend la première valeur définie parmi :

 - le paramètre optionnel `transition_delay` de la fonction `move_to_xxx`,
 - le temps spécifique au game object, défini via la fonction `game_object.set_transition_delay(transition_delay)`,
 - la variable membre `game_model.transition_delay` (initialisée à 200 millisecondes, que vous pouvez modifier).

#### Pour le sprite name

Il suffit de changer directement la valeur dans le game object. La transition sera instantanée.

### Fonction add_transition

Cette fonction permet d'ajouter une séquence, pouvant contenir plusieurs transitions, elle nécessite deux paramètres :

 - une chaîne désignant une variable membre (`"coord"` ou `"sprite_name"`),
 - une liste contenant des tuples de délais et de valeurs.

Avec `"coord"`, les valeurs doivent être des `Coord`. Le Game Object se déplacera vers ces coordonnées, les unes après les autres.

Dans l'exemple ci-dessous, après un clic dans l'aire de jeu, le diamant vert se déplace à vitesse normale vers la coordonnée (3, 1), puis très rapidement vers (7, 1), puis lentement vers (5, 2).

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

Vous ne pouvez définir que le temps de déplacement, et non pas une vitesse générique. Par exemple, si vous souhaitez que votre game object se déplace toujours à la même vitesse quel que soit la distance à parcourir, vous allez devoir coder vous-même le calcul des temps de déplacement. (On fera mieux à la prochaine version de Squarity).

Lorsque le premier paramètre de `TransitionSteps` est `"sprite_name"`, les valeurs doivent être des strings correspondant à des noms de sprites. Le game object changera successivement d'apparence.

Une transition est affichée progressivement, mais elle est appliquée dans le jeu dès qu'elle est démarrée. Pour les coordonnées, c'est simple à comprendre. Pour un sprite name, l'image change dès le début de la transition et reste telle quelle durant le temps indiqué. Donc pour une transition de sprite name, le dernier temps n'est pas très utile et peut être zéro.

Dans le futur, on changera l'ordre des paramètres. D'abord le sprite name, puis le temps. Ce sera plus logique à comprendre.

Si votre game object a une callback de fin de transition, définie à l'aide de la fonction `game_object.set_callback_end_transi`, cellec-ci sera déclenchée à la fin de la liste des transitions.

### Enchaînement des transitions

Même si des transitions sont en cours, vous pouvez en ajouter d'autres via la méthode `add_transition`. Elles vont s'ajouter après les transitions existantes.

La prise en compte des transitions par le moteur est effectuée à la fin de l'exécution du code en cours (`on_click`, `on_button_xxx`, une callback, ...). Si vous ajoutez plusieurs transitions dans le même code, elles seront déclenchées au même moment et seront exécutées en même temps. Cela permet d'avoir un objet qui se déplace tout en changeant de sprite.

Dans votre game object, les variables membres `coord` et `sprite_name` changent automatiquement, au fur et à mesure de l'enchaînement des transitions. Ce changement n'est pas progressif, il est appliqué au début de chaque transition. Cela permet de garder des nombres entiers dans les coordonnées, même si visuellement l'objet s'affiche entre les deux.

Le moteur essaye, autant que faire se peut, d'avoir le même type de gestion pour les transitions ajoutées suite à une modification de variable et les transitions ajoutées avec `add_transition` :

 - Durant une transition provenant d'une modification de variable, la variable contient la valeur finale. C'est normal, c'est vous même qui l'avez définie avec votre code python.
 - Si vous remodifiez la variable pendant une transition, celle-ci va s'enchaîner après les transitions existantes. Le moteur utilise toujours la valeur finale de l'enchaînement de transitions pour ajouter la prochaine.
 - Durant les transitions provenant de `add_transition`, c'est le moteur du jeu qui modifie automatiquement la variable transitionnée. Cette modification se fait au début de chaque transition, comme si c'était votre code qui le changeait manuellement, à chaque fois que la transition précédente se termine.

**Attention** : il est fortement déconseillé d'avoir, sur un même game object et à un même instant, des transitions provenant de modifications de variable et des transitions provenant de `add_transition`. C'est une situation ambigüe, dans laquelle on ne pourrait pas déterminer les valeurs des variables. Le moteur essaiera de le gérer comme il peut, c'est à dire pas très bien. Avant d'ajouter de nouvelles transitions, vous devez donc vous assurer des transitions en cours et de leurs origines.

Si vous avez des doutes, le plus simple est de s'assurer qu'il n'y a aucune transition en cours sur un game object avant d'effectuer des actions qui en ajouteraient. La méthode `game_object.get_nb_undone_transitions()` renvoie le nombre de transitions restant à effectuer. Si cette fonction renvoie 0, vous pouvez ajouter des transitions en toute sécurité sur ce game object.

Dans l'exemple ci-dessous, lorsque vous appuyez sur un bouton de direction, le diamant se déplace tout en clignotant (jaune-vert-jaune-vert). Lorsque vous cliquez, la console affiche son état actuel : coordonnées, nom du sprite et nombres de transitions restantes. Appuyez plusieurs fois sur un bouton, puis cliquez à fond dans le jeu pour avoir une démonstration de la manière dont les transitions peuvent s'accumuler.

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

Si une touche d'action ou de direction reste appuyée, la fonction de callback correspondante sera exécutée plusieurs fois très vite, ce qui peut poser problème.

Il est possible de bloquer automatiquement toute l'interface du jeu (clics et boutons) tant qu'un game object spécifique a au moins une transition en cours. C'est utile si votre jeu comporte un objet principal dirigé par la personne qui joue. Si un bouton est appuyé durant le mouvement de cet objet, ce ne sera pas pris en compte.

Modifiez la variable membre `plock_transi` de votre game object principal. Celle-ci peut prendre 3 valeurs:

 - `PlayerLockTransi.NO_LOCK` : pas de blocage (valeur par défaut).
 - `PlayerLockTransi.INVISIBLE` : blocage invisible. Les boutons ne changent pas d'apparence, mais rien ne se passe si on clique dessus.
 - `PlayerLockTransi.LOCK` : blockage visible. Les boutons s'affichent en grisé.

```
self.gobj = squarity.GameObject(squarity.Coord(5, 2), "gem_green")
self.gobj.plock_transi = squarity.PlayerLockTransi.INVISIBLE
```

Avec le blocage visible, les boutons d'interface s'affichent en grisé pendant une fraction de seconde, à chaque mouvement de l'objet principal, ce qui peut être déroutant. C'est pourquoi il vaut mieux utiliser un blocage invisible. Les blocages visibles sont utiles pour les animations narratives (les "cut-scenes"), ils permettent d'indiquer explicitement que ce n'est pas le moment de jouer.

Les deux types de blocages ont exactement le même effet, la différence est seulement visuelle.

Les blocages "Player Lock Transi" sont appliqués durant tous les types de transitions, aussi bien celles provenant d'une modification de variable que celles ajoutées avec `add_transition`.

Vous pouvez avoir plusieurs game objects bloquant l'interface. Dans ce cas, l'interface est utilisable lorsqu'aucun de ces objets n'a de transition en cours.

Vous pouvez ajouter des transitions à un objet bloquant même s'il a déjà des transitions en cours.

### Annuler les transitions en cours

La méthode `game_object.clear_transitions_to_record()` permet de supprimer les transitions que vous auriez ajoutées via des méthodes `add_transition`, **avant** qu'elles aient été prises en compte par le moteur du jeu.

La méthode `game_object.clear_all_transitions()` permet d'annuler toutes les transitions prises en compte par le moteur. Dans le code, vous pouvez exécuter cette fonction, puis exécuter des `add_transition`. Dans ce cas, les transitions précédentes seront toutes annulées, celles que vous avez ajoutées seront prises en compte.

Attention, si vous avez ajouté un enchaînement de transition et que vous l'annulez, la transition actuellement en cours est immédiatement terminée (l'objet se déplace instantanément à la destination de la transition). Les transitions qui n'étaient pas commencées sont entièrement annulées.

Pour essayer, remettez le code du chapitre "Gestion des transitions", puis ajoutez ce code à la fin:

```
    def on_button_action(self, action_name):
        self.gobj.clear_all_transitions()
```

Cliquez sur un bouton de direction, immédiatement après, cliquez sur un bouton d'action (le "1" ou le "2").

Selon le moment où vous avez cliqué, le diamant s'arrêtera à un endroit différent, il sera jaune ou vert.


## Info supplémentaires pour les sprites

Chaque valeur du dictionnaire `config.img_coords` (dans la config JSON) définit un sprite. Elle est constituée d'une liste. Les deux premiers éléments sont obligatoires, les 3 suivants optionnels. Il s'agit des éléments suivants :

 - Un nombre entier. Coordonnée x du coin supérieur gauche de l'image, dans le tileset. L'unité est le pixel de tileset.

 - Coordonnée y du coin supérieur gauche de l'image.

 - Un nombre entier, par défaut : `config.tile_size`. Largeur de l'image prise dans le tileset. L'unité est le pixel de tileset. La largeur et la hauteur ont une influence sur la taille de l'image affichée dans l'aire de jeu. Par exemple, si on indique une largeur qui vaut un tiers de `config.tile_size`, l'image affichée fera un tiers de case dans l'aire de jeu.

 - Un nombre entier, par défaut : `config.tile_size`. Hauteur de l'image prise dans le tileset.

 - Une chaine de caractères qui vaut "center" ou "corner_upleft", par défaut : "corner_upleft". Indique où ancrer l'image par rapport à la case de l'aire de jeu.
   * "corner_upleft" : le coin haut gauche de l'image reste fixé sur le coin haut gauche de la case. Si on agrandit l'image, elle va dépasser vers le bas et vers la droite.
   * "center" : le centre de l'image reste fixé sur le centre de la case. Si on agrandit l'image, elle va dépasser par les 4 côtés.

Voir schéma dans le chapitre suivant (class `ComponentImageModifier`).


## class ComponentImageModifier

### Initialisation

Cette classe doit être placée dans un game object au moment de sa création. Elle permet de modifier son affichage dans l'aire de jeu.

Si le `ComponentImageModifier` est ajouté après la création du game object, il ne sera pas pris en compte. Il faut donc instancier votre game object comme ceci :

```
gobj = squarity.GameObject(
    Coord(0, 0),
    "gem_green",
    image_modifier=squarity.ComponentImageModifier()
)
```

### Variables membres

Toutes les variables commençant par `img_` représentent un nombre de pixels dans l'image de tileset. Ce sont des nombres entiers, positifs ou négatifs.

Toutes les variables commençant par `area_` représentent un nombre de cases dans l'aire de jeu. Ces nombres peuvent être négatifs, pour indiquer un sens inverse (vers le haut ou vers la gauche). Ils peuvent être également décimaux, pour indiquer une fraction de case.

Le `ComponentImageModifier` possède les variables suivantes :

 - `img_offset_x`, `img_offset_y` : décalage, dans le tileset, de l'image à afficher. Modifier ces valeurs revient à modifier, pour un seul game object, les 2 premières valeurs du sprite name, dans `config.img_coords`.

 - `img_size_x`, `img_size_y` : taille, dans le tileset, de l'image à afficher. Modifier ces valeurs revient à modifier, pour un seul game object, les 3ème et 4ème valeurs du sprite name, dans `config.img_coords`. Par défaut, ces valeurs `img_size` valent `config.tile_size`.

 - `area_offset_x`, `area_offset_y` : décalage, dans l'aire de jeu, de l'objet affiché. Ces variables permettent d'afficher un objet entre deux cases (même si, dans la logique du jeu, l'objet appartient toujours à une seule case). Par exemple, si `area_offset_x = -1.25`, l'objet sera décalé vers la gauche, sur une distance de une case et un quart. L'objet peut s'afficher partiellement en dehors de l'aire de jeu. Par défaut, ces valeurs `area_offset` valent 0.0.

 - `area_scale_x`, `area_scale_y` : facteur d'échelle de l'image affichée dans l'aire de jeu. Par exemple, si `area_scale_x = 2.5`, l'image sera affichée 2,5 fois plus large que sa taille normale. Le positionnement de l'image retaillée est déterminée à l'aide de l'anchor (la valeur "center"/"corner_upleft" définie dans `config.img_coords`). Par défaut, ces valeurs `area_scale` valent 1.0.

Ces 8 valeurs peuvent être définies lors de la création du `ComponentImageModifier` puis modifiées pendant le jeu. Le component se trouve dans la variable membre `image_modifier` du game object.

Dans l'exemple ci-dessous, le diamant vert est affiché de manière écrasée. Appuyez sur la flèche de gauche ou de droite pour l'écraser encore plus, appuyez sur la flèche du haut ou du bas pour l'étirer.

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

![Schéma décrivant les informations que l'on peut indiquer dans un "image modifier"](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/schema_sprite_infos.png)

### Transitions

Les 8 valeurs du `ComponentImageModifier` sont transitionnables, comme les coordonnées d'un game object.

 - Une simple modification de l'une de ces valeurs déclenche une transition entre la valeur courante et la valeur finale, sur une durée définie via `game_object.set_transition_delay`.
 - Selon la valeur de `game_object.plock_transi`, l'interface peut être lockée durant une transition.
 - La fonction de callback de fin de transition du game object sera appelée, si elle est définie.
 - Il est possible d'ajouter et d'enchaîner des séquences de transition avec la fonction `gobj.image_modifier.add_transitions`.

L'exemple ci-dessous effectue une petite animation avec le diamant vert. Cliquez dans l'aire de jeu pour la déclencher.

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
            squarity.TransitionSteps("area_scale_x", TRANSI_SCALE)
        )
        self.gobj.image_modifier.add_transition(
            squarity.TransitionSteps("area_scale_y", TRANSI_SCALE)
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


## class ComponentBackCaller

Cette classe doit être placée dans un game object, au moment de sa création. Elle permet d'exécuter des callbacks au bout d'un temps défini. Il s'agit du même principe que les callbacks de `EventResult`, mais associées à un game object.

Si le game object est supprimé ou s'il est retiré de son layer, les callbacks prévues ne sont pas exécutées.

Lors de l'instanciation du game object, définisssez le paramètre optionnel `back_caller` avec `ComponentBackCaller()`. Puis, ajoutez une callback avec `back_caller.add_callback(delayed_callback)`.

Contrairement aux autres transitions (coordonnées, sprite name, image modifier), lorsqu'il n'y a plus de callback à exécuter, celles du back_caller ne déclenche pas la callback de fin de transition du game object.

En revanche, les callbacks ajoutées dans le back_caller et qui n'ont pas encore été exécutées sont comptées par la fonction `get_nb_undone_transitions`. (Note: et c'est bizarre et on devrait avoir une fonction spéciale pour renvoyer le nombre de callback restantes).

Dans le code ci-dessous, le diamant vert ajoute deux callbacks dès le lancement du jeu. L'une sera lancée au bout de 2 secondes, l'autre au bout de 4 secondes. Lorsque vous cliquez dans le jeu, le nombre de transitions restantes s'affiche dans la console.

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


## Itérer dans l'aire de jeu

Il est très souvent nécessaire de parcourir tout ou une partie de l'aire de jeu, pour rechercher des game objects spécifiques. La classe `Sequencer` permet d'effectuer les itérations les plus communes.

Cette classe contient uniquement des fonctions statiques, vous n'avez pas besoin de l'instancier.

La fonction `Sequencer.seq_iter` renvoie un itérateur. Les paramètres de cette fonction sont des "mini-itérateurs" mis bout à bout. Selon ces paramètres, votre séquenceur renverra des coordonnées, des game objects ou des listes de game objects.

Les mini-itérateurs sont créés à l'aide d'autres fonctions statiques du séquenceur.

### Itérer sur des coordonnées

Le séquenceur permet d'éviter deux itérations imbriquées sur x et sur y. Il nécessite un seul paramètre, renvoyé par `Sequencer.iter_on_rect(rect, instanciate_coord=False)`.

Le paramètre `rect` est un objet `Rect`. Le paramètre `instanciate_coord` est un booléen. Lorsqu'il vaut True, l'itérateur recrée un nouvel objet `Coord` à chaque itération. C'est nécessaire dans une situation où vous auriez besoin de modifier temporairement les coordonnées sur lesquelles vous itérez.

L'exemple ci-dessous remplit l'aire de jeu avec une alternance de diamant vert et de diamant jaune, pour créer une sorte d'échiquier.

```
import squarity
S = squarity.Sequencer

def get_chessed_gem(coord):
    chessed_gems = ["gem_yellow", "gem_green"]
    chess_index = (coord.x + coord.y) % 2
    return chessed_gems[chess_index]

class GameModel(squarity.GameModelBase):

    def on_start(self):
        seq = S.seq_iter(S.iter_on_rect(self.rect))
        for coord in seq:
            sprite_name = get_chessed_gem(coord)
            self.gobj = squarity.GameObject(coord, sprite_name)
            self.layer_main.add_game_object(self.gobj)
```

### Itérer sur les bords d'un rectangle

La méthode `iter_on_border` du séquenceur permet de faire le tour d'un rectangle, en commençant en haut à gauche, puis vers la droite, vers le bas, et retour en haut à gauche.

Le paramètre optionnel `include_corners` (True par défaut) permet d'indiquer si l'itération se fait avec ou sans les coins du rectangle.

Le paramètre `instanciate_coord` fonctionne de la même manière qu'avec `iter_on_rect`.

```
import squarity
S = squarity.Sequencer

class GameModel(squarity.GameModelBase):

    def on_start(self):
        seq = S.seq_iter(S.iter_on_border(self.rect))
        for coord in seq:
            self.gobj = squarity.GameObject(coord, "gem_green")
            self.layer_main.add_game_object(self.gobj)
```

### Itérer sur des Game Objects

Avec un deuxième paramètre, le séquenceur permet d'itérer sur les game objects d'un ou plusieurs layers.

`Sequencer.gobj_on_layers(layers)` renverra les game objects les un après les autres. Le paramètre `layers` est la liste de layers dans laquelle on les recherche. L'itération est effectuée sur le rectangle spécifié par `iter_on_rect`.

`Sequencer.gobj_on_layers_by_coords(layers)` renverra des listes de game objects, en les groupant par coordonnées. Les coordonnées n'ayant aucun game objects généreront des listes vides.

Le troisième paramètre du séquenceur permet de filtrer sur des noms de sprites spécifique: `Sequencer.filter_sprites(sprite_names, skip_empty_lists=False)`.

 - Le paramètre `sprite_names` est une liste de strings.
 - Le paramètre `skip_empty_lists` est utile avec la fonction `gobj_on_layers_by_coords`, il permet de passer les cases ne contenant aucun game objects.

L'exemple ci-dessous place un diamant vert sur une case et deux diamants verts + un diamant jaune sur une autre. Chaque bouton de direction effectue une itération spécifique et logge les infos dans la console.

 - La flèche du haut itère sur tous les Game Objects.
 - La flèche du bas itère sur les listes de Game Objects (le log est moche mais c'est pas grave).
 - La flèche de gauche itère sur les diamants verts.
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

Il est possible de récupérer directement le premier élément renvoyé par un séquenceur, au lieu d'itérer avec. Pour cela, utilisez la fonction `Sequencer.seq_first` à la place de `Sequencer.seq_iter`. Le fonctionnement des paramètres est le même. La fonction `seq_first` itère une seule fois sur la séquence que vous avez fournie et renvoie le premier élément. Si l'itération est vide, la fonction renvoie `None`.

Pour information, la fonction `GameModel.get_first_gobj` utilise un séquenceur.


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

Cet exemple de code fonctionne avec tous les jeux (à condition de les mettre en version 2). Il peut être utile si vous voulez vérifier que vous avez bien défini toutes les coordonnées de tous les noms de sprites.



