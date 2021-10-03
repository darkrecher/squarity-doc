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
     - spec détaillée : un lien vers un doc (sur github ou ailleurs), décrivant tout ce qu'on veut faire pour cette sous-zone.
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

Vision : une console en live, et de la coloration syntaxique.

Vision : timeline de debug, avec un zoom sur la timeline. Les valeurs de quelques variables. Des mini-screenshots dans la timeline montrant l'état du jeu à différentes étapes.

Détecter les erreurs de la config json/yaml
 - Afficher le message catché par-dessus l'aire de jeu
 - Montrer la ligne d'erreur dans la config
 - Détecter et proposer des corrections : On ajoute une virgule ou un guillemet à l'endroit de l'erreur, on teste si ça fait un texte valide, si oui on propose la correction.

Permettre une config écrite en YAML : c'est un peu plus human-readable, et on peut mettre des commentaires. Ça veut dire que dans les gists, faudra indiquer quelque part si c'est du YAML ou du JSON. Ou alors on l'auto-détecte à la bourrin.

Améliorer la page web
 - Placer une slide-bar horizontale entre la conf et le game code : pour partager comme on veut l'espace entre les deux fenêtres.
 - Ajouter un bouton pour maximiser l'espace conf et l'espace game code.

Faciliter le débuggage : exécution pas-à-pas, tracking, replay, variables watch, profiling, time-line d'exécution, avec les callbacks, la situation du jeu, etc. Tout cela est encore très flou. Il faudra aussi faciliter le débuggage du super-langage de pattern qui est prévu d'ajouter mais pour lequel on n'a encore rien décidé.

Améliorer la fenêtre de code : ajout automatique d'espace en début de ligne, coloration syntaxique, multi-curseurs. Il faut essayer de trouver quelque chose de tout fait. Et s'inspirer de CodinGame, Jupyter et autres plate-formes.

Ajouter un framework de test unitaire : des tests unitaires de code pur, mais aussi du jeu. Simulation d'inputs, vérification du résultat affiché dans le jeu.

Documenter des solutions pour utiliser un IDE externe.
 - documenter la technique du serveur local et du bout de javascript dans le game code qui interroge ce serveur.
 - chercher des extensions de nav qui associent fichier texte - zone de texte.

Faciliter le stockage du game code
 - Permettre l'importation de libs de code stockées dans un github : on indique l'adresse du répertoire ou des fichiers dans le github, puis on importe. Je ne sais pas si on peut faire une instruction "import", ou si on les prend directement.
 - Aller chercher le code principal sur un github : en plus des gists.
 - Aller chercher le code principal sur un pastebin : pastebin est relou à cause des CORS. Faudra trouver un moyen d'arranger ça. C'est le serveur qui fera la requête.
 - Ajouter un bouton pour reloader l'image et les libs de code.

Voir si on peut core-dumper toutes les valeurs des variables python, pour avoir un état global de la mémoire au moment où a eu lieu une exception non gérée.

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

Vision : gif animée. on clique sur un sort "create monsters", on fait un rectangle de sélection, ça crée 4 monstres qui tombent. Puis ils tournent et retombent. Et ils disent "ouch" dans une minibulle.

Pour la config : au lieu de répéter les coordonnées des sprites, on donne un point (x, y) de départ, une suite de nom, et ça crée tous les sprites à la suite.

Gamobj qui dépassent de leur tile.

Afficher du texte sous forme de bulle.

Afficher des éléments d'interface : des nombres, des barres de mana, des couleurs, une mini-map, ... Mais pas trop, parce qu'il faut que ça reste simple.

Fonctions python helpers, classe BoardModel de base. Des classes qui gèrent des array 2D, en matrice normale et en matrice creuse.

Règles de pattern matching. On doit pouvoir faire un jeu complet rien qu'avec ces règles. À la PuzzleScript.

Gamobj simples (pour du décor qui ne bouge pas trop) et gamobj plus compliqués, avec des fonctions associées genre move().

Réagir au clic de souris. En mode "sur une case", ou en mode "direction déduite à partir d'un gamobj spécifique".

"Gestures" pour smartphone.

client stand-alone pour jouer déconnecté.

sandboxer le jeu, car on fait de l'exécution de code arbitraire sur des navigateurs.

Zoom/dézoom

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


