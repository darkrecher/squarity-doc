# Tutoriel Squarity

Ce tutoriel vous montrera comment créer un petit jeu simple avec Squarity. Il s'agit d'un jeu de type [soko-ban](https://fr.wikipedia.org/wiki/Sokoban), dans lequel un personnage doit pousser des caisses pour les ranger dans des emplacements spécifiques.

Il ne vous est pas nécessaire de connaître le langage python, mais ça peut aider.

Certaines notions seront utilisées sans être expliquées en détail, par exemple : le format JSON, la programmation objet, les itérations, etc. À vous d'approfondir ces sujets par vous-mêmes, si vous le souhaitez. Il y a plein de cours de python sur internet.

Ce tutoriel est un peu long, mais rassurez-vous, il est décomposé en plusieurs étapes, et vous êtes récompensé·e par un résultat à chaque fois.

À la fin (TODO : quand j'aurais fini de l'écrire), vous devriez avoir un petit jeu simple qui fonctionne sur Squarity.


## Le tileset

Pour commencer, il faudrait dessiner un "tileset", c'est à dire une image contenant tous les éléments qui s'affichent dans votre jeu.

En voici un déjà prêt :

TODO : ça va pas, faut déplacer le bonhomme dans la deuxième ligne. Ça donne plus de chances d'avoir des trucs quand on joue avec les coordonnées.

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/sokoban_tileset.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/sokoban_tileset.png)

Il comporte 5 images d'objets :

 - un sol avec de l'herbe
 - un mur
 - une caisse
 - le personnage
 - une cible, représentant un endroit où il faut placer une caisse.

Ce tileset comporte des pixels transparents. Si vous créez les vôtres, vous aurez peut-être besoin d'un logiciel de dessin capable de gérer la transparence (donc, quelque chose de mieux que Paint).

Pour pouvoir être utilisé dans un jeu, le tileset doit être publié sur internet, et vous devez connaître son url. Vous pouvez utiliser pour cela des sites d'hébergement d'images, comme https://imgbb.com/ .

Le tileset de ce tutoriel est déjà publié, son url est : https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/sokoban_tileset.png


## Un peu d'herbe

Nous allons créer un premier programme qui fonctionne, mais qui ne constitue pas un vrai jeu. Commencez par vous rendre sur le site http://squarity.fr .

Dans le champ *"Url de l'image tileset"*, supprimez le texte existant, puis copier-collez l'url de notre tileset :

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

Puis cliquez sur le bouton tout en bas "Exécutez le jeu"

Vous devriez voir un petit morceau d'herbe apparaître. Oh comme c'est impressionnant !

Votre écran devrait ressembler à ceci (certains boutons ont été supprimés pour simplifier l'image) :

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_01.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_01.png)


## Bidouillons un peu

Nous allons effectuer des modifications dans le code, pour essayer de comprendre ce que font certaines parties.

À chaque modification, vous devez recliquer sur le bouton "Exécutez le jeu". Pour aller plus vite, vous pouvez utiliser le raccourci clavier Ctrl+Entrée.

Si vous faites une modification incorrecte, un message d'erreur apparaîtra en bas à gauche, que vous ne comprendrez pas forcément. Le plus simple est alors de revenir à une version du jeu qui fonctionne : faite des Ctrl-Z, ou au pire refaites les copié-collés du chapitre précédent.

Dans la configuration du jeu, sur la ligne `"herbe": [0, 0]`, remplacez l'un des deux zéros par un nombre entre 1 et 64, et regardez le résultat. Modifiez l'autre nombre. Essayez de comprendre ce qu'ils représentent. Pour vous aidez, vous pouvez réafficher dans un autre onglet l'image du tileset que nous avons vu dans le premier chapitre.

Toujours dans la configuration du jeu, sur la ligne `"tile_size": 32,`, remplacez le "32" par un autre nombre, entre 1 et 100. Essayez de comprendre ce que ce nombre représente.

Dans le code du jeu, sur la ligne `self.tiles[3][5].append("herbe")`, remplacez l'un des deux nombres par un nombre entre 0 et 13. Modifiez l'autre nombre. Essayez de comprendre ce que ces nombres représentent.

Lequel définit l'abscisse (X) du carré d'herbe ? Lequel définit son ordonnée (Y) ? Est-ce que l'un des deux nombres pourrait être plus grand que 13 ? Modifiez-le pour vérifier. Quelle est la valeur maximale pour X et la valeur maximale pour Y ?

Dupliquez la ligne `self.tiles[3][5].append("herbe")` (attention à l'indentation, il faut garder les espaces au début). Dans cette deuxième ligne, modifiez le 3 et le 5. Que voyez-vous dans l'aire de jeu ?

Vous pouvez re-dupliquer la ligne plusieurs fois si vous le souhaitez.

Ne vous embêtez pas à la dupliquer des dizaines de fois pour remplir d'herbe toute l'aire de jeu. Il y a une méthode plus simple que nous verrons juste après.

Pour finir, appuyez sur les boutons du jeu : les flèches ou les actions 1 et 2. Votre jeu va planter et affichera un message d'erreur. C'est normal, nous réglerons ça dans une étape ultérieure.


## Quelques explications concernant tout ce code

Le champ *"config du jeu (en JSON)"* ne contient pas votre programme, mais des informations structurées.

La ligne avec le mot `tile_size` définit la taille des images (en pixels) dans le tileset. On gardera la valeur 32, sinon ça fait n'importe quoi.

Les informations dans `tile_coords` définissent tous les types d'objets que vous utilisez dans votre jeu. Pour l'instant, il n'y en a qu'un seul, qui s'appelle "herbe".

Les deux valeurs entre crochets correspondent aux coordonnées, dans le tileset, de la portion d'image de ce type d'objet. Il s'agit des coordonnées du coin supérieur gauche. On rajoutera très vite les autres types d'objets.

Le champ *"code du jeu (en python)"* contient votre programme. Ce programme doit définir une classe intitulée `BoardModel`.

Tout le code écrit après définit trois fonctions dans cette classe :

 - la fonction `__init__`, c'est la plus longue.
 - la fonction `get_size`, elle ne contient qu'une seule ligne de code.
 - la fonction `export_all_tiles`, qui ne contient elle aussi qu'une seule ligne de code.

Dans un environnement python plus classique, vous devez "instancier votre classe" pour l'utiliser après. Vous n'avez pas besoin de faire ça avec la classe `BoardModel`. Le système de Squarity s'occupe de l'instancier et d'appeler les bonnes fonctions aux bons moments.

Cependant, rien ne vous empêche de créer vos propres classes et de les instancier quand vous en avez besoin.

Dans le code, les noms de variables commençant par `self.` signifient qu'elles appartiennent à la classe. Elles sont accessible en lecture et en écriture depuis toutes les fonctions de la classe. Leur valeur est conservée entre deux "tours" de jeu.

Les variables ne commençant pas par `self.`, par exemple `line` ou `game_objects` ne sont pas conservées. Vous les définissez et les utilisez dans une fonction, ensuite elles sont effacées.

Vous n'avez pas besoin de savoir ce que signifie une "classe", ni "instancier une classe" pour la suite de ce tutoriel. Si ça vous intéresse, vous trouverez des explications sur le sujet dans des cours pour apprendre le python.

Les variables `self.w` et `self.h` définissent la taille de l'aire de jeu, en nombre de case.

 - w = width = largeur = 20 cases,
 - h = height = hauteur = 14 cases.

La variable `self.tiles` est importante. Elle contient tous les objets à afficher dans le jeu. C'est un tableau en deux dimensions. Chaque case de ce tableau peut contenir plusieurs objets du jeu. Chacun est identifié par une chaîne de caractère, correspondant à son nom.

Dans notre programme, nous avons ajouté un seul objet de jeu dans une seule case du tableau. Il a pour nom : "herbe".

Selon ce que vous avez bidouillé dans le chapitre précédent, vous en avez peut-être ajouté d'autres, dans d'autres cases du tableau.

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/annotations_code.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/annotations_code.png)


## Plein d'herbe

Dans le code du jeu, remplacez la ligne

`game_objects = []`

par

`game_objects = ["herbe"]`

Exécutez votre jeu. Vous devriez voir de l'herbe partout.

La ligne que vous venez de modifier se trouve dans une boucle (pour être exact : dans une boucle de boucle). Elle est exécutée pour chaque case de l'aire de jeu, ce qui ajoute de l'herbe partout.

La ligne `self.tiles[3][5].append("herbe")` n'est plus utile, mais on va la laisser pour l'instant.


## Attention à l'indentation

Vous avez peut-être un peu de mal à comprendre entièrement le code du jeu. Ne vous inquiétez pas, ça n'empêche pas de terminer ce tutoriel.

Il y a cependant un point très important à prendre en compte avec le langage de programmation python : l'indentation est significative. Autrement dit : faites attention aux espaces qui se trouvent au début de chaque ligne, ils servent à indiquer la manière dont les blocs de code sont imbriqués.

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

Une image utilisée pour afficher un élément dans l'aire de jeu s'appelle **image de tile**. Autres appellations : **image de tuile**, **tile image**, ou tout simplement **image**.

La grande image contenant toutes les images de tile s'appelle le **tileset**. Autres appellations : **tilesheet**, **image set**, **image atlas**, **atlas**. On utilise le mot "atlas" pour représenter le fait que c'est un ensemble d'images exhaustif. Comme les atlas de cartes géographiques.

Ce qui est affichée dans la partie gauche de l'écran s'appelle **l'aire de jeu**. C'est là où se tout déroule : les personnages se déplacent, ramassent des objets, discutent entre eux, etc.

Une case dans l'aire de jeu s'appelle une **tile**. Autres appellations : **tuile**, **case**. Ces tiles sont organisées sous forme d'un tableau en deux dimensions. Dans notre programme, ce tableau est enregistré dans la variable `self.tiles`. Il a une largeur de 20 tiles et une hauteur de 14 tiles.

Pour repérer une tile dans le tableau, on utilise les coordonnées x et y.

X augmente lorsqu'on va vers la droite. Les tiles tout à gauche ont pour coordonnée x = 0. Les tiles tout à droite ont pour coordonnée x = 19.

Y augmente lorsqu'on va vers le bas. Les tiles tout en haut ont pour coordonnée y = 0. Les tiles tout en bas ont pour coordonnée y = 13.

Les graphiques que l'on dessine en cours de maths ont la coordonnée Y dans l'autre sens : Y augmente lorsqu'on va vers le haut. En programmation, on préfère que l'axe des Y soit dans la direction du bas. C'est plus logique car ça correspond au sens de lecture, à l'ordre des pixels sur l'écran, etc.

Les coordonnées sont comptées à partir de zéro, et non pas à partir de un, parce que c'est comme ça qu'on fait en informatique. Il y a une justification, mais ce serait un peu long de l'expliquer ici.

Un élément placé dans une tile s'appelle un **objet de jeu**. Autres appellations : **game object**, **gamobj**, **gobject**, **gobj**. Il peut y avoir plusieurs game objects sur une même tile. Ils seront dessinés les uns par-dessus les autres.

Chaque game object possède un **type de game object**. Autre appellation : **game object type**. Dans notre programme, les mots "herbe" et "mur" sont des types de game object.

Dans les noms de variables des programmes et dans les documentations, il faut essayer d'utiliser ce vocabulaire au maximum, pour qu'il devienne commun aux personnes utilisant Squarity.

On évitera d'utiliser les mots "objet" et "type" tout seul, car ce sont des termes trop génériques, qui sont déjà beaucoup utilisés en programmation.

On peut se permettre d'utiliser les noms anglais ("game object", "tile", ...) dans un texte français, puisque la langue française possède déjà des anglicismes. Vous pouvez aussi faire le contraire, puisque la langue anglaise possède des francicismes. Ha ha ha.

Dans notre programme, nous avons commencé par placer dans toutes les tiles un seul game object, de type "herbe". Puis, pour la tile qui est aux coordonnées (x=5, y=3), nous avons ajouté un second game object, de type "mur".

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/schema_self_tiles.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/schema_self_tiles.png)

Dans la tile x=5, y=3, on ne voit pas le game object "herbe", car le game object "mur" est dessiné par dessus, et la recouvre entièrement. Mais cette tile possède bien deux game objects.


## Quelques règles du fonctionnement de Squarity

 - On peut créer et supprimer les game objects dans les tiles, et les déplacer d'une tile vers une autre.
 - Une tile peut contenir autant de game objects que l'on veut.
 - Une tile peut posséder plusieurs game objects de même type.
 - L'ordre des game objects dans une tile est important, car il définit l'ordre dans lequel ils seront affichés.
 - On ne peut pas déplacer, ajouter ou supprimer des tiles. Ce sont les cases du tableau, et le tableau ne change pas.
 - Pour l'instant, on ne peut pas changer la largeur ou la hauteur du tableau. C'est forcément largeur = 20, hauteur = 14. Mais ce sera amélioré dans des versions futures de Squarity.
 - On ne peut pas placer un game object sur plusieurs tiles en même temps. (Mais on peut créer plusieurs game object de même type et les placer chacun sur une tile)
 - **On ne peut pas placer un game object à cheval sur plusieurs tiles**. Les coordonnées sont forcément des nombres entiers. Vous ne pourrez donc jamais avoir un personnage qui se déplace légèrement et se retrouve entre deux tiles, comme dans le premier Zelda ou les jeux Bombermans. C'est un choix de conception dans Squarity, pour simplifier la création des jeux.

Dans la configuration du jeu, la donnée `tile_coords` permet de lister tous les types de game object de votre jeu, et de faire la correspondance avec leurs images respectives.

Au passage, le nom `tile_coords` est un peu illogique, et je le renommerais en `img_coords` dès que possible.


## Une liste de liste de liste

La notion de "tableau" n'existe pas vraiment en python, on ne peut créer que des listes.

Mais on peut créer une liste contenant des liste.

 - La variable `self.tiles` est une liste de 14 éléments, représentant les 14 lignes de l'aire de jeu,
   - chacun de ces éléments est une sous-liste de 20 éléments, représentant les 20 cases d'une ligne de l'aire de jeu,
     - chacun de ces éléments est une sous-sous-liste ayant un nombre variable d'éléments, représentant les game objects de la case,
       - chacun de ces éléments est un nom, correspondant à un type de game object.

Lorsqu'on accède à des listes imbriquées, on donne les index dans le même ordre d'imbrication.

Le code `self.tiles[3][5]` signifie : "la ligne numéro 3, et dans cette ligne, la case numéro 5". On indique d'abord l'ordonnée (le y), et ensuite l'abscisse (le x).

L'accès à la tile de coordonnée (x, y) se fait avec ce code : `self.tiles[y][x]`.

C'est un peu embarrassant, car l'ordre est inversée par rapport à l'ordre habituel. Ce serait mieux si on indiquait d'abord le x, puis le y.

On va créer une petite fonction effectuant l'accès à une tile, avec les paramètres dans l'ordre. Ce sera plus lisible pour tout le code qu'on ajoutera après.

Rajoutez ceci à la fin du code du jeu :

```

    def get_tile(self, x, y):
        return self.tiles[y][x]

```

Et ensuite, remplacez la ligne

`        self.tiles[3][5].append("mur")`

par la ligne :

`        self.get_tile(5, 3).append("mur")`

Pensez à bien garder le même nombre d'espace au début de la ligne.

Exécutez le jeu. Vous verrez la même chose qu'avant. Mais maintenant nous avons une fonction qui rend le code plus cohérent.

La fonction `append("game_object_type")` permet d'ajouter un game object dans une tile. La fonction `remove("game_object_type")` permet d'en supprimer un. Vous pouvez utiliser ces deux fonctions juste après un appel à la fonction `self.get_tile(x, y)`.

Attention à la fonction `remove`. Si vous indiquez un type de game object qui n'est pas présent dans la tile, le programme se terminera en erreur. Vous pouvez vérifier la présence d'un game object avec une instruction comme ceci :

`if "mur" in self.get_tile(5, 3):self.get_tile(5, 3).remove("mur")`


## Des prints, des prouts, et du python pur

Au tout début de votre programme, ajoutez la ligne `print("prout")`

Exécutez le jeu. Vous devriez voir apparaître, dans la fenêtre en bas à gauche, le texte "prout".

Juste après la ligne :

`        self.get_tile(5, 3).append("mur")`

ajoutez la ligne :

`        print(self.tiles)`

Exécutez le jeu. Vous devriez voir apparaître un grand texte avec écrit plein de fois le mot "herbe". Il s'agit du contenu complet de self.tiles.

Tout est écrit sur une seule ligne, c'est un peu difficile à lire. Essayez de repérer les double crochets ouvrants `[[` et fermants `]]`, ils marquent la coupure entre deux lignes de tiles. Vous devriez aussi trouver le mot "mur" écrit une seule fois.

La fonction `print` écrit ce que vous lui indiquez en paramètre. Du texte simple (entre guillemets), ou bien le contenu d'une variable.

Cette fonction est très utile pour le déboguage, c'est à dire lorsque votre programme fait des messages d'erreur ou qu'il n'exécute pas ce que vous aviez prévu. Vous placez des `print` à différents endroits pour essayer de comprendre ce qu'il se passe, le chemin d'exécution, le contenu des variables, etc.

Si vous n'êtes pas très à l'aise en python, vous pouvez vous entrainer sur le langage en lui-même. Le mieux est d'installer un interpréteur sur votre ordinateur. Si vous n'avez pas l'envie ou les connaissances pour le faire, vous pouvez aller directement sur ce site : https://trinket.io/python3 .

Il s'agit d'un interpréteur python dans votre navigateur. Vous écrivez du code dans la partie gauche, vous cliquez sur le bouton "Play" (le triangle orienté vers la droite) et le résultat s'affiche dans la partie droite.

C'est du "pur python", vous pouvez donc écrire le code directement. Vous n'avez pas besoin de créer une classe `BoardModel`. La seule chose que vous pouvez faire, ce sont des `print`. Mais c'est déjà suffisant pour s'entrainer et faire des tutoriels de python.


## On en fait des caisses

Pour cette étape, vous allez essayer de vous débrouiller un peu tout seul.

Vous devez faire les modifications nécessaires pour afficher une caisse à côté du mur :

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_mur_et_caisse.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_mur_et_caisse.png)

Dans la configuration du jeu, ajoutez un type de game object appelé "caisse". Définissez ses coordonnnées d'image à `[64, 0]`. N'oubliez pas les virgules entre chaque définition de type de game object.

Dans le code du jeu, copiez la ligne `self.get_tile(5, 3).append("mur")` et collez-la juste en dessous (attention aux espaces en début de ligne !).

Dans cette nouvelle ligne de code, modifiez les coordonnées : la tile choisie doit être un peu plus à droite.

Ensuite, modifiez le type d'objet : il faut que ce soit le type "caisse".

Si vous n'y arrivez pas, ce n'est pas trop grave, vous pouvez quand même passer au chapitre suivant.


## Plein d'objets et une carte du niveau

Dans le champ *"Config du jeu"*, copier-collez la configuration suivante :

```
{
    "tile_size": 32,
    "tile_coords": {
        "herbe": [0, 0],
        "mur": [32, 0],
        "caisse": [64, 0],
        "personnage": [0, 32],
        "cible": [0, 64]
    }
}
```

Dans le champ : *"Le code du jeu"*, copier-collez le code suivant :

```
PLAN_DU_NIVEAU = (
    "                    ",
    "                $   ",
    "                    ",
    "    ######          ",
    "    #.              ",
    "    ####            ",
    "         $   @      ",
    "                    ",
    "           #    #   ",
    "           #    #   ",
    "           # .$ #   ",
    "           #  . #   ",
    "           ######   ",
    "                    ",
)

corresp_game_objects_a_partir_char = {
    " ": ["herbe"],
    "#": ["mur"],
    "@": ["personnage"],
    "$": ["caisse"],
    ".": ["cible"]
}

class BoardModel():

    def __init__(self):

        self.w = 20
        self.h = 14
        self.tiles = []

        for y in range(self.h):
            ligne_plan_du_niveau = PLAN_DU_NIVEAU[y]
            line = []
            for x in range(self.w):
                char_carte = ligne_plan_du_niveau[x]
                game_objects = corresp_game_objects_a_partir_char[char_carte]
                game_objects = list(game_objects)
                line.append(game_objects)
            self.tiles.append(line)

    def get_size(self):
        return self.w, self.h

    def export_all_tiles(self):
        return self.tiles
```

Exécutez le jeu. Vous devriez voir ceci :

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_level_map.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_level_map.png)

Que constate-t-on ? C'est très moche !


## Bidouillons un peu et rendons ça plus beau

Dans le programme que vous avez copié-collé, où est définie la disposition des game objects dans l'aire de jeu ? Essayez de changer cette disposition, par exemple en ajoutant ou en supprimant des caisses et des murs.

Essayez de trouver pourquoi c'est moche. Quel est le problème avec les tiles contenant une cible, une caisse ou un personnage ? Qu'est-ce qu'il manque dans ces tiles ? Que faudrait-il faire pour qu'elles s'affichent en moins moche ?

Le plan du niveau est un ensemble de textes, contenant uniquement les caractères `#   @ $ .`. Pourtant, les noms de vos types d'objets sont : "herbe",
 "mur", "caisse", "personnage", "cible". À quel caractère correspond quel type d'objet ?

Dans le programme, où est définie cette correspondance entre les caractères du plan du niveau et le nom des game objects ?

Pour que l'affichage soit moins moche, vous avez uniquement besoin de modifier cette correspondance. Pas besoin de changer le reste du code. Essayez de la modifier.

Petit indice : si on prend le caractère "$". Celui-ci correspond à `["caisse"]`, c'est à dire : une liste avec un seul game object dedans, qui est de type "caisse".

Dans un chapitre précédent, lorsqu'on avait fait un print de la variable self.tiles, l'une des cases avait pour valeur : `['herbe', 'mur']`.

Cette valeur peut également s'écrire avec des guillemets double : `["herbe", "mur"]`.

Cette valeur signifie : une liste avec deux game objects dedans. Le premier est de type "herbe", le second de type "mur".

Et si vous mettiez des listes de plusieurs game objects dans la correspondance ente caractères et game objects ? Ce sera peut-être mieux que d'avoir des listes de un seul game object.


## La réponse pour que ce soit plus beau

Dans le code du jeu, remplacez la correspondance :

```
corresp_game_objects_a_partir_char = {
    " ": ["herbe"],
    "#": ["mur"],
    "@": ["personnage"],
    "$": ["caisse"],
    ".": ["cible"]
}
```

Par celle-ci :

```
corresp_game_objects_a_partir_char = {
    " ": ["herbe"],
    "#": ["herbe", "mur"],
    "@": ["herbe", "personnage"],
    "$": ["herbe", "caisse"],
    ".": ["herbe", "cible"],
}
```

On a ajouté le type de game object "herbe" à toutes les correspondances, sauf la première.

Exécutez le jeu, ça devrait être plus beau. C'est à dire que chaque objet n'est plus sur un fond noir moche.

Un dernier petit détail, si vous vous y connaissez un peu en python. Cette ligne : `game_objects = list(game_objects)` est importante. La fonction list permet de créer une nouvelle copie de la liste, pour chaque tile. Si vous ne le faites pas, vous aurez plusieurs références à la même liste. Et lorsque vous changerez le contenu de l'une des tiles (en ajoutant ou supprimant un game object), cela modifiera également toutes les autres. On ne va pas rentrer plus loin dans les explications, tout ce que vous avez à savoir pour l'instant, c'est qu'il faut laisser cette ligne.


## Petite pause

Si vous avez lu et effectué ce qui est demandé jusqu'ici, bravo ! Vous avez bien mérité une petite pause ! Mangez un morceau, jouez à un jeu qui vous plaît et nourrissez votre poisson rouge. Pour la suite, on s'attaquera à un gros morceau : l'interactivité, les boutons d'actions.


## On écrit (pas sur les murs)

Dans le code du jeu, tout à la fin, ajoutez la fonction suivante :

```
    def on_game_event(self, event_name):
        print(event_name)
```

Exécutez le jeu, puis cliquez sur les boutons. Le programme ne plante plus, et du texte s'affiche en bas à gauche à chaque appui de boutons.

Le texte dépend du bouton appuyé :

 - "U" (up) : le bouton "haut"
 - "D" (down) : bouton "bas"
 - "L" (left) : bouton "gauche"
 - "R" (right) : bouton "droit"
 - "action_1" : bouton "1"
 - "action_2" : bouton "2"

