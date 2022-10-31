# Mise en prod.

## Mise en prod 01

### Création du compte sur pythonanywhere

Tout à la main et un peu à l'arrache, parce que pour l'instant, pas le temps de chercher comment automatiser ça.

Connexion sur squarity.pythonanywhere.com.

Création de l'appli web. Je ne sais plus sur quels boutons j'ai cliqué, mais c'est assez simple.

Sélection de la version python la plus récente : 3.8. La version associée de Django est indiquée, mais j'ai pas noté laquelle c'est. Je la retrouverais plus tard.

Dans l'onglet Files se trouve les fichiers du site web. Il y a les fichiers par défaut placés par Django. Notamment /home/squarity.

Pour l'instant, on ne touche pas à tout ce qu'il y a dans Django. On veut juste mettre des fichiers statiques.

### Génération des fichiers du site

Dans la racine du repository de squarity-code, exécuter `npm run build`. Cela crée/update le contenu du répertoire `dist` (il n'est pas versionné dans git).

### Copie dans pythonanywhere

Dans pytonanywhere, création d'un répertoire `/home/squastatic`

Copie de tout le contenu du répertoire `dist` dans le répertoire `/home/squastatic` de pythonanywhere.

J'ai juste omis 2 fichiers :

 - `favicon.ico`, parce que c'est juste un icône par défaut.
 - `lib_test.py`, parce que ce fichier ne sert plus à rien. J'aurais dû le nettoyer avant de mettre en prod.

Il faut créer toute l'arborescence de répertoires, et copier tous les fichiers statiques manuellement, un par un. C'est lourdingue. Je dois trouver un moyen de simplifier ce process (CI/CD, toussa...).

### Création des urls pour les fichiers statiques

Dans l'onglet Web de pythonanywhere, partie "Static files", ajouter toutes les correspondances suivantes :

| URL             | Directory                                |
| --------------- | ---------------------------------------- |
| /static/        | /home/squarity/squarity/static           |
| /media/         | /home/squarity/squarity/media            |
| /board_model.py | /home/squarity/squastatic/board_model.py |
| /index.html     | /home/squarity/squastatic/index.html     |
| /brython/       | /home/squarity/squastatic/brython        |
| /css/           | /home/squarity/squastatic/css            |
| /img/           | /home/squarity/squastatic/img            |
| /js/            | /home/squarity/squastatic/js             |
| /sm/            | /home/squarity/squastatic/sm             |

Tout en haut de la fenêtre, cliquer sur le bouton "Reload squarity.pythonanywhere.com".

À partir de là, on peut faire un premier test. Aller sur l'url [http://squarity.pythonanywhere.com/index.html](http://squarity.pythonanywhere.com/index.html). Le jeu devrait fonctionner, là tout de suite, complètement. Il est possible de jouer aux deux jeux d'exemple, de modifier le code python et de relancer le jeu, de changer les images, etc.

Mais l'url [http://squarity.pythonanywhere.com/](http://squarity.pythonanywhere.com/) ne fonctionnera pas.

C'est le serveur django qui prend cette url, et s'en sert pour renvoyer une page par défaut. Je ne crois pas que ce soit possible de lier un fichier statique à l'url racine `/`. Et de toutes façons ce serait très étrange.

### Redirection de / vers /index.html

Cette redirection doit être faite par Django.

Inspiration :

 - https://stackoverflow.com/questions/14959217/django-url-redirect
 - https://stackoverflow.com/questions/15706489/redirect-to-named-url-pattern-directly-from-urls-py-in-django

Attention, la méthode pour faire une redirection n'a pas arrêté de changer au fur et à mesure des versions de Django. La doc en ligne et les questions sur StackOverflow donnent souvent des solutions obsolètes.

D'où l'intérêt de connaître sa version de Django. Il faudra que je retrouve celle que j'ai actuellement.

Dans l'onglet Files de pythonanywhere, éditer le fichier `/home/squarity/squarity/squarity/urls.py` (Ça fait beaucoup de répertoire squarity imbriqués !!).

Laisser la docstring comme elle est, et remplacer le code par ceci :

    from django.contrib import admin
    from django.urls import path

    from django.shortcuts import redirect

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('/', lambda request: redirect('/index.html', permanent=False)),
        path('', lambda request: redirect('/index.html', permanent=False)),
    ]

Sauvegarder le fichier.

Dans l'onglet web, recliquer sur le bouton "Reload squarity.pythonanywhere.com".

Il est maintenant possible de tester [http://squarity.pythonanywhere.com/](http://squarity.pythonanywhere.com/). Dans le navigateur, l'url se modifie automatiquement, pour ajouter "index.html" à la fin, et le site se charge automatiquement. Tout fonctionne pareil qu'avant.

Bon, c'est bien, mais ça reste assez rustique et fastidieux. Faudra vraiment automatiser tout ça.


## Mise en prod 02

2020-09-16

commit : 61346d42

Même méthode que la 1ère mise en prod. C'est à dire, à l'arrache.


## Mise en prod 03

2022-09-26

commit : 1ac6598

Il y a eu quelques problèmes, mais on a fini par y arriver.

### Échec

Cette nouvelle version du site intègre le router Vue : une librairie magique de Vue qui sert à gérer plusieurs urls, par exemple `squarity.fr/` et `squarity.fr/roadmap`.

Le début de la mise en prod est effectuée de la même manière qu'avant. C'est à dire :

 - Dans la racine du repository de squarity-code, exécution de `npm run build`, pour mettre à jour tout le contenu du répertoire `dist` (non versionné dans le repository).
 - Connexion sur le site pythonanywhere.com , avec le mot de passe qui va bien.
 - Copie de toute l'arborescence du répertoire `dist`, dans pythonanywhere, dans le répertoire `/home/squastatic`. Il faut effacer les anciens fichiers, et copier les nouveaux un par un, via le menu Files de pythonanywhere.com. C'est relou, mais j'ai pas mieux.
 - Dans le menu Web, ajout d'un élément dans les "static files", car on a un fichier en plus dans la racine : url=`/road_map_data.json`, directory=`/home/squarity/squastatic/road_map_data.json`
 - Toujours dans le menu Web, clic sur le bouton "Reload squarity.pythonanywhere.com"

Test du site.

L'url `http://squarity.fr` redirige automatiquement vers `http://squarity.fr/index.html`, et ... ça ne marche pas ! On voit une page toute noire, et c'est tout. Aucun message d'erreur dans la console javascript. Les url spécifiques fonctionnent très bien, on peut récupérer une image du répertoire "img", un fichier javascript, etc.

### Et finalement réussite

De ce que j'ai compris, avec le router Vue, le site doit respecter les conditions suivantes :

 - l'url `http://squarity.fr/index.html` ne fonctionne pas. Les personnes utilisant le site ne doivent pas l'utiliser. C'est comme ça.
 - l'url `http://squarity.fr/` ou `http://squarity.fr` doit renvoyer le contenu du fichier `index.html` mais ne doit pas faire de redirection vers une autre url.

Les serveurs web les plus simples respectent ces conditions (par exemple `python -m http.server`), mais pas le mien.

Il faut donc corriger tout ça.

Dans l'onglet Files de pythonanywhere, édition du fichier `/home/squarity/squarity/squarity/urls.py`. Mise en commentaire des deux redirections vers `index.html`.

Et au passage, édition du fichier `home/squarity/squarity/squarity/settings.py`. Mise en commentaire de la ligne `DEBUG = True`. Ça aurait dû être fait depuis le début ...

Versionnement de ces deux fichiers dans le repository, répertoire `squarity-doc/pythonanywhere`. Évidemment, la valeur de `SECRET_KEY` a été modifiée au préalable.

Pour autant, ça ne fonctionne toujours pas.

Ajout d'un autre élément dans les static files : url=`/`, directory=`/home/squarity/squastatic/index.html`. J'y croyais pas, mais on peut faire ça. Et maintenant, le site marche tout bien comme il faut !

Liste actuelle de tous les static files :

| URL                 | Directory                                    |
| ------------------- | -------------------------------------------- |
| /static/            | /home/squarity/squarity/static               |
| /media/             | /home/squarity/squarity/media                |
| /index.html         | /home/squarity/squastatic/index.html         |
| /pyodide/           | /home/squarity/squastatic/pyodide            |
| /css/               | /home/squarity/squastatic/css                |
| /img/               | /home/squarity/squastatic/img                |
| /js/                | /home/squarity/squastatic/js                 |
| /favicon.ico        | /home/squarity/squastatic/favicon.ico        |
| /squarity.py        | /home/squarity/squastatic/squarity.py        |
| /pyodide.js         | /home/squarity/squastatic/pyodide.js         |
| /road_map_data.json | /home/squarity/squastatic/road_map_data.json |
| /                   | /home/squarity/squastatic/index.html         |

### Dernière recommandation

Il ne faut pas bookmarker ni communiquer des urls contenant index.html.

L'url de base du site est : `http://squarity.fr`

Pour partager un jeu, ajouter tout de suite après l'url de base le caractère dièse, et l'identifiant permettant d'accéder au github gist (voir la doc qui va bien pour savoir comment créer cet identifiant).

Exemple : `http://squarity.fr#fetchez_githubgist_darkrecher/4c3e3f95c67da728f89274c9e8a317e8/raw/catfragmentator`

On peut mettre un slash juste après le ".fr", mais ce n'est pas obligé.

Dans tous les cas, pas de "index.html", et pas de squarity.pythonanywhere.com, car je ne peux pas garantir que je conserverais ces urls. (Faudrait d'ailleurs que je gère mon DNS mieux que ça, mais ça viendra plus tard).


## Mise en prod 03

2022-10-31

commit : 4d12fc23

C'était juste pour ajouter la gif animée d'un carré de roadmap (celui de "moteur du jeu").

Comme d'hab : `npm run build`

Ensuite, connexion à pythonanywhere.com.

Je pensais qu'il suffirait d'ajouter l'image et de mettre à jour le fichier `road_map_data.json`, mais ça ne marche pas. La nouvelle image n'est pas gérée par l'ancien code.

Donc, mise à jour de tous les fichiers à la racine, et des répertoires `css`, `img` et `js`.

Petits tests rapide : affichage de la nouvelle gif, lancement d'un jeu existant. Tout marche bien.


