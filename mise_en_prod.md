# Mise en prod.

## Première mise en prod

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

| URL             |  Directory                               |
|-----------------|------------------------------------------|
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


