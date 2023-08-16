# La road map de Squarity

## Fonctionnement de la road map

Ce document regroupe les tâches de la roadmap accessible ici : https://squarity.pythonanywhere.com/roadmap. Ce sont exactement les mêmes noms de tâches et les mêmes textes détaillés. Le contenu de la roadmap sur le site web est généré à partir de ce document.

Il permet une lecture plus facile et plus linéaire, pour les personnes qui voudraient connaître le détail de toutes les tâches.

Les tâches sont regroupées en 8 catégories principales. Dans chaque catégorie, l'ordre des tâches est arbitraire et n'est pas une indication de l'ordre dans lequel elles seront réalisées.

Il y aura bientôt, sur le site et dans ce document, des gifs animés de "vision". Elles donneront un aperçu de certaines fonctionnalités de Squarity.

Bonne lecture !


## IDE, Environnement de développement

Vision : Une console en live, et de la coloration syntaxique.

### Faciliter l'écriture des gameconfs.

Une gameconf, c'est le texte en json (ou en yaml) associé à un jeu. C'est ce qui définit les noms des game objects, la taille de l'aire de jeu, etc.

Le YAML a un intérêt, car il est plus human-readable, et permet les commentaires.

Actions prévues :

 - Détecter les erreurs de syntaxe, les afficher dans l'IDE, montrer la ligne où se trouve l'erreur.
 - Déterminer automatiquement si la syntaxe est en YAML ou en JSON. Si il y a une accolade ou un crochet, c'est du JSON. Sinon c'est du YAML.
 - Rendre la gameconf accessible dans le code du jeu. Ça peut être utile, par exemple pour récupérer la taille initiale de l'aire de jeu.
 - Permettre la définition d'images "bulk". On indique une zone dans le tileset (top, left, width, height), une suite de nom, et ça crée automatiquement tous les game object types à la suite.

### Automatiser la génération des gameconfs

Un page web avec un formulaire dans lequel on définit les valeurs de config.

On indique l'url de l'image de tileset, elle s'affiche, on sélectionne des zones et on les nomme, afin de créer automatiquement la liste des game object types.

### Faciliter le débuggage

Exécution pas-à-pas, tracking, replay, variables watch, profiling, time-line d'exécution comportant les callbacks et la situation du jeu, etc.

Essayer de core-dumper toutes les valeurs des variables python, pour avoir un état global de la mémoire au moment où a eu lieu une exception non gérée.

C'est très flou pour l'instant. On le précisera en ajoutant d'autres squares de roadmap.

### Améliorer la zone de texte du gamecode

Ajout automatique d'espace en début de ligne, coloration syntaxique, multi-curseurs...

Il faut essayer de trouver quelque chose de tout fait. Les plates-formes comme CodinGame et Jupyter ont déjà toutes ces fonctionnalités.

### Vision : Timeline de debug

Timeline de debug, avec un zoom sur la timeline. Les valeurs de quelques variables. Des mini-screenshots dans la timeline montrant l'état du jeu à différentes étapes.

### Gérer des tests unitaires

On pourra commencer avec des tests unitaires validant uniquement du code.

Et ensuite, on pourra intégrer ces tests dans le moteur du jeu. Par exemple, on donne une situation initiale, des inputs (touches de flèches, boutons d'actions, clics), et une situation finale à vérifier.

### Se connecter à des IDE externes.

Techniquement, ce n'est pas trivial de connecter un navigateur web à un IDE externe. Les navigateurs ne sont pas prévus pour, et ça poserait des problèmes de sécurité. C'est tout de même possible, on le documentera avec des tutoriels.

La technique du serveur local, avec un bout de javascript dans le game code qui interroge ce serveur.

Chercher des extensions de navigateur qui synchronisent un fichier texte sur le disque avec une zone de texte dans une page web.

### Importer des librairies de code personnalisées

Ce sera possible avec les comptes utilisateurs.

On doit pouvoir enregistrer sur son compte des fichiers de code, que l'on peut ensuite importer dans les jeux. Il faudra également faciliter la mise à disposition de ces libs à d'autres personnes.


## Éditeur de niveaux, gestion des tilesets

Vision : une gif où on place des éléments de H2O, et ça met automatiquement les bonnes images. Et à côté on voit d'autres niveaux. level 1, level 2, ...

### Créer un éditeur de niveaux.

Lorsque la notion de niveau sera implémentée, on pourra créer un éditeur.

Dans la gameconf, on définit la liste des game objects du jeu qui sont plaçables avec l'éditeur.

Un éditeur permet des interactions et des collaborations : une première personne crée un jeu avec quelques niveaux, une seconde personne reprend ce jeu et y ajoute des niveaux supplémentaires, que la première personne pourra reprendre ensuite.

L'éditeur doit pouvoir exporter/importer la map d'un niveau, selon le même format de définition que la gameconf.

### Ajouter une fonction de préparation d'un niveau

Ajouter une callback "prepare_level()" dans l'API. Elle est définissable dans le gamecode comme les autres, mais n'est pas appelée pendant le déroulement d'une partie.

La fonction est appelée durant l'édition d'un niveau, à chaque modification de la map.

Elle prend en entrée la map définie par la personne créant un niveau, et renvoie en sortie des layers, contenant des game objects.

Ça permettra d'agencer automatiquement des game objects. Par exemple, avec H2O, on a juste à placer des game objects de base (murs, tunnels), et la fonction place automatiquement les dessins spécifiques, pour faire plus joli.

Cette fonction de préparation pourra aussi utiliser les patterns (voir "Implémenter un système de pattern").

### Générer une image d'aperçu de niveau

Cette image permet d'explorer et de naviguer plus facilement dans les niveaux d'un jeu. Lorsqu'on veut les tester, les sélectionner pour en faire une compilation, etc.

### Implémenter la notion de "solution"

Une solution est une suite de mouvements effectués par une personne qui joue, associé à un niveau. Elle permet de résoudre le niveau.

Tous les jeux ne peuvent pas implémenter cette notion. Il faut déjà avoir la notion de "niveau", et ne pas faire intervenir le hasard.

On peut également associer un score à une solution (nombre minimal de mouvement, nombre de fruits ramassés, ...). Mais pour cela, il faut à nouveau une fonction d'API, qui renvoie le score.

La notion de score permettra de comparer des solutions, de publier des classements, etc.

Pour aller jusqu'au bout, il faudrait valider les solutions et les scores côté serveur, sinon des personnes pourront tricher. On va laisser ça de côté pour l'instant, c'est trop compliqué et trop risqué au niveau de la sécurité.

### Associer des éditeurs 2D externes

LDtk, Tiled, ...

Il faut regarder comment ces éditeurs fonctionnent, créer des fonctions d'import/export avec Squarity et documenter leur utilisation.

C'est aussi une occasion de faire connaître Squarity auprès des gens utilisant ces éditeurs.

### Enregistrer des tilesets

Une personne ayant un compte utilisateur doit pouvoir uploader des tilesets.

Un tileset est un ensemble d'image, qui peut être ensuite utilisé dans un jeu.

Deux types de tileset :

 - mono-taille : toutes les images ont la même taille et sont des carrés.
 - multi-taille : les images peuvent avoir des tailles différentes, mais il faut spécifier un hotpoint par image.

### Gérer les tilesets plus finement

Une personne créant un tileset doit pouvoir grouper des images et qualifier ce groupe. Par exemple :

 - les 4 (ou 8) directions d'un même personnage,
 - les étapes de l'animation d'un même objet,
 - les différentes combinaisons d'une route (verticale, horizontale, tournant, croisement, ...),
 - les différentes combinaisons d'une zone étendue (de l'eau, adjacente à d'autres cases comportant de l'eau).

C'est encore assez flou, car pour l'instant, c'est difficile de voir ce qui serait faisable avec ces groupes.

On doit également pouvoir créer un nouveau tilesets en piochant des images et des groupes de tilesets différents.

### Vision : Construction d'un tileset

Construction d'un tileset en piochant des images de plusieurs tilesets existants. Certaines images sont des animations. D'autres sont toutes les possibilités de connexions d'une route.


## Moteur du jeu

Vision : gif animée. on clique sur un sort "create monsters", on fait un rectangle de sélection, ça crée 4 monstres qui tombent. Puis ils tournent et retombent. Et ils disent "ouch" dans une minibulle.

### Faire naître le moteur du jeu

Un jeu est défini par une image de tileset, sa game configuration et son game code, en python.

Le moteur récupère et affiche correctement les exceptions python durant l'exécution du jeu, ce qui permet de débugger le game code.

Le game code comporte des fonctions de callback, qui sont automatiquement appelées par le moteur, sur un appui de touche de clavier ou sur un bouton du jeu.

La situation du jeu est définie par un tableau contenant les game objects. À partir de ce tableau, le moteur construit et affiche l'image représentant la situation du jeu.

Le moteur gère également des actions différées. Les fonctions de callback peuvent renvoyer des informations indiquant au moteur qu'il doit relancer automatiquement une autre callback plus tard. Cela permet, par exemple, d'avoir un personnage qui se déplace tout seul.

Les actions différées peuvent être bloquante, ou pas. Lorsqu'elle est bloquante, les boutons du jeu sont désactivés. Une autre fonction de callback doit alors explicitement renvoyer une information de déblocage.

### Configurer la taille de l'aire de jeu

Cette taille est définie en nombre de tiles (largeur et hauteur).

La taille en pixels de l'affichage est calculée automatiquement, en fonction des tailles en nombre de tiles, et de la zone disponible dans la page web.

Les proportions sont conservées. Chaque tile est affichée sous forme d'un carré, plus ou moins grand selon la place disponible.

Pour l'instant, la taille est définissable uniquement au moment de l'exécution du jeu, via la game config.

### Spécifier l'API et la structure des données

Actuellement, la situation du jeu est définie par un simple tableau de chaînes de caractère, c'est trop basique.

Il faut des layers. Les game objects doivent être des objets python, ce qui permettra d'y associer d'autres infos (effet visuel, déplacement de transition) et des fonctions (move(), hide(), ...).

Il y a deux méthodes de stockage interne pour un layer : tableau normal ou matrice creuse. L'idéal serait d'avoir les mêmes fonctions publiques quelle que soit la méthode. Certains traitements sont plus optimisés pour une méthode que pour l'autre.

Il faudra peut-être gérer des id numériques de layers et de game objects, pour simplifier les échanges d'infos entre le moteur et le game code.

On peut aussi imaginer des layers spéciaux n'affichant pas de game objects, mais un effet visuel global : du brouillard, une distortion d'image, un filtre de couleur, ...

Il faut structurer les diverses informations que peuvent renvoyer Les fonctions de callback. Actuellement, on n'a que le json mal foutu indiquant des actions différées. Il faut améliorer ça. Les fonctions de callback pourrait aussi renvoyer des indications de sons à jouer.

C'est le cœur du système. Il faut mettre tout ça au propre dans un document de référence, et ensuite le coder. Si possible, essayer de garder la rétro-compatibilité.

### Ajouter des game objects qui dépassent de la tile

Ça devrait être assez facile une fois qu'on aura les layers.

Dans la définition du game object, on ajoute un hot point (x, y), et une taille (width, height).

### Vision : Un dialogue de visual novel

Vision : des personnages et du texte qui apparaît par dessus, pour faire des "visual novel". Avec Blondeau George Jacques Babylas dedans.

### Afficher du texte sous forme de bulle.

C'est un game object spécial. Au lieu de lui associer une image, on définit le texte à afficher, la couleur, la position relative de la bulle par rapport à la tile qui la génère, etc.

Si possible, associer un comportement par défaut à ce game object, qui le supprime automatiquement au bout de quelques secondes.

### Ajouter des game objects affichant une valeur ou une information.

Types de Game Object :

- Du texte ou des nombres, pour indiquer un score, une quantité d'argent, ...
- Un rectangle de taille variable, qui s'étend sur plusieurs cases, pour indiquer une barre de vie, de mana, ...
- Affichage d'une quantité sous forme de camembert.
- Une mini-map ? (À déterminer précisément)

Il faudra rendre ces indicateurs suffisamment configurables : taille, couleur, bord arrondi, police de caractère, ... Mais pas trop, car ça doit rester simple.

Pour des indicateurs plus spécifiques, il faudra se créer ses propres game objects, et coder leur comportement directement dans le gamecode.

### Rendre l'aire de jeu redimensionnable dynamiquement

Le nombre de tile en largeur et en hauteur doivent pouvoir être changées pendant le jeu.

Lorsque le jeu est constitué d'une succession de niveaux, ils pourraient avoir des tailles différentes.

### Réagir aux clics de souris

Une fonction de callback pour gérer les clics de souris.

Un mode de gestion spécifique des clics peut être ajouté. On définit un game object censé être unique dans le jeu, qui serait le personnage principal. Un clic n'appelle pas la callback de clic, mais la callback d'appui sur une flèche. La direction est déduite des positions relatives du clic et du personnage principal.

### Implémenter un système de pattern

Inspiré par le moteur PuzzleScript.

Exemples :

 - lorsqu'il y a un objet de type "fruit" sur une case, et que la case en-dessous n'a pas d'objet de type "fruit", alors on dépace l'objet vers le bas.
 - lorsqu'il y a un objet de type H2O liquide et un objet de type "chauffage" sur la même case, alors on enlève le H2O liquide et on met un H2O gazeux.

Dans un premier temps, on implémente les patterns sous forme de fonctions de layer, que l'on exécute dans le gamecode.

Ensuite, ce serait bien d'avoir une interface spécifique dans le site web, pour créer et tester les patterns. Le but serait de pouvoir créer un jeu uniquement avec ça, pour les personnes qui n'ont pas envie de coder.

Avec, bien sûr : du debug, du log, des tests unitaires spécifiques aux patterns, etc.

C'est encore très flou et aussi très pharaonique. Ça nécessitera d'autres squares de roadmap.

Lien vers PuzzleScript

https://www.puzzlescript.net/

### Vision : Exemples de pattern

édition de pattern à la puzzlescript, pour créer un jeu.

### Ajouter une fonction d'export

Un jeu doit pouvoir être exporté sous forme d'un ensemble de fichiers, pour pouvoir y jouer en local.

L'export devrait ensuite permettre d'uploader le jeu sur une autre plate-forme (itch.io ou autre).

### Exécuter le jeu dans une sandbox

Actuellement, le gamecode permet d'exécuter du javascript arbitraire sur le site. C'est un petit peu une faille de sécurité.

Il faudrait trouver le moyen d'interdire l'accès aux éléments du site, et empêcher d'exécuter du javascript dans le python. C'est actuellement possible avec un simple "import javascript".

Le gamecode ne doit pouvoir faire que des returns de fonctions, et modifier des variables internes.

### Jouer à plusieurs, à distance

Uniquement pour les jeux turn-based, ne comportant pas d'actions différées. Ce serait trop compliqué de gérer des événements à synchroniser en temps réel sur plusieurs machines.

Il faudra des fonctions spécifiques dans l'API, pour définir les tours de jeux. L'interface de toutes les personnes dont ce n'est pas le tour est bloquée. Bien entendu, l'API devra permettre de donner plusieurs tours de suite à une même personne, de changer le sens, etc.

### Rendre les boutons configurables

La disposition des boutons est définie par la gameconf.

Différents mode prédéfinis :

 - flèches de direction uniquement.
 - pavé numérique, avec les 4 directions + les 4 diagonales.
 - 2 groupes de flèches de direction, pour jouer à deux sur une même machine.
 - un ou plusieurs boutons d'actions, en plus des flèches.

Si possible, configuration totalement libre, mais il faut réfléchir à un format de config.

### Sauvegarder les parties

L'API doit comporter deux fonctions :

 - export_game_situation() : renvoie une grande chaîne de caractère, contenant la situation du jeu sérialisée (position des game objects, actions différées en cours, score, niveau actuel, ...)
 - import_game_situation(game_situ) : recrée la situation du jeu à partir de la grande chaîne passée en paramètre.

Dans un premier temps, ces fonctions doivent être définies par la personne qui crée le jeu. Si elles ne le sont pas : pas de sauvegarde.

Ensuite, on proposera un export/import par défaut, qui fonctionnera pour les jeux simples. Cet export/import sera activée par une info de config.

Tant que Squarity n'a pas de gestion de compte utilisateur, l'export est enregistré dans le local storage du navigateur. Lorsqu'il sera stocké dans les infos du compte, on pourra continuer sa partie sur une autre machine.

### Implémenter la notion de "niveau"

Certains jeux peuvent être découpés en niveaux (H2O, soko-ban, soko-punk). Les maps des niveaux pourraient être définies dans la config. Un niveau est constitué de layers, comportant des game objects. C'est une situation de jeu comme une autre.

L'API pourra ensuite utiliser cette notion de niveau, avec les fonctions suivantes :

 - on_init_level()
 - check_lose_level()
 - go_to_level(level_id)
 - check_win_level() -> renvoie l'identifiant du prochain niveau.

Dans un premier temps : gérer les niveaux comme dans PuzzleScript. Ils sont rangés linéairement, lorsqu'on gagne un niveau, on passe au suivant.

Si possible, une gestion comme dans le jeu Drod : les niveaux sont agencés selon un plan global, on se déplace dedans comme on le souhaite. Chaque niveau a un état "résolu/à faire". On peut les résoudre dans n'importe quel ordre, et on peut revenir à un niveau résolu.

Cette notion de niveau permet de débloquer beaucoup de fonctionnalité de la partie "Éditeur de niveaux, gestion des tilesets".

Elle permet aussi d'implémenter très facilement une sauvegarde simple de partie : il suffit d'enregistrer l'état résolu/à faire de chaque niveau, et le niveau courant. On ne peut pas enregistrer d'état intermédiaire, mais c'est déjà ça.

Pour l'instant, cette notion est un peu floue (mais moins que d'autres choses très floues).


## "Effets spéciaux"

Vision : screenshot de drod, avec éclairage et déplacement progressif. Et des morceaux de cafards qui giclent.

### Emettre des sons "blip-blop"

Les sons blip-blop ont 3 avantages :

 - un petit côté rétro qui rappelle l'époque des sons 8-bits de la NES et des PC speakers.
 - très facile à stocker, à transmettre et à éditer : une chaîne de quelques caractère suffit (associée au player qui va bien).
 - permet aux personnes non musiciennes de créer une ambiance sonore, même si ça reste basique

On pourra s'inspirer des players blip-blop existants. Il y en a dans PuzzleScript, ZZT, 3D Construction Kit... Il existe peut-être des players dédiés.

### Emettre des vrais sons

Jouer des fichiers .wav, .mp3, ...

Avec les fonctions qui vont bien : jouer une fois ou en boucle, stopper le son, ...

Le problème, c'est l'hébergement des fichiers. Un son prend plus de place que des images de tileset. Solution : limiter la taille des fichiers, permettre d'accéder à des sons accessibles publiquement depuis des hébergeurs gratuits.

### Afficher des déplacements progressifs

L'idéal serait d'indiquer dans la game config ou bien dans des directives, qu'un certain game object (ou type de game object) se déplace progressivement. Durant le jeu, on se contente de changer des coordonnées. Les déplacements progressifs se déduisent tout seul.

Ca veut dire que les game objects doivent avoir des identifiants uniques, sinon on ne peut pas retrouver lequel a bougé où.

### Transformer visuellement les game objects et les layers

Exemples de transformation : rotation, transparence, filtre de couleur, décalage X/Y, agrandissement/rétrécissement, flou, distortion, pixelisation, changement de l'image affichée, ...

Ces opérations pourraient s'appliquer sur des game objects ou des layers entiers.

### Animer les transformations visuelles

Exemples :

 - Transformation de type "hide". La transparence augmente progressivement, pour montrer la disparition d'un game object.
 - Enchainement d'images successifs, pour montrer un personnage qui marche.

Certaines animations risquent d'être plus difficile à décrire. Par exemple, un "shake" est constitué de plusieurs décalages X/Y. Il faut définir ces décalages, ou bien définir une fonction qui va les générer aléatoirement.

Ces transformations visuelles animées pourraient s'appliquer sur des game objects ou des layers entiers.

Exemple : la taille de l'aire de jeu est de 8x8 tiles. En une seule opération, on passe à 12x12 tiles, mais on applique un agrandissement sur tous les layers, de façon à n'afficher que le milieu de l'aire de jeu. Puis, on diminue progressivement l'agrandissement pour finir par afficher les 12x12 tiles. Ca fait un dézoom progressif.

Peut-être qu'on pourrait s'inspirer des mots-clés "transitions" et "transform" du CSS. Sans avoir la prétention de réimplémenter tout ce que fait le CSS...

### Ajouter des effets de lumière

Un game object, en plus de s'afficher sous forme d'une image, pourrait aussi être une source lumineuse, avec couleur, intensité, direction, etc.

Il est possible d'indiquer qu'une source lumineuse est sur un même plan que un ou plusieurs layers. Dans ce cas, les game objects de ces layers bloquent la lumière.

Ensuite, on peut indiquer, pour chaque type de game object, dans quelle mesure il laisse passer la lumière. On pourrait carrément définir des height map pour chaque game object. Une pyramide ne renvoit pas la lumière dans les mêmes directions qu'un mur.

### Vision : Pif paf boum !

Des effets spéciaux (éclair, explosion, distortion, ...)

### Utiliser du WebGL

Pour ajouter des shaders, des moteurs de particules, etc.

Fonctionnalité très floue. Il faudrait prendre connaissance de ce que peut faire le WebGL.


## Tutoriels, docs, exemples

Vision : un site genre un blog, avec des articles : "recensement des jeux de type soko-ban", "transitions entre types de terrain", "les objets squarity.layer"

### Écrire un article pour créer un mini-jeu

C'est fait. Mais il faut remettre à jour les screenshots, car le site web a un peu changé d'aspect.

Lien vers l'article.

https://github.com/darkrecher/squarity-doc/blob/master/user_manual/tutoriel_sokoban.md

### Créer des vidéos de tutoriels

La vidéo expliquera les mêmes choses que l'article de création d'un mini-jeu.

Il y a des gens qui préfèrent apprendre avec du texte, d'autres avec des vidéos, il faut essayer de toucher le plus de monde possible.

### Écrire des snippets de code

Des bouts de code et des mini-jeux, pour présenter chaque fonctionnalité de la manière la plus isolée possible.

Décrire en particulier la notion d'action différée, car pour l'instant ce n'est documenté nul part.

Ces snippets seront organisés en dépendances : "pour comprendre la fonctionalité X, il faut avoir déjà vu les fonctionnalités Y et Z".

### Rédiger des articles sur les jeux vidéo

Une pléthoritude de sujets pourraient être abordés : la perspective (vue de haut/côté/entre les deux), la narration, les codes culturels, un peu d'histoire, ...

Il faudra aussi documenter le vocabulaire spécifique des objets manipulés dans Squarity : arena, tile, game object (gamobj), sprite...

"Gamobj", est un terme un peu moche, mais il n'y a pas de meilleure idée pour l'instant.

### Traduire les tutoriels et les articles en anglais

Et si possible dans d'autres langues, si de gentilles personnes veulent bien s'y coller.


## Contenu et promotion

Vision : une liste avec plein de jeux comme dans Youtube. Squarenigma, Match-conquest, Footnotes, ...

### Participer au Ludum Dare

C'est en cours depuis 2 ans. Il s'agit d'une "tâche infinie".

Lien vers les contributions existantes.

https://ldjam.com/users/recher/games

### Créer des jeux pour une personne ou une organisation spécifique

 - Des challenges de hacking sous forme de jeu Squarity,
 - Un mini-remake de Drod,
 - Des remakes de plein d'autres jeux,
 - Des jeux "privés" (pour des anniversaires de potes, des événements),
 - Le jeu Footnotes, à révéler en temps voulu,
 - Un jeu où tous les gamobj sont des caractères UTF-8 (comme ZZT), pour lutter contre l'illetrisme,
 - ...

### Recenser et qualifier des tilesets

Un début de recensement a été fait dans la partie "Bouillonnement créatif" du serveur Discord.

Lien vers le site opengamearts.org, contenant beaucoup de jolies choses.

https://opengameart.org/

### Faire des live coding

Live coding durant les game jams, ou durant le développement de Squarity en lui-même.

Il s'agit d'une "tache infinie".

Mon compte twitch super génial.

https://www.twitch.tv/recher_squarity


## Social et site web

Vision : un jeu, avec des avis en dessous, dont un avis de résumé. Des icônes ESRB. Une liste de sources (tileset, niveaux, jeux original, ...).

### Améliorer le "point d'entrée"

Une home page avec, dans l'ordre :

 - "Jouer" : liste de jeux prédéfinis.
 - "Créer des jeux" : un jeu vide pour commencer de coder, le jeu d'exemple de soko-ban, liens vers les tutoriels, documentations et référence de l'API.
 - "En savoir un peu plus" : des liens vers mastodon, roadmap, repo git, le document décrivant les intentions de Squarity.

Dans la page du jeu, on met juste un lien vers cette home page et un lien vers le Discord. Ça supprimera plein de petites infos qui polluent la page du jeu.

Le bouton de plein écran ne doit pas occuper toute une bande horizontale de la page.

Trois onglets : url et affichage de l'image, gameconf, gamecode. Par défaut, on affiche le game code. Une docstring au début du game code permet de donner une petite description du jeu.

Les personnes qui veulent juste jouer seront moins polluées par des infos secondaires. Elles ne verront que le jeu et une zone de texte affichant une description en langage naturel. Les personnes interessées pourront scroller pour découvrir du code python, cliquer sur les autres onglets, etc.

### Utiliser correctement le nom de domaine

squarity.fr fait une redirection moche vers squarity.pythonanywhere.com. Il faut garder le nom de domaine tout le temps.

Et aussi mettre du https. Avec Letsencrypt ou quelque chose du genre.

### Gérer des comptes utilisateurs

Un compte permet d'enregistrer ses jeux, et de simplifier les urls de partage de jeux.

L'authentification pourra s'effectuer de différentes manières : classique, OAuth, Google, github, ... afin d'éviter d'embêter les gens avec un login-password supplémentaire.

C'est un peu flou pour l'instant, mais il y a sûrement des bonnes pratiques et de la doc sur le sujet.

### Vision : les infos de profil

Le profil d'une personne. Les badges gagnés. Les scores. Les jeux favoris. Les suggestions de jeux.

### Créer un mini-CMS

CMS = Content Management System.

Le but est de pouvoir écrire des articles, des tutoriels, des analyses de jeux vidéos, etc.

On le fera sans se prendre la tête, pas besoin de recréer un moteur de blog entier.

Fonctionnalités prévues :

 - rangement des articles par catégories,
 - convertisseur markdown to html,
 - moteur de recherche dans les textes des articles.

Ce sera amplement suffisant.

### Ajouter des commentaires

Les commentaires pourront être associé à un jeu ou à un article du mini-CMS.

Quelque chose d'assez simple :

 - mise en forme de texte, avec du markdown,
 - affichage d'images, qui seront hébergées ailleurs,
 - organisation arborescente, pour répondre à un commentaire par un autre commentaire,
 - permalinks.

### Faciliter les forks et les mashups de jeux

Exemple de cas d'utilisation :

Une personne crée un premier jeu, avec tous les éléments nécessaires (gamecode, tilesets, ...). Une seconde personne, qui sait mieux dessiner, forke le jeu et remplace le tileset. Une troisième personne reforke le jeu et ajoute des niveaux en plus. La première personne récupère ses éléments, crée une nouvelle version du jeu, avec des images plus jolies et plus de niveaux.

Exemple avec un jeu utilisant uniquement le système de pattern : la seconde personne forke le jeu pour y ajouter un type de game object et les patterns associés.

Les forks doivent pouvoir être traçables. Pour un jeu donné, on connait les éléments provenant de jeux précédents et les forks qui en ont découlés.

Ça n'empêchera pas des gens irrespectueux de créer un jeu non forké en copiant-collant manuellement du code ou des images, puis de prétendre que c'est eux qui ont tout fait. Techniquement c'est impossible à interdire.

### Faire de la curation de commentaires

"Curation" signifie : analyser un gros tas de données (jeux, commentaires, ...) pour garder ce qui est le plus pertinent. C'est censé être fait par des humains, même si les premiers filtrages peuvent être faits par des machines.

Une personne "curateuse" va lire des dizaines de commentaires et rédiger un récapitulatif, avec des références/citations vers les commentaires initiaux.

Une curation peut être de qualité plus ou moins bonne, ce qui signifie qu'il faudrait curater les curations. Ha ha !! Bref, c'est flou pour le moment.

Pas de curation de jeux. Pour l'instant, ce serait trop ambitieux de croire que Squarity va générer des centaines de jeux. On n'aura donc pas besoin de les classer par pertinence pour s'y retrouver.

On pourrait imaginer un système de notation, mais il faudrait trouver quelque chose de plus subtil qu'un nombre d'étoiles à choisir entre 0 et 5. Un classement a tendance a "s'auto-exagérer". Le jeu le mieux classé devient le plus joué, récolte encore plus de bonnes notes et devient de plus en plus indétrônable de la première place.

### Générer des statistiques pour les jeux

Combien de personnes ont testé le jeu, combien ont réussi quels niveaux, quel est le temps de jeu moyen.

Des statistiques par jour / semaine / mois / année.

### Gérer le contenu "choquant"

Une personne créant un jeu doit pouvoir indiquer la présence de contenu "choquant" : note ESRB, descripteur de contenu (sexe, violence, drogue, ...), limite d'âge, etc.

Une personne qui parcourt la liste des jeux (même si elle n'a pas créé de compte) doit pouvoir filtrer selon ces différentes indications.

Idée amusante : le masquage d'indicateur. Une personne choisit de ne pas filtrer un type de contenu particulier, et en plus de ne pas en être avertie. Pour les gens qui aiment se faire surprendre par une scène choquante dans un jeu sans en avoir été prévenu.

Gérer des comptes "enfants", associé à un compte parent qui décide des filtrages. C'est flou pour l'instant, car rien n'empêche l'enfant de se déconnecter et d'afficher la liste des jeux sans filtre. Peut-être que le compte parent pourrait enregistrer une liste de machines, sur lesquelles on ne pourrait plus se déconnecter du compte enfant, à moins de saisir le mot de passe du compte parent.

### Ajouter des badges et du score

Fortement inspiré de Kongregate, Steam et toutes les plate-formes de jeux.

Comme d'habitude : des fonctions en plus dans le moteur, pour que des actions spécifiques dans un jeu attribuent un badge au compte de la personne qui joue.

Les badges sont affichés sur la page de profil. On peut faire des statistiques avec (combien de personnes ont le badge, au bout de combien de temps de jeu, etc).

Même chose avec du score. Des fonctions dans le moteur permettent d'attribuer un score à une partie. On peut faire des classements, des statistiques, etc.

Le code du jeu étant exécuté par le navigateur web, il sera très facile de tricher, de s'auto-attribuer des badges et des scores très hauts. Dans un premier temps, on laissera comme ça.

Pour (beaucoup) plus tard : trouver le moyen de répliquer le déroulement d'une partie sur le serveur. C'est très flou et très compliqué à réaliser, voire risqué (exécution de code arbitraire sur un serveur).

### Permettre l'organisation de game jams

Avec un thème, une date de début, une date de fin, un classement, des petites icônes pour les jeux les mieux classés.

Le mode de classement doit être configurable : notation par les personnes participantes, jury prédéfini, basé sur des statistiques, etc.

C'est très flou. Avant de permettre les game jams, il faut une base de personnes utilisatrices plus conséquente.


## Auto-formation, Optimisation

Vision : une image avec une cervelle qui explose et puis c'est tout.

### Documenter le projet

Les choix d'architecture et d'outils utilisés, une vision d'ensemble des composants, etc.

Pour l'instant, c'est sous forme de devlogs, avec des infos notées au fur et à mesure.

On ajoutera des squares pour chaque élément de documentation important.

Lien vers les devlogs

https://github.com/darkrecher/squarity-doc/tree/master/environnement_dev

### Héberger un système de gestion de tâches

Actuellement on utilise Trello. Mais c'est tellement plus classe d'avoir les outils annexes en interne.

### Héberger une instance peertube

Pour y mettre les démos des jeux, les tutoriels vidéos, etc.

Même si on laissera des vidéos sur Youtube, parce que "tout le monde est sur Youtube".

### Mettre en place des tests unitaires

Selenium est prévu pour les tests des environnements web client. On peut automatiser des actions, des clics de boutons, etc.

### Optimiser les process

Tâche très floue pour l'instant. Lorsqu'on aura un vrai serveur avec une vraie base de donnée, il y aura sûrement beaucoup de choses à optimiser.

Webpack, déploiement automatique, dump régulier de base de données, etc.

### Auto-formation

C'est une tâche infinie, qui s'effectue au fur et à mesure des développements.

Auto-formation à Vue,au javascript, au CSS, plus tard à Django, etc.

