# Design approximatif

## Pouet

Squarity

"Créer et partager des mini jeux vidéos, en python, dans un navigateur web"

trois boutons : Jouer, Créer des jeux, Squarity ?

En bas, on met des liens vers 2 jeux.
 - sokoban V2
 - H2O


 - "Jouer" : liste des jeux existants.
   * Entangled ribbons
   * Tiny Skweek plays Breakout
   * Une émeraude cherche son ami
   * Unlimited space
   * Unstable Isotopes (on le laisse sur gist)
   * Le pseudo-jeu du sorcier
   * "Je rajouterai les autres jeux plus tard"
 - "Créer des jeux" : lien vers d'autres trucs :
   * un jeu vide pour commencer à créer
   * plein d'autres mini-jeux d'exemple qui montrent un seul truc chacun.
     * afficher un seul objet, qui ne bouge pas.
     * afficher un quadrillage immobile, printer les callbacks (start, action, click)
     * afficher deux objets, qui bougent.
     * les layers
     * le jeu d'exemple de soko-ban V2
   * Partager votre jeu
   * documentation de référence de la V2.
   * Le code python de la librairie squarity
   * ressources externes pour apprendre le python
     * doctor python (sur webarchive https://web.archive.org/web/20230130015248/https://python.doctor/ )
     * l'autre truc qu'il faut que je retrouve - https://codingforkids.io/fr/ - https://py-rates.fr/
     * https://diveintopython.org/fr
     * https://koor.developpez.com/tutoriels/python/apprendre_python_video/?page=les-bases-de-la-syntaxe-python
     * https://frederic-lang.developpez.com/tutoriels/python/python-de-zero/
     * https://courspython.com/bases-python.html
     * des bouquins en ligne, peut-être - https://wiki.python.org/moin/FrenchPythonBooks

   * --- grosse barre de séparation "Squarity V1". ---
   * doc expliquant comment choisir entre V2 et V1
   * un jeu vide en V1.
   * le jeu d'exemple de soko-ban V1
   * doc de référence de la V1 (faut ajouter les actions différées)
   * le grand tutoriel V1
 - "Squarity ?" lien vers d'autres trucs :
   * petit blabla expliquant Squarity en quelques phrases
   * mastodon
   * discord
   * roadmap
   * le document décrivant les intentions de Squarity.
   * repo git (doc et code)

Pour les mini-jeux d'exemple, un tileset avec:

 - deux tronches simples. Une verte et une bleue.
 - deux sols. Terre, briques.
 - un rond rouge transparent, comme un viseur.
 - un chapeau violet
 - une clé
 - une porte

Qu'est-ce qu'on affiche et comment ?

Si l'url contient un lien vers un jeu : on est initialement en mode "plein écran". C'est à dire que le code est masqué.

Si la fenêtre est large (la limite se situe entre les tailles "sm" et "md", comme c'est fait actuellement) :

 - on met 3 boutons, empilé verticalement, en bas à droite de la page.
 - C'est juste 3 images. Si possible, du texte apparaît à gauche quand la souris va dessus.
   * "manuel du jeu" (image de parchemin) (pas pour tout de suite)
   * "aller à la page d'accueil de Squarity" (image de Squassos, la fameuse mascotte de Squarity)
   * "afficher le code du jeu" (image d'accolades / curly brackets)
 - Les 3 boutons sont intégrées dans le bloc des boutons du jeu. Mais quand on mouse-hover dessus, le texte apparait par dessus tout le reste.

Si la fenêtre est petite :

 - on met une barre horizontale tout en bas de la page.
 - quand on clique sur cette barre, un sous-menu se déroule (par le haut), avec les 3 boutons et leur texte de mouseover.


## Re-design de la description d'un jeu

La description est définie dans le JSON (elle est optionnelle).

Elle apparaît systématiquement en bas de la page web. Il faut donc scroller pour la voir.

Pas besoin de faire des fonctionnalités pour masquer/afficher la description. Pour ne plus la voir, on scrolle.

Mais la personne qui joue ne réalise pas forcément qu'elle peut scroller pour afficher une description.

Donc on ajoute une autre fonctionnalité (activable avec la config JSON) : le gros signalement que y'a une description. Ce sera sûrement sous la forme d'une grosse flèche rouge, avec indiqué un truc du genre : "read the description".

Ou alors, les instructions, elles s'affichent à la place du code. Oui mais non, parce que sur les écrans petits, ça apparaîtra en dessous...

Non. Pas de flèche rouge à la con. On peut mettre les instructions au-dessus ou en-dessous. C'est indépendant du fait d'afficher/masquer le code. On choisit via la config.

Mode au-dessus: il y a une croix rouge pour masquer les instructions. Quand on clique dessus, ça fait "pouf" dans le bouton pour réafficher les instructions. On utilise ce mode quand il faut vraiment lire les instructions au début.

Mode en-dessous: les instructions sont en-dessous. Il faut scroller pour les voir. On ne peut pas les masquer (parce qu'on s'en fout).

Pour plus tard: on enregistre dans le local storage la liste des jeux pour lesquels on a déjà masqué les instructions. Comme ça, on les remet pas à chaque fois, pour les personnes qui jouent plusieurs fois au même jeu.

Et pour super plus tard, ce sera du markdown.


## Juste des liens, si y'a besoin pour tester

// https://squarity.pythonanywhere.com/#fetchez_githubgist_darkrecher/9f4abdcecb567b7e6d7d8abb9f2c44a0/raw/skweek-breakout.txt
// http://localhost:5173/#fetchez_githubgist_darkrecher/9f4abdcecb567b7e6d7d8abb9f2c44a0/raw/skweek-breakout.txt


## Les étapes de chargement d'un jeu.

C'est un peu compliqué à gérer.
Le chargement d'un jeu peut provenir de deux sources différentes:

1. chargement initial de la page web. Et à ce moment là, il faut tout faire.

  - définir une proportion d'aire de jeu par défaut 1:1
  - récupérer les game specs (depuis github, ou un code d'exemple)
  - parser le json, enregistrer les game specs
  - arranger certains trucs initiaux de l'interface, en fonction du json (hideCode, descriptionAbove, ...)
  - mettre la description au bon endroit, avec éventuellement le bouton associé. Récupérer les proportions de l'aire de jeu.
  - (future) : arranger d'autres trucs de l'interface. les flèches, les boutons d'actions, ...
  - arranger la taille de l'aire de jeu
  - récupérer pyodide
  - interpréter le code python
  - démarrer le jeu

2. Clic sur le bouton "Exécuter", qui est dans le composant DevZone.

  - récupérer les game specs, mais cette fois-ci depuis les zones de texte de la DevZone.
  - parser le json, enregistrer les game specs
  - mettre la description au bon endroit, avec éventuellement le bouton associé. Récupérer les proportions de l'aire de jeu.
  - (future) : arranger d'autres trucs de l'interface. les flèches, les boutons d'actions, ...
  - arranger la taille de l'aire de jeu
  - interpréter le code python
  - démarrer le jeu

Et c'est le bin's, parce que y'a des trucs qui sont dans le cas 1, mais pas dans le cas 2. Mais c'est un peu tout dispersé. En particulier : "parser le json" qui est au milieu de nul part, mais qu'il faut faire à chaque fois.

Et le déclencheur du cas 1 est dans le GameBoard, alors que le déclencheur du cas 2 est dans la DevZone. Ça non plus, ça aide pas.

C'est quand même le GameBoard qui est le gérant principal de tout le bazar. Mais c'est pas de lui que viennent les game specs. Faut faire comme on fait actuellement, mais chaque étape est dans une petite fonction du GameBoard. Et après, on a deux grosses fonctions, qui font le cas 1 et le cas 2, et qui appellent des trucs ou d'autres.


## Description et Notes

La description apparaît par-dessus le jeu, dès le départ. Elle doit être utilisé pour les jeux nécessitant obligatoirement des explications initiales. L'interface possède les boutons nécessaires pour afficher/masquer cette description. Ces boutons ne sont pas présents s'il n'y a pas de description.

Les notes apparaissent en-dessous du jeu. Il faut scroller pour les lire. Elles doivent être utilisée pour des infos facultatives (les crédits, des anecdotes, etc.). On ne peut pas afficher/masquer les notes.

Le bouton pour afficher/masquer le code est toujours présent. Mais on peut indiquer dans la config que le code peut être masqué au départ.

Tout ça est à définir dans le json de config. Clés:

```
"show_code": true,
"texts": {
  "description": "blabla bla",
  "show_desc": true,
  "notes": "bla blou",
}
```

Et plus tard, peut-être qu'on mettra des textes en plusieurs langues, et on montre le bon texte selon les params régionaux. Mais on n'en est pas là.



