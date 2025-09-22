# Partager un jeu

Il est possible d'enregistrer vos jeux et de les partager avec d'autres personnes par un simple lien, si vous avez un compte [github](https://github.com).


## Méthode

Connectez-vous sur github, cliquez sur votre avatar en haut à droite et sélectionnez "Your gists".

Cliquez sur le bouton "+" en haut à droite pour créer un nouveau gist (un texte que vous rendez public).

Choisissez un nom pour votre texte, **attention, pas d'underscore dans le nom du fichier, uniquement des caractères alphanumériques et des tirets "-"**.

Dans le contenu du texte, mettez les informations suivantes les unes à la suite des autres :

 - L'url de votre tileset.
 - À la ligne en-dessous, un séparateur. Le plus simple est de mettre 8 tirets : `------`. Attention, pas d'espace au début de la ligne.
 - Votre configuration json.
 - Le même séparateur que précédemment. Attention, il faut exactement les mêmes caractères (les 8 tirets).
 - Votre game_code.

En bas à droite, cliquez sur la flèche du bouton pour sélectionner "Create public gist", puis cliquez sur le bouton.

Lorsque votre gist est sauvegardé, cliquez sur le bouton "Raw" à droite du fichier texte.

L'url affichée dans votre navigateur devrait avoir cette forme :

`https://gist.githubusercontent.com/votre-nom/xxx123/raw/yyy456/super-jeu.txt`

Les parties "xxx123" et "yyy456" sont de longues suites de caractères alphanumériques, permettant d'identifier votre gist de manière unique.

Supprimez la partie `yyy456/` et rechargez la page. Vérifiez que le texte brut de votre jeu s'affiche toujours.

Garder la fin de cette url, à partir de votre nom de compte github. C'est à dire : `votre-nom/xxx123/raw/super-jeu.txt`.

Ajoutez ce texte au début  l'url de squarity et le préfixe `https://squarity.fr/game/#fetchez_githubgist_`.

Exemple : `https://squarity.fr/game/#fetchez_githubgist_votre-nom/xxx123/raw/super-jeu.txt`.

Cette url reconstruite est le lien vers votre jeu. Vérifiez qu'il fonctionne bien, puis distribuez-le à vos ami(e)s et devenez une star de la scène vidéoludique indépendante !

Vous pouvez ensuite modifier votre gist pour améliorer ou corriger votre jeu, le lien restera le même. Attention, la mise à jour par github n'est pas instantanée. Vous devrez donc [attendre un peu](https://stackoverflow.com/questions/47066049/github-gist-raw-permalink-wont-update) avant de revérifier votre lien.


## Exemple

Voici un pacman créé par une gentille personne du nom de 10kbis.

Lien vers le gist : [https://gist.githubusercontent.com/darkrecher/b5240940356e3bb7e59c8a2522c279d9/raw/pacman-10kbis.txt](https://gist.githubusercontent.com/darkrecher/b5240940356e3bb7e59c8a2522c279d9/raw/pacman-10kbis.txt)

Lien pour jouer directement : [https://squarity.fr/game/#fetchez_githubgist_darkrecher/b5240940356e3bb7e59c8a2522c279d9/raw/pacman-10kbis.txt](https://squarity.fr/game/#fetchez_githubgist_darkrecher/b5240940356e3bb7e59c8a2522c279d9/raw/pacman-10kbis.txt)


## Redirections d'url

La configuration DNS de "squarity.fr" effectue une redirection vers "squarity.pythonanywhere.com", qui est le vrai site web hébergeant les fichiers.

C'est assez moche. À terme, ce sera corrigé, l'url "interne" de pythonanywhere ne devrait plus être visible.

D'autre part, les versions précédentes de Squarity n'avait pas le texte `/game/` dans les urls de partage des jeux. La rétro-compatibilité est assurée avec une autre redirection moche. Lorsque le chemin de l'url est un simple `/`, sans le `/game/`, et qu'elle contient un bookmark avec `#fetchez`, on ajoute automatiquement `/game/`. À terme, cette rétro-compatibilité ne sera peut-être pas conservée.

Pour ces deux raisons :

**pensez bien à utiliser des urls commençant par `https://squarity.fr/game/#fetchez_githubgist_` pour partager vos jeux**.

C'est le seul format d'url qui est garanti de rester (tant que Squarity existera sur internet).

