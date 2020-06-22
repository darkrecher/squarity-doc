# Installation de Vue et TypeScript


## Justification du choix

Angular ça me semble trop overkill. Et comme j'y connais rien en front-end, je préfère utiliser un framework qui ne demande pas de tout connaître d'un coup.

Javascript tout seul, ça me fait flipper en continu, car pour n'importe quel élément du langage, je suis toujours en train de me demander si ça va bien être compatible sur tous les navigateurs. TypeScript est censé régler ce problème, si j'ai bien compris à quoi il sert.

Pour le reste, je vais découvrir en même temps : npm, la minification, gestion du CSS, ...


## Installation npm

Npm vient avec cette cochonnerie de node.js. On va faire avec.

Inspiration :

https://vuejs.org/v2/guide/typescript.html

https://cli.vuejs.org/

https://nodejs.org/en/download/

En fait je l'avais déjà installé sur mon ordi B, lors d'une formation.

    λ node -v
    v10.15.3
    λ npm -v
    6.4.1
    λ npm install npm@latest -g
    C:\Users\recher\AppData\Roaming\npm\npm -> C:\Users\recher\AppData\Roaming\npm\node_modules\npm\bin\npm-cli.js
    C:\Users\recher\AppData\Roaming\npm\npx -> C:\Users\recher\AppData\Roaming\npm\node_modules\npm\bin\npx-cli.js+ npm@6.14.5
    added 435 packages from 873 contributors in 21.238s
    λ npm -v
    6.14.5


    λ npm install --global @vue/cli
    npm WARN deprecated request@2.88.2: request has been deprecated, see https://github.com/request/request/issues/3142 npm WARN deprecated chokidar@2.1.8: Chokidar 2 will break on node v14+. Upgrade to chokidar 3 with 15x less dependencies.
    npm WARN deprecated fsevents@1.2.13: fsevents 1 will break on node v14+ and could be using insecure binaries. Upgrade to fsevents 2.
    C:\Users\recher\AppData\Roaming\npm\vue -> C:\Users\recher\AppData\Roaming\npm\node_modules\@vue\cli\bin\vue.js
    > core-js@3.6.5 postinstall C:\Users\recher\AppData\Roaming\npm\node_modules\@vue\cli\node_modules\core-js
    > node -e "try{require('./postinstall')}catch(e){}"
    Thank you for using core-js ( https://github.com/zloirock/core-js ) for polyfilling JavaScript standard library!
    The project needs your help! Please consider supporting of core-js on Open Collective or Patreon:
    > https://opencollective.com/core-js
    > https://www.patreon.com/zloirock
    Also, the author of core-js ( https://github.com/zloirock ) is looking for a good job -)
    > @apollo/protobufjs@1.0.4 postinstall C:\Users\recher\AppData\Roaming\npm\node_modules\@vue\cli\node_modules\@apollo\protobufjs
    > node scripts/postinstall
    > nodemon@1.19.4 postinstall C:\Users\recher\AppData\Roaming\npm\node_modules\@vue\cli\node_modules\nodemon
    > node bin/postinstall || exit 0
    Love nodemon? You can now support the project via the open collective:
    > https://opencollective.com/nodemon/donate
    > ejs@2.7.4 postinstall C:\Users\recher\AppData\Roaming\npm\node_modules\@vue\cli\node_modules\ejs
    > node ./postinstall.js
    Thank you for installing EJS: built with the Jake JavaScript build tool (https://jakejs.com/)
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@^1.2.7 (node_modules\@vue\cli\node_modules\chokidar\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
    npm WARN jscodeshift@0.9.0 requires a peer of @babel/preset-env@^7.1.6 but none is installed. You must install peer dependencies yourself.
    + @vue/cli@4.4.1
    added 1103 packages from 660 contributors in 78.204s

Comme d'hab', à chaque fois qu'on installe des trucs avec npm, il y a tout un tas de warning anxiogènes. Mais je suppose que c'est mieux de le savoir que de pas le savoir.

    λ vue -V
    @vue/cli 4.4.1


## Création de projets Vue

Création d'un projet avec le preset par défaut. On va faire simple pour commencer.

    λ vue create test-vue
    ?  Your connection to the default npm registry seems to be slow.
    Use https://registry.npm.taobao.org for faster installation? Yes
    Vue CLI v4.4.1
    ? Please pick a preset: default (babel, eslint)
    Vue CLI v4.4.1
    ✨  Creating project in C:\Recher\personnel\test_vue\test-vue.
    �  Initializing git repository...
    ⚙️  Installing CLI plugins. This might take a while...
    > yorkie@2.0.0 install C:\Recher\personnel\test_vue\test-vue\node_modules\yorkie
    > node bin/install.js
    setting up Git hooks
    done
    > core-js@3.6.5 postinstall C:\Recher\personnel\test_vue\test-vue\node_modules\core-js
    > node -e "try{require('./postinstall')}catch(e){}"
    > ejs@2.7.4 postinstall C:\Recher\personnel\test_vue\test-vue\node_modules\ejs
    > node ./postinstall.js
    added 1220 packages from 846 contributors in 119.031s
    43 packages are looking for funding
    run `npm fund` for details
    �  Invoking generators...
    �  Installing additional dependencies...
    added 53 packages from 36 contributors in 25.955s
    46 packages are looking for funding
    run `npm fund` for details
    ⚓  Running completion hooks...
    �  Generating README.md...
    �  Successfully created project test-vue.
    �  Get started with the following commands:
    $ cd test-vue
    $ npm run serve

Lancement du serveur web local, pour tester.

    C:\Recher\personnel\test_vue
    λ cd test-vue\

    C:\Recher\personnel\test_vue\test-vue (master -> origin)
    λ npm run serve
    > test-vue@0.1.0 serve C:\Recher\personnel\test_vue\test-vue
    > vue-cli-service serve
    INFO  Starting development server...
    98% after emitting CopyPlugin
    DONE  Compiled successfully in 3189ms 10:07:39
    App running at:
    - Local:   http://localhost:8080/
    - Network: http://192.168.1.23:8080/
    Note that the development build is not optimized.
    To create a production build, run npm run build.
    Terminer le programme de commandes (O/N) ? O

Cool.


Installation de l'extension de VS-Code "Vetur" 0.24.0. Parce que VS-Code le suggère.


Lorsque le serveur est lancé : modif de C:\Recher\personnel\test_vue\test-vue\src\App.vue
On change la ligne `<HelloWorld msg="Welcome to Your Vue.js App"/>`, en indiquant le texte qu'on veut dans "msg".

Dès qu'on sauvegarde le fichier, la page se rafraîchit dans localhost:8080, et le nouveau texte s'affiche. Pas besoin de recharger.

C'est putain de cool.


Création d'un projet avec du TypeScript

    λ vue create test-vue-typescript

    Vue CLI v4.4.1
    ? Please pick a preset: Manually select features
    ? Check the features needed for your project: Babel, TS, Linter
    ? Use class-style component syntax? No
    ? Use Babel alongside TypeScript (required for modern mode, auto-detected polyfills, transpiling JSX)? Yes
    ? Pick a linter / formatter config: Standard
    ? Pick additional lint features: Lint on save
    ? Where do you prefer placing config for Babel, ESLint, etc.? In dedicated config files
    ? Save this as a preset for future projects? No

Ça marche, ainsi que `npm run serve`.

Du coup, est-ce que j'ai vraiment besoin de TypeScript ? En fait c'est Babel qui fait tout le boulot, et qui assure qu'on va pas s'embêter avec le javascript qui fonctionne différemment selon les navigateurs.

Réflexion, lecture, inspiration :

 - https://iamturns.com/typescript-babel/
 - https://blogs.infinitesquare.com/posts/web/babel-et-typescript-et-si-c-etait-simple
 - https://vuejs.org/v2/guide/typescript.html


**Architectural Decision Record** : pour l'instant, on utilise Vue avec TypeScript, mais on ne fait pas les préconisations indiquées dans les deux premiers liens. C'est peut-être pas nécessaire parce que tout serait (hypothétiquement configuré et intégré comme il faut avec Vue).

Et on verra plus tard quand on connaîtra un peu mieux tout ce fatras.

Ça me semble à priori plus simple d'enlever le TypeScript si on s'aperçoit que c'était pas la bonne solution, que de le rajouter si on s'aperçoit que c'était pas la bonne solution de pas l'avoir.


## Vue avec des canvas

https://medium.com/@scottmatthew/using-html-canvas-with-vue-js-493e5ae60887

https://codepen.io/integrateus/pen/dyyVbJZ


## Création du projet

Le problème c'est que j'ai déjà le repo git du code, et il faut que je crée un projet à partir de zéro, ce qui va créer un nouveau répertoire qui devrait être mon répertoire git.

C'est toujours un peu relou, ça.

Ça marche comme ça (et tant pis si c'est pas du tout l'usage ni la bonne pratique) :

 - dans un répertoire bidon, genre C:\Recher\temp, créer un projet vue+typescript, intitulé "squarity-code".
 - copier tout le bazar dans le repo git initial squarity-code.
 - faire un commit.
 - tester rapidement que ça marche comme les projets précédents (`npm run serve`, les modifs sont prises en compte en live).

La config du projet est la même que le précédent test :

    C:\Recher\personnel\temp
    λ vue create squarity-code
    Vue CLI v4.4.1
    ┌─────────────────────────────────────────┐
    │                                         │
    │   New version available 4.4.1 → 4.4.4   │
    │    Run npm i -g @vue/cli to update!     │
    │                                         │
    └─────────────────────────────────────────┘

    ? Please pick a preset: Manually select features
    ? Check the features needed for your project: Babel, TS, Linter
    ? Use class-style component syntax? No
    ? Use Babel alongside TypeScript (required for modern mode, auto-detected polyfills, transpiling JSX)? Yes
    ? Pick a linter / formatter config: Standard
    ? Pick additional lint features: Lint on save
    ? Where do you prefer placing config for Babel, ESLint, etc.? In dedicated config files
    ? Save this as a preset for future projects? No

    Vue CLI v4.4.1
    ✨  Creating project in C:\Recher\personnel\temp\squarity-code.
    �  Initializing git repository...
    ⚙️  Installing CLI plugins. This might take a while...
    > yorkie@2.0.0 install C:\Recher\personnel\temp\squarity-code\node_modules\yorkie
    > node bin/install.js
    setting up Git hooks
    done
    > core-js@3.6.5 postinstall C:\Recher\personnel\temp\squarity-code\node_modules\core-js
    > node -e "try{require('./postinstall')}catch(e){}"
    > ejs@2.7.4 postinstall C:\Recher\personnel\temp\squarity-code\node_modules\ejs
    > node ./postinstall.js
    added 1243 packages from 855 contributors in 40.9s
    43 packages are looking for funding
    run `npm fund` for details
    �  Invoking generators...
    �  Installing additional dependencies...
    added 108 packages from 58 contributors in 16.157s
    55 packages are looking for funding
    run `npm fund` for details
    ⚓  Running completion hooks...
    �  Generating README.md...
    �  Successfully created project squarity-code.
    �  Get started with the following commands:
    $ cd squarity-code
    $ npm run serve


## Truc bizarre avec Vetur

J'ai créé une classe contenant une méthode `getTheA`.

Dans le fichier `App.vue`, je déclare un objet ayant cette classe, et j'utilise cette méthode.

Le code se lance bien. Pas d'erreur dans les logs du serveur, ni dans la page web. La méthode exécute bien ce que je lui demande.

Mais dans VSCode, j'ai ce message : "Property 'getTheA' does not exist on type 'BoardModel' Vetur (2339)".

Apparemment, c'est un bug dans l'extension Vetur :

https://github.com/vuejs/vetur/issues/1242
https://github.com/vuejs/vetur/issues/1414
https://github.com/vuejs/vetur/issues/1834

Pour corriger, j'ai activé puis désactivé l'option "vetur.experimental.templateInterpolationService".

Puis j'ai arrêté-relancé VSCode.

C'est bizarre, et l'erreur risque de revenir. On fera d'autres tests à ce moment là.


## fonction "require"

Vue connait cette fonction.

Le code `console.log('paf ' + require('../assets/logo.png'))` affiche le texte `paf /img/logo.82b9c7a5.png` dans la console. C'est ce que je veux.

Mais VSCode considère que la fonction "require" est inconnue.

> Cannot find name 'require'. Do you need to install type definitions for node? Try `npm i @types/node` .Vetur(2580)

Et c'est clairement TypeScript qui fait son relou. Parce que la même ligne de code dans le projet "test-vue", qui n'est pas typescript, n'affiche pas d'erreurs. Et elle marche tout aussi bien.

Tentative de faire des trucs, avec ces docs :

https://vuejs.org/v2/guide/typescript.html
https://github.com/vuejs/vue/issues/8406

Mais j'arrive à rien.

Dans le repo squarity-code, le commit 4e2b26ccac25b078bc9ae2a46daaab15f7c5c549 est le résultat final de mes tentatives de faire du TypeScript.

Lorsqu'on lance le serveur (npm run serve), on n'a aucun message d'erreur, ni dans les logs du serveur, ni dans la page web.

Mais on a ce message d'erreur obscur dans la console.

```
componentNormalizer.js?2877:24 Uncaught TypeError: Cannot set property 'render' of undefined
    at normalizeComponent (componentNormalizer.js?2877:24)
    at eval (GameBoard.vue?4915:9)
    at Module../src/components/GameBoard.vue (app.js:1158)
    at __webpack_require__ (app.js:849)
    at fn (app.js:151)
    at eval (App.vue?ec60:10)
    at Module../node_modules/cache-loader/dist/cjs.js?!./node_modules/babel-loader/lib/index.js!./node_modules/ts-loader/index.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/App.vue?vue&type=script&lang=ts& (app.js:938)
    at __webpack_require__ (app.js:849)
    at fn (app.js:151)
    at eval (App.vue?96c8:1)
```

De plus, avec le code TypeScript, la complétion automatique de VSCode donne un peu n'importe quoi. Ce qui laisse penser que ma config actuelle de VSCode ne comprend rien à TypeScript.

**Architectural Decision Record** : on vire TypeScript. On refait un projet Vue de zéro, sans TypeScript. Je m'y connais pas encore assez dans toutes ces javascripteries pour attaquer à la fois Vue et TypeScript.

Donc on refait la technique pourrie de création d'un projet.


    c:\Recher\personnel\temp
    λ vue create squarity-code
    Vue CLI v4.4.1
    ┌─────────────────────────────────────────┐
    │                                         │
    │   New version available 4.4.1 → 4.4.4   │
    │    Run npm i -g @vue/cli to update!     │
    │                                         │
    └─────────────────────────────────────────┘
    ? Please pick a preset: default (babel, eslint)
    Vue CLI v4.4.1
    ✨  Creating project in c:\Recher\personnel\temp\squarity-code.
    �  Initializing git repository...
    ⚙️  Installing CLI plugins. This might take a while...
    > yorkie@2.0.0 install c:\Recher\personnel\temp\squarity-code\node_modules\yorkie
    > node bin/install.js
    setting up Git hooks
    done
    > core-js@3.6.5 postinstall c:\Recher\personnel\temp\squarity-code\node_modules\core-js
    > node -e "try{require('./postinstall')}catch(e){}"
    > ejs@2.7.4 postinstall c:\Recher\personnel\temp\squarity-code\node_modules\ejs
    > node ./postinstall.js
    added 1218 packages from 847 contributors in 44.857s
    42 packages are looking for funding
    run `npm fund` for details
    �  Invoking generators...
    �  Installing additional dependencies...
    added 53 packages from 36 contributors in 14.794s
    45 packages are looking for funding
    run `npm fund` for details
    ⚓  Running completion hooks...
    �  Generating README.md...
    �  Successfully created project squarity-code.
    �  Get started with the following commands:
    $ cd squarity-code
    $ npm run serve

Puis on copie tout dans le vrai repo existant, en remplaçant tout le bazar existant (sauf le répertoie .git, évidemment).

Juste pour marquer le coup, et aussi parce que le nom de ce fichier est devenu obsolète, la suite des aventures va se passer ici : [vue_apprentissage.md](vue_apprentissage.md).

