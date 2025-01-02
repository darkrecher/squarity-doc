# Fonctionnement de la barre de progress pour le chargement de pyodide

TL;DR : cette barre de progress est une grosse truanderie.


## Contexte

Squarity utilise la webassembly Pyodide (v0.15.0) pour pouvoir exécuter du code python dans un navigateur web. Avant de démarrer un jeu, 3 fichiers assez volumineux sont téléchargés en parallèle :

 - `pyodide.asw.wasm` : 13.0 Mo
 - `pyodide.asm.data` : 6.9 Mo
 - `pyodide.asm.js` : 3.3 Mo

Ces téléchargements peuvent prendre plusieurs dizaines de secondes, il sont effectués par du code javascript fournis par Pyodide (`public/pyodide.js` et autres). Ce code javascript a été intégré dans Squarity, au début sans y apporter aucune modification.

Ça fonctionne, mais si rien de concret ne s'affiche durant les téléchargements, la personne qui joue peut croire que la page est bloquée et risque de passer à autre chose. Le but est donc de trouver la meilleure manière possible d'afficher une barre de progression durant les téléchargements.


## Tentative 1 : utilisation du cache

Les navigateurs mettent automatiquement certains fichiers en cache, durant un temps acceptable (quelques heures, voire plus). Cette mise en cache a été vérifiée pour les fichiers de Pyodide, avec Chrome et Firefox. Lorsqu'on rafraîchit la page (F5), le jeu démarre beaucoup plus vite. L'onglet "réseau" de la console développeur confirme que les fichiers proviennent du cache.

L'idée était de télécharger un première fois les 3 fichiers pyodide.* avec du code spécifique dans Squarity, tout en montrant des barres de progress. Les fichiers ne sont pas utilisés, mais ça les met dans le cache. Ensuite, on lance l'initialisation de Pyodide, qui demande à avoir les 3 fichiers. Ceux-ci arriveront beaucoup plus vite car ils sont déjà dans le cache.

Pour information, il existe deux manières de télécharger un fichier en javascript : la fonction native `fetch` et l'utilisation de `XmlHttpRequest`. C'est assez compliqué de faire une barre de progress avec `fetch`, mais très facile avec `XmlHttpRequest`, il suffit de redéfinir la fonction `onprogress`.

Cette tentative n'a pas fonctionné. Lors de la première visite de la page web, le code de Squarity télécharge les 3 fichiers, puis le code de Pyodide les retélécharge sans les prendre à partir du cache. Lors de la deuxième visite de la page web, le code de Squarity et le code de Pyodide utilisent tous les deux le cache, ce qui est fort louable, mais trop tard. Je ne sais pas pourquoi ça fonctionne de cette manière. Je suppose que le cache ne se remplit pas instantanément. Il faut attendre qu'une page web soit totalement chargée avant que le navigateur web mette en cache tout ce qui a été récupéré.


## Tentative 2 : utilisation des service workers

En résumé, les service workers permettent d'exécuter du code personnalisé à chaque requête externe. Il est possible de renvoyer un autre résultat (pouvant provenir d'un cache) au lieu d'effectuer réellement la requête.

Plus d'info ici : https://developer.mozilla.org/fr/docs/Web/API/Service_Worker_API/Using_Service_Workers

Code d'exemple ici : https://github.com/mdn/dom-examples/tree/main/service-worker/simple-service-worker

Je n'ai jamais réussi à faire fonctionner correctement le code d'exemple, alors qu'il semble assez simple et n'utilise aucun framework javascript. Le service worker était bien enregistré, mais son code spécifique n'était jamais exécuté.


## Tentative 3 : modifier le code téléchargeant pyodide.asm.wasm

Il s'agit du premier et du plus volumineux fichier téléchargé par Pyodide.

Mais il est récupéré avec une fonction `fetch`, dont le résultat est transmis à une fonction `WebAssembly.compileStreaming`, qui télécharge et compile en même temps la web assembly.

Méthode pour afficher la progression d'un fetch générique : https://dev.to/tqbit/how-to-monitor-the-progress-of-a-javascript-fetch-request-and-cancel-it-on-demand-107f

Méthode pour afficher la progression d'un fetch d'une webassembly : https://stackoverflow.com/questions/65491241/get-webassembly-instantiatestreaming-progress

Ça me semblait trop risqué de modifier ce code pour y ajouter une barre de progression. Les commentaires de Stack Overflow indiquent que ça ne marche pas dans certains contextes, peu de gens ont tenté ça, etc.


## Choix final : modifier le code téléchargeant pyodide.asm.data

Le fichier `pyodide.asm.data` est téléchargé peu de temps après le début de l'initialisation de Pyodide, par le javascript `pyodide.asm.data.js`.

Le code javascript est minifié, mais on peut voir que le téléchargement est effectué via une `XmlHttpRequest`, avec une fonction `xhr.onprogress` déjà définie.

Extrait de `pyodide.asm.data.js` : `xhr.onprogress=function(event){;var url=packageName;var size=packageSize; [...]`

J'ai ajouté ma petite fonction de callback personnelle dans ce code.

Même extrait de `pyodide.asm.data.js`, après ma modification : 

`xhr.onprogress=function(event){if (window.pyodideDownloadProgress) {window.pyodideDownloadProgress(event.loaded, event.total)};var url=packageName;var size=packageSize; [...]`

La fonction `window.pyodideDownloadProgress` est définie dans le composant `src/components/GameBoard.vue`. Cette fonction s'occupe de mettre à jour la barre de progression.

Ça fonctionne, mais ce n'est pas très précis. La barre de progression atteint 100%, puis il faut attendre plusieurs secondes, le temps que les autres fichiers de Pyodide soient téléchargés.


## Ajout de la truanderie

Les fichiers sont téléchargés à peu près tous en même temps, et la taille de `pyodide.asm.data` (6.9 Mo) est à peu près la moitié du fichier le plus volumineux (13.0 Mo).

On peut donc raisonnablement penser que lorsque `pyodide.asm.data` est entièrement téléchargé, on est à la moitié du temps total de téléchargement.

Pendant le téléchargement de `pyodide.asm.data` :

 - on enregistre la date de début (en milliseconde).
 - on remplit les 50 premiers pourcents de la barre de progress, de manière précise, grâce à la fonction `window.pyodideDownloadProgress`.
 - on enregistre la date de fin.

Avec ces deux dates, on peut calculer la vitesse moyenne de téléchargement.

Ensuite, grosse truanderie ! Les 50 derniers pourcents de la barre de progress sont remplis de manière linéaire, selon la vitesse calculée précédemment.

Lorsque Pyodide est entièrement téléchargé et initialisé, on enlève la barre de progression et on affiche la tâche d'initialisation suivante.

Cette truanderie est implémentée dans la classe `src/classes/ProgressImposter.js`

Ce n'est pas très précis. Parfois la barre de progress arrive à 100% et il faut encore attendre quelques secondes. D'autres fois, on passe immédiatement à la tâche suivante alors que la barre n'était qu'à 90%. D'autre part, si l'un des fichiers a été mis en cache mais pas l'autre, ça donnera certainement n'importe quoi. Pour l'instant, on n'a pas mieux.


## Dans le futur

La version actuelle de Pyodide est 0.27.0. Celle utilisée dans Squarity est 0.15.0. À'm'ment donné, il faudra peut-être se réactualiser...

Les fichiers et les méthodes de téléchargement ne sont pas du tout les mêmes avec les nouvelles versions de Pyodide. Il faudra donc re-réfléchir à tout ça.

Ce sera pour plus tard. Je mets une tâche dans Trello à ce sujet, merci et salutations à tous les truands du web !

