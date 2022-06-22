# Doc diverses

(On va essayer que ça devienne pas un fourre-tout).

Grande image, publiquement accessible, pour vérifier que la récupération d'un atlas fonctionne bien : https://i.imgur.com/TQZDMUu.gif


## Modifs à faire pour intégrer le site squarity dans itch.io

Je ne sais plus exactement tout ce qu'il faut faire. Mais, entre autres, il faut créer dans la racine du repository un fichier `vue.config.js` avec ça dedans :

    module.exports = {
    publicPath: '',
    };

Il y a un exemple ici : https://squarity.itch.io/snake-match


## Changements dans l'authentification de github

Maintenant il faut utiliser un "Access Personal Token" dans github.

Je met ici comment y accéder, parce que je m'en souviens jamais.

se connecter à github.com comme d'habitude.
bouton tout en haut à droite, settings - developer settings - personal access token.

Ils sont tous là.
Ensuite, on s'en sert comme des mots de passe normaux.
En local, c'est censé être géré correctement dans le "gestionnaire d'identification" sur la machine de dev.

https://stackoverflow.com/questions/15381198/remove-credentials-from-git

