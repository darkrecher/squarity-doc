# Design approximatif

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
     * afficher deux objets placés en diagonale, qui bougent.
   * le jeu d'exemple de soko-ban V2
   * documentation de référence de la V2.
   * --- grosse barre de séparation "Squarity V1". ---
   * doc expliquant comment choisir entre V2 et V1
   * un jeu vide en V1.
   * le jeu d'exemple de soko-ban V1
   * les 2 tutoriels V1
 - "Squarity ?" lien vers d'autres trucs :
   * petit blabla expliquant Squarity en quelques phrases
   * mastodon
   * discord
   * roadmap
   * repo git (doc et code)
   * le document décrivant les intentions de Squarity.


Qu'est-ce qu'on affiche et comment ?

Si l'url contient un lien vers un jeu : on est initialement en mode "plein écran". C'est à dire que le code est masqué.

Si la fenêtre est large (la limite se situe entre les tailles "sm" et "md", comme c'est fait actuellement) :

 - on met 3 boutons, empilé verticalement, en bas à droite de la page.
 - C'est juste 3 images. Si possible, du texte apparaît à gauche quand la souris va dessus.
   * "manuel du jeu" (image de parchemin) (pas pour tout de suite)
   * "aller à la page d'accueil de Squarity" (image de Squassos, la fameuse mascotte de Squarity)
   * "afficher le code du jeu" (image d'accolades / curly brackets)

Si la fenêtre est petite :

 - on met une barre verticale en haut de la page, qui prend toute la largeur, mais qui n'a que quelques pixels de haut.
 - quand on clique sur cette barre, un sous-menu se déroule, avec les 3 boutons et le texte.




