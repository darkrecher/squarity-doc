# Partager un jeu

Il est possible d'enregistrer vos jeux et de les partager avec d'autres personnes par un simple lien, si vous avez un compte [github](https://github.com).

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

Ajoutez au début l'url de squarity et le préfixe `/#fetchez_githubgist_` :

`http://squarity.fr/#fetchez_githubgist_votre-nom/xxx123/raw/super-jeu.txt`.

Attention, si vous indiquez le protocole, mettez `http://`, et non pas `https://`. Pour l'instant le site n'est pas en HTTPS. Ce n'est pas grave, les infos qu'il contient sont publiques et non critiques.

Cette url reconstruite est le lien vers votre jeu. Vérifiez qu'il fonctionne bien, puis distribuez-le à vos ami(e)s et devenez une star de la scène vidéoludique indépendante !

Vous pouvez ensuite modifier votre gist pour améliorer ou corriger votre jeu, le lien restera le même. Attention, la mise à jour par github n'est pas instantanée. Vous devrez donc [attendre un peu](https://stackoverflow.com/questions/47066049/github-gist-raw-permalink-wont-update) avant de revérifier votre lien.

À titre d'exemple, voici un pacman créé par une gentille personne du nom de 10kbis.

Lien vers le gist : https://gist.githubusercontent.com/darkrecher/b5240940356e3bb7e59c8a2522c279d9/raw/pacman-10kbis.txt

Lien pour jouer directement : [http://squarity.fr/#fetchez_githubgist_darkrecher/b5240940356e3bb7e59c8a2522c279d9/raw/pacman-10kbis.txt](http://squarity.fr/#fetchez_githubgist_darkrecher/b5240940356e3bb7e59c8a2522c279d9/raw/pacman-10kbis.txt)

