# Quelle version choisir ?


## Versions disponibles

La version actuelle du moteur de Squarity est la V2. Son nom complet est "2.1.0".

L'ancienne version V1 est toujours disponible. Son nom complet est "1.0.0".

Le code des jeux n'est pas compatible entre les deux versions. Si vous créez un jeu avec la V1, vous ne pourrez pas le transférer directement en V2.

La V1 n'évoluera pas (sauf si un bug critique est découvert). Il n'y aura pas de versions "1.0.1", "1.1.0" ou autres. Mais tant que le site de Squarity sera disponible sur le web, la V1 restera disponible.

La V2 évoluera ("2.1.1", etc.). Il n'y aura toujours qu'une seule version V2 disponible sur le site (la plus récente). Dans la mesure du possible, les futures versions V2 seront compatibles avec l'actuelle "2.1.0". Cependant, ce n'est pas garanti à 100%.

Si vous créez un jeu avec la V2, vous avez donc le risque de devoir réadapter votre code quelques mois/années plus tard, pour que votre jeu continue de fonctionner. Nous mettons tout en œuvre pour que ce risque soit le plus minimal possible. Veuillez nous excuser pour la gêne occasionnée. C'est la vie.

Pas de V3 prévue pour l'instant.


## Comment indiquer la version de votre jeu

Ça se passe dans la configuration JSON.

Pour utiliser la V1, indiquez dans la config : `"version": "1.0.0"`

Pour utiliser la V2, indiquez : `"version": "2.1.0"`

Le moteur de Squarity vérifie uniquement le premier caractère que vous avez indiqué dans la version. Si c'est "1" -> "1.0.0". Si c'est "2" -> "2.1.0".

Un message d'avertissement apparaîtra dans le log de Squarity si vous oubliez d'indiquer la version.


## Comment choisir ?

Si vous débutez vraiment, que vous n'avez jamais écrit aucun programme, ni en python, ni dans un autre langage, ce sera peut-être plus facile pour vous de commencer avec la V1. Le code des jeux est plus simple à écrire, il n'y a pas d'objets spécifiques à Squarity (pas de `Coord`, pas de `Layer`, etc.).

Si vous souhaitez créer un seul petit jeu très simple, sans intention de le faire évoluer, vous pouvez également utiliser la V1. L'apprentissage et la création devrait vous prendre moins de temps.

Dans tous les autres cas, c'est mieux d'utiliser la V2, car elle permet de faire plus de choses et elle est plus pratique pour certaines fonctionnalités.

Bien entendu, votre choix n'est pas définitif. Vous pouvez commencer à créer quelques jeux avec la V1, puis passer à la V2. L'apprentissage de la V2 ira plus vite si vous connaissez déjà la V1, car les deux versions ont beaucoup d'éléments et de notions en commun.

Il est possible de partager vos jeux aussi bien en V1 qu'en V2, la méthode est la même. Voir la page expliquant [comment partager un jeu](share-your-game).


## Fonctionnalités communes aux deux versions

 - Exécuter du code python (version 3.7.4), récupérer les messages d'erreurs et les exceptions de votre code.
 - Utiliser une aire de jeu de n'importe quelle taille, ayant la forme d'un quadrillage en deux dimensions.
 - Afficher des images sur les cases de cette aire de jeu, chaque image tient exactement dans sa case.
 - Afficher des images avec une transparence progressive, grâce au format d'image .png.
 - Récupérer les événements de clics de souris, avec l'indication de la case cliquée.
 - Récupérer les événements de touches de clavier (les 4 directions, les actions "1" et "2").
 - Écrire du texte et des emojis dans le log de Squarity.
 - Définir l'ordre d'affichage des objets situés sur une même case (de manière pas très pratique).
 - Exécuter une action différée (un code python spécifique qui se déclenche après un délai et qui peut changer des objets dans le jeu).
 - Exécuter des actions différées en boucle (une action différée qui planifie une autre action différée, et ainsi de suite).
 - Bloquer temporairement l'interface de jeu, pour afficher des animations ou des "cut scenes".


## Fonctionnalités disponibles uniquement en V2

 - Afficher des objets décalés par rapport aux cases de l'aire de jeu.
 - Grossir/rétrécir les objets, qui peuvent dépasser sur les cases adjacentes.
 - Animer automatiquement des transitions pixel par pixel, pour les déplacements, les décalages et les tailles d'objets.
 - Définir des séquences de mouvements, décalage et tailles.
 - Récupérer la configuration JSON dans le code du jeu.
 - Définir l'ordre d'affichage des objets de manière plus pratique, avec les `Layer`.
 - Utiliser des classes de base pour faciliter le code des jeux (`Coord`, `Direction`, `Rect`, ...).
 - Récupérer rapidement un ou plusieurs game objects spécifiques, avec des itérateurs spécifiques (classe `Sequencer`, fonction `get_first_gobj`).
 - Définir des actions différées avec des fonctions de callbacks.
 - Bloquer l'interface du jeu, de manière visible ou invisible.
 - Bloquer automatiquement l'interface du jeu tant que certains objets effectuent des transitions.
 - Exécuter automatiquement une callback lorsqu'un objet a fini toutes ses transitions.
 - Connaître le nombre de transitions restant à effectuer pour un objet.
 - plein d'autres choses dans le futur.





