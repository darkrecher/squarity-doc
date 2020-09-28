# Manuel utilisateur de Squarity

Fucking tagline

[Squarity](squarity.fr) est un espace de création et de partage de jeux vidéos jouable en ligne.

Les jeux sont en 2D "case par case". C'est à dire que l'aire de jeu est une grille composée de carrés, sur lesquelles sont placés les éléments du jeu (comme par exemple les dames, le démineur, ...)

La "game logic" (le fonctionnement et les règles du jeu) sont définis par du code en python 3. Il s'agit d'un langage de programmation, dont vous trouverez beaucoup de tutoriels et de références sur internet.

Pour créer un jeu, il faut définir trois composants :

 - le tileset
 - la configuration
 - le "game_code"

## Tileset

Il s'agit d'une image, dans un format classique (.jpg, .png, ...) contenant tous les éléments (décors, personnages, objets) de votre jeu. Voici quelques exemples de tileset : h2O, simple-pimple.

Chaque élément doit être contenu dans un carré. Tous les éléments doivent avoir la même taille en pixels.

La définition des pixels transparents, dans le format d'image png, est prise en compte.

Il est conseillé d'utiliser le format png plutôt que jpg, car le jpg modifie légèrement les couleurs des pixels pour diminuer la taille en octets de l'image. C'est très bien pour des photos, mais très gênant pour des tilesets qui doivent rester précis.


## La configuration

Il s'agit d'un texte, au format JSON. Ce format permet de définir des informations de manière structurée. Par exemple : une liste de nombre, une correspondance entre des mots et des nombres, une liste contenant une sous-liste contenant des sous-sous-correspondances de mots, etc.

Exemple de configuration de jeu :

[TODO]

La configuration est structurée comme suit :

 - l'élément principal est un dictionnaire (une "correspondance"), contenant deux sous-éléments
   - le premier a pour clé "tile_size", et pour valeur un nombre. Ce nombre correspond à la taille, en pixels, de tous les éléments du jeu, tel que vous les avez dessinés dans votre tileset.
   - le suivant a pour clé "tile_coords", et pour valeur un sous-dictionnaire, contenant plusieurs sous-élément
     - chacun de ces sous-éléments a pour clé un texte (de un ou plusieurs caractères), correspondant à un nom d'objet dans votre jeu.


[Exemple avec un tileset]


