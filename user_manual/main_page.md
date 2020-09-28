# Manuel utilisateur de Squarity

"Ici, il y a tout ce qu'il faut pour créer des histoires en jeux vidéos."

[Squarity](squarity.fr) est un espace de création et de partage de jeux vidéo jouables en ligne.

Les jeux sont en 2D "case par case", (exemple : les dames, le démineur, ...). L'aire de jeu est une grille composée de carrés, sur lesquelles sont placés les éléments.

La "game logic" (le fonctionnement et les règles du jeu) sont définis par du code en python 3. Il s'agit d'un langage de programmation, dont vous trouverez beaucoup de tutoriels et de références sur internet.

Pour créer un jeu, il faut définir trois composants :

 - le tileset
 - la configuration
 - le "game_code"

[TODO screenshot squarity]

## Tileset

Il s'agit d'une image, au format jpg, png ou autre, contenant tous les éléments (décors, personnages, objets) de votre jeu. Voici quelques exemples de tileset : h2O, simple-pimple [TODO].

Chaque élément doit être contenu dans un carré. Tous les éléments doivent avoir la même taille en pixels.

La définition des pixels transparents, dans le format png, est prise en compte.

Il est conseillé d'utiliser le format png, car le jpg modifie légèrement les couleurs des pixels pour diminuer la taille en octets de l'image. C'est très bien pour des photos, mais très gênant pour des tilesets qui doivent rester précis.

Pour qu'il soit accessible dans Squarity, votre tileset doit être publié sur internet (vous pouvez utiliser des sites d'hébergement d'images comme imgur ou [TODO]). Vous devez indiquer dans le champ tileset l'url directe vers le fichier image. Sur la plupart des sites d'hébergement, cette url peut être trouvée en faisant un clic droit sur l'image, option "ouvrir l'image dans un nouvel onglet".

TODO : tester les url data.


## Configuration

Il s'agit d'un texte, au format JSON. Ce format permet de définir des informations de manière structurée. Par exemple : une liste de nombre, une correspondance entre des mots et des nombres, une liste contenant une sous-liste contenant des sous-sous-correspondances de mots, etc.

Exemple de configuration de jeu :

[TODO]

La configuration est structurée comme ceci :

 - l'élément principal est un dictionnaire (une "correspondance"), contenant deux sous-éléments
   - le premier a pour clé "tile_size", et pour valeur un nombre. Ce nombre correspond à la taille, en pixels, de tous les éléments du jeu, tel que vous les avez dessinés dans votre tileset.
   - le suivant a pour clé "tile_coords", et pour valeur un sous-dictionnaire, contenant plusieurs sous-élément
     - chacun de ces sous-éléments a pour clé un texte (de un ou plusieurs caractères), correspondant à un nom d'objet dans votre jeu. La valeur est une liste de deux nombres, indiquant les coordonnées du coin supérieur gauche, dans le tileset, de l'image de cet objet du jeu.


## game_code

Il s'agit d'un texte, correspondant à un code informatique écrit en langage python version 3.

Ce code doit décrire le contenu de l'aire de jeu (quels objets se trouvent sur quelle case), et les changements qui surviennent lorsque la personne qui joue appuie sur une touche de direction ou d'action.

L'aire de jeu affiche 20 cases en largeur et 14 en hauteur. Ces tailles sont fixes. Elles seront configurables dans une version ultérieure de Squarity (qui sortira à une date indéterminée, vous savez ce que c'est).

Votre code python doit posséder la structure minimale suivante :

```
class BoardModel():

    def __init__(self):
        pass

    def get_tile(self, x, y):
        return []

    def on_player_action(action_type):
        pass
```

Ce code définit une classe `BoardModel`, contenant la fonction __init__ et deux callbacks, c'est à dire des fonctions qui sont appelées par le système du jeu à des moments précis.

Vous pouvez bien entendu ajouter d'autres classes, d'autres fonctions, d'autres variables membres dans BoardModel, etc.

### Fonction BoardModel.__init__

Cette fonction est exécutée une seule fois, au début du jeu.

Une bonne pratique est d'initialiser, dans cette fonction, une variable membre appelée `game_arena` (TODO, c'est ce nom ou bien ?), constituée d'un tableau de 20*14 cases, chacune contenant une liste vide.

TODO : code d'init.

Ensuite, vous pouvez remplir le contenu des cases de ce tableau, en ajoutant une ou plusieurs chaînes de caractères dans la liste, correspondants aux noms de vos objets défini dans la partie `tile_coords` de la configuration.

### Fonction BoardModel.get_tile




### Quelques détails techniques

Brython


## Démarrer le jeu




## Partager un jeu


TODO code : afficher tout le tileset en une seule instruction dans le code python.

