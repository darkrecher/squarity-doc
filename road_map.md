# La road map de Squarity

## Fonctionnement de la road map

Ce sera des road squares.

Square map :

7:effets_spéciaux 0:moteur 1:IDE
6:tutos_doc -1:(le milieu) 2:edition_de_level_et_tileset
5:contenu_promotion 4:social 3:autoformation_optimisation_prod

Le milieu : document "fondateur" expliquant pourquoi je fais ce jeu. Et un autre mini-document expliquant comment je vais fonctionner avec cette road map

Toute la description des tâches doit être en JSON.

Les tâches peuvent être notées comme "terminées".

Avec ce json, on construit (automatiquement via un petit script) :
 - un document markdown, versionné dans github-doc.
 - une page html statique avec tout le bazar dedans.
 - si possible, une image, qu'on pourra poster un peu où on veut.

Toutes les tâches Trello doivent rentrer dans l'une de ces 8 zones. Mais on ne les fait pas apparaître dans la road-map, parce que ça mettrait trop de bazar. Trop de tâches détaillées.

Le document fondateur contiendra en bas tous les liens vers tous les trucs :
 - les githubs
 - discord, mastodon
 - la roadmap en page statique, la roadmap en jeu Squarity
 - comment je vais fonctionner avec la roadmap, et que il y a les annonces dans Discord.
 - les trellos

Il faut montrer des "visions". Un écran d'exemple et un récit d'utilisation d'une feature de Squarity. Pour montrer aux personnes interessées ce que je compte faire avec cet outil. Même si c'est très résumé et très flou. Ça donnera une idée globale.

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

Vision : édition d'un pack de niveaux, avec des liens entre les niveaux. (ou pas, parce que c'est flou).

### Créer un éditeur de niveaux.

Lorsque la notion de niveau sera implémenté, on pourra créer un éditeur.

Dans la gameconf, il faut pouvoir définir la liste des game objects du jeu qui sont plaçables avec l'éditeur.

Ça permettra des interactions et des collaborations entre les personnes créant les jeux.

Une première personne crée un jeu, avec un tileset, le game code, les game objects, et quelques niveaux. Une autre personne crée d'autres niveaux que la première pourra reprendre.

L'éditeur de niveau doit pouvoir exporter/importer la map d'un niveau, selon le même format que les niveaux définis dans la gameconf.

### Ajouter une fonction de préparation d'un niveau

Ajouter une callback prepare_level() dans l'API. Elle est définissable dans le gamecode comme les autres, mais elle n'est pas appelée pendant le déroulement d'une partie.

La fonction est appelée pendant l'édition d'un niveau, à chaque modification de la map.

Elle prend en entrée la map définie par la personne créant un niveau, et renvoie en sortie des layers, contenant des game objects.

Ça permettra, par exemple, d'agencer automatiquement des game objects pour faire plus joli. Par exemple, avec H2O, on a juste à placer des game objects de base (murs, tunnels), et la fonction place automatiquement les dessins de murs spécifiques.

Cette fonction de préparation pourra aussi utiliser les patterns (voir le square de roadmap "Implémenter un système de pattern").

### Générer une image d'aperçu pour les niveaux

Cette image d'aperçu permet d'explorer et de naviguer plus facilement dans les niveaux d'un jeu. Lorsqu'on veut les tester, les sélectionner pour en faire une compilation, etc.

### Implémenter la notion de "solution"

Une solution est une suite de mouvements effectués par une personne qui joue, associé à un niveau. Elle permet de résoudre le niveau.

Tous les jeux ne peuvent pas implémenter cette notion, il faut déjà que le jeu ait la notion de "niveau", et qu'il ne fasse jamais intervenir le hasard.

On peut également associer un score à une solution (nombre minimal de mouvement, nombre de fruits ramassés, ...). Mais pour cela, il faut à nouveau une fonction d'API, qui renvoie le score.

La notion de score permettra à des personnes de comparer leurs solutions, de publier des classements, etc.

Et pour aller jusqu'au bout, il faudrait valider les solutions et les scores côté serveur, sinon des personnes pourront tricher. Mais on va laisser ça de côté pour l'instant, c'est trop compliqué et trop risqué au niveau de la sécurité.

### Associer des éditeurs 2D externes

Exemple d'éditeur externe : LDtk, Tiled.

Il faut regarder comment ces éditeurs fonctionnent, créer des fonctions d'import/export entre eux et Squarity, documenter leur utilisation.

C'est aussi une occasion de faire connaître Squarity auprès des gens qui utilisent ces éditeurs.

### Enregistrer et gérer des tilesets

Une personne ayant un compte doit pouvoir uploader des tilesets.

Un tileset est un ensemble d'image, qui peut être ensuite utilisé dans des jeux.

Deux types de tileset :

 - "monotaille" : toutes les images ont la même taille et sont des carrés.
 - "multitaille" : les images peuvent avoir des tailles différentes, mais il faut spécifier un hotpoint par image.

### Gérer les tilesets plus finement

Une personne créant un tileset doit pouvoir regrouper des images pour une signification précise. Par exemple :

 - les 4 (ou 8) directions d'un même personnage
 - les étapes de l'animation d'un même objet
 - les différentes combinaisons d'une route (verticale, horizontale, tournant, croisement, ...)
 - les différentes combinaisons d'une zone étendue (de l'eau, adjacente à d'autres cases comportant de l'eau)

C'est encore assez flou, car pour l'instant, c'est difficile de voir ce qui serait faisable avec ces infos de regroupement.

Créer un nouveau tilesets en prenant des images provenant de tileset différents.


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

### Ajouter des game objects affichant une valeur ou une information.

Types de Game Object :

- Du texte ou des nombres, pour indiquer un score, une quantité d'argent, ...
- Un rectangle de taille variable, qui s'étend sur plusieurs cases, pour indiquer une barre de vie, de mana, ...
- Affichage d'une quantité sous forme de camembert.
- Une mini-map ? (À déterminer précisément)

Il faudra rendre ces indicateurs suffisamment configurables : taille, couleur, bord arrondi, police de caractère, ... Mais pas trop, car ça doit rester simple.

Pour des indicateurs plus spécifiques, il faudra se créer ses propres game objects, et coder leur comportement directement dans le game-code.

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

### Sauvegarder les parties

L'API doit comporter deux fonctions :

 - export_game_situation() : renvoie une grande chaîne de caractère, contenant la situation du jeu sérialisée (position des game objects, actions différées en cours, score, niveau actuel, ...)
 - import_game_situation(game_situ) : recrée la situation du jeu à partir de la grande chaîne passée en paramètre.

Dans un premier temps, ces fonctions doivent être définies par la personne qui crée le jeu. Si elles ne le sont pas : pas de sauvegarde.

Et ensuite, on propose un export/import par défaut, qui fonctionnera pour les jeux simples. Cet export/import sera activée par une info de config.

Tant que Squarity n'a pas de gestion de compte utilisateur, l'export est enregistré dans le local storage du navigateur. Et ensuite, ce sera stocké dans les infos du compte, ce qui permettra de continuer sa partie sur une autre machine.

### Implémenter la notion de "niveau"

Certains jeux peuvent être découpés en niveaux (par exemple : H2O, soko-ban, soko-punk). On doit pouvoir définir les maps des niveaux dans la config. Un niveau est constitué de layers, comportant des game objects (c'est une situation de jeu comme une autre).

L'API pourra ensuite utiliser cette notion de niveau, avec les fonctions suivantes :

 - on_init_level()
 - check_lose_level()
 - go_to_level(level_id)
 - check_win_level() -> renvoie l'identifiant du prochain niveau.

Dans un premier temps : gérer les niveaux comme dans PuzzleScript. Ils sont rangés linéairement, lorsqu'on gagne un niveau, on passe au suivant.

Si possible : permettre une gestion comme dans le jeu Drod : les niveaux sont agencés selon un plan global, on se déplace dedans comme on le souhaite. Chaque niveau a un état résolu/à faire. On peut les résoudre dans n'importe quel ordre, et on peut revenir à un niveau résolu.

Cette notion de niveau permet de débloquer beaucoup de fonctionnalité de la partie "Éditeur de niveaux, gestion des tilesets".

Elle permet aussi d'implémenter très facilement une fonctionnalité de sauvegarde de partie : il suffit d'enregistrer l'état résolu/à faire de chaque niveau, et le niveau courant. On ne peut pas enregistrer d'état intermédiaire dans un niveau, mais c'est déjà ça.

C'est encore un peu flou (mais moins que d'autres choses très floues).


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


## Social et site web

Vision : un jeu, avec des avis en dessous, dont un avis de résumé. Des icônes ESRB. Une liste de sources (tileset, niveaux, jeux original, ...).

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

### Utiliser correctement le nom de domaine

squarity.fr fait une redirection moche vers squarity.pythonanywhere.com. Il faut garder le nom de domaine tout le temps.

Et aussi mettre du https. Avec Letsencrypt, ou quelque chose du genre.

### Gérer des comptes utilisateurs

Une personne crée un compte sur le site, pour enregistrer ses jeux (la gameconf, le gamecode, l'image de tileset).

Authentification classique / OAuth / Google / github / autre. Pour éviter d'embêter des gens avec un login-password supplémentaire.

Un peu flou pour l'instant, mais il y a sûrement des bonnes pratiques et de la doc sur le sujet.

### Créer un mini-CMS

Content Management System.

Le but est de pouvoir écrire des articles, des tutoriels, des analyses de jeux vidéos, etc.

Sans prise de tête. On ne va pas recréer tout un moteur de blog.

 - ranger les articles par catégories,
 - convertisseur markdown to html,
 - un petit moteur de recherche de texte.

Ce sera amplement suffisant.

### Ajouter des commentaires

Les commentaires pourront être associé à un jeu ou à un article du mini-CMS.

Quelque chose de basique, mais avec un peu de fonctionnalité quand même :

 - mise en forme de texte, avec du markdown,
 - affichage d'images (qui seront hébergées ailleurs),
 - organisation arborescente (un commentaire de réponse à un autre commentaire),
 - permalinks.

### Faciliter les forks et les mashups de jeux

Exemple de cas d'utilisation :

Une personne crée un premier jeu, avec tous les éléments nécessaires (gamecode, tilesets, ...). Une seconde personne, qui sait mieux dessiner, forke le jeu, et remplace le tileset. Une troisième personne reforke le jeu et ajoute des niveaux en plus. La première personne récupère ses éléments, et crée une nouvelle version du jeu, avec des images plus jolies et plus de niveaux.

On pourrait avoir un autre exemple avec un jeu utilisant uniquement le système de pattern (pas de gamecode). Une autre personne forke le jeu, rajoute un type de game object et les patterns associés.

Les forks doivent pouvoir être traçable. Pour un jeu donné, on peut voir tous les éléments (pattern, tileset, etc.) provenant de jeux précédents, et on peut aussi voir tous les forks qui ont été fait à partir de ce jeu.

Ça n'empêchera pas des gens irrespectueux de copier-coller manuellement du code ou des images, puis de créer ensuite un nouveau jeu non forké, en disant que c'est eux qui ont tout fait, mais ça c'est difficilement gérable.

### Faire de la curation de commentaires

Si j'ai bien compris le terme, "curation" signifie : analyser un gros tas de données (des jeux, des commentaires ou autres), et ne garder que les plus pertinents. C'est censé être fait par des humains, même si les premiers filtrages peuvent être faits par des machines.

Une personne "curateuse" va lire des dizaines de commentaires, et rédiger un seul commentaire récapitulatif, avec des références/citations vers les commentaires initiaux.

Une curation peut être de plus ou moins bonne qualité, ce qui signifie qu'il faudrait curater les curations. Ha ha ha !!

Bref, c'est un peu flou pour le moment.

Pas de curation de jeux, car pour l'instant, ce serait trop ambitieux de dire qu'il y aura beaucoup de jeux créés avec Squarity. On ne devrait pas avoir besoin de les classer par pertinence pour s'y retrouver.

On pourrait imaginer un système pour noter les jeux, mais il faudrait trouver quelque chose de plus subtil qu'un nombre d'étoiles à choisir entre 0 et 5. Un classement a tendance a "s'auto-exagérer". Le jeu le plus classé devient le jeu le plus joué, il récolte encore plus de bonnes notes, et devient de plus en plus indétrônable de la première place.

### Générer des statistiques pour les jeux

Combien de personnes ont testé le jeu, combien ont réussi quels niveaux, temps de jeu moyen.

Tout ça par jour / semaine / mois / année.

### Gérer le contenu "choquant"

Une personne créant un jeu doit pouvoir indiquer la présence de contenu "choquant" : note ESRB, descripteur de contenu (sexe, violence, drogue, ...), limite d'âge, etc.

Une personne qui parcourt la liste des jeux (même si elle n'a pas créé de compte) doit pouvoir filtrer selon ces différentes indications.

Truc amusant : le masquage d'indicateur. Pour un descripteur de contenu, non seulement on le filtre pas, mais en plus on n'affiche pas que le jeu possède ce contenu. Pour les personnes qui aiment se faire surprendre par une scène choquante dans un jeu alors qu'elles ne s'y attendent pas.

Gérer des comptes "enfants". Le compte est associé à un compte parent, qui décide des filtrages. C'est flou pour l'instant, car rien n'empêche l'enfant de se déconnecter et d'afficher la liste des jeux sans filtre. Peut-être que le compte parent pourrait enregistrer une liste de machines accessible par l'enfant, sur lesquelles on ne pourrait plus se déconnecter du compte enfant, à moins de saisir le mot de passe du compte parent.

### Ajouter des badges et du score

Fortement inspiré de Kongregate, Steam, et toutes les autres plate-formes de jeux.

Comme d'habitude : des fonctions en plus dans l'API, pour que des actions spécifiques dans un jeu attribuent un badge au compte de la personne qui joue.

On affiche les badges sur le profil de la personne. Et on peut faire un peu de statistiques dessus (combien de personnes ont le badge, au bout de combien de temps de jeu, etc).

Même chose avec du score. Des fonctions dans l'API permettent de donner un score à une partie jouée. Les scores sont enregistrés dans les comptes utilisateurs, on peut faire des classements, des statistiques, etc.

Comme le code du jeu est exécuté par le navigateur web, il sera très facile de tricher, de s'auto-attribuer des badges et des scores très haut. Dans un premier temps, on laissera comme ça.

Pour plus tard : il faudra réfléchir à répliquer le déroulement d'une partie sur le serveur. C'est une idée très floue, assez compliquée à réaliser, voire risquée (exécution de code arbitraire sur un serveur). Donc ce sera vraiment pour plus tard.

### Permettre l'organisation de game jams

Avec un thème, une date de début, une date de fin, un classement, des petites icônes pour indiquer les jeux qui sont arrivés les premiers.

Le mode de classement est à définir, il peut y en avoir plusieurs : notation par les personnes participant au game jam, jury prédéfini, etc.

Est-ce qu'on met ensemble le classement normal sur le site et les classement de game jam, ou est-ce qu'on sépare ?

C'est très flou, et avant de permettre les game jams, il faut une base de personnes utilisatrices un peu plus conséquente que ce qu'on a maintenant.


## Meta

Vision : une image avec une cervelle qui explose et puis c'est tout.

Documenter le projet, son architecture, les choix d'architecture et d'outils techniques.

Héberger son propre système de gestion de tâches, à la place de Trello.

Auto-formation à Vue, à Django, au CSS, etc.

Tests unitaires automatisés avec Selenium.

Héberger une instance peertube pour y mettre les démos de jeu.



