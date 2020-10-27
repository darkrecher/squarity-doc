# Manuel utilisateur de Squarity

[Squarity](http://squarity.fr) est un espace de création et de partage de jeux vidéo jouables en ligne.

Les jeux sont en 2D "case par case", (exemple : les dames, le démineur, ...). L'aire de jeu est une grille composée de carrés, sur lesquels sont placés des éléments.

La "game logic" (le fonctionnement et les règles du jeu) est définie par du code en python 3. Il s'agit d'un langage de programmation, que vous pourrez découvrir par une [foisonnance de tutoriels](https://python.developpez.com/cours/).

Pour créer un jeu, il faut définir trois composants :

 - tileset,
 - configuration,
 - "game_code".

## Le tileset

Il s'agit d'une image, au format jpg, png ou autre, contenant les éléments (décors, personnages, objets) de votre jeu. En voici quelques exemples :

![https://squarity.pythonanywhere.com/img/h2o_tileset.c174edea.png](https://squarity.pythonanywhere.com/img/h2o_tileset.c174edea.png)

![https://opengameart.org/sites/default/files/HighContrastRoguelikeCastle.png](https://opengameart.org/sites/default/files/HighContrastRoguelikeCastle.png)

Chaque élément de jeu doit être contenu dans un carré. Ils doivent tous avoir la même taille en pixels.

La définition des pixels transparents, dans le format png, est prise en compte.

Il est conseillé d'utiliser le format png, car le jpg modifie légèrement les couleurs des pixels pour diminuer la taille en octets de l'image. C'est très bien pour des photos, mais très gênant pour des tilesets qui doivent rester précis.

Pour qu'il soit accessible dans Squarity, votre tileset doit être publié sur internet. Utilisez des sites d'hébergement d'images comme imgur ou imgbb, puis récupérez l'url directe de votre fichier image (clic droit, option "ouvrir l'image dans un nouvel onglet"). Indiquez cette url dans le champ Tileset.

Si l'image n'est pas trop grande, vous pouvez également la convertir en url-data, avec un service en ligne comme [ezgif](https://ezgif.com/image-to-datauri).


## La configuration

Il s'agit d'un texte, au format JSON. Ce format permet de définir des informations de manière structurée. Par exemple :

 - une liste de nombre,
 - une correspondance entre des mots et des nombres,
 - une liste contenant une sous-liste contenant des sous-sous-correspondances de mots,
 - etc.

Exemple de configuration de jeu :

    {
        "tile_size": 32,
        "tile_coords": {
            "X": [0, 0],
            ".": [32, 0],
            "H": [64, 0],
            "C": [96, 0],
            "water_right": [0, 32],
            "water_down": [32, 32],
            "water_left": [64, 32],
            "water_up": [96, 32],
            "O": [0, 256],
            "wet_grid": [32, 256],
            "S": [64, 256]
        }
    }


La configuration est structurée comme ceci :

 - l'élément principal est un dictionnaire (une "correspondance"), contenant deux sous-éléments :
   - le premier a pour clé `tile_size`, et pour valeur un nombre. Ce nombre correspond à la taille, en pixels, de chacun des éléments du jeu, tel que vous les avez dessinés dans votre tileset.
   - le suivant a pour clé `tile_coords`, et pour valeur un sous-dictionnaire, contenant plusieurs sous-éléments :
     - chacun de ces sous-éléments a pour clé un texte (de un ou plusieurs caractères), correspondant à un nom d'objet dans votre jeu. La valeur est une liste de deux nombres, indiquant les coordonnées du coin supérieur gauche, dans le tileset, de l'image de cet objet du jeu.


## Le game_code

Il s'agit d'un texte écrit dans le langage python version 3.

Ce code doit décrire le contenu de l'aire de jeu (quels objets se trouvent sur quelle case), et les changements qui surviennent lorsque la personne qui joue appuie sur une touche de direction ou d'action.

L'aire de jeu affiche 20 cases (tiles) en largeur et 14 en hauteur. Ces tailles sont fixes. Elles seront configurables dans une version ultérieure de Squarity (qui sortira à une date indéterminée, side-project personnel, vous savez ce que c'est).

Votre code python doit posséder la structure minimale suivante :

```
class BoardModel():

    def __init__(self):
        self.w = 20 # width (largeur) : 20 cases
        self.h = 14 # height (hauteur) : 14 cases
        self.tiles = [
            [
                [] for x in range(self.w)
            ]
            for y in range(self.h)
        ]

    def get_size(self):
        return self.w, self.h

    def export_all_tiles(self):
        return self.tiles

    def on_game_event(self, event_name):
        pass
```

Ce code définit une classe `BoardModel`, contenant la fonction `__init__` et trois callbacks, c'est à dire des fonctions appelées à des moments précis par le système de jeu.

Vous pouvez bien entendu ajouter d'autres classes, d'autres fonctions, d'autres variables membres dans BoardModel, etc.

### Fonction BoardModel.\_\_init\_\_(self)

Cette fonction est exécutée une seule fois, au début du jeu.

Vous n'êtes pas obliger d'initialiser une variable membre `self.tiles` dans cette fonction, mais c'est une bonne pratique.

Cete variable membre est constituée d'un tableau de 20*14 cases, chacune contenant une liste vide.

Vous pouvez ensuite remplir le contenu des cases de ce tableau, en ajoutant une ou plusieurs chaînes de caractères dans les listes, correspondants aux noms de vos objets définis dans la partie `tile_coords` de la configuration.

### Fonction BoardModel.get_size(self)

Cette fonction est exécutée une seule fois, au début du jeu.

Elle servira à définir les dimensions (largeur, hauteur) de l'aire de jeu. Pour l'instant, ça ne fonctionne pas bien, vous devez donc renvoyer le tuple (20, 14). Vous pouvez utiliser les variables membres contenant ces dimensions :

    return self.w, self.h

### Fonction BoardModel.export_all_tiles(self)

Cette fonction est appelée à chaque rendu de l'aire de jeu (lorsqu'elle est redessinée à l'écran).

Il faut renvoyer une tableau 2D dont chaque case contient une liste de strings, c'est à dire : "une liste de liste de liste de strings".

Chaque élément des listes de strings doit correspondre à l'un des noms définis dans la partie "tile_coords" de la config json, et déclenchera le dessin de l'objet concerné, dans la case concerné.

L'ordre des noms dans la liste définit l'ordre de dessin des objets sur la case.

Cette fonction peut effectuer des traitements spécifiques, par exemple construire le nom d'un objet complexe et le placer dans la liste à renvoyer. Mais le comportement le plus commun est de renvoyer directement `self.tiles`.

### Fonction BoardModel.on_game_event(self, event_name)

Cette fonction est appelée à chaque événement du jeu : une action de la personne qui joue, ou bien une action différée qui a été préalablement enregistrée.

Le paramètre `event_name` est une string indiquant le type d'action. Il peut prendre les valeurs suivantes :

 - "U" (up) : le bouton "haut" a été appuyé
 - "D" (down) : bouton "bas"
 - "L" (left) : bouton "gauche"
 - "R" (right) : bouton "droit"
 - "action_1" : bouton "1"
 - "action_2" : bouton "2"

Ces événements sont également déclenchés lorsque la personne qui joue appuie sur une touche (flèches de direction, "1" et "2" du pavé numérique ou du clavier normal). Pour cela, le focus doit être sur l'aire de jeu ou sur les touches. Il faut avoir cliqué dessus avec la souris.

Le paramètre `event_name` peut prendre d'autres valeurs, dans le cas des actions différées. Elle est définie lors de l'enregistrement de l'action. Ce fonctionnement n'est pas documenté pour l'instant, mais ça devrait venir très vite.

La fonction `on_game_event` a pour charge de modifier la situation du jeu, c'est à dire le contenu de `self.tiles` et des autres variables internes, en fonction de l'événement. Elle implémente la plus grande partie de la "game logic".

Un rendu complet de l'aire de jeu est déclenché après chaque appel de cette fonction. Sauf si on indique explicitement qu'on n'en veut pas (fonctionnement non documenté pour l'instant).

### Différences entre export_all_tiles et get_tile_gamobjs

`export_all_tiles(self)` est une fonction "externe", elle est appelée automatiquement par le système, lors des rendus. Elle ne devrait pas être appelée par votre game_code.

Elle pourra, dans le futur, renvoyer d'autres informations sur la situation du jeu.

La fonction `get_tile_gamobjs(self, x, y)` est "interne ", elle renvoie la liste des objets d'une seule case. C'est une fonction d'aide pour ajouter/enlever des éléments dans l'aire de jeu. Vous pouvez l'appeler dans votre game_code. Elle est facultative, si vous ne la définissez pas, le jeu pourra quand même fonctionner.

### Actions différées, actions bloquantes, annulation du rendu

Non documentés pour l'instant, car pas le temps. Consultez l'exemple du jeu du magicien pour (essayer de) déterminer à quoi ça sert et comment ça fonctionne.

Ce sont les strings json renvoyées par `on_game_event`, permettant de montrer le déplacement progressif des boules de feu et les étapes intermédiaires lorsque le personnage passe une porte.


## Démarrer le jeu

Cliquez sur le bouton "<< Envoyer le jeu" en bas de la page. Le jeu est entièrement réinitialisé, la classe `BoardModel` est reconstruite à partir du nouveau game_code.

Si l'url du tileset a changée, l'image est rechargée, sinon, celle qui est déjà en mémoire est conservée. Si vous avez modifié et republié votre tileset, mais que l'url est restée la même, vous devez changer l'url, envoyer le jeu, puis remettre l'ancienne url. Ce petit désagrément sera corrigé dès que possible.

Il n'est pas possible de sauvegarder la partie en cours. On recommence du début à chaque renvoi du jeu, et à chaque rechargement de la page web. Ce sera amélioré dans un futur proche, quoi que indéterminé.


## Quelques détails techniques

Le code python écrit dans le game_code est exécuté par votre navigateur web, grâce à la librairie [Brython 3.8](https://brython.info/). À priori, cela fonctionne également sur les smartphones, le peu de tests déjà effectués est assez concluant.

Lorsque votre code python comporte des erreurs, celles-ci s'écrivent dans la zone de texte en bas à gauche de la page web.

Lorsque vous appelez la fonction `print("message")`, le texte s'affiche également dans cette zone de texte. Vous pouvez utiliser cette fonctionnalité pour le debug et pour le jeu lui-même.

Évitez de déclencher des prints trop fréquents et sur chaque action. Les temps de réactions seront un peu diminués, car chaque print modifie le DOM (la structure interne de la page web), ce qui nécessite d'effectuer diverses opérations par le navigateur web.

Une bonne pratique serait d'avoir une fonction `debug(message)`, exécutant un print uniquement si un booléen global `debug_mode` est mis à True. Avant la distribution de votre jeu, mettez ce booléen à False.

Dans un futur indéterminé, il sera possible de configurer où vont les prints et les messages d'erreurs : dans la console javascript ou bien dans la zone de texte.


## Partager un jeu

Il est possible d'enregistrer vos jeux et de les partager avec d'autres personnes grâce à une simple url (quoi que un peu longue).

Un compte sur https://github.com est nécessaire.

Connectez-vous sur github, cliquez sur votre avatar en haut à droite et sélectionnez "Your gists".

Cliquez sur le bouton "+" en haut à droite pour créer un nouveau gist : il s'agit d'un texte que vous publiez sur github.

Choisissez un nom pour votre texte, **attention, pas d'underscore dans le nom du fichier, uniquement des caractères alphanumériques et des tirets "-"**.

Dans le contenu du texte, mettez les informations suivantes les unes à la suite des autres :

 - L'url de votre tileset.
 - À la ligne immédiatement en dessous, un séparateur. Le plus simple est de mettre 8 tirets : `------`. Attention, pas d'espace au début de la ligne.
 - Copié-collé de toute votre configuration json.
 - Le même séparateur que précédemment. Attention, il faut exactement les mêmes caractères, et toujours pas d'espaces au début de la ligne. Le plus simple est de remettre les 8 tirets.
 - Copié-collé de tout votre game_code.

En bas à droite, cliquez sur la flèche du bouton pour sélectionner "Create public gist", puis cliquez sur le bouton.

Lorsque votre gist est sauvegardé, cliquez sur le bouton "Raw" à droite du fichier texte.

L'url affichée dans votre navigateur devrait avoir cette forme :

`https://gist.githubusercontent.com/votre-nom/xxx123/raw/yyy456/raw/mon-super-jeu.txt`

Les parties "xxx123" et "yyy456" sont de longues suites de caractères alphanumériques, permettant d'identifier votre gist de manière unique.

Supprimer la partie "yyy456/" et recharger la page. Vérifier que le texte brut de votre jeu s'affiche toujours.

Garder la fin de cette url, à partir de votre nom de compte github. C'est à dire : `votre-nom/xxx123/raw/mon-super-jeu.txt`.

Ajoutez au début l'url de squarity et le préfixe indiquant qu'il faut aller sur gist :

`squarity.fr/#fetchez_githubgist_votre-nom/xxx123/raw/mon-super-jeu.txt`.

Attention, si vous indiquez le protocole, mettez `http://`, et non pas `https://`. Le site n'est pas sécurisé. Ce n'est pas grave, c'est pas comme si c'était le site de votre messagerie mail ou de votre banque en ligne.

Cette url reconstruite est le lien vers votre jeu. Vérifiez qu'il fonctionne bien, puis distribuez-le à vos ami(e)s et devenez une star de la scène vidéoludique indépendante !

Vous pouvez ensuite modifier votre gist pour améliorer ou corriger votre jeu. Le lien restera le même. Attention, après modification, il faut attendre quelques minutes pour que github mette à jour le lien vers la dernière version de votre gist. Vous devrez donc [attendre un peu](https://stackoverflow.com/questions/47066049/github-gist-raw-permalink-wont-update) avant de revérifier votre lien.

À titre d'exemple, voici un pacman créé par une gentille personne du nom de 10kbis.

Lien vers le gist : https://gist.githubusercontent.com/darkrecher/b5240940356e3bb7e59c8a2522c279d9/raw/pacman-10kbis.txt

Lien pour jouer directement : [http://squarity.fr#fetchez_githubgist_darkrecher/b5240940356e3bb7e59c8a2522c279d9/raw/pacman-10kbis.txt](http://squarity.fr#fetchez_githubgist_darkrecher/b5240940356e3bb7e59c8a2522c279d9/raw/pacman-10kbis.txt)

J'ai l'impression que son jeu plante. Il se bloque parfois après que vous récupériez une deuxième super-pat'gomm'. J'essayerais de corriger ça.


## Améliorations prévues

Beaucoup, mais indéterminées. Une roadmap sera fournie dès que possible. En attendant, la liste des tâches en cours est publiée sur Trello : https://trello.com/b/bt91FVOH/squarity


## Contacter l'admin de Squarity

Moi c'est Réchèr. Je développe Squarity pendant mon temps libre, juste pour voir jusqu'où ça va me mener, et pour faire foisonner la créativité vidéoludique de l'humanité.

Je n'ai pour l'instant prévu aucun moyen "officiel" pour me contacter. Il vous reste ceux que vous connaissez éventuellement déjà (réseau social, en vrai, etc.). En dernier recours, postez une petite issue dans github. J'essayerais de les consulter fréquemment.

Amusez-vous bien !

