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

Si ce nombre est "1", la version utilisée sera "1.0.0". **Son fonctionnement est figé**, sauf pour la correction d'éventuels bugs majeurs.

Si ce nombre est "2", la version utilisée sera la version 2.x.y la plus récente (actuellement : "2.1.0"). Vous n'avez donc pas accès aux précédentes versions 2.x.y, mais elles sont censées être rétro-compatibles.


## Notions de base

GameModel, avec des callbacks.
Layer.
GameObject, avec des coordonnées et une image.

schéma d'affichage, avec les différentes tailles.

## Direction

## Coord

## Rect

## GameObject

transition par défaut quand on change des coordonnées.

## Layer

## GameModel

## EventResult

### DelayedCallBack

### plock custom

### no redraw

TODO: je l'ai toujours ce truc ou pas ?

## Transition

### transition time

### plock transi

### TransitionSteps

## Info supplémentaires dans la config

## ComponentImageModifier

## ComponentBackCaller

## Itérer sur les GameObjects

## Créer un lien direct vers votre jeu


