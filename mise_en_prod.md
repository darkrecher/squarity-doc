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


## Reconstruction et mise en prod 04

2023-06-19

Je suis passé à Ubuntu ! Il faut donc reconstruire tout le projet.

`git clone https://github.com/darkrecher/squarity-code.git`

Ah, j'ai même pas npm.

`sudo apt install nodejs npm`

Purée... 103 MB dans la tronche pour cette cochonnerie de nodejs.

`npm -v`
8.5.1

`npm install`

Ça plante.

    npm WARN old lockfile
    npm WARN old lockfile The package-lock.json file was created with an old version of npm,
    npm WARN old lockfile so supplemental metadata must be fetched from the registry.
    npm WARN old lockfile
    npm WARN old lockfile This is a one-time fix-up, please be patient...
    npm WARN old lockfile
    npm WARN deprecated axios@0.20.0: Critical security vulnerability fixed in v0.21.1. For more information, see https://github.com/axios/axios/pull/3410
    npm WARN deprecated popper.js@1.16.1: You can find the new Popper v2 at @popperjs/core, this package is dedicated to the legacy v1
    npm ERR! Cannot read property 'insert' of undefined

    npm ERR! A complete log of this run can be found in:
    npm ERR!     /home/paf/.npm/_logs/2023-06-19T21_37_20_691Z-debug-0.log


`npm install`

Ça replante pareil.

Suppression du fichier `package-lock.json`. (Peut-être qu'un package-lock créé avec un windows n'est pas compatible sur du Ubuntu). Ha ha ha !!

Puis on re-essaye `npm install`

    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: 'sass@1.63.4',
    npm WARN EBADENGINE   required: { node: '>=14.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    npm WARN deprecated axios@0.20.0: Critical security vulnerability fixed in v0.21.1. For more information, see https://github.com/axios/axios/pull/3410
    npm WARN deprecated stable@0.1.8: Modern JS already guarantees Array#sort() is a stable sort, so this library is deprecated. See the compatibility table on MDN: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#browser_compatibility
    npm WARN deprecated urix@0.1.0: Please see https://github.com/lydell/urix#deprecated
    npm WARN deprecated source-map-url@0.4.1: See https://github.com/lydell/source-map-url#deprecated
    npm WARN deprecated resolve-url@0.2.1: https://github.com/lydell/resolve-url#deprecated
    npm WARN deprecated source-map-resolve@0.5.3: See https://github.com/lydell/source-map-resolve#deprecated
    npm WARN deprecated har-validator@5.1.5: this library is no longer supported
    npm WARN deprecated uuid@3.4.0: Please upgrade  to version 7 or higher.  Older versions may use Math.random() in certain circumstances, which is known to be problematic.  See https://v8.dev/blog/math-random for details.
    npm WARN deprecated popper.js@1.16.1: You can find the new Popper v2 at @popperjs/core, this package is dedicated to the legacy v1
    npm WARN deprecated svgo@1.3.2: This SVGO version is no longer supported. Upgrade to v2.x.x.
    npm WARN deprecated consolidate@0.15.1: Please upgrade to consolidate v1.0.0+ as it has been modernized with several long-awaited fixes implemented. Maintenance is supported by Forward Email at https://forwardemail.net ; follow/watch https://github.com/ladjs/consolidate for updates and release changelog
    npm WARN deprecated @hapi/bourne@1.3.2: This version has been deprecated and is no longer supported or maintained
    npm WARN deprecated @hapi/topo@3.1.6: This version has been deprecated and is no longer supported or maintained
    npm WARN deprecated @hapi/address@2.1.4: Moved to 'npm install @sideway/address'
    npm WARN deprecated @hapi/hoek@8.5.1: This version has been deprecated and is no longer supported or maintained
    npm WARN deprecated request@2.88.2: request has been deprecated, see https://github.com/request/request/issues/3142
    npm WARN deprecated @hapi/joi@15.1.1: Switch to 'npm install joi'
    npm WARN deprecated html-webpack-plugin@3.2.0: 3.x is no longer supported
    npm WARN deprecated eslint-loader@2.2.1: This loader has been deprecated. Please use eslint-webpack-plugin
    npm WARN deprecated babel-eslint@10.1.0: babel-eslint is now @babel/eslint-parser. This package will no longer receive updates.
    npm WARN deprecated chokidar@2.1.8: Chokidar 2 does not receive security updates since 2019. Upgrade to chokidar 3 with 15x fewer dependencies
    npm WARN deprecated chokidar@2.1.8: Chokidar 2 does not receive security updates since 2019. Upgrade to chokidar 3 with 15x fewer dependencies

    added 1420 packages, and audited 1421 packages in 1m

    125 packages are looking for funding
    run `npm fund` for details

    31 vulnerabilities (1 low, 6 moderate, 20 high, 4 critical)

    To address issues that do not require attention, run:
    npm audit fix

    To address all issues (including breaking changes), run:
    npm audit fix --force

    Run `npm audit` for details.


C'est une orgie de warning, mais ça a quand même l'air de mieux fonctionner.

Ensuite, on lance `npm run serve`

    WARNING  Compiled with 1 warning

    Module Warning (from ./node_modules/eslint-loader/index.js):

    /home/wilfried/Documents/personnel/squarity/squarity-code/src/components/DevZone.vue
    117:9   warning  Unexpected console statement  no-console
    121:11  warning  Unexpected console statement  no-console

    ✖ 2 problems (0 errors, 2 warnings)


    You may use special comments to disable some warnings.
    Use // eslint-disable-next-line to ignore the next line.
    Use /* eslint-disable */ to ignore all warnings in a file.

    App running at:
    - Local:   http://localhost:8080/
    - Network: http://192.168.1.30:8080/

    Note that the development build is not optimized.
    To create a production build, run npm run build.


Le site est bien présent sur http://localhost:8080/ , on peut jouer au jeu du sorcier. L'url http://localhost:8080/roadmap fonctionne aussi. Youpi !!

Mais ce serait peut-être le moment de passer à Vue 3.

D'abord on reconstruit la version actuelle et on vérifie qu'on peut la publier. Ensuite on passera à Vue 3.

Dans le repository squarity-doc, lancement du script python `road_map_text_to_json.py`, pour intégrer les nouvelles gif dans le fichier `public/road_map_data.json`.

Commit de squarity-code : f58464f0.

On lance `npm run build`.

Tout semble bien se passer.

Connexion à pythonanywhere, comme d'hab'.

Avant de faire quoi que ce soit, petite sauvegarde du contenu de squastatic, squastatic/css, squastatic/js et squastatic/pyodide. (Non versionné, mais je me garde ça ici : `~/Documents/personnel/squarity/vieux_trucs/squarity_old_dist`).

Et ensuite on copie tous les fichiers générés par dist, sur pythonanywhere, dans squastatic.



## Mise en prod 05 (avec la petite flipette sur le type MIME des fichiers statiques)

Avec le passage de Vue 2 à Vue 3. Youhou !!!

Commit de squarity-code : b0a26dce

Comme d'hab', on lance `npm run build`. Ça met à jour le contenu du répertoire dist.

Petit conseil : avant de mettre en prod, testez la version buildée, en lançant un petit serveur statique. Il faut se mettre dans le répertoire dist et lancer la commande `python3 -m http.server`. Ça m'a permis de me rendre compte que je m'étais planté pour servir les gif animées de roadmap (faut faire "import" et non pas je-sais-plus-quel-autre-truc).

Et ensuite, on met dans les fichiers dans pythonanywhere, comme d'habitude.

Sauf qu'il faut changer la structure. Maintenant, avec Vue 3, la plupart des fichiers (js, css, images, ...) sont dans un unique répertoire "assets".

Alors j'ai du changer la config des liens statiques dans pythonanywhere. Ensuite j'ai reloadé le site et j'ai testé, plus rien ne marchait !!

Dans la console du navigateur, j'avais des messages d'erreur complètement WTF :

> Loading module from “https://squarity.pythonanywhere.com/assets/index-54527515.js” was blocked because of a disallowed MIME type (“text/html”).

Ça m'a fait très peur, j'ai cru qu'il fallait configurer manuellement les MIME types indiqués dans les headers HTTP. Et je ne sais pas du tout où on doit faire ça dans pythonanywhere !

En fait le problème venait pas de là. C'est ce crétin de browser qui me renvoyait un message d'erreur totalement inadapté. C'est un peu expliqué ici : https://stackoverflow.com/questions/48248832/stylesheet-not-loaded-because-of-mime-type#comment91526535_48248832

Le vrai problème, c'est que les fichiers statiques n'étaient pas accessibles. Le navigateur ne récupérait pas un fichier avec un mauvais MIME type. Il récupérait carrément rien du tout !

La raison pour laquelle ce n'était pas accessible, c'est que je m'étais planté dans la config des fichiers statiques.

Dans pythonanywhere, j'avais ça :

| URL      | Directory                            |
| -------- | ------------------------------------ |
| (un tas de trucs divers)                        |
| ...      |                                      |
| /        | /home/squarity/squastatic/index.html |
| /assets/ | /home/squarity/squastatic/assets     |

L'ordre des éléments dans la config est important. Le lien statique appelé avec le slash tout seul attrape absolument tout, et balançait à chaque fois le fichier index.html. Forcément ça pète. Le contenu du répertoire assets n'était jamais servi.

Donc il faut, bien évidemment, **toujours mettre en dernier le lien statique avec le slash tout seul**.

Et quand on aura un site un peu plus sérieux (avec un vrai serveur et pas que des fichiers statiques), il faudra sûrement virer ce slash tout seul, et le gérer autrement. Voili voilà.

Voici la config actuelle de tous les static files :


| URL                | Directory                                   |
| ------------------ | ------------------------------------------- |
| /static/           | /home/squarity/squarity/static              |
| /media/            | /home/squarity/squarity/media               |
| /index.html        | /home/squarity/squastatic/index.html        |
| /pyodide/          | /home/squarity/squastatic/pyodide           |
| /favicon.ico       | /home/squarity/squastatic/favicon.ico       |
| /squarity.txt      | /home/squarity/squastatic/squarity.txt      |
| /pyodide.js        | /home/squarity/squastatic/pyodide.js        |
| /road_map_data.txt | /home/squarity/squastatic/road_map_data.txt |
| /assets/           | /home/squarity/squastatic/assets            |
| /                  | /home/squarity/squastatic/index.html        |

Et maintenant ça marche !
