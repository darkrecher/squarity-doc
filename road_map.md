# La road map de Squarity

## Fonctionnement de la road map

Ce sera des road squares.

Square map :

7:effets_spéciaux 0:moteur 1:IDE
6:tutos_doc -1:(le milieu) 2:edition_de_level_et_tileset
5:contenu_promotion 4:social 3:autoformation_optimisation_prod

le milieu : document "fondateur" expliquant pourquoi je fais ce jeu. Et un autre mini-document expliquant comment je vais fonctionner avec cette road map

Toute la description doit être en YAML, avec les niveaux suivants :

 - zones : 8 zones + le milieu
   - sous-zones : des petites zones ayant une taille de quelques cases
     - tâches : un objet ponctuel, avec une descrip. On peut en avoir plusieurs sur une même case. Certaines peuvent contenir un lien vers une tâche Trello (ou pas, parce qu'on va pas se prendre la tête à connecter tout le bordel que je fous dans Trello avec la road-map).
     - spec détaillée : un lien vers un doc (sur github ou ailleurs), décrivant tout ce qu'on veut faire pour cette sous-zone.
     - une "vision"

On peut noter des tâches et des sous-zones comme "terminées".

On peut avoir des tâches, des spec et des visions directement dans la zone, sans sous-zone.

Avec ce json, on construit (automatiquement via un petit script) :
 - un document markdown, versionné dans github-doc.
 - un jeu Squarity, versionné dans github-doc aussi. On intègre directement le json dans le jeu, et c'est le code python du jeu qui le parse.
 - une page html statique avec tout le bazar dedans.
 - si possible, une image, qu'on pourra poster un peu où on veut.

Ça fait une dépendance de Squarity à github-doc, mais c'est pas grave. Si ça pète, tout le reste fonctionnera quand même. Et comme ça je met à jour plus facilement. C'est un simple commit vers github-doc.

Toutes les tâches Trello doivent rentrer dans l'une de ces 8 zones, et si possible, dans une sous-zone. Mais on ne les fait pas apparaître dans la road-map, parce que ça mettrait trop de bazar. Trop de tâches détaillées.

Le document fondateur contiendra en bas tous les liens vers tous les trucs :
 - les githubs
 - discord, mastodon
 - la roadmap en page statique, la roadmap en jeu Squarity
 - comment je vais fonctionner avec la roadmap, et que il y a les annonces dans Discord.
 - les trellos

Il faut montrer des "visions". Un écran d'exemple et un récit d'utilisation d'une feature de Squarity. Pour montrer aux personnes interessés ce que je compte faire avec cet outil. Même si c'est très résumé et très flou. Ça donnera une idée globale.

Si possible, au moins une vision par zone.

## IDE, Environnement de développement

Vision : une console en live, et de la coloration syntaxique.

Vision : timeline de debug, avec un zoom sur la timeline. Les valeurs de quelques variables. Des mini-screenshots dans la timeline montrant l'état du jeu à différentes étapes.

### Faciliter la gestion des gameconfs.

Une gameconf, c'est le texte en json (ou en yaml) définit avec le code d'un jeu. C'est ce qui définit les noms des game objects, la taille de l'aire de jeu, etc.

Le YAML a un intérêt, car il est plus human-readable, et permet d'indiquer des commentaires.

 - Détecter les erreurs de syntaxe, les afficher dans l'IDE, montrer la ligne où se trouve l'erreur.
 - Détection automatique YAML/JSON. Si il y a une accolade ou un crochet, c'est du JSON. Sinon c'est du YAML.
 - La gameconf doit être accessible dans le code du jeu. Pour récupérer la taille initiale de l'aire de jeu, et d'autres infos.
 - Au lieu de répéter les coordonnées dans le tileset, on indique une zone dans l'image (top, left, width, height), une suite de nom, et ça crée automatiquement tous les gamobj types à la suite.

### Automatiser la génération des gameconfs

Un page web avec un formulaire dans lequel on définit les valeurs.

On indique l'url de l'image de tileset, elle s'affiche, on sélectionne dedans les sprites et on les nomme, pour créer la liste des game objects.

### Faciliter le débuggage

Exécution pas-à-pas, tracking, replay, variables watch, profiling, time-line d'exécution comportant les callbacks et la situation du jeu, etc.

Essayer de core-dumper toutes les valeurs des variables python, pour avoir un état global de la mémoire au moment où a eu lieu une exception non gérée.

Tout ça est encore très flou. On le précisera en ajoutant d'autres squares de roadmap.

### Améliorer la zone de texte du gamecode

Ajout automatique d'espace en début de ligne, coloration syntaxique, multi-curseurs...

Il faut essayer de trouver quelque chose de tout fait. Les plates-formes comme CodinGame et Jupyter ont déjà toutes ces fonctionnalités.

### Ajouter une gestion des tests unitaires

Pour commencer des tests unitaires validant uniquement du code.

Et ensuite, intégrer ces tests dans le moteur du jeu. Par exemple, on donne une situation initiale, des inputs (appui sur les flèches et les boutons d'actions), et une situation finale à vérifier.

### Documenter des solutions d'IDE externe.

Documenter la technique du serveur local et du bout de javascript dans le game code qui interroge ce serveur.

Chercher des extensions de navigateur qui synchronisent un fichier texte sur le disque avec une zone de texte dans une page web. Ce qui permettra d'écrire le gamecode avec n'importe quel éditeur de texte.

### Gérer des librairies personnalisées

Lorsqu'il sera possible de se créer un compte et d'y associer des infos (images, jeux, ...)

On doit pouvoir enregistrer des fichiers de code, que l'on peut ensuite importer dans les jeux. Avec la possibilité de mettre ces libs à disposition des autres.


## Éditeur de niveaux, gestion des tilesets

Vision : une gif où on place des éléments de H2O, et ça met automatiquement les bonnes images.

Vision : construction d'un tileset en piochant des images de plusieurs tilesets existants. Certaines images sont des animations. D'autres sont toutes les possibilités de connexions d'une route.

Vision : édition d'un pack de niveaux, avec des liens entre les niveaux.

Créer un éditeur de niveaux.

Permettre de définir les niveaux dans la conf : ça permettra à des personnes qui ne codent pas de créer des niveaux dans les jeux fait par d'autres personnes. Ça veut dire aussi qu'il faut des bouts d'API pour gérer ça : start_level, is_level_ended -> (no, win, lost). Et ce serait bien que, même avec ces bouts d'API, on puisse coder un jeu principal qui ne se contente pas d'enchainer les niveaux les uns après les autres.

fonction de préparation d'un niveau (placer automatiquement des gamobjs selon certains patterns d'autres gamobjs).

pré-rendu d'une image.

enregistrement de la solution d'un niveau. pour valider qu'il est réalisable.

notion de win/loss sur un niveau. Pour passer automatiquement au niveau suivant, par exemple. Et pour avoir une touche permettant de réinitialiser le niveau (avec la fonction callback qui va bien).

Notion de score. Par exemple le nombre de mouvements, ou le nombre d'objets ramassés. La personne ayant créé le niveau donne une solution, avec un certain score. D'autres personnes peuvent trouver une solution avec un meilleur score. Le score est calculé par le code python, et renvoyé lorsque le niveau est réussi. Ça peut être un tuple. Par exemple (nb_objet_ramassés, nb_monstres_tués, -nb_mouvements_effectués)

Si on calcule des scores, soit on publie la solution qui va avec, soit il faut le valider côté serveur (et ça on sait que c'est trop compliqué pour l'instant).

Utilisation d'éditeur 2D (LDtk, mapeditor) dans le cadre de Squarity. Convertisseur automatique. Manuel d'utilisation.


## Moteur du jeu

Vision : des personnages et du texte qui apparaît par dessus, pour faire des "visual novel".

Vision : édition de pattern à la puzzlescript, pour créer un jeu.

Vision : gif animée. on clique sur un sort "create monsters", on fait un rectangle de sélection, ça crée 4 monstres qui tombent. Puis ils tournent et retombent. Et ils disent "ouch" dans une minibulle.

### Spécifier l'API et la structure des données

Une fonction on_draw() renvoyant un tableau de chaînes de caractère, c'est trop basique.

Il faut des layers. Les game objects doivent être des objets python, et non pas juste une chaîne de caractère. Ce qui permettra d'y associer d'autres infos (effet visuel, déplacement de transition) et des fonctions (move(), hide(), ...).

Des layers en mode "tableau normal" et des layers en mode "matrice creuse". L'idéal, ce serait d'avoir les mêmes fonctions pour les deux types de layers. Certains traitements sont plus optimisés pour un mode que pour l'autre.

Il faudra peut-être gérer des id numériques de layers et de game objects, pour simplifier les échanges d'infos entre le moteur Squarity et le game code.

On pourra aussi imaginer des layers spéciaux n'affichant pas de game objects, mais un effet visuel global : du brouillard, une distortion d'image, un filtre de couleur, ...

Les fonctions de callback peuvent renvoyer diverses informations, qu'il faudra structurer. On a un début de quelque chose avec le json mal foutu qui indique des actions différées. Il faut améliorer ça. Les fonctions de callback pourrait aussi renvoyer des indications de sons à jouer.

C'est le coeur du système. Il faut mettre tout ça au propre dans un document de référence, et ensuite le coder. Si possible, essayer de garder une rétro-compatibilité.

### Ajouter des game objects qui dépassent de la tile

Ca devrait se gérer assez facilement une fois qu'on aura les layers.

Dans la définition du game object, on ajoute une coordonnée de hot point, et une taille (width, height).

### Afficher du texte sous forme de bulle.

C'est un game object spécial. Au lieu de lui associer une image, on définit le texte à afficher, la couleur, la position relative de la bulle par rapport à la tile qui la génère, etc.

Si possible, un comportement par défaut dans ce game object, qui le supprime automatiquement au bout de quelques secondes.

### Rendre l'aire de jeu redimensionnable dynamiquement

Les dimensions initiales (width, height) sont définies dans la config.

Elles doivent pouvoir être changées pendant le jeu. Si c'est un jeu avec plusieurs niveaux qui s'enchaînent, ils pourraient avoir des tailles différentes.

### Réagir aux clics de souris

Une fonction de callback comme une autre, pour gérer les clics de souris.

La possibilité d'indiquer dans la gameconf, un mode de gestion spécifique des clics. On définit un game object censé être unique dans le jeu, qui serait le personnage principal. Un clic n'appelle pas la callback de clic, mais la callback d'appui sur une touche de direction. La direction est déduite des positions relatives du clic et du personnage principal.

### Implémenter un système de pattern

Inspiré par le moteur PuzzleScript.

Exemples :

 - lorsqu'il y a un objet de type "fruit" sur une case, et que la case en-dessous n'a pas d'objet de type "fruit", alors on dépace l'objet vers le bas.
 - lorsqu'il y a un objet de type H2O liquide et un objet de type "chauffage" sur la même case, alors on enlève le H2O liquide et on met un H2O gazeux.

Dans un premier temps, on implémente les patterns uniquement sous forme de fonctions dans les layers. On exécute ces patterns dans le gamecode.

Ensuite, ce serait bien d'avoir une interface spécifique dans le site, pour créer et tester les patterns. Le but serait de pouvoir créer un jeu uniquement avec les patterns, pour les personnes qui n'ont pas envie de coder.

Avec, bien sûr, du debug, du log, des tests unitaires spécifiques pour les patterns.

C'est encore très flou. On le précisera en ajoutant d'autres squares de roadmap.

### Ajouter une fonction d'export

Un jeu doit pouvoir être exporté sous forme d'un ensemble de fichiers, pour pouvoir y jouer en local.

L'export devrait ensuite permettre d'uploader le jeu sur une autre plate-forme (itch.io, ou autre).

### Exécuter le jeu dans une sandbox

Actuellement, le gamecode permet d'exécuter du javascript arbitraire sur le site. C'est un petit peu une faille de sécurité.

Il faudrait trouver le moyen d'interdire l'accès aux éléments du site. Le gamecode ne peut faire que des returns de fonctions, et modifier des variables internes.

Il faudrait auusi trouver le moyen d'empêcher d'exécuter du javascript dans le python. C'est actuellement possible avec un simple "import javascript".

### Jouer à plusieurs, à distance

Uniquement pour les jeux turn-based, et qui ne comportent pas d'actions différées. Ce serait trop compliqué de gérer des événements à synchroniser en temps réel sur plusieurs machines.

Il faudra des fonctions spécifiques dans l'API, pour indiquer la personne qui a la main. L'interface de toutes les autres personnes est alors bloquée.

### Rendre les boutons configurables

Différents mode prédéfinis :

 - flèches de direction uniquement.
 - pavé numérique, avec les 4 directions + les 4 diagonales.
 - 2 groupes de flèches de direction, pour jouer à deux sur une même machine.
 - un ou plusieurs boutons d'actions, en plus des flèches.

Si possible, configuration totalement libre. Mais ça veut dire qu'il faut pouvoir définir la disposition des boutons.

### Sauvegarder une partie

TODO : à décrire mieux.

Sauvegarder sa partie. Lier les sauvegardes au compte, pour pouvoir continuer une partie sur une autre machine.


###


Afficher des éléments d'interface : des nombres, des barres de mana, des couleurs, une mini-map, ... Mais pas trop, parce qu'il faut que ça reste simple.
Game Object affichant une valeur ou une information.
Du texte ou des nombres, pour indiquer un score, une quantité d'argent, ...
Un rectangle de taille variable, qui s'étend sur plusieurs cases, pour indiquer une barre de vie, de mana, ...
Affichage d'une quantité sous forme de camembert.
Une mini-map ? (À déterminer précisément)
Il faudra rendre ces indicateurs suffisamment configurables : taille, couleur, bord arrondi, police de caractère, ... Mais pas trop, car ça doit rester simple. Pour des indicateurs plus spécifiques, il faudra se créer ses propres game objects, et coder leur comportement directement dans le game-code.

Fonctions python helpers, classe BoardModel de base. Des classes qui gèrent des array 2D, en matrice normale et en matrice creuse.

Règles de pattern matching. On doit pouvoir faire un jeu complet rien qu'avec ces règles. À la PuzzleScript. Il faudra aussi faciliter le débuggage du super-langage de pattern qui est prévu d'ajouter mais pour lequel on n'a encore rien décidé.


Gamobj simples (pour du décor qui ne bouge pas trop) et gamobj plus compliqués, avec des fonctions associées genre move().

Réagir au clic de souris. En mode "sur une case", ou en mode "direction déduite à partir d'un gamobj spécifique".

"Gestures" pour smartphone.

client stand-alone pour jouer déconnecté.

sandboxer le jeu, car on fait de l'exécution de code arbitraire sur des navigateurs.

changer les dimensions de l'aire de jeu pendant une partie.

Jeux à deux sur un même poste.

Jeux à deux à distance (turn-based).

Sauvegarder sa partie. Lier les sauvegardes au compte, pour pouvoir continuer une partie sur une autre machine.

boutons configurables.

des layers de différents types : tableau 2D, liste d'objets avec leurs coordonnées, layers statiques qu'on n'a plus besoin de renvoyer mais qu'on peut supprimer après, ...

## "Effets spéciaux"

Vision : screenshot de drod, avec éclairage et déplacement progressif.

Vision : des effets spéciaux (éclair, explosion, distortion, ...)

Du son, de la musique. Où est-ce qu'on va stocker ces trucs ? Ça prend toujours plein de place.

Animation de transition (déplacements, rotations, shake, disparition/apparition, fade)

Objets animés. Par exemple un personnage qui marche.

Zoom/dézoom

Shaders, webGL. Mais pour l'instant j'y connais rien.

Effets de lumière, moteurs de particules.

animation globale, et animation d'un gamobj.


## Tutoriels, manuels, conseils, ...

Vision : un site genre un blog, avec des articles : "recensement des jeux de type soko-ban", "transitions entre types de terrain", "les objets squarity.layer"

Des tutoriels, texte ou vidéo.

Définir un vocabulaire spécifique : arena, tile, gamobj, sprite. Mais "gamobj" c'est pourri comme mot.

Snippets de code python pour faire une chose ou une autre.

Des articles sur des sujets de jeux vidéo (la perspective, la narration, les autres éditeurs de jeu)

CMS pour mettre tout ce bazar là-dedans. Tester SocialHome.


## Contenu et promotion

Vision : une liste avec plein de jeux comme dans Youtube. Squarenigma, Match-conquest, Footnotes, ...

Participer au Ludum Dare et à d'autres game jams.

Créer des jeux pour une personne ou une organisation spécifique, pour faire connaître Squarity.

Recenser et qualifier des tilesets

Live coding (Twitch, Youtube, ...)


## Social

Vision : un jeu, avec des avis en dessous, dont un avis de résumé. Des icônes ESRB. Une liste de sources (tileset, levels, jeux original, ...).

Vision : le profil d'une personne. Les badges gagnés. Les scores. Les jeux favoris. Les suggestions de jeux.

### Améliorer le "point d'entrée"

Une home page avec, dans l'ordre :

 - "Jouer" : liste de jeux prédéfinis.
 - "Créer des jeux" : un jeu vide pour commencer de coder, le jeu d'exemple de soko-ban, tutoriel, documentation, référence de l'API.
 - "En savoir un peu plus" : lien vers mastodon, roadmap, repo git, doc décrivant les intentions de Squarity.

Dans la page du jeu, on met juste un lien vers cette home page, et un lien vers le discord. Ca permettra de supprimer plein de petites infos qui polluent la page du jeu.

Le bouton de plein écran ne doit pas occuper toute une bande horizontale de la page, ça fait de la place perdue.

Deux onglets, un pour l'url de l'image + gameconf, un autre pour le gamecode. Par défaut, on affiche le game code. Une docstring au début du game code permet de donner une petite description du jeu.

Les personnes qui veulent juste jouer seront moins polluées par des infos secondaires. Elles ne verront que le jeu, et une zone de texte affichant une description en langage naturel. Et ça laisse quand même la possibilité d'être curieux, de scroller pour découvrir du code python, de cliquer sur l'autre onglet pour découvrir la conf, etc.

###

Création de comptes sur le site, pour enregistrer ses jeux et commenter ceux des autres.

Forker des jeux pour changer le code ou le tileset ou les niveaux.

Forum / discord / mastodon. Bref, un truc où on échange des infos.

Le même compte pour le forum et pour le site.

Curation.

Faire un résumé d'un ensemble de commentaire (avec des liens de citations).

Classer les jeux selon je-sais-pas-quoi. (Si on pouvait faire plus subtil qu'un simple nombre d'étoiles, ce serait bien)

Statistiques sur les jeux : combien l'ont testé, combien ont réussi quel niveaux, combien de temps de jeux.

Tagger les jeux avec les ratings ESRB, 18+, violence, etc.

Compte parent qui gère des comptes enfants.

Des badges, des achievements, des stats. Avec la validation côté serveur qui va avec (sécurité, exécution de code python arbitraire, etc.).

Organisation de game jams.



## Meta

Vision : une image avec une cervelle qui explose et puis c'est tout.

Documenter le projet, son architecture, les choix d'architecture et d'outils techniques.

Héberger son propre système de gestion de tâches, à la place de Trello.

Auto-formation à Vue, à Django, au CSS, etc.

Tests unitaires automatisés avec Selenium.

Héberger une instance peertube pour y mettre les démos de jeu.


Le bouton magique : "publier dans itch.io", ça va dans la catégorie "IDE, environnement de dev".
(Si tant est qu'on puisse créer un bouton magique de ce genre, car c'est pas gagné).


