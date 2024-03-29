# Tutoriel Soko-ban Squarity

Ce tutoriel vous montrera comment créer un petit jeu simple avec Squarity. Il s'agit d'un [soko-ban](https://fr.wikipedia.org/wiki/Sokoban), un jeu dans lequel un personnage doit pousser des caisses pour les ranger.

Squarity utilise le langage de programmation python et le format de description de données JSON. Vous n'avez pas besoin de connaître ces notions, mais ça peut aider. Si vous souhaitez découvrir ou approfondir ces sujets, voici [un lien vers des cours de python](https://python.developpez.com/cours/), et la [la page Wikipedia sur le JSON](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation).

Ce tutoriel est un peu long, mais chacune des étapes que vous effectuez vous récompense par un résultat visible dans l'interface de jeu, ce qui permet de garder le courage de continuer.


## Le tileset

Pour commencer, il faudrait dessiner un "tileset", c'est à dire une image contenant tous les éléments affichés dans votre jeu.

En voici un déjà prêt :

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/sokoban_tileset.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/sokoban_tileset.png)

Il comporte 5 images d'objets :

 - un sol avec de l'herbe
 - un mur
 - une caisse
 - le personnage
 - une cible, représentant un endroit où placer une caisse.

Ce tileset comporte des pixels transparents. Si vous créez le vôtre, vous aurez peut-être besoin d'un logiciel gérant la transparence (donc, quelque chose de mieux que Paint).

Le tileset doit être publié sur internet et vous devez connaître son url. Vous pouvez utiliser pour cela des sites d'hébergement d'images, comme https://imgbb.com/ . Lorsque l'image est publiée, vous devez récupérer l'url directe vers le fichier. En général, c'est possible avec un clic droit sur l'image, puis l'option "ouvrir l'image dans un nouvel onglet". L'url se trouve alors dans la barre d'adresse de votre navigateur web.

Pour vous simplifier la vie, le tileset de ce tutoriel est déjà publié, son url est : https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/sokoban_tileset.png


## Un peu d'herbe

Nous allons créer un premier programme qui fonctionne, mais qui ne constitue pas encore un vrai jeu. Allez sur le site http://squarity.fr .

Vous verrez un jeu de démonstration, que nous allons remplacer.

Dans le champ *"Url de l'image"*, supprimez le texte existant, puis copier-collez le texte suivant :

`https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/sokoban_tileset.png`

Dans le champ en-dessous *"Config du jeu (en JSON)"*, remplacez le texte existant par cette configuration :

```
{
    "tile_size": 32,
    "img_coords": {
        "herbe": [0, 0]
    }
}
```

Dans le dernier champ : *"Le code du jeu (en python)"*, remplacez le texte existant par ce code :

```
class GameModel():

    def __init__(self):

        self.w = 20
        self.h = 14
        self.tiles = []

        for y in range(self.h):
            ligne = []
            for x in range(self.w):
                game_objects = []
                ligne.append(game_objects)
            self.tiles.append(ligne)

        self.tiles[3][5].append("herbe")

    def export_all_tiles(self):
        return self.tiles
```

Puis cliquez sur le bouton "Exécuter" au milieu de la page.

Vous devriez voir un petit morceau d'herbe dans le cadre de droite. Youpi !

Votre écran devrait ressembler à ceci (certains boutons ont été supprimés pour simplifier l'image) :

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_01.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_01.png)


## Bidouillons un peu

Nous allons modifier le code, pour essayer de comprendre ce que font certaines parties.

À chaque modification, vous devez recliquer sur le bouton "Exécuter". Pour aller plus vite, vous pouvez utiliser le raccourci clavier Ctrl-Entrée.

Si votre code est incorrect, un message d'erreur apparaîtra en bas, que vous ne comprendrez pas forcément. Le plus simple est alors de revenir à une version du jeu qui fonctionne : faites des Ctrl-Z, ou au pire refaites les copié-collés du chapitre précédent.

Dans la configuration du jeu, sur la ligne `"herbe": [0, 0]`, remplacez l'un des deux zéros par un nombre entre 1 et 64 et regardez le résultat. Modifiez l'autre nombre. Essayez de comprendre ce qu'ils représentent. Pour vous aidez, vous pouvez réafficher dans un autre onglet l'image du tileset que nous avons vu dans le premier chapitre.

Toujours dans la configuration du jeu, sur la ligne `"tile_size": 32,`, remplacez le "32" par un autre nombre, entre 1 et 100. Essayez de comprendre ce que ce nombre représente.

Dans le code du jeu, sur la ligne `self.tiles[3][5].append("herbe")`, remplacez l'un des deux nombres par un nombre entre 0 et 13. Modifiez l'autre nombre. Essayez de comprendre ce que ces nombres représentent.

Lequel définit l'abscisse (X) du carré d'herbe ? Lequel définit son ordonnée (Y) ? Est-ce que l'un des deux nombres pourrait être plus grand que 13 ? Modifiez-le pour vérifier. Quelle est la valeur maximale pour X et la valeur maximale pour Y ?

Dupliquez la ligne :
```
        self.tiles[3][5].append("herbe")
```

Attention à l'indentation, il faut garder les espaces au début. Dans la ligne dupliquée, modifiez le 3 et le 5. Que voyez-vous dans l'aire de jeu ?

Vous pouvez re-dupliquer la ligne plusieurs fois si vous le souhaitez.

Ne vous embêtez pas à la dupliquer des dizaines de fois pour remplir d'herbe toute l'aire de jeu. Il y a une méthode plus simple que nous verrons juste après.

Pour finir, appuyez sur les boutons du jeu : les flèches ou les actions 1 et 2. Votre jeu va planter et affichera un message d'erreur. C'est normal, nous réglerons ça dans une étape ultérieure.


## Quelques explications concernant le code

Le champ *"config du jeu (en JSON)"* ne contient pas votre programme, mais des informations structurées.

La ligne avec le mot `tile_size` définit la taille des images (en pixels) dans le tileset. On gardera la valeur 32, sinon ça fait n'importe quoi.

Les informations dans `img_coords` définissent tous les types d'objets que vous utilisez dans votre jeu. Pour l'instant, il n'y en a qu'un seul, qui s'appelle "herbe".

Les deux valeurs entre crochets correspondent aux coordonnées, dans le tileset, de la portion d'image de ce type d'objet. Il s'agit des coordonnées du coin supérieur gauche. On rajoutera très vite les autres types d'objets.

Le champ *"code du jeu (en python)"* contient votre programme. Ce programme doit définir une classe intitulée `GameModel`.

Tout le code qui vient après définit trois fonctions dans cette classe :

 - la fonction `__init__`: la plus longue.
 - la fonction `export_all_tiles`, qui ne contient qu'une ligne de code.

Dans un environnement python plus classique, vous devez "instancier" votre classe pour l'utiliser après. Vous n'avez pas besoin de faire ça avec `GameModel`. Le système dans Squarity s'occupe de l'instancier et d'appeler les bonnes fonctions aux bons moments.

Cependant, rien ne vous empêche de créer vos propres classes et de les instancier quand vous en avez besoin.

Dans le code, les noms de variables commençant par `self.` signifient qu'elles appartiennent à la classe. Elles sont accessible en lecture et en écriture depuis toutes les fonctions de la classe. Leur valeur est conservée entre deux "tours" de jeu.

Les variables ne commençant pas par `self.`, par exemple `ligne` ou `game_objects` ne sont pas conservées. Vous les définissez et les utilisez dans une fonction, ensuite elles sont effacées.

Vous n'avez pas besoin de savoir ce que signifie une "classe", ni "instancier une classe" pour la suite de ce tutoriel. Si ça vous intéresse, vous pouvez consulter des cours de python.

Les variables `self.w` et `self.h` définissent la taille de l'aire de jeu, en nombre de cases.

 - w = width = largeur = 20 cases,
 - h = height = hauteur = 14 cases.

La variable `self.tiles` est importante. Elle contient tous les objets à afficher dans le jeu. C'est un tableau en deux dimensions. Chaque case de ce tableau peut contenir plusieurs objets du jeu. Chacun est identifié par une chaîne de caractère, correspondant à son nom.

Au départ, nous avons ajouté un seul objet de jeu dans une seule case du tableau. Il a pour nom : "herbe".

Selon ce que vous avez bidouillé dans le chapitre précédent, vous en avez peut-être ajouté d'autres.

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/annotations_code.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/annotations_code.png)


## Plein d'herbe

Dans le code du jeu, remplacez la ligne

```
                game_objects = []
```

par

```
                game_objects = ["herbe"]
```

Exécutez votre jeu. Vous devriez voir de l'herbe partout.

La ligne que vous venez de modifier se trouve dans une boucle (pour être exact : dans une boucle de boucle). Elle est exécutée pour chaque case de l'aire de jeu, ce qui ajoute de l'herbe partout.

La ligne `self.tiles[3][5].append("herbe")` n'est plus utile, mais on va la garder pour l'instant.


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
    "img_coords": {
        "herbe": [0, 0],
        "mur": [32, 0]
    }
}
```

Vous avez maintenant deux types d'objets, l'herbe et le mur. N'oubliez pas la virgule entre les deux.

Puis, dans le code du jeu, à la ligne `self.tiles[3][5].append("herbe")`, remplacez le mot `"herbe"` par `"mur"`. Attention de bien garder les guillemets.

Exécutez le jeu. Vous devriez voir de l'herbe et un objet de type mur.


## Vocabulaire spécifique à Squarity

Une image utilisée pour afficher un élément dans l'aire de jeu s'appelle **image de tile**. Autres appellations : **image de tuile**, **tile image**, ou tout simplement **image**.

La grande image contenant toutes les images de tile s'appelle le **tileset**. Autres appellations : **tilesheet**, **image set**, **image atlas**, **atlas**. On utilise le mot "atlas" pour représenter le fait que c'est un ensemble exhaustif, comme les atlas de cartes géographiques.

Ce qui est affichée dans la partie droite de l'écran s'appelle **l'aire de jeu**. C'est là où tout se déroule : les personnages se déplacent, ramassent des objets, discutent entre eux, etc.

Une case dans l'aire de jeu s'appelle une **tile**. Autres appellations : **tuile**, **case**. Ces tiles sont organisées sous forme d'un tableau en deux dimensions. Dans notre programme, ce tableau est enregistré dans la variable `self.tiles`.

Pour repérer une tile dans ce tableau, on utilise les coordonnées x et y.

X augmente lorsqu'on va vers la droite. Les tiles tout à gauche ont pour coordonnée x = 0. Les tiles tout à droite ont pour coordonnée x = 19.

Y augmente lorsqu'on va vers le bas. Les tiles tout en haut ont pour coordonnée y = 0. Les tiles tout en bas ont pour coordonnée y = 13.

Pour info : les graphiques des cours de maths ont la coordonnée Y dans l'autre sens : Y augmente lorsqu'on va vers le haut. En programmation, on préfère que l'axe des Y soit orienté vers le bas. C'est plus logique car ça correspond au sens de lecture et à l'ordre des pixels sur l'écran.

Les coordonnées sont comptées à partir de zéro, et non à partir de un, parce que c'est comme ça qu'on fait en informatique. Il y a une justification, mais ce serait un peu long de l'expliquer ici.

Un élément placé dans une tile s'appelle un **objet de jeu**. Autres appellations : **game object**, **gamobj**, **gobject**, **gobj**. Il peut y avoir plusieurs game objects sur une même tile. Ils seront dessinés les uns par-dessus les autres.

Chaque game object est défini par son **type de game object**. Autre appellation : **game object type**. Dans notre programme, les mots "herbe" et "mur" sont des types de game object.

Il faut essayer d'utiliser ce vocabulaire pour les noms de variables dans vos programmes, afin qu'il devienne commun aux personnes utilisant Squarity.

On évitera d'utiliser les mots "objet" et "type" tout seul, car ce sont des termes trop génériques, qui sont déjà beaucoup utilisés en programmation.

On peut se permettre d'utiliser les noms anglais ("game object", "tile", ...) dans un texte français, puisque la langue française possède déjà des anglicismes. Vous pouvez aussi faire le contraire, car la langue anglaise possède des francicismes. Ha ha ha.

Dans notre programme, nous avons commencé par placer dans chaque tile un seul game object, de type "herbe". Puis, pour la tile qui est aux coordonnées (x=5, y=3), nous avons ajouté un second game object, de type "mur".

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/schema_self_tiles.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/schema_self_tiles.png)

Dans la tile x=5, y=3, on ne voit pas le game object "herbe", car le game object "mur" est dessiné par dessus et la recouvre entièrement. Mais cette tile possède bien deux game objects.


## Quelques règles du fonctionnement de Squarity

 - On peut créer et supprimer les game objects dans les tiles, et les déplacer d'une tile vers une autre.
 - Une tile peut contenir autant de game objects que l'on veut.
 - Une tile peut posséder plusieurs game objects de même type.
 - L'ordre des game objects dans une tile est important, car il définit l'ordre dans lequel ils seront affichés.
 - On ne peut pas déplacer, ajouter ou supprimer les tiles elles-mêmes. Ce sont les cases du tableau, et le tableau ne change pas.
 - Il est possible de changer la taille de l'aire de jeu, mais ce n'est pas expliqué dans ce tutoriel.
 - On ne peut pas placer un game object sur plusieurs tiles en même temps.
 - **On ne peut pas placer un game object à cheval sur plusieurs tiles**. Les coordonnées sont forcément des nombres entiers. Vous ne pourrez donc jamais avoir un personnage qui se déplace légèrement et se retrouve entre deux tiles, comme dans le premier Zelda ou dans les jeux Bombermans. C'est un choix de conception dans Squarity, pour simplifier la création des jeux.

Les types de game object d'un jeu sont tous référencés dans la donnée `img_coords` de la configuration.


## Une liste de liste de liste

La notion de "tableau" n'existe pas vraiment en python, on ne peut créer que des listes.

Mais on peut créer une liste contenant des listes.

 - La variable `self.tiles` est une liste de 14 éléments, représentant les 14 lignes de l'aire de jeu,
   - chacun de ces éléments est une sous-liste de 20 éléments, représentant les 20 cases d'une ligne de l'aire de jeu,
     - chacun de ces éléments est une sous-sous-liste ayant un nombre variable d'éléments, représentant les game objects de la case,
       - chacun de ces éléments est un nom, correspondant à un type de game object.

Lorsqu'on accède à des listes imbriquées, on donne les index dans le même ordre d'imbrication.

Le code `self.tiles[3][5]` signifie : "la ligne numéro 3, et dans cette ligne, la case numéro 5". On indique d'abord l'ordonnée (le y), et ensuite l'abscisse (le x).

L'accès à la tile de coordonnée (x, y) se fait avec ce code : `self.tiles[y][x]`. C'est embarrassant, car l'ordre est inversé par rapport à d'habitude (d'abord le x, puis le y).

Pour avoir un code plus clair, nous allons créer une petite fonction qui renvoie une tile, avec les paramètres dans l'ordre.

Rajoutez ceci à la fin du code du jeu :

```
    def get_tile(self, x, y):
        return self.tiles[y][x]
```

Et ensuite, remplacez la ligne :
```
        self.tiles[3][5].append("mur")
```
par la ligne :
```
        self.get_tile(5, 3).append("mur")
```

Pensez à bien garder le même nombre d'espace au début de la ligne.

Exécutez le jeu. Vous verrez la même chose qu'avant, mais maintenant nous avons une fonction qui remet les coordonnées dans l'ordre habituel.

La fonction `append("game_object_type")` permet d'ajouter un game object dans une tile. La fonction `remove("game_object_type")` permet d'en supprimer un. Vous pouvez utiliser ces deux fonctions juste après un appel à la fonction `self.get_tile(x, y)`.

Attention à la fonction `remove`. Si vous indiquez un type de game object qui n'est pas présent dans la tile, ça fera une erreur. Vous pouvez vérifier préalablement la présence d'un game object comme ceci :
```
if "mur" in self.get_tile(5, 3):
    self.get_tile(5, 3).remove("mur")
```


## Des prints, des prouts, et du python pur

Au tout début du code du jeu, avant `class GameModel()`, ajoutez une ligne, et écrivez :

`print("prout")`

Exécutez le jeu. Vous devriez voir apparaître, dans la fenêtre en bas, le texte "prout".

Juste après la ligne :
```
        self.get_tile(5, 3).append("mur")
```
ajoutez ceci :
```
        print(self.tiles)
```

Exécutez le jeu. Vous devriez voir apparaître un grand texte avec beaucoup de mots "herbe". Il s'agit du contenu complet de `self.tiles`.

Tout est écrit sur une seule ligne, c'est un peu difficile à lire. Essayez de repérer les double crochets ouvrants `[[` et fermants `]]`, ils marquent la coupure entre deux lignes de tiles. Vous devriez aussi trouver le mot "mur".

La fonction `print` écrit ce que vous lui indiquez en paramètre. Du texte simple lorsqu'il est mis entre guillemets, ou bien le contenu d'une variable.

Cette fonction est très utile pour le déboguage, c'est à dire lorsque votre programme fait des messages d'erreur ou qu'il n'exécute pas ce que vous aviez prévu. Vous placez des `print` à différents endroits pour essayer de comprendre ce qu'il se passe, le chemin d'exécution, le contenu des variables, etc.

Si vous n'êtes pas très à l'aise en python, vous pouvez vous entrainer en allant sur ce site : https://trinket.io/python3 . Il s'agit d'un interpréteur python dans votre navigateur. Vous écrivez du code dans la partie gauche, vous cliquez sur le bouton "Play" et le résultat de votre programme s'affiche dans la partie droite.


## On en fait des caisses

Pour cette étape, vous allez essayer de vous débrouiller un peu tout seul.

Vous devez faire les modifications nécessaires pour afficher une caisse à côté du mur :

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_mur_et_caisse.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_mur_et_caisse.png)

Dans la configuration du jeu, ajoutez un type de game object appelé "caisse". Définissez ses coordonnnées d'image à `[64, 0]`. N'oubliez pas les virgules entre chaque définition de type de game object.

Dans le code du jeu, copiez la ligne `self.get_tile(5, 3).append("mur")` et collez-la juste en dessous (attention aux espaces en début de ligne !).

Dans cette nouvelle ligne de code, modifiez les coordonnées : la tile choisie doit être un peu plus à droite.

Ensuite, modifiez le type d'objet : il faut que ce soit "caisse".

Si vous n'y arrivez pas, ce n'est pas trop grave, vous pouvez quand même passer au chapitre suivant.


## Plein d'objets et un plan du niveau

Dans le champ *"Config du jeu"*, supprimer l'ancien texte et copier-collez la configuration suivante :

```
{
    "tile_size": 32,
    "img_coords": {
        "herbe": [0, 0],
        "mur": [32, 0],
        "caisse": [64, 0],
        "personnage": [0, 32],
        "cible": [32, 32]
    }
}
```

Dans le champ : *"Le code du jeu"*, supprimer l'ancien texte et copier-collez le code suivant :

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

class GameModel():

    def __init__(self):

        self.w = 20
        self.h = 14
        self.tiles = []

        for y in range(self.h):
            ligne_plan_du_niveau = PLAN_DU_NIVEAU[y]
            ligne = []
            for x in range(self.w):
                char_carte = ligne_plan_du_niveau[x]
                game_objects = corresp_game_objects_a_partir_char[char_carte]
                game_objects = list(game_objects)
                ligne.append(game_objects)
            self.tiles.append(ligne)

    def export_all_tiles(self):
        return self.tiles

    def get_tile(self, x, y):
        return self.tiles[y][x]

```

Exécutez le jeu. Vous devriez voir ceci :

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_level_map.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_level_map.png)

Que constate-t-on ? C'est très moche !


## Bidouillons un peu et rendons ça plus beau

Dans le programme que vous avez copié-collé, à quel endroit est définie la disposition des game objects dans l'aire de jeu ? Essayez de changer cette disposition, par exemple en ajoutant ou en supprimant des caisses et des murs.

Essayez de comprendre pourquoi c'est moche. Quel est le problème avec les tiles contenant une cible, une caisse ou un personnage ? Qu'est-ce qu'il manque dans ces tiles ? Que faudrait-il faire pour qu'elles s'affichent en moins moche ?

Le plan du niveau est un ensemble de textes, contenant uniquement les caractères `#   @ $ .`. Pourtant, les noms de vos types d'objets sont : "herbe", "mur", "caisse", "personnage", "cible". À quel caractère correspond quel type d'objet ?

Dans le programme, où est définie cette correspondance entre les caractères du plan du niveau et le nom des game objects ?

Pour que l'affichage soit moins moche, vous avez uniquement besoin de modifier cette correspondance. Pas besoin de changer le reste du code.

Petit indice : si on prend le caractère "$", celui-ci correspond à `["caisse"]`, c'est à dire : une liste avec un seul game object dedans, qui est de type "caisse".

Dans un chapitre précédent, lorsqu'on avait fait un print de la variable self.tiles, l'une des cases avait pour valeur : `['herbe', 'mur']`.

Cette valeur peut également s'écrire avec des guillemets double : `["herbe", "mur"]`. Elle signifie : une liste avec deux game objects dedans. Le premier est de type "herbe", le second de type "mur".

Et si vous mettiez des listes de plusieurs game objects dans la correspondance ente caractères et game objects ? Ce sera peut-être mieux que d'avoir des listes de un seul game object.


## La réponse pour que ce soit plus beau

Dans le code du jeu, remplacez cette partie :
```
corresp_game_objects_a_partir_char = {
    " ": ["herbe"],
    "#": ["mur"],
    "@": ["personnage"],
    "$": ["caisse"],
    ".": ["cible"]
}
```
Par ceci :
```
corresp_game_objects_a_partir_char = {
    " ": ["herbe"],
    "#": ["mur"],
    "@": ["herbe", "personnage"],
    "$": ["herbe", "caisse"],
    ".": ["herbe", "cible"],
}
```

On a ajouté le type de game object "herbe" dans toutes les listes, sauf les deux premières.

Exécutez le jeu, ça devrait être plus beau, chaque objet devrait s'afficher sur l'herbe, au lieu d'avoir un fond noir moche.

Un dernier petit détail, pour les gens qui s'y connaissent un peu en python. La ligne `game_objects = list(game_objects)` est importante. La fonction `list` permet de créer une copie pour chaque tile. Si vous ne le faites pas, vous aurez plusieurs références à la même liste. Lorsque vous changerez le contenu de l'une des tiles (en ajoutant ou supprimant un game object), cela modifiera également toutes les autres. On ne va pas rentrer plus loin dans les explications, tout ce que vous avez à savoir pour ce tutoriel, c'est qu'il faut laisser cette ligne de code.


## Petite pause

Si vous avez lu et effectué ce qui est demandé jusqu'ici, bravo ! Vous avez bien mérité une petite pause ! Mangez un morceau, jouez à un jeu qui vous plaît et nourrissez votre poisson rouge. Pour la suite, on s'attaquera à un gros morceau : l'interactivité et le déplacement du personnage.

![https://www.clipartmax.com/middle/m2H7i8m2Z5N4K9K9_goldfish-fish-pixel-pixels-pixelart-aesthetic-localcupc-goldfish-pixel-art/](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/goldfish.png)


## On écrit (pas sur les murs)

Dans le code du jeu, tout à la fin, ajoutez la fonction suivante :

```
    def on_game_event(self, event_name):
        print(event_name)
```

Exécutez le jeu, puis cliquez sur les boutons. Le programme ne plante plus, et du texte s'affiche en bas, selon le bouton appuyé :

 - "U" (up) : le bouton "haut"
 - "D" (down) : bouton "bas"
 - "L" (left) : bouton "gauche"
 - "R" (right) : bouton "droit"
 - "action_1" : bouton "1"
 - "action_2" : bouton "2"

La fonction que vous avez ajoutée se nomme `on_game_event`, elle se trouve à l'intérieur de la classe `GameModel`. Elle est spéciale (on appelle ça une "callback"), car elle est exécutée lorsqu'on appuie sur un bouton du jeu. Le paramètre `event_name` permet de savoir quel bouton a été appuyé.

Vous pouvez ensuite écrire du code dans la fonction, pour déclencher ce que vous voulez : ouvrir des portes, répandre de la lave, téléporter des monstres, ...


## Ça bouge !

Pour commencer, il faut que le personnage se déplace. C'est l'élément principal du jeu, il mérite bien quelques variables que pour lui.

Dans la fonction d'initialisation, juste après la ligne `def __init__(self):`, ajoutez ces deux lignes :
```
        self.personnage_x = 13
        self.personnage_y = 6
```

Puis, dans la fonction `on_game_event` (c'est à dire à la fin du code du jeu), ajoutez ce code :
```
        tile_personnage = self.get_tile(self.personnage_x, self.personnage_y)
        if "personnage" in tile_personnage:
            tile_personnage.remove("personnage")

        self.personnage_x += 1

        tile_personnage = self.get_tile(self.personnage_x, self.personnage_y)
        tile_personnage.append("personnage")
```

Exécutez le jeu.

Appuyez sur un bouton, n'importe lequel. À chaque fois, le personnage se déplacera vers la droite. Arrivé au bord du jeu, ça plante.

C'est un début.


## Rebidouillons un peu

Dans la fonction `on_game_event`, nous avons ajouté trois morceaux de code, séparés par une ligne vide. Le premier supprime le personnage de l'aire de jeu, le deuxième modifie ses coordonnées, le troisième le replace à sa nouvelle position.

Le deuxième bloc de code ne contient qu'une seule ligne : `self.personnage_x += 1`. L'opérateur `+=` permet d'ajouter une valeur à une variable. L'opérateur `-=` permet de soustraire.

Mettez une autre valeur que "1" dans cette ligne de code et essayez de comprendre ce que ça fait.

Remettez la valeur "1". Essayez de faire en sorte que le personnage se déplace vers la gauche lorsqu'on appuie sur un bouton, puis vers le haut, puis vers le bas.

C'est amusant, mais vous n'avez toujours pas de personnage se déplaçant dans la bonne direction selon le bouton appuyé.


## Ça bouge mieux

Remplacez la ligne que vous avez bidouillé :
```
        self.personnage_x += 1
```

Par tout ce bloc :
```
        if event_name == "R":
            self.personnage_x += 1
        elif event_name == "L":
            self.personnage_x -= 1
        if event_name == "D":
            self.personnage_y += 1
        if event_name == "U":
            self.personnage_y -= 1
```

Exécutez le jeu.

Cette fois-ci, le personnage devrait pouvoir se déplacer dans les 4 directions.

Essayez de sortir des bords de l'aire de jeu. À droite et en bas, ça fera une erreur et vous devrez re-exécutez le jeu.

En haut et à gauche, le personnage réapparaîtra de l'autre côté.

Il y a une raison à cela, provenant de la manière dont les éléments d'une liste sont indexés. Vous trouverez des explications à ce sujet dans des cours de python, si ça vous intéresse. Juste comme ça rapidement : `["a", "b", "c", "d"][0] == "a"` et `["a", "b", "c", "d"][-1] == "d"`.

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_move_border.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_move_border.png)


## Empêcher le personnage de dépasser les bords

Dans le code du jeu, remplacez toute la fonction `on_game_event` par ce code :

```
    def on_game_event(self, event_name):

        personnage_dest_x = self.personnage_x
        personnage_dest_y = self.personnage_y

        if event_name == "R":
            personnage_dest_x += 1
        elif event_name == "L":
            personnage_dest_x -= 1
        if event_name == "D":
            personnage_dest_y += 1
        if event_name == "U":
            personnage_dest_y -= 1

        if not (0 <= personnage_dest_x < self.w and 0 <= personnage_dest_y < self.h):
            return

        tile_personnage = self.get_tile(self.personnage_x, self.personnage_y)
        if "personnage" in tile_personnage:
            tile_personnage.remove("personnage")

        self.personnage_x = personnage_dest_x
        self.personnage_y = personnage_dest_y

        tile_personnage = self.get_tile(self.personnage_x, self.personnage_y)
        tile_personnage.append("personnage")
```

Le personnage ne peut plus sortir de l'aire de jeu.

Voici ce que fait le code que nous venons d'ajouter :

 - Création des variables temporaires `personnage_dest_x` et `personnage_dest_y`. Initialisation aux coordonnées actuelles du personnage.
 - Modification de l'une de ces deux variables, selon le déplacement à faire, comme dans le chapitre précédent.
 - Vérification que le personnage sort par un bord.
 - Si il sort, le mouvement n'est pas appliqué. On quitte directement la fonction, en utilisant l'instruction python `return`.
 - Si il ne sort pas, on applique le mouvement.
 - Comme précédemment, on enlève le game object, on modifie les coordonnées réelles du personnage, on rajoute le game object à la nouvelle position.


## Placement initial du personnage

Petite bidouille : la variable `PLAN_DU_NIVEAU`, au début du code, indique où se trouvent les différents objets. Le personnage est représenté par le caractère `@`. Placez ce caractère à un autre endroit du plan, exécutez le jeu, déplacez le personnage. Est-ce que ça fonctionne comme il faut ? Manifestement non.

Lors de l'initialisation du jeu, la valeur des variables `self.personnage_x` et `self.personnage_y` devrait dépendre du plan du niveau, et plus précisément de l'endroit où se trouve le caractère "@".

Il faut parcourir tout le plan du niveau, repérer le caractère "@", prendre ses coordonnées et les placer dans ces deux variables.

Nous effectuons déjà un parcours du plan au début du jeu, profitons-en !

Dans la fonction `def __init__(self)`, dans la boucle de boucle, juste après la ligne de code `ligne.append(game_objects)`, ajoutez le code suivant :
```
                if char_carte == "@":
                    self.personnage_x = x
                    self.personnage_y = y
```

Comme d'habitude, attention aux espaces au début de chaque ligne.

Exécutez le jeu. Il devrait fonctionner comme avant.

Dans la variable `PLAN_DU_NIVEAU`, déplacez le caractère "@".

Exécutez le jeu. Déplacez le personnage. Ça devrait être beaucoup mieux qu'avant. Le personnage ne fait plus de téléportation bizarre.

Vous n'avez maintenant plus besoin de ces deux lignes qui sont restées au début de la fonction :
```
        self.personnage_x = 13
        self.personnage_y = 6
```

Vous pouvez tester une mini-bidouille : remodifiez le `PLAN_DU_NIVEAU` en ajoutant plusieurs caractères "@". Exécutez le jeu. On voit plusieurs personnages, mais un seul d'entre eux se déplace.

Ajoutez ou déplacez des caractères "@" comme vous le souhaitez, essayez de repérer à chaque fois quel est le personnage qui sera déplaçable. Il n'est pas choisi au hasard.

Dans la suite de ce tutoriel, on gardera des niveaux avec un seul caractère "@". On ne gère pas le cas avec plusieurs personnages. Mais rien ne vous empêche de créer une autre version du jeu où ce serait géré.


## On se cogne sur les murs

Un personnage qui passe à travers tout, c'est un super-pouvoir génial. Mais ça ne fait pas un jeu très intéressant.

Avant d'effectuer le mouvement, il faut vérifier le contenu de la case de destination. Si cette case contient un game object de type "mur", il faut annuler le mouvement.

Il est possible que vous soyez un peu dans les choux après ces nombreuses modifs dans le code. C'est comme ça que fonctionne la programmaton. On rajoute des petits morceaux au fur et à mesure. Tout n'est pas écrit d'une traite du début à la fin.

Je vais quand même vous aider, voici un récapitutif complet du code, avec la gestion des murs.

Effacez tout le code de votre jeu, et copier-collez à la place ce gigantesque texte :

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
    "#": ["herbe", "mur"],
    "@": ["herbe", "personnage"],
    "$": ["herbe", "caisse"],
    ".": ["herbe", "cible"],
}

class GameModel():

    def __init__(self):

        self.w = 20
        self.h = 14
        self.tiles = []

        for y in range(self.h):
            ligne_plan_du_niveau = PLAN_DU_NIVEAU[y]
            ligne = []
            for x in range(self.w):
                char_carte = ligne_plan_du_niveau[x]
                game_objects = corresp_game_objects_a_partir_char[char_carte]
                game_objects = list(game_objects)
                if char_carte  == "@":
                    self.personnage_x = x
                    self.personnage_y = y
                ligne.append(game_objects)
            self.tiles.append(ligne)

    def export_all_tiles(self):
        return self.tiles

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def on_game_event(self, event_name):

        personnage_dest_x = self.personnage_x
        personnage_dest_y = self.personnage_y

        if event_name == "R":
            personnage_dest_x += 1
        elif event_name == "L":
            personnage_dest_x -= 1
        if event_name == "D":
            personnage_dest_y += 1
        if event_name == "U":
            personnage_dest_y -= 1

        if not (0 <= personnage_dest_x < self.w and 0 <= personnage_dest_y < self.h):
            return

        tile_dest = self.get_tile(personnage_dest_x, personnage_dest_y)
        if "mur" in tile_dest:
            return

        tile_personnage = self.get_tile(self.personnage_x, self.personnage_y)
        if "personnage" in tile_personnage:
            tile_personnage.remove("personnage")

        self.personnage_x = personnage_dest_x
        self.personnage_y = personnage_dest_y

        tile_personnage = self.get_tile(self.personnage_x, self.personnage_y)
        tile_personnage.append("personnage")
```

Exécutez le jeu. Ça devrait fonctionner. Le personnage se déplace, mais ne peut pas aller sur les murs.


## Seconde petite pause

Re-nourrissez votre poisson rouge, il en a besoin.

![http://pixelartmaker.com/art/c9d0a98ae70ec58](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/fish2.png)


## On pousse des caisses (mais on n'en largue pas)

Vous allez bientôt avoir un jeu jouable. Il faudrait maintenant que le personnage puisse pousser les caisses.

Dans le chapitre précédent, nous avons ajouté une vérification sur le contenu de la tile de destination. S'il y a un mur, la fonction se termine tout de suite.

Il faut une vérification supplémentaire. Si la tile de destination contient une caisse, il faut appliquer le même mouvement sur la caisse et sur le personnage. C'est à dire qu'on enlève la caisse de la tile où elle se trouve, et on la remet sur une tile à côté.

Nous définirons trois variables :

 - `tile_depart_perso` : la tile où se trouve le personnage au départ.
 - `tile_dest_perso` : la tile de destination du personnage.
 - `tile_dest_caisse` : la tile de destination de la caisse, si on pousse une caisse.

On n'a pas besoin d'une variable `tile_depart_caisse`, car c'est la même tile que `tile_dest_perso`.

Ça ajoute beaucoup de modifications, mais uniquement dans la fonction `on_game_event`. Ci-dessous, la fonction complète mise à jour. Supprimez celle qui est dans le code du jeu et copier-collez celle-ci à la place.

```
    def on_game_event(self, event_name):

        tile_depart_perso = self.get_tile(self.personnage_x, self.personnage_y)
        personnage_dest_x = self.personnage_x
        personnage_dest_y = self.personnage_y

        if event_name == "R":
            personnage_dest_x += 1
        elif event_name == "L":
            personnage_dest_x -= 1
        if event_name == "D":
            personnage_dest_y += 1
        if event_name == "U":
            personnage_dest_y -= 1

        if not (0 <= personnage_dest_x < self.w and 0 <= personnage_dest_y < self.h):
            return

        tile_dest_perso = self.get_tile(personnage_dest_x, personnage_dest_y)

        if "mur" in tile_dest_perso:
            return

        if "caisse" in tile_dest_perso:
            caisse_dest_x = personnage_dest_x
            caisse_dest_y = personnage_dest_y
            if event_name == "R":
                caisse_dest_x += 1
            elif event_name == "L":
                caisse_dest_x -= 1
            if event_name == "D":
                caisse_dest_y += 1
            if event_name == "U":
                caisse_dest_y -= 1

            tile_dest_caisse = self.get_tile(caisse_dest_x, caisse_dest_y)
            tile_dest_perso.remove("caisse")
            tile_dest_caisse.append("caisse")

        if "personnage" in tile_depart_perso:
            tile_depart_perso.remove("personnage")

        tile_dest_perso.append("personnage")
        self.personnage_x = personnage_dest_x
        self.personnage_y = personnage_dest_y
```

Exécutez le jeu et essayez de pousser une caisse.


## Empêcher les caisses d'aller n'importe où

Essayez de pousser des caisses un peu partout. Woups ! ça devient bizarre. La caisse sort de l'écran, se téléporte éventuellement de l'autre côté, rentre dans un mur, etc.

Lors d'un mouvement, que ce soit un personnage ou une caisse, il faut effectuer les mêmes vérifications. Si une vérification échoute, il faut annuler tout le mouvement (du personnage et de la caisse).

On pourrait copier-coller des morceaux de code dans la fonction `on_game_event`. Mais ça ferait un code moche et plus difficile à comprendre.

Nous avons déjà une portion de code qui se répète : l'application d'un mouvement sur des coordonnées.

Dans ces cas là, il faut essayer de ranger le code, de placer les morceaux qui se répètent dans des fonctions et d'utiliser ces fonctions. On appelle ça une "factorisation".

Allons-y ! Resupprimez toute la fonction `on_game_event` et remplacez-là par tout le bazar qui suit :

```
    def coord_mouvement(self, x, y, direction):
        if direction == "R":
            x += 1
        elif direction == "L":
            x -= 1
        if direction == "D":
            y += 1
        if direction == "U":
            y -= 1
        return (x, y)

    def verifier_mouvement(self, dest_x, dest_y):
        if not (0 <= dest_x < self.w and 0 <= dest_y < self.h):
            return False
        if "mur" in self.get_tile(dest_x, dest_y):
            return False
        return True

    def on_game_event(self, event_name):

        personnage_dest_x, personnage_dest_y = self.coord_mouvement(
            self.personnage_x,
            self.personnage_y,
            event_name
        )
        if not self.verifier_mouvement(personnage_dest_x, personnage_dest_y):
            return

        tile_depart_perso = self.get_tile(self.personnage_x, self.personnage_y)
        tile_dest_perso = self.get_tile(personnage_dest_x, personnage_dest_y)

        if "caisse" in tile_dest_perso:
            caisse_dest_x, caisse_dest_y = self.coord_mouvement(
                personnage_dest_x,
                personnage_dest_y,
                event_name
            )
            if not self.verifier_mouvement(caisse_dest_x, caisse_dest_y):
                return
            tile_dest_caisse = self.get_tile(caisse_dest_x, caisse_dest_y)

            tile_dest_perso.remove("caisse")
            tile_dest_caisse.append("caisse")

        tile_depart_perso.remove("personnage")
        tile_dest_perso.append("personnage")
        self.personnage_x = personnage_dest_x
        self.personnage_y = personnage_dest_y
```

Exécutez le jeu. Essayez de pousser les caisses. Elles ne peuvent plus sortir de l'aire de jeu et ne peuvent plus aller dans les murs.


## Une caisse qui encaisse

Essayez de pousser une caisse sur une autre caisse.

Oups, bug ! Les deux caisses se retrouvent sur la même tile. Si vous poussez encore une fois, l'une des deux caisses se déplace et le personnage se retrouve sur l'autre caisse. C'est amusant mais ce n'est pas du tout ce qu'on veut.

Il faut rajouter une dernière vérification : une caisse ne peut pas être poussée sur une autre caisse.

Cette vérification ne peut pas être ajoutée dans la fonction générique `verifier_mouvement`, car on s'en sert pour vérifier à la fois les mouvements des caisses et du personnage. Or, il y a une différence entre les deux types d'objets : un personnage peut pousser une caisse mais une caisse ne peut pas pousser une caisse. On ne peut pas factoriser toute la vérification.

Il faut donc ajouter la dernière vérification dans la fonction `on_game_event`.

Après cette ligne :
```
            tile_dest_caisse = self.get_tile(caisse_dest_x, caisse_dest_y)
```

Ajoutez ce code :

```
            if "caisse" in tile_dest_caisse:
                return
```

Exécutez le jeu. Essayez de pousser une caisse sur une autre caisse. Ça ne devrait plus être possible.


## Condition de victoire

Le jeu est maintenant jouable, mais il n'est pas très fun.

Le but est d'amener chaque caisse sur une cible. Mais si vous y parvenez, il ne se passera rien de spécial. Le minimum serait d'afficher un message de récompense.

Il faut consulter toutes les tiles de l'aire de jeu. Si l'une d'elles contient une caisse mais pas de cible, cela signifie que les caisses n'ont pas toutes été rangées, et le jeu n'est pas gagné. Pas la peine de continuer la consultation des tiles. Mais si chaque caisse est sur une cible, alors on peut afficher un message.

Ce traitement est indépendant de tous les traitements existant dans le code. Nous le placerons donc dans une fonction, même si elle ne sera utilisée qu'une seule fois.

Ajoutez ceci à la fin du code :

```
    def verifier_caisses_sur_cible(self):
        for y in range(self.h):
            for x in range(self.w):
                current_tile = self.get_tile(x, y)
                if "caisse" in current_tile and "cible" not in current_tile:
                    return False
        return True
```

On n'a besoin de faire cette vérification que lorsqu'une caisse a été déplacée.

Dans la fonction `on_game_event`, après cette ligne :
```
            tile_dest_caisse.append("caisse")
```

Ajoutez ce morceau de code :
```
            if self.verifier_caisses_sur_cible():
                print("Bravo, vous avez gagné !")
```

Exécutez le jeu. Placez chaque caisse sur une cible. Vous verrez votre superbe message de félicitations s'afficher en bas.


## Le grand final

Voilà, votre jeu est jouable et il affiche un message en cas de victoire. C'est fun, yeah !

Il reste à ajouter quelques détails :

 - D'autres caractères dans le plan du niveau, pour représenter une tile contenant à la fois une caisse et une cible, et une une tile contenant à la fois une cible et le personnage.
 - La possibilité de définir plusieurs niveaux. Le jeu passe automatiquement au niveau suivant après une victoire.
 - Lorsqu'on appuie deux fois de suite sur le bouton d'action numéro 1, le niveau en cours est réinitialisé.

Ce tutoriel est déjà assez long comme ça et ces détails ajoutent des morceaux de code un peu partout, je vais donc directement vous donner tout le code final.

Les niveaux sont définis au début du code, sous forme d'une liste de variables structurées de la même manière que l'ancienne variable `PLAN_DU_NIVEAU`. Vous pouvez ajouter, modifier, ou supprimer des niveaux comme bon vous semble.

Voici tous les caractères utilisés :

 - `#` : mur
 - `@` : personnage
 - `+` : personnage sur une cible
 - `$` : caisse
 - `*` : caisse sur une cible
 - `.` : cible
 - " " (un espace) : rien

Au final, votre jeu ressemblera à ceci :

![https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_final.png](https://raw.githubusercontent.com/darkrecher/squarity-doc/master/user_manual/tuto_screenshot_final.png)

Effacez tout le code du jeu actuel, copier-collez tout le texte ci-dessous. Comme ça, même si vous êtes dans les choux et que vous n'avez pas entièrement compris les étapes précédentes, vous avez votre jeu complet :

```
PLANS_DES_NIVEAUX_ET_DESCRIPTIONS = (
    (
        "Origine de ce niveau : http://www.sokobano.de/wiki/index.php?title=Optimizer",
        (
            "                    ",
            "          ####      ",
            "         ##. ##     ",
            "     ##### .  #     ",
            "     #   #  # #     ",
            "     # $ #  # #     ",
            "     # $      #     ",
            "     ######  ##     ",
            "          # ##      ",
            "          # #       ",
            "          # #       ",
            "         ## ##      ",
            "         # @ #      ",
            "         #   #      ",
        )
    ),
    (
        "Origine : https://www.mathsisfun.com/games/sokoban.html (un peu transformé)",
        (
            "    #####           ",
            "    #   #      ###  ",
            "    #$  #      #.#  ",
            "  ###  $###    # #  ",
            "  #  $  $ #   ## ###",
            "### # ### #   #   .#",
            "#   # ### #####  ###",
            "# $  $           ..#",
            "########### ###  ###",
            "          # # #   .#",
            "          # # ## ###",
            "          # #  # #  ",
            "          # #  #.#  ",
            "          #@#  ###  ",
        )
    ),
    (
        "Origine : https://www.mathsisfun.com/games/sokoban.html",
        (
            "                    ",
            "                    ",
            "                    ",
            "         #####      ",
            "##########   #      ",
            " @      . $  #      ",
            "########## $.#      ",
            "       #.##$ #      ",
            "       # # . ##     ",
            "       #$ *$$.#     ",
            "       #   .  #     ",
            "       ## #####     ",
            "        # #         ",
            "        # #         ",
        )
    ),
    (
        "Origine : https://alonso-delarte.medium.com/the-basics-of-sokoban-level-formats-"
        "for-designing-your-own-sokoban-levels-51882a7a36f0",
        (
            "       #####        ",
            "   #####   #####    ",
            "   #           #    ",
            "   #  ### ###  #    ",
            " #### #     # ####  ",
            "##    #  *  #    #  ",
            "   $  # *+*      #  ",
            "##    #  *  #    #  ",
            " #### #     # ####  ",
            "   #  ### ###  #    ",
            "   #           #    ",
            "   #####   #####    ",
            "       #####        ",
            "                    ",
        ),
    ),
    (
        "Bravo, vous avez réussi tous les niveaux. Pourquoi ne pas en profiter pour créer les vôtres ?",
        (
            "         @          ",
            "#  #  ### #   #  #  ",
            "#  #  #    # #   #  ",
            "####  ##    #    #  ",
            "#  #  #     #       ",
            "#  #  ###   #    #  ",
            "                    ",
            "        ####        ",
            "       #    #       ",
            "      # .  . #      ",
            "      #      #      ",
            "      #  ..  #      ",
            "       #    #       ",
            "        ####        ",
        ),
    ),
)

corresp_game_objects_a_partir_char = {
    " ": ["herbe"],
    "#": ["herbe", "mur"],
    "@": ["herbe", "personnage"],
    "$": ["herbe", "caisse"],
    ".": ["herbe", "cible"],
    "+": ["herbe", "cible", "personnage"],
    "*": ["herbe", "cible", "caisse"],
}

class GameModel():

    def debuter_niveau(self):

        description, plan_du_niveau = PLANS_DES_NIVEAUX_ET_DESCRIPTIONS[self.numero_niveau]
        print(description)
        print()
        self.tiles = []

        for y in range(self.h):
            ligne_plan_du_niveau = plan_du_niveau[y]
            ligne = []
            for x in range(self.w):
                char_carte = ligne_plan_du_niveau[x]
                game_objects = corresp_game_objects_a_partir_char[char_carte]
                game_objects = list(game_objects)
                if "personnage" in game_objects:
                    self.personnage_x = x
                    self.personnage_y = y
                ligne.append(game_objects)
            self.tiles.append(ligne)

    def __init__(self):
        self.w = 20
        self.h = 14
        self.numero_niveau = 0
        self.debuter_niveau()
        self.niveau_reussi = False
        self.confirm_reset_level = False

    def export_all_tiles(self):
        return self.tiles

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def coord_mouvement(self, x, y, direction):
        if direction == "R":
            x += 1
        elif direction == "L":
            x -= 1
        if direction == "D":
            y += 1
        if direction == "U":
            y -= 1
        return (x, y)

    def verifier_mouvement(self, dest_x, dest_y):
        if not (0 <= dest_x < self.w and 0 <= dest_y < self.h):
            return False
        if "mur" in self.get_tile(dest_x, dest_y):
            return False
        return True

    def verifier_caisses_sur_cible(self):
        for y in range(self.h):
            for x in range(self.w):
                current_tile = self.get_tile(x, y)
                if "caisse" in current_tile and "cible" not in current_tile:
                    return False
        return True

    def on_game_event(self, event_name):

        if self.niveau_reussi:
            self.numero_niveau += 1
            self.debuter_niveau()
            self.niveau_reussi = False
            return

        if event_name == "action_1":
            if self.confirm_reset_level:
                self.debuter_niveau()
                self.confirm_reset_level = False
                print("réinitialisation niveau")
            else:
                self.confirm_reset_level = True
                print("Appuyez à nouveau sur le bouton '1'")
                print("pour confirmer la réinitialisation du niveau.")
            return

        self.confirm_reset_level = False

        personnage_dest_x, personnage_dest_y = self.coord_mouvement(
            self.personnage_x,
            self.personnage_y,
            event_name
        )
        if not self.verifier_mouvement(personnage_dest_x, personnage_dest_y):
            return

        tile_depart_perso = self.get_tile(self.personnage_x, self.personnage_y)
        tile_dest_perso = self.get_tile(personnage_dest_x, personnage_dest_y)

        if "caisse" in tile_dest_perso:
            caisse_dest_x, caisse_dest_y = self.coord_mouvement(
                personnage_dest_x,
                personnage_dest_y,
                event_name
            )
            if not self.verifier_mouvement(caisse_dest_x, caisse_dest_y):
                return
            tile_dest_caisse = self.get_tile(caisse_dest_x, caisse_dest_y)
            if "caisse" in tile_dest_caisse:
                return

            tile_dest_perso.remove("caisse")
            tile_dest_caisse.append("caisse")
            if self.verifier_caisses_sur_cible():
                print("Bravo, vous avez gagné !")
                print("Appuyez sur un bouton pour passer au niveau suivant")
                print("")
                self.niveau_reussi = True

        tile_depart_perso.remove("personnage")
        tile_dest_perso.append("personnage")
        self.personnage_x = personnage_dest_x
        self.personnage_y = personnage_dest_y
```

Si vous en avez assez de faire des copié-collés, vous pouvez directement jouer à la version finale de ce sokoban, ici : http://squarity.fr/#fetchez_githubgist_darkrecher/aa3e1338998cc2a20a030011fbca9ce2/raw/sokoban-tuto.txt .

J'ai ajouté plein de commentaires dans le code, pour le re-expliquer plus en détail. Ça peut vous aider à comprendre comment fonctionnne certaines parties.

Si vous êtes arrivés jusqu'ici, bravo ! N'hésitez pas à bidouiller le code autant que vous le pouvez, pour mieux comprendre comment il fonctionne. Consultez des tutoriels et des cours spécifiques sur le python. Créez d'autres jeux, ou modifiez celui-là. Bref : amusez-vous !
