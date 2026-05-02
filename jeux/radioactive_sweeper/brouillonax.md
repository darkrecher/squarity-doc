# Brouillon en vrac

## Idée pour le prochain jeu


Genre Dungeon Sweeper, mais juste avec des couleurs.


Il y a des tonneaux radioactifs à enlever. Ils fuient de différentes manières, ce qui permet de détecter la radioactivité sur différentes cases. Mais ça s'additionne, donc des fois on sait pas trop où c'est.

Lorsqu'on révèle une case, on voit la radioactivité dessus.

Si on révèle une case contenant un tonneau, on crève direct.

On peut acheter des "bouclier". Un type de bouclier par tonneau.

Si on active un bouclier avant de révéler une case contenant un tonneau, on ne meurt pas, le bouclier est utilisé, le tonneau est supprimé.

Si on active un bouclier et qu'on révèle une case ne contenant pas de tonneau, le bouclier est utilisé. Dommage !

Et après, on peut imaginer d'autres bonus : scan d'une zone précise, etc.



Exemple.


Les tonneaux radioactifs jaunes fuient de cette manière.

      1
      2
    3 3 3
1 2 3 J 3 2 1
    3 3 3
      2
      1

Si on en met plusieurs, ça donne ceci :

1
2
3 3       1
J 3 2 1   2
3 3   1 3 3 3
2   1 4 3 J 3 2 1
1   3 3 6 3 3
1 2 3 J 3 4 1
    3 3 3 1
      2
      1

Il y a des tonneaux qui font d'autres patterns : diagonale, quadrillage, dans une seule direction, ...

Et peut-être qu'on peut construire/poser des trucs sur des zones étendus et non radioactives : un détecteur spécifique, une machine à fabriquer de l'argent, une boutique, etc.

Les tonneaux verts fuient comme ça :

1           1
  2       2
    3 3 3
    3 G 3
    3 3 3
  2       2
1           1

Les tonneaux violets fuient comme ça :

1   1   1   1
  1   1   1
1   3 3 3   1
  1 3 V 3 1
1   3 3 3   1
  1   1   1
1   1   1   1

Lorsqu'on révèle une case, on a la somme, et les couleurs présentes, mais on sait pas le détail.

Exemple :

    1
    2
  3 3 3
2 3 J 3 2 1
1 3 3 3     1
  2 2     2
    4 3 3
    3 G 3
    3 3 3
  2       2
1           1

Dans la disposition ci-dessus, il y a une case avec 4. On sait qu'il y a du jaune et du violet dans cette case. Mais on ne sait pas que c'est 3 violet + 1 jaune.

Et on pourrait même imaginer, dans des niveaux plus haut, de n'avoir que l'info "4". On sait pas de quelles couleurs il est composé. Et il faut un équipement spécial pour le décomposer.

À tester, voir si c'est intéressant...

On change cette histoire de bouclier.

Pour enlever un tonneau, il faut révéler toutes les cases autour de lui, puis poser un désactivateur (ou pas, si c'est relou de le faire à chaque fois).

Du coup, on peut pas enlever un tonneau adjacent à un autre tonneau. Les boucliers peuvent être posé sur une case adjacente à un tonneau, sans la révéler.

Un tonneau dont toutes les cases adjacentes sont, soit révélées, soit avec un bouclier, peut être enlevé.

Les boucliers sont réutilisables.

On a besoin, au max, de 3 boucliers en même temps.

Exemple:

. . . . .
V V V V .
V V V V .
V V V V .
. . . . .

On commence par enlever ceux des coins.

Les cases peuvent donner, comme bonus : de l'argent, du "scrap", des échantillons radioactifs (quand on enlève un tonneau).

Objets à acheter/débloquer :

 - convertisseur scrap->argent.
 - boucliers.
 - détecteur directionnel/distanciel de cases contenant des gros tas d'argent. (on peut les déplacer)
 - indicateur de couleurs (ils ont une portée limitée).
 - connexion entre indicateur de couleurs (ça augmente leur portée, jusqu'à pouvoir couvrir toute l'aire de jeu).
 - indicateur du nombre total de tonneau d'une couleur précise.
 - upgrade de l'indicateur du nombre total de tonneau, pour indiquer le nombre de chaque type.
 - indicateur de la case la plus proche ayant une radioactivité supérieure à 5 ? Je sais pas si c'est utile.
 - indicateur de où exactement se trouve un tonneau, à partir d'une case ayant de la radioactivité lui appartenant. (très pratique, mais très cher).
 - kamikaze qui révèle une case et enlève le tonneau qu'il y a dessus, sans que ça fasse perdre le jeu.

Les bâtiments :

 - constructeur pour acheter la boutique, le convertisseur scrap, indicateur de couleurs, connexions, centre de recherche.
 - boutique pour acheter les boucliers, indicateur d'argent, indicateur de tonneau, kamikaze, réparation du désactivateur.
 - centre de recherche pour les indicateur de nombre total et leurs upgrades ? Et peut-être les boucliers aussi.


Peut-être que les boucliers, il faut qu'ils correspondent à la couleur du tonneau sur lequel on le pose ? Et si c'est pas bon, ça pète quand on essaie d'enlever le tonneau au milieu. Comme ça, faut en acheter plus. Parce que là, pour l'instant, il y a pas grand chose à acheter, donc ça a peu d'intérêt d'amasser de l'argent.

Est-ce qu'il faudrait acheter les désactivateurs ? Genre au bout de 5 utilisations, il pète, faut le réparer.



On double toute les valeurs, et on met 2 type de tonneaux par couleur.

Courte portée :

      2
      4
    6 6 6
2 4 6 J 6 4 2
    6 6 6
      4
      2

Longue portée :

            1
            2
            3
            4
            5
          6 6 6
1 2 3 4 5 6 J 6 5 4 3 2 1
          6 6 6
            5
            4
            3
            2
            1

Baril violet à courte portée :

1 . 1 . 1 . 1
. 2 . 2 . 2 .
1 . 6 6 6 . 1
. 2 6 V 6 2 .
1 . 6 6 6 . 1
. 2 . 2 . 2 .
1 . 1 . 1 . 1

longue portée :

1 . 1 . 1 . 1 . 1 . 1
. 1 . 1 . 1 . 1 . 1 .
1 . 2 . 2 . 2 . 2 . 1
. 1 . 2 . 2 . 2 . 1 .
1 . 2 . 6 6 6 . 2 . 1
. 1 . 2 6 V 6 2 . 1 .
1 . 2 . 6 6 6 . 2 . 1
. 1 . 2 . 2 . 2 . 1 .
1 . 2 . 2 . 2 . 2 . 1
. 1 . 1 . 1 . 1 . 1 .
1 . 1 . 1 . 1 . 1 . 1

As-t-on besoin des barils à longue portée ? Y'a déjà suffisamment de trucs à faire avec les 3 couleurs en courte portée.

Autre bonus possible : un truc qui indique la direction des radioactivités jaune et violette. (Les vertes, y'a pas vraiment de direction).

Sans oublier le bonus de pouvoir annoter des cases.


au début, quand il y a trop de points sur une case, on voit juste marqué "MAX". Et on peut acheter des trucs pour augmenter le max.

On oublie cette histoire de scrap, car ça complique pour pas grand-chose. Il y a des cases avec beaucoup d'argent, et des cases avec peu d'argent.

Les détecteurs d'argent peuvent être configurés pour repérer les cases avec des grosses ou des petites quantités d'argent. Ou alors, c'est des détecteurs différents.

Pas d'interface. L'interface se fait avec les objets qu'on a posés dans l'aire de jeu.

Par exemple, le dôme de désactivation, il est dans l'aire de jeu. On clique dessus pour dire qu'on veut le placer quelque part pour désactiver un tonneau. Et ensuite, il revient à sa place tout seul. Mais y'a pas d'option "poser le dôme".

Au passage, il faut un dôme de désactivation par couleur de tonneau. Comme ça, ça fait plus de trucs à acheter. Mais on va dire que ces dômes ne s'usent pas. Parce que c'est chiant.


On achète les boucliers (qui ont des couleurs spécifiques). Ils sont de plus en plus chers.

Au départ, ils ne servent qu'une seule fois. Mais on peut acheter une "assurance de bouclier" (qui coûtent pas très cher) (une assurance pour chaque couleur).

L'assurance te redonne automatiquement un bouclier si tu en utilises un et que c'est justifié. Sinon, c'est perdu. Faut racheter un bouclier (et une assurance, aussi).

Si on met une mauvaise couleur de bouclier, ça le casse et l'assurance le rembourse pas.

C'est bizarre, cette histoire de bouclier. J'arrive pas à le justifier comme il faut.

Ou alors, c'est l'inverse. On met des trucs sur les cases vides autour et faut mettre un minimum de trucs. Donc y'aurait pas de bouclier du tout. Mais des dômes de désactivation qui ont besoin de plus ou moins de cases vide autour d'eux.

On récupère plus ou moins d'argent selon le type de dôme qu'on utilise.

Du coup, si j'ai la flemme, j'utilise des dômes plus performant, au lieu de m'embêter à trouver précisement les cases vides autour d'un tonneau. C'est pas top, mais pourquoi pas.

Et on ajoute des étoiles pour noter la réussite d'un niveau. Si on utilise des dômes performants là où c'est pas nécessaire, on n'a pas toutes les étoiles.

Quelles seraient les autres moyens de noter la réussite d'un niveau ?

 - avoir plus ou moins d'argent à la fin. Mais j'aime pas trop cette idée, car ça donne pas envie de dépenser son argent pour acheter des équipements cools, durant une partie. Ou sinon, on ajoute un équipement spécifique, qui coûte assez cher, qui sert à rien, mais qui apporte une étoile à la fin.



Un mini-dôme de désactivation, qui doit être connecté à une "safe place" (une case sans aucune radioactivité, avec un chemin vers le point de départ).

Est-ce qu'on veut obliger la personne qui joue à connaître complètement les 8 cases autour d'un barril pour le désactiver ? Ce serait bien que oui, mais peut-être c'est trop compliqué.

-------
|...XX|
|..XXX|
|.XXXX|
-------

-------
|.XXXX|
|.XXXX|
|.XXXX|
-------


C'est peut-être pas une très bonne idée cette connexion obligatoire. Un mécanisme intéressant, ce serait d'obliger la personne à découvrir le schéma global d'un ensemble de baril, pour enlever ceux du milieu d'abord, et maximiser le nombre de baril isolés, afin de les désactiver avec un dôme classique.

Exemple, il y a trois baril alignés comme ça :

.....
.XXX.
.....

Si on découvre ce schéma entièrement, on peut décider d'enlever celui du milieu par le procédé restant à déterminer. Ensuite on enlève les deux autres avec un dôme classique.

Ça devrait rapporter plus que d'enlever le baril de gauche, puis celui du milieu, puis le dernier avec un dôme classique.

Quel devrait donc être ce fameux procédé ?

Juste deux autres types de dôme, un avec une forme comme ça:

DDD
.X.

Et un avec une forme comme ça :

DD
DX

(que l'on peut tourner, évidemment)

Et on peut aussi avoir un dôme comme ça :

DDD
DXD

qui rapporte un peu d'argent, mais moins que le dôme classique.

Et en même temps, ça règle le problème des barils placés sur les bords et les coins de l'aire de jeu.

Et y'a pas besoin de boucliers, ni d'assurance de boucliers.

Ça force pas la personne à connaître toutes les cases autour d'un baril, mais ça l'encourage à connaître globalement un ensemble, pour l'attaquer au mieux. Et ça l'encourage à réfléchir comment optimiser l'utilisation des dômes classiques, dans le cas de schéma vraiment complexes.

Allez, hop, adjugé vendu, on fait comme ça !!

Et y'aura un dôme par couleur de baril. Donc faut au moins connaître le baril que l'on veut désactiver.

Et maintenant, comment on peut avoir une évaluation, pour donner un nombre d'étoiles ? (Réponse: voir plus loin, y'a un chapitre pour ça)

Les cases où y'avait un baril ne révèlent pas leurs infos (force, couleur), même une fois que le baril est éliminé. Sinon, c'est super facile, on attaque les bords petit à petit, et voilà.

Tous les éléments à poser dans l'aire de jeu doivent l'être dans la zone "conquise". (voir chapitre "trucs automatique")

Par défaut, les éléments à poser sont non déplaçable, sauf indication contraire.

Trucs qu'on peut acheter :
 - boutique où on peut acheter tout le reste (on l'a déjà au départ). 2*2.
 - indicateur du nombre d'éprouvette à obtenir avoir une autre étoile. (on l'a déjà au départ). 1*1.
 - point d'interrogation de tutoriel. Lorsqu'on clique dessus, un objet de curseur de souris se déplace et indique successivement les endroits où il faut cliquer. (on l'a au départ). 1*1.
 - séparateur de couleurs (portée de 15 cases). Les cases révélées indique la quantité de radioactivité, et les couleurs qui la composent (sans qu'on ait le détail). 2*2.
 - augmentation du seuil max d'affichage de radioactivité (c'est pas un élément à poser, on l'achète et c'est tout). Ou alors c'est un élément 1*1.
 - compteur du nombre total de baril, upgradable en détaillant les couleurs, puis en détaillant les portées. 6*6. (Est-ce qu'on a vraiment besoin de ce truc ? bof...)
 - emplacement de dôme de désactivation (ils sont de plus en plus chers). 3*3.
 - dôme de désactivation, achetable à partir d'un emplacement de dôme, voire gratuit. 0*0.
 - maison très chère, pour avoir une étoile. 6*6.
 - convertisseur éprouvette -> argent. 1 pour 1, et 4 argents pour 3 éprouvettes de couleur différentes.
 - révélateur automatique de case non-radioactive, qui sont adjacentes à une case révélée et non-radioactive. (Comme dans le démineur initial). 2*2. (upgrade de Quality Of Life). Si on l'achète, on ne peut plus acheter la maison. Mais on peut acheter d'abord la maison et ensuite le révélateur.
 - nettoyeur de baril désactivé. Permet de révéler les infos d'une case qui contenait un baril éliminé. Ça coûte de plus en plus cher. 2*2.
 - truc qui donne de l'argent par rapport au nombre d'étoiles possédées. 1*1. (ne coûte vraiment pas cher).
 - marqueur de case (drapeaux), avec les 3 couleurs (Quality Of Life). 3*2.
 - indicateur, directement dans le jeu, combien on a d'argent et d'éprouvettes. 4*2. (upgrade de Quality Of Life)

Le convertisseur d'éprouvette vers argent, et l'indicateur de combien on en a, pourrait être la même construction. Pour éviter de multiplier les trucs et les machins.

Dans les niveaux les plus durs, on peut mettre systématiquement un tonneau de chaque couleur dans chaque coin. Pour forcer à acheter les dômes de désactivation de coin. Pareil avec les bords. Ah ouais, ça claque, comme idée!!

À voir si ça ajoute de l'intérêt : les barils désactivés ne rapportent pas directement de l'argent, mais des éprouvettes de liquide radioactif. 3 couleur d'éprouvette, comme les couleurs de baril. Certains éléments à acheter nécessitent des éprouvettes de n'importe quelle couleur, ou bien des éprouvette de couleurs spécifique.

On ajoute également un élément achetable : convertisseur d'éprouvette en argent. On peut les vendre une par une, ou bien 3 d'un coup, de 3 couleurs différentes, et ça rapporte plus. Et on peut ajouter une upgrade de quality of life : convertisseur automatique de 3 éprouvette différentes en argent. À acheter quand on n'a plus rien d'autre à acheter avec les éprouvettes.

Il faut une grosse pénalisation si on pose un dome sur une case qui ne contient pas de baril. Et je vois pas comment le justifier. Mais il faut. Sinon les gens vont essayer "juste au cas où". Si c'est un baril de la mauvaise couleur, il explose et on perd la partie. C'est facile à justifier. Mais si y'a rien ?

Le dôme explose. On perd un emplacement de dôme. Il faut en racheter un (alors que ça coûte de plus en plus cher), et il faut aussi racheter un dôme. Ou alors, non, faut juste payer un nettoyage de l'emplacement. Mais ça coûte cher. Et on perd l'étoile de base.

Lorsque la zone conquise se propage sur un baril désactivé, on enlève le baril. C'est un nettoyage automatique. Et du coup, ça révèle les barils qui masque une radioactivité de 0. C'est bizarre, mais c'est une mécanique intéressante.

As-t-on vraiment besoin de la notion de "safe zone" ? Peut-être pas. On peut juste contrôler que tous les éléments posés dans le jeu le sont sur des cases qui n'ont aucune radioactivité. On garde, bien entendu, l'upgrade de révélateur automatique de cases à côté d'une case adjacente.

Mais on perd l'idée d'enlever les barils désactivés lorsque la safe zone arrive dessus. Et puis c'est chouette de voir un "sentiment de conquête". Donc on ajoutera la safe zone si on a le temps.

Lorsqu'on utilise le gros dome 3*3 pour désactiver un baril, on gagne plein d'argent et une éprouvette de la couleur du baril. Certaines bonus ne peuvent s'acheter qu'avec des éprouvettes.


## (Tentative d') équilibrage entre les coûts et les bénéfices

Pour l'argent, on en gagne un par case de dôme + 1 par carré de 2x2 de dôme. Et le dôme 3x3 a un argent remplacé par une éprouvette.

Ça donne :
 - dôme en forme de T : 4 argent
 - dôme de coin : 5 argent
 - dôme de bord : 8 argent
 - dôme en rond : 12 argent + 1 éprouvette

On peut assez facilement avoir 50 ou 70 argent.
Le max, c'est 12 dômes. Mais on peut s'arranger pour finir un jeu sans avoir les 12.

Prix progressif des dômes :

 - 0 argent (ben oui)
 - 10
 - 30
 - 60
 - 100
 - 150
 - 2 éprouvettes jaunes
 - 2 éprouvettes vertes
 - 2 éprouvettes violettes
 - 2 éprouvettes de chaque couleur
 - 4 éprouvettes de chaque couleur + 100 argent
 - 6 éprouvettes de chaque couleur + 200 argent

Nettoyage de baril désactivé : 5, 10, 15, 25, 40, 65 (Fibonacci...)


## Tutoriels

Ce sont des niveaux spéciaux. Si possible, la seule particularité du tutoriel, c'est un curseur de souris qui se déplace au début, pour montrer les endroits où cliquer. Le moins de texte possible, car les gens lisent pas les textes.

Les premiers tutos permettent d'obtenir une seule étoile. Jusqu'au tutos expliquant comment gagner 2 autres étoiles.

### Tuto 1 (base)

Un baril jaune avec toutes les cases autour révélés. Comme ça on voit bien son pattern 6-4-2.

À côté, un baril jaune avec trois cases non révélées autour.

Encore à côté, un rectangle de cases non révélées, avec un seul baril dedans, à trouver.

Tuto : Le curseur se déplace sur le dôme, puis sur le premier baril, puis sur les cases à révéler du deuxième baril. puis il se dirige vers le rectangle et part en multi-curseurs qui disparaissent (pour montrer que c'est à la personne qui joue de se débrouiller).

### Tuto 2 (adjacence)

Deux baril jaunes proches, pour montrer que les nombres s'additionnent.

À côté, deux baril jaunes adjacents.

Encore à côté, un rectange avec 3 barils dedans, placé aléatoirement.

On a un dôme 3x3 et un dôme 3x2.

Tuto : Le curseur se déplace sur le dôme 3x2, puis sur le baril adjacent, puis sur le 3x3, puis sur le baril qui reste.

### Tuto 3 (achat de construction)

Aucun dôme au départ. Seul les dômes jaunes sont disponibles.

Un rectangle de cases non révélés, avec des patterns dedans. Toujours les mêmes, mais placés aléatoirement :

 - 2 barils tout seuls.
 - Une ligne de 3 barils.
 - Un X avec une patte coupée.
 - Une grande ligne qui prend toute la hauteur ou toute la largeur.
 - Un baril dans un coin.

Avec ces patterns, on est obligé d'acheter un dôme rond, un dôme de coin et un dôme T.

On peut gagner l'étoile du nombre d'éprouvette.

Tuto :Le curseur se déplace sur la boutique (si possible, ça ouvre automatiquement la boutique), puis sur un emplacement de dôme à acheter, puis sur un endroit où on peut placer l'emplacement.

### Tuto 4 (couleurs)

La boutique est dans le coin haut gauche.

Les dômes ronds de 3 couleur sont disponibles. On peut acheter les autres.

À droite : 3 barils de couleur différente, avec toutes les cases révélées autour. Mais on voit pas de quelle couleur ils sont, on ne voit que les patterns.

En bas : un rectangle de cases non révélées, avec 3 barils de couleur différentes dedans, placés aléatoirement, mais sans adjacence.

En bas et à droite : un rectangle de cases non révélées, avec 3 barils de couleur différentes dedans, sur une ligne de 3. Mais l'ordre est aléatoire.

Tuto : Le curseur ouvre la boutique, choisit le séparateur de couleur, puis va sur une case situé à droite, pour indiquer qu'il faut poser le séparateur à cet endroit. Ensuite il va sur le dôme jaune, sur le baril jaune, sur le dôme vert, le baril vert, le dôme violet, le baril violet.

On peut gagner l'étoile du nombre d'éprouvette. (Même si y'a que la ligne de 3 qui est critique).

### Tuto 5 (propagations)

Rectangle de cases non révélées, avec 9 barils dedans, placés aléatoirement, mais sans adjacence.

Pas de murs. Donc la zone conquise se propage.

Tous les dômes sont achetables, mais on n'en a pas au départ. La banque et le révélateur automatique sont achetables.

Pas de tuto, mais c'est le premier niveau où on voit la propagation de la zone conquise.

Pour ce tuto et tous les tutos suivants, on peut gagner l'étoile du nombre d'éprouvette.

### Tuto 6 (posage de drapeau)

Tout est achetable, sauf la maison et le nettoyeur de baril.

Tuto à déterminer, mais ce sera un truc assez simple.

### Tuto 7 (seuil de radioactivité et conversion d'éprouvette en argent)

Tout est achetable, sauf la maison et le nettoyeur de baril.

La construction permettant d'augmenter le seuil d'affichage de radioactivité n'est pas présente au départ. Faut l'acheter et l'upgrader.

Un gros rectangle non révélé.

Pour chaque couleur de barils, on a deux carrés de 3*3 barils, un avec une case vide au milieu, l'autre sans case vide. Ça fait des grosses valeur de radioactivité. On a les valeurs exactes que si on upgrade la construction.

### Autres tutos

 - nettoyeur de case (un rectangle de 7*7 avec que des barils jaune désactivés, sauf au milieu où il y a un baril dont on ne connait pas la couleur). Deux rectangles comme ça, un où la propagation de safe zone va révéler le pattern, un autre où ça se propage pas, et on doit acheter le nettoyage.
 - compteur du nombre total de baril. (ou pas).
 - la maison !


## Niveaux

 - Zone safe déjà faite, avec la zone à explorer à côté.
 - on démarre au milieu de l'aire de jeu, on peut s'étendre un peu partout.
 - on démarre dans un coin. plus on s'éloigne du coin, plus il y a de barils.
 - espace restreint, on peut poser juste les dômes dont on a besoin.


## Les étoiles

Pour chaque niveau, on peut gagner entre 1 et 3 étoiles, selon sa config.

 - 1 étoile pour finir le niveau sans avoir cassé aucun dôme.
 - 1 étoile pour avoir acheté, avant un certain nombre de tours de jeu, une construction qui coûte assez cher, qui prend un terrain de 8*8, et qui ne sert à rien. (la construction pourrait être une maison pour robot, ou un truc marrant du genre).
 - 1 étoile pour avoir gagné un nombre prédéfini d'éprouvette dans le niveau. Le nombre est configurable pour chaque niveau, il est indiqué au joueur. Il y a une construction spéciale pour ça (1*1), représentant une statue d'étoile qui se colore quand on gagne. Pas besoin d'acheter la construction, elle est présente dès le début, ou pas, selon le niveau.

Le résultat final d'un niveau est juste le nombre d'étoile obtenu, pas leur type. Exemple : on joue un niveau et on gagne l'étoile de non-cassage de dôme et celle de la maison. Ça fait 2 étoiles. On rejoue le niveau et on gagne celle de non-cassage de dôme et celle des éprouvettes. Ça fait toujours 2 étoiles. Faut vraiment gagner les 3 dans une même partie pour avoir les 3.

Pour certains niveaux, on peut acheter (à vraiment pas cher), une banque (1*1). On clique sur la banque et elle rapporte de l'argent, proportionnellement au nombre total d'étoiles obtenues dans tous les niveaux. On clique une seule fois.

Pour tous les niveaux de non-tutoriels, la banque est déjà présente dès le départ, et on a juste à cliquer dessus. On embête pas la personne qui joue, à lui faire acheter un truc qu'elle va systématiquement acheter de toutes façons.


Pour les niveaux plus durs, on ne disposera pas les barils complètement aléatoirement. Il faut placer certains patterns prédéfinis. Ces patterns, quand ils sont bien gérés, permettent d'avoir plein d'éprouvettes.

Exemples :

 - Une ligne de 3 barils. On désactive celui du milieu avec un dôme en T, puis on désactive les 2 extrémités avec un dôme rond. Ça fait 2 éprouvettes.
 - Un diagonale de 3 barils. Pareil, mais faut un dôme de coin.
 - Un carré de 3*3 vide au milieu. On désactive les 4 bords avec des T, puis on prend les 4 restants avec des ronds. 4 éprouvettes.
 - Une ligne de 2 barils, puis un troisième baril en diagonale. On enlève le milieu, puis les 2 restants avec des ronds.
 - Une dagonale de 3, puis un 4ème sur l'autre diagonale (genre, un X auquel il manqerait une patte). On enlève le milieu avec un coin, les 3 restants avec des ronds.
 - Ligne de 5.

Si on met un baril sur un bord, puis un second baril adjacent au premier, mais pas sur le bord, ça fait 2 barils sans aucune éprouvette possible. C'est un peu frustrant. Si ça arrive au moment de la génération d'un niveau, il faut peut-être enlever le baril du bord.


## Trucs automatiques

Le terrain doit être "conquis". Ça se fait automatiquement, selon ce principe :

 - Pour une case donnée, non conquise, on vérifie si elle est révélée et si son niveau de radioactivité est 0 (elle peut contenir un baril désactivé).
 - On chercher la case de boutique la plus proche (la boutique étant une construction en 4*4).
 - On prend le rectangle de cases englobant la case à vérifier et la case de boutique (ce rectangle peut être une ligne, si la case à vérifier est sur l'alignement de la boutique)
 - Si ce rectangle ne contient que des cases conquise + la case à vérifier, alors la case devient conquise.

Les barils désactivés présent sur une case conquise sont enlevés complètement.

Ça permet de faire une conquête assez souple, sans pour autant avoir des formes de terrain complètement tordues due à un flood-fill à la con.

Les cases conquises adjacentes à une case non conquises (diagonales comprises) ont un sprite de "travaux" dessus. Le sprite représente des rayures noires et oranges.

Une construction doit être placé entièrement sur des cases conquises et qui ne sont pas en travaux. Sauf exception, on ne peut pas déplacer une construction.


Lorsqu'on a acheté la construction correspondante, les cases non révélées qui sont adjacentes (diagonales comprises) à une case révélée et non-radioactive sont automatiquement révélée.

Juste pour le fun, on met un petit robot qui se déplace de sa construction jusqu'à la case non révélée et qui la révèle.

Donc y'aura du pathfinding. Et une case ne peut être révélée que s'il y a un chemin de case révélée et non-radioactive entre elle et la construction.

Les révélations automatiques peuvent déclencher des conquêtes automatiques, et c'est cool.

On peut désactiver la révélation automatique en cliquant sur la construction. Parce qu'on n'a pas forcément envie d'avoir un robot qui se promène partout pendant qu'on réfléchit.


