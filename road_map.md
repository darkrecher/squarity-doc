# La road map de Squarity

## Fonctionnement de la road map

Ce sera des road squares.

Square map :

7:effets_spéciaux 0:moteur 1:IDE
6:tutos -1:(le milieu) 2:level_design
5:contenu_promotion 4:social 3:meta

le milieu : document "fondateur" expliquant pourquoi je fais ce jeu. Et un autre mini-document expliquant comment je vais fonctionner avec cette road map

Toute la description doit être en json, avec les niveaux suivants :

 - zones : 8 zones + le milieu
   - sous-zones : des petites zones ayant une taille de quelques cases
     - tâches : un objet ponctuel, avec une descrip. On peut en avoir plusieurs sur une même case. Certaines peuvent contenir un lien vers une tâche Trello.

Avec ce json, on construit (automatiquement via un petit script) :
 - un document markdown, versionné dans github-doc.
 - un jeu Squarity, versionné dans github-doc aussi, et le code va le chercher via une url.
 - le json en lui-même, dans github-doc. Et dans le code, on a une page web qui va le chercher pour construire la roadmap sous forme de grosse page statique
 - si possible, une image, qu'on pourra poster un peu où on veut.

Ça fait une dépendance de Squarity à github-doc, mais c'est pas grave. Si ça pète, tout le reste fonctionnera quand même. Et comme ça je met à jour plus facilement. C'est un simple commit vers github-doc.

Le document fondateur contiendra en bas tous les liens vers tous les trucs :
 - les githubs
 - discord, mastodon
 - la roadmap en page statique, la roadmap en jeu Squarity
 - comment je vais fonctionner avec la roadmap, et que il y a les annonces dans Discord.
 - les trellos


## Environnement de développement

Affichage des erreurs dans le json, en indiquant la ligne et le caractère en rouge.

Barre horizontale entre la fenêtre json et le game code, pour agrandir l'une des deux fenêtre au max.

Au lieu de répéter les coordonnées des sprites, on donne un point (x, y) de départ, une suite de nom, et ça crée tous les sprites à la suite.

Mode debug : debug, tracking, replay, variables watch, profiling.

truc à la jupyter. coloration syntaxique. tests unitaires.

binding avec un fichier texte, si il existe des extensions de nav pour ça.

debug avec le langage de pattern.

timeline d'exécution, avec les callbacks, la situation de la map, etc.


## Level design

éditeur de niveaux.

séparer les niveaux des jeux.

fonction de préparation d'un niveau (placer automatiquement des gamobjs selon certains patterns d'autres gamobjs).

pré-rendu d'une image.

enregistrement de la solution d'un niveau. pour valider qu'il est réalisable.

notion de win/loss sur un niveau. Pour passer automatiquement au niveau suivant, par exemple. Et pour avoir une touche permettant de réinitialiser le niveau (avec la fonction callback qui va bien).

Notion de score. Par exemple le nombre de mouvements, ou le nombre d'objets ramassés. La personne ayant créé le niveau donne une solution, avec un certain score. D'autres personnes peuvent trouver une solution avec un meilleur score. Le score est calculé par le code python, et renvoyé lorsque le niveau est réussi. Ça peut être un tuple. Par exemple (nb_objet_ramassés, nb_monstres_tués, -nb_mouvements_effectués)

Si on calcule des scores, soit on publie la solution qui va avec, soit il faut le valider côté serveur (et ça on sait que c'est trop compliqué pour l'instant).

Utilisation d'éditeur 2D (LDtk, mapeditor) dans le cadre de Squarity. Convertisseur automatique. Manuel d'utilisation.


## Moteur du jeu

Gamobj qui dépassent de leur tile.

Afficher du texte sous forme de bulle.

Afficher des éléments d'interface : des nombres, des barres de mana, des couleurs, une mini-map, ... Mais pas trop, parce qu'il faut que ça reste simple.

Fonctions python helpers, classe BoardModel de base.

Règles de pattern matching. On doit pouvoir faire un jeu complet rien qu'avec ces règles. À la PuzzleScript.

Gamobj simples (pour du décor qui ne bouge pas trop) et gamobj plus compliqués, avec des fonctions associées genre move().

Réagir au clic de souris. En mode "sur une case", ou en mode "direction déduite à partir d'un gamobj spécifique".

Responsive design.

"Gestures" pour smartphone.

client stand-alone pour jouer déconnecté.

sandboxer le jeu, car on fait de l'exécution de code arbitraire sur des navigateurs.

Zoom/dézoom

Jeux à deux sur un même poste.

Jeux à deux à distance (turn-based).

Sauvegarder les jeux.


## "Effets spéciaux"

Du son, de la musique. Où est-ce qu'on va stocker ces trucs ? Ça prend toujours plein de place.

Animation de transition (déplacements, shake, disparition/apparition, fade)

Objets animés. Par exemple un personnage qui marche.

Shaders, webGL. Mais pour l'instant j'y connais rien.

Effets de lumière, moteurs de particules.


## Tutoriels, manuels, conseils, ...

Des tutoriels, texte ou vidéo.

Définir un vocabulaire spécifique : arena, tile, gamobj, sprite. Mais "gamobj" c'est pourri comme mot.

Snippets de code python pour faire une chose ou une autre.

Des articles sur des sujets de jeux vidéo (la perspective, la narration, les autres éditeurs de jeu)

CMS pour mettre tout ce bazar là-dedans. Tester SocialHome.


## Contenu et promotion

Participer au Ludum Dare et à d'autres game jams.

Créer des jeux pour une personne ou une organisation spécifique, pour faire connaître Squarity.

Recenser et qualifier des tilesets

Live coding (Twitch, Youtube, ...)


## Social

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

Documenter le projet, son architecture, les choix d'architecture et d'outils techniques.

Héberger son propre système de gestion de tâches, à la place de Trello.

Auto-formation à Vue, à Django, au CSS, etc.

Tests unitaires automatisés avec Selenium.

