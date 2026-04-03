# Brouillon en vrac

## Idée pour le prochain jeu


Genre Dungeon Sweeper, mais juste avec des couleurs.


Il y a des tonneaux radioactifs à enlever. Ils fuient de différentes manières, ce qui permet de détecter la radioactivité sur différentes cases. Mais ça s'additionne, donc des fois on sait pas trop où c'est.

Lorsqu'on révèle une case, on gagne parfois un peu d'argent, et on voit la radioactivité dessus.

Si on révèle une case contenant un tonneau, on crève direct.

On peut acheter des "bouclier". Un type de bouclier par tonneau.

Si on active un bouclier avant de révéler une case contenant un tonneau, on ne meurt pas, le bouclier est utilisé, le tonneau est supprimé.

Si on active un bouclier et qu'on révèle une case ne contenant pas de tonneau, le bouclier est utilisé. Dommage !

Et après, on peut imaginer d'autres bonus : scan d'une zone précise, détection de la case la plus proche contenant de l'argent, etc.



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

Les tonneaux violets fuient comme ça :

1           1
  2       2
    3 3 3
    3 V 3
    3 3 3
  2       2
1           1

Les tonneaux verts fuient comme ça :

1   1   1   1
  1   1   1
1   3 3 3   1
  1 3 G 3 1
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
    3 V 3
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

Et maintenant, comment on peut avoir une évaluation, pour donner un nombre d'étoiles ?

On peut juste faire avec l'argent. Mais si y'a d'autres trucs possibles, ce serait cool.

 - avoir libéré un gros carré de terrain assez tôt dans la partie (genre, on construit une maison dessus)
 - dépenser un gros tas de pognon assez tôt dans la partie (une statue à la gloire de je-sais-pas-quoi)
 - finir le niveau, tout bêtement

Ça fait 3 étoiles, c'est tout à fait bien.

Chaque étoile apporte un peu d'argent en plus au début d'un niveau.




