# Apprentissage de Vue

(sans TypeScript)

## asynchrone, async, await

Je m'étais toujours mélangé les pinceaux avec ces trucs.

Voici un lien vers une explication qui tient la route : https://openclassrooms.com/fr/courses/5543061-ecrivez-du-javascript-pour-le-web/5577676-gerez-du-code-asynchrone

Merci !!


## ESLint

C'est un Linter javascript, qui permet de garantir les conventions d'écriture de code. Et que donc, on ne code pas comme un porcassou.

Inspirations :

 - https://vuejs.github.io/eslint-plugin-vue/user-guide/#installation
 - https://eslint.org/docs/user-guide/configuring

Il est déjà installé quand on crée un projet Vue par défaut.

Pour lancer la vérification et correction du code sur l'ensemble du projet .

```
C:\Recher\personnel\squarity-code (master -> origin)
λ npm run lint

> squarity-code@0.1.0 lint C:\Recher\personnel\squarity-code
> vue-cli-service lint

 DONE  No lint errors found!
```

Mais par défaut, ESLint ne vérifie pas grand chose, à part l'absence d'erreur de syntaxe. J'ai testé avec des indentations incorrectes, et lignes de code très moches, comme : `this .    tiles   =[            ]`. Ça ne le traumatise absolument pas.

Il faut modifier la config d'ESLint. Par exemple, voici la doc pour définir la règle pour les indentations, par exemple : https://eslint.org/docs/rules/indent

Dans le fichier `package.json` se trouve déjà un élément `eslintConfig`, contenant lui-même un élément `rules`, qui est vide.

On ajoute ceci dans rules : `"indent": ["error", 2]`.

Puis on relance le linter.

```
C:\Recher\personnel\squarity-code (master -> origin)
λ npm run lint

> squarity-code@0.1.0 lint C:\Recher\personnel\squarity-code
> vue-cli-service lint

The following files have been auto-fixed:

  src\classes\BoardModel.js
  src\components\GameBoard.vue

 DONE  All lint errors auto-fixed.
```

Les défauts d'indentations dans le javascript ont été corrigées dans les deux fichiers. Mais les erreurs d'indentations des templates HTML, et mes autres lignes de code moches n'ont pas été modifiées.

C'est bien, mais si on pouvait avoir un ruleset prédefini de eslint, ce serait cool. Parce que je vais pas tout me configurer un par un.

https://eslint.vuejs.org/rules/

Dans `package.json`, remplacement de la ligne `"plugin:vue/essential",` par `"plugin:vue/recommended",`.

Le lintage me lève un warning concernant la définition des props. Corrigé grâce à ce qui est indiqué ici : https://stackoverflow.com/questions/40365741/default-values-for-vue-component-props-how-to-check-if-a-user-did-not-set-the .

Ça corrige des choses en plus, dont l'indentation mal fichue dans le HTML. Mais ça corrige pas ma fameuse ligne de code moche mentionnée plus haut.

Apparamment, il y a plein de gens qui disent que les conventions de codage JS de airbnb sont trop la classe. https://travishorn.com/setting-up-eslint-on-vs-code-with-airbnb-javascript-style-guide-6eb78a535ba6

Y'a qu'à partir là-dessus.

```
C:\Recher\personnel\squarity-code (master -> origin)
λ npm i -D eslint eslint-config-airbnb-base eslint-plugin-import
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@2.1.3 (node_modules\fsevents):
npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@2.1.3: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\webpack-dev-server\node_modules\fsevents):
npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\watchpack-chokidar2\node_modules\fsevents):
npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})

+ eslint-config-airbnb-base@14.2.0
+ eslint-plugin-import@2.22.0
+ eslint@6.8.0
added 29 packages from 18 contributors, updated 29 packages and audited 1306 packages in 10.223s

48 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```

Mais peut-être que j'aurais du installer directement ça :

https://developer.aliyun.com/mirror/npm/package/@vue/eslint-config-airbnb
https://www.npmjs.com/package/@vue/eslint-config-airbnb

```
C:\Recher\personnel\squarity-code (master -> origin)
λ npm i @vue/eslint-config-airbnb
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@2.1.3 (node_modules\fsevents):
npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@2.1.3: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\watchpack-chokidar2\node_modules\fsevents):
npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\webpack-dev-server\node_modules\fsevents):
npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})

+ @vue/eslint-config-airbnb@5.1.0
added 10 packages from 11 contributors and audited 1318 packages in 8.454s

48 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```

Dans le fichier `package.json`, élément `eslintConfig`, sous-élément `extends`. On ajoute, au début de la liste : `"airbnb-base",`.

Et sinon, je remet rules à vide. Suppression de `"indent": ["error", 2]`. C'est déjà intégré dans les règles de airbnb.

Le airbnb rajoute plein de règles, dont certaines sont un peu relou. Il m'a foutu des points-virgules partout ce con !

Et sinon, il m'a viré les quotes dans mes clés du dictionnaire des tiles. Je savais même pas qu'on pouvait faire ça. Bon, c'est un détail, osef.

Si je rajoute `"semi": ["error", "never"]` dans les rules, ça vire les points-virgules, mais ça fait tout planter. Je suppose qu'il y a d'autres rules dans airbnb qui ne fonctionnent que si y'a des points-virgules. Donc on met pas cette règle. On aura des points-virgules.

On va faire avec... Quel genre de crétin fout des points-virgules quand il code ?

C'est pas fini, car il faudrait intégrer le linter dans VSCode. Mais là c'est déjà pas mal.


## Canvas

Plein de conseils pour dessiner dans des canvas de manière optimisée :

https://www.html5rocks.com/en/tutorials/canvas/performance/

Chapitres qui pourraient me concerner :

 - Pre-render to an off-screen canvas
 - Render screen differences only, not the whole new state
 - Use multiple layered canvases for complex scenes
 - Optimize your animations with `requestAnimationFrame`


## Re ESLint

Installation du module ESLint dans VSCode, via le menu des extensions.

v2.1.5

Redémarrage de VSCode, on sait jamais.

Rien à configurer, ça marche tout seul.

Lorsque j'écris des conneries, ça souligne en rouge ou en jaune, selon le niveau de connerie.

À priori, il a correctement pris la config de mon projet, car : "une connerie signalée dans VS Code <=> la même connerie indiquée dans la page web quand je sauvegarde."

Enfin presque...

Quand j'écris des conneries dans le HTML d'un fichier .vue, ça se souligne en jaune (warning).

Par exemple : `<canvas id="c" truc="machin" />`

Rien n'est affiché dans la page web quand je sauvegarde. Par contre, quand je lance la commande `npm run lint`, ça corrige automatiquement ma connerie. Et ça l'écrit comme ça :

    <canvas
      id="c"
      truc="machin"
    />

Dans les fichiers .js, le comportement est le même.

Par contre, un truc amusant : il n'y a aucun check de case, d'utilisation de variable ou d'initialisation sur les variables membres.

J'ai écrit `this.magician_x` et ça ne pose pas de problème. Je peux même le renommer en `this.magician_z` à un seul endroit, sans changer les autres occurrences du même nom. Le site ne marche plus, mais personne ne râle : ni VSCode, ni le site, ni "npm run lint".

Je suppose que c'est un choix et une convention. On va laisser comme ça.

Du coup, je me permet :

**Architectural Decision Record** : Toutes les variables membres sont en snake case, parce que c'est ça que je suis habitué à écrire, et c'est ce qui est le plus lisible. Et si les conventions et les linters l'autorisent, y'a pas de raison de s'en priver.

Et si c'est pas une bonne pratique, y'avait qu'à qu'ils configurent leurs linters pour signaler explicitement que c'est pas une bonne pratique !!

**Architectural Decision Record** : Le même qu'avant, mais en plus prononcé : tous les attribut "ref=quelque_chose", les noms de fonctions, et les variables membres sont en snake_case. C'est contraire aux conventions du javascript, mais le linter me l'autorise. Et je suis désolé, mais j'ai beaucoup trop l'habitude d'écrire des choses en snake case, et je trouve ça tellement plus lisible. Je décide donc de vraiment aller contre les conventions du javascript. C'est très vilain, mais c'est comme ça. J'espère juste que j'aurais pas à le regretter quelques années plus tard, quand d'autres personnes voudront hypothétiquement m'aider à coder ce projet.

Les noms des composants Vue restent en CamelCase. C'est comme si c'était des classes.


## Intégration de brython

Va y avoir plein de choses à dire sur le sujet.

Pour l'instant, rien n'est fixé.

Sinon que j'ai besoin d'un plugin de Vue, parce que ceci : https://stackoverflow.com/questions/45047126/how-to-add-external-js-scripts-to-vuejs-components

    C:\Recher\personnel\squarity-code (master -> origin)
    λ npm install --save vue-plugin-load-script
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@2.1.3 (node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@2.1.3: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\watchpack-chokidar2\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\webpack-dev-server\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})

    + vue-plugin-load-script@1.3.0
    added 1 package from 1 contributor and audited 1319 packages in 6.541s

    48 packages are looking for funding
      run `npm fund` for details

    found 370 low severity vulnerabilities
      run `npm audit fix` to fix them, or `npm audit` for details


## Librairie de responsive design (1)

J'ai besoin de faire ça : https://vuejsexamples.com/responsive-grid-system-based-on-bootstrap-for-vue/

Les deux moitiés de la page (la partie jeu et la partie code) doivent être côte à côte sur des grands écrans, et l'une au-dessus de l'autre sur des petits écrans.

Allez, zou !

    C:\Recher\personnel\squarity-code (master -> origin)
    λ npm install vue-grid-responsive
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\watchpack-chokidar2\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\webpack-dev-server\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@2.1.3 (node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@2.1.3: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})

    + vue-grid-responsive@0.2.0
    added 1 package from 1 contributor and audited 1320 packages in 7.174s

    48 packages are looking for funding
      run `npm fund` for details

    found 371 vulnerabilities (370 low, 1 high)
      run `npm audit fix` to fix them, or `npm audit` for details

Comme d'hab, quelques warnings anxiogènes.


## Mise à jour suite à une alerte de sécurité

J'ai github qui m'envoie un message automatique de dependabot, à propos d'une vulnérabilité dans lodash.

> Bump lodash from 4.17.15 to 4.17.19 #1

Je vais faire ça manuellement plutôt que par un merge de github, parce que ça me semble plus maîtrisable.

    C:\Recher\personnel\squarity-code (master -> origin)
    λ npm update lodash

    C:\Recher\personnel\squarity-code (master -> origin)
    λ git diff

    C:\Recher\personnel\squarity-code (master -> origin)
    λ npm install lodash
    npm ERR! code ENOENT
    npm ERR! syscall rename
    npm ERR! path C:\Recher\personnel\squarity-code\node_modules\lodash
    npm ERR! dest C:\Recher\personnel\squarity-code\node_modules\.lodash.DELETE
    npm ERR! errno -4058
    npm ERR! enoent ENOENT: no such file or directory, rename 'C:\Recher\personnel\squarity-code\node_modules\lodash' -> 'C:\Recher\personnel\squarity-code\node_modules\.lodash.DELETE'
    npm ERR! enoent This is related to npm not being able to find a file.
    npm ERR! enoent

    npm ERR! A complete log of this run can be found in:
    npm ERR!     C:\Users\wlanglois\AppData\Roaming\npm-cache\_logs\2020-08-28T22_11_31_784Z-debug.log

OK, donc c'était pas ça.

Et du coup, ça m'a fait planter mon serveur local. Merci !!

Failed to compile.

    Error: Child compilation failed:
    Module build failed: Error: ENOENT: no such file or directory, open 'C:\Recher\personnel\squarity-code\node_module  s\lodash\lodash.js':
    Error: ENOENT: no such file or directory, open 'C:\Recher\personnel\squarity-code\node_modules\lodash\lodash.js'

    - compiler.js:79 childCompiler.runAsChild
      [squarity-code]/[html-webpack-plugin]/lib/compiler.js:79:16
    - Compiler.js:343 compile
      [squarity-code]/[webpack]/lib/Compiler.js:343:11
    - Compiler.js:681 hooks.afterCompile.callAsync.err
      [squarity-code]/[webpack]/lib/Compiler.js:681:15
    - Hook.js:154 AsyncSeriesHook.lazyCompileHook
      [squarity-code]/[tapable]/lib/Hook.js:154:20
    - Compiler.js:678 compilation.seal.err
      [squarity-code]/[webpack]/lib/Compiler.js:678:31
    - Hook.js:154 AsyncSeriesHook.lazyCompileHook
      [squarity-code]/[tapable]/lib/Hook.js:154:20
    - Compilation.js:1423 hooks.optimizeAssets.callAsync.err
      [squarity-code]/[webpack]/lib/Compilation.js:1423:35
    - Hook.js:154 AsyncSeriesHook.lazyCompileHook
      [squarity-code]/[tapable]/lib/Hook.js:154:20
    - Compilation.js:1414 hooks.optimizeChunkAssets.callAsync.err
      [squarity-code]/[webpack]/lib/Compilation.js:1414:32
    - Hook.js:154 AsyncSeriesHook.lazyCompileHook
      [squarity-code]/[tapable]/lib/Hook.js:154:20
    - Compilation.js:1409 hooks.additionalAssets.callAsync.err
      [squarity-code]/[webpack]/lib/Compilation.js:1409:36

Et quand on essaie de relancer le serveur, ça pète.

    C:\Recher\personnel\squarity-code (master -> origin)
    λ npm run serve

    > squarity-code@0.1.0 serve C:\Recher\personnel\squarity-code
    > vue-cli-service serve

    internal/modules/cjs/loader.js:584
        throw err;
        ^

    Error: Cannot find module 'lodash/values'
        at Function.Module._resolveFilename (internal/modules/cjs/loader.js:582:15)
        at Function.Module._load (internal/modules/cjs/loader.js:508:25)
        at Module.require (internal/modules/cjs/loader.js:637:17)
        at require (internal/modules/cjs/helpers.js:22:18)
        at Object.<anonymous> (C:\Recher\personnel\squarity-code\node_modules\webpack-merge\lib\index.js:3:16)
        at Module._compile (internal/modules/cjs/loader.js:701:30)
        at Object.Module._extensions..js (internal/modules/cjs/loader.js:712:10)
        at Module.load (internal/modules/cjs/loader.js:600:32)
        at tryModuleLoad (internal/modules/cjs/loader.js:539:12)
        at Function.Module._load (internal/modules/cjs/loader.js:531:3)
    npm ERR! code ELIFECYCLE
    npm ERR! errno 1
    npm ERR! squarity-code@0.1.0 serve: `vue-cli-service serve`
    npm ERR! Exit status 1
    npm ERR!
    npm ERR! Failed at the squarity-code@0.1.0 serve script.
    npm ERR! This is probably not a problem with npm. There is likely additional logging output above.

    npm ERR! A complete log of this run can be found in:
    npm ERR!     C:\Users\wlanglois\AppData\Roaming\npm-cache\_logs\2020-08-28T22_17_20_743Z-debug.log

Ah, mais maintenant, quand je refais l'install, ça pète pas.

    C:\Recher\personnel\squarity-code (master -> origin)
    λ npm install lodash
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\watchpack-chokidar2\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\webpack-dev-server\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})

    + lodash@4.17.20
    added 1 package from 2 contributors and audited 1321 packages in 6.218s

    48 packages are looking for funding
      run `npm fund` for details

    found 1 high severity vulnerability
      run `npm audit fix` to fix them, or `npm audit` for details

Peut-être que j'aurais dû couper mon serveur avant de refaire l'install. Il pouvait pas gérer ça tout seul, ce gros con de npm, plutôt que de me faire flipper ?

Le serveur refonctionne.

Bon, il reste quand même une "high severity vulnerability", qui sort de je-sais-pas-où.

Je vais pas trop chercher à comprendre, et je vais faire ce qu'il dit.

    C:\Recher\personnel\squarity-code (master -> origin)
    λ npm update copy-webpack-plugin --depth 2
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\watchpack-chokidar2\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\webpack-dev-server\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})

    + copy-webpack-plugin@5.1.2
    updated 6 packages and audited 1321 packages in 5.685s

    48 packages are looking for funding
      run `npm fund` for details

    found 0 vulnerabilities

Yeaaaaaahh....

Et github ne râle plus. Cool.


## Librairie de responsive design (2)

C'est de la merde le package que j'ai installé : vue-grid-responsive

Ça fait des grid, mais ça fait pas de putain d'offset.

Je vais carrément foutre bootstrap dans la gueule, de toutes façons je sais rien utiliser d'autre que boostrap (et même ça, j'y connais que d'alle).

    C:\Recher\personnel\squarity-code (master -> origin)
    λ npm uninstall vue-grid-responsive
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\watchpack-chokidar2\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\webpack-dev-server\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})

    removed 1 package and audited 1320 packages in 5.317s

    48 packages are looking for funding
      run `npm fund` for details

    found 0 vulnerabilities

Et maintenant, bootstrap, le vrai !

    C:\Recher\personnel\squarity-code (master -> origin)
    λ npm install bootstrap-vue
    npm WARN deprecated popper.js@1.16.1: You can find the new Popper v2 at @popperjs/core, this package is dedicated to the legacy v1

    > bootstrap-vue@2.16.0 postinstall C:\Recher\personnel\squarity-code\node_modules\bootstrap-vue
    > opencollective || exit 0


                              ;iiiiiiiiiiSSSSSSSSiiiiiiiiii;
                              .rXXXXXXXXXrrrrrrrSXXXXXXXXXr.
                              :iXXXXXXXX2. ;;;;, r3XXXXXXXi;
                            ,rSSSSSXXXX2..sSSi: r3XXXSSSSSr,
                              ,siiiiS2XX2. :;;:,.rXX2Siiiis,
                              ,riiiii2X2..5XXXi .22iiiiir,
                                .riiiii22..::::,,r2iiiiir.
                                .riiiii5SSiiiiS22iiiiir.
                                  ;iiiii5X3333X5iiiii;
                                    :iiiiiSXXXXSiiiii:
                                    :siiiiSXXSiiiis:
                                      ,siiiiiiiiiis,
                                      .riiiiiiiir.
                                        .riiiiiir.
                                        .;iiii;.
                                          ;ii;
                                            ::

                          Thanks for installing bootstrap-vue
                    Please consider donating to our open collective
                            to help us maintain this package.

                              Number of contributors: 257
                                  Number of backers: 160
                                Annual budget: US$ 8,826
                                Current balance: US$ 5,813

              Donate: https://opencollective.com/bootstrap-vue/donate

    npm WARN bootstrap@4.5.2 requires a peer of jquery@1.9.1 - 3 but none is installed. You must install peer dependencies yourself.
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\webpack-dev-server\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\watchpack-chokidar2\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})

    + bootstrap-vue@2.16.0
    added 8 packages from 20 contributors and audited 1328 packages in 10.925s

    50 packages are looking for funding
      run `npm fund` for details

    found 0 vulnerabilities

Et ensuite bootstrap lui-même.

    C:\Recher\personnel\squarity-code (master -> origin)
    λ npm install bootstrap
    npm WARN bootstrap@4.5.2 requires a peer of jquery@1.9.1 - 3 but none is installed. You must install peer dependencies yourself.
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\watchpack-chokidar2\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\webpack-dev-server\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})

    + bootstrap@4.5.2
    updated 1 package and audited 1329 packages in 5.905s

    50 packages are looking for funding
      run `npm fund` for details

    found 0 vulnerabilities

Commit de la version actuelle car faut le faire avant de faire `vue add`. (Commit temporaire, qui n'apparaîtra pas dans le serveur git, car il est assez sale).

    C:\Recher\personnel\squarity-code (master -> origin)
    λ vue add bootstrap-vue

    �  Installing vue-cli-plugin-bootstrap-vue...

    + vue-cli-plugin-bootstrap-vue@0.6.0
    added 1 package from 1 contributor in 6.467s

    50 packages are looking for funding
      run `npm fund` for details

    ✔  Successfully installed plugin: vue-cli-plugin-bootstrap-vue

    ? Use babel/polyfill? No

    �  Invoking generator for vue-cli-plugin-bootstrap-vue...
    �  Installing additional dependencies...

    added 5 packages from 4 contributors in 7.386s

    51 packages are looking for funding
      run `npm fund` for details

    ⚓  Running completion hooks...

    ✔  Successfully invoked generator for plugin: vue-cli-plugin-bootstrap-vue

    C:\Recher\personnel\squarity-code (master -> origin)

(Je comprends pas grand-chose à ce que je fais, mais c'est pas grave).

N'empêche que maintenant ça marche. Mes layout de grid s'affichent bien.


## Il faut que je fasse des requêtes HTTP

La bonne pratique pour faire ça dans Vue, c'est de pas spécialement le faire avec Vue.

On met dans un fichier à part le code qui fait les requêtes HTTP, et on importe ce fichier où il faut. C'est tout.

Inspirations :

 - https://itnext.io/anyway-heres-how-to-do-ajax-api-calls-with-vue-js-e71e57d5cf12
 - https://stackoverflow.com/questions/40813975/how-to-structure-api-calls-in-vue-js
 - https://medium.com/canariasjs/vue-api-calls-in-a-smart-way-8d521812c322

Et pour ça, il semblerait que la plupart des gens utilisent axios : https://www.npmjs.com/package/axios

    C:\Recher\personnel\squarity-code (master -> origin)
    λ npm install axios
    npm WARN bootstrap@4.5.2 requires a peer of jquery@1.9.1 - 3 but none is installed. You must install peer dependencies yourself.
    npm WARN The package bootstrap is included as both a dev and production dependency.
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\webpack-dev-server\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\watchpack-chokidar2\node_modules\fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})

    + axios@0.20.0
    added 1 package from 1 contributor and audited 1337 packages in 6.479s

    51 packages are looking for funding
      run `npm fund` for details

    found 0 vulnerabilities


## Pour avoir plusieurs pages

Parce qu'il me faut quand même une autre page pour la doc. Même si actuellement, la doc, c'est pas ce que j'ai de mieux.

https://router.vuejs.org/installation.html#direct-download-cdn

Nan, on fera ça plus tard.

Pour la doc, je vais pointer directement sur la page github, parce que je suis vraiment à l'arrache.


## Installation du router vue

Comme ça je vais pourrais avoir une page de roadmap, et la page avec Squarity.

Source :

https://v3.router.vuejs.org/installation.html#npm

Attention, il est conseillé de d'abord sauvegarder le contenu du fichier App.vue, car le router modifie ce fichier, pour créer un premier exemple.

Ensuite, il faut lancer la commande `vue add router`.

    λ vue add router
    WARN  There are uncommited changes in the current repository, it's recommended to commit or stash them first.
    ? Still proceed? Yes

    �  Installing @vue/cli-plugin-router...

    + @vue/cli-plugin-router@4.4.6
    added 6 packages from 2 contributors and updated 1 package in 19.373s

    51 packages are looking for funding
      run `npm fund` for details

    ✔  Successfully installed plugin: @vue/cli-plugin-router

    ? Use history mode for router? (Requires proper server setup for index fallback in production) Yes

    �  Invoking generator for @vue/cli-plugin-router...
    �  Installing additional dependencies...

    added 1 package from 1 contributor in 10.172s

    51 packages are looking for funding
      run `npm fund` for details

    -  Running completion hooks...warning: Unexpected console statement (no-console) at src\components\DevZone.vue:150:9:
      148 |       const urlGameSpec = gameSpecLoader.url_game_spec_from_loc_hash(locHash);
      149 |       if (urlGameSpec === null) {
    > 150 |         console.log('Le hash de l\'url ne correspond pas à un lien vers une définition de jeu.');
          |         ^
      151 |       } else {
      152 |         const gameSpec = await gameSpecLoader.fetch_game_spec(urlGameSpec);
      153 |         if (gameSpec === null) {


    warning: Unexpected console statement (no-console) at src\components\DevZone.vue:154:11:
      152 |         const gameSpec = await gameSpecLoader.fetch_game_spec(urlGameSpec);
      153 |         if (gameSpec === null) {
    > 154 |           console.log('Le texte récupéré ne correspond pas à une définition de jeu.');
          |           ^
      155 |         } else {
      156 |           this.$refs.url_tileset.value = gameSpec.url_tileset;
      157 |           this.$refs.json_conf.value = gameSpec.json_conf;


    warning: Unexpected console statement (no-console) at src\components\ProgressIndicator.vue:64:7:
      62 |
      63 |     add_progress_message(msg) {
    > 64 |       console.log(`progress: ${msg}`);
        |       ^
      65 |       // On met à vide le message d'avant.
      66 |       // Sinon ça fait trop de texte à lire juste pour une barre de progress.
      67 |       this.messages[this.messages.length - 1] = ' ';


    error: Unable to resolve path to module '@/components/HelloWorld.vue' (import/no-unresolved) at src\views\Home.vue:13:24:
      11 | <script>
      12 | // @ is an alias to /src
    > 13 | import HelloWorld from '@/components/HelloWorld.vue';
        |                        ^
      14 |
      15 | export default {
      16 |   name: 'Home',

Ça ne marche pas immédiatement, il faut faire quelques modifs dans le code, pour recâbler les bons components, remettre le jeu dans la page principale, etc. Tout ceci est tracé dans le [commit 0b69e7df](https://github.com/darkrecher/squarity-code/commit/0b69e7dfb9ed3b9eea834c6945abd9073addb1cb) du repository squarity-code.


## Linting dans VSCode qui fait n'importe quoi

ESLint ne veut pas lancer mon site lorsque j'utilise des double quotes pour mes strings. Par exemple :

`import GameBoard from "../components/GameBoard.vue";`

No problem, si c'est la convention, respectons là.

Mais lorsque je sauvegarde un fichier dans VSCode, il me remet automatiquement des double quotes !

Quand j'ouvre un fichier .vue à l'arrache avec VSCode, il ne me remplace pas les double quotes. Quand j'ouvre VSCode en me plaçant dans le répertoire du projet (squarity-code), puis que je fais `code .`. Là, il remplace. VSCode doit sûrement comprendre qu'il est dans un projet de site web avec Vue, et il se comporte pas pareil. Je pense que j'avais ce problème depuis le début, mais c'est que maintenant que je le vois. (J'avais jamais ouvert mon projet en faisant "code .").

Désactivation, puis désinstallation de l'extension VSCode Vetur.

Installation de l'extension "Vue Language Features (Volar)".

C'est mieux, tout le monde est d'accord pour obliger à mettre des simple quotes.

Mais pour les attributs HTML, c'est pas encore ça.

ESLint veut que je mette comme ça (règle "vue/max-attributes-per-line") :

    <img
      alt="Vue logo"
      src="../assets/logo.png"
    >

Volar me les remet automatiquement comme ça quand je sauvegarde :

    <img alt="Vue logo" src="../assets/logo.png">

Mettez-vous d'accord, bordel !!

Quelqu'un a le même problème. https://www.reddit.com/r/vuejs/comments/se5466/having_a_tough_time_setting_up_eslintprettier_to/

J'ai essayé de créer mon propre fichier .eslintrc, ça a tout fait péter. On oublie. Dans le fichier `package.json`, il y a une partie `eslintConfig`, on peut mettre ce qu'on veut dedans. En particulier, désactiver des règles.

Explication détaillée sur le fonctionnement du fichier de config eslint : https://eslint.org/docs/latest/user-guide/configuring/configuration-files .

**Architectural Decision Record** : (c'est plus "environmental" que "architectural", mais bon). Volar a la priorité sur ESLint. D'abord parce qu'il est spécifique pour Vue, et aussi parce que je ne sais pas comment le configurer !

Quand il y a conflit entre une règle de lintage de ESLint et un formattage automatique de Volar, on désactive ou on reconfigure la règle ESLint, pour qu'il n'y ait plus le conflit.

Par exemple, dans package.json / eslintConfig / rules, j'ajoute ça : `"vue/max-attributes-per-line": "off"`. Et ESLint ne m'embête plus.

Je teste une balise HTML avec plein d'attributs, il y a encore des conflits. Hop, désactivation d'autres règles (voir directement le fichier package.json pour le détail).

Pour plus tard : ce sera bien d'essayer de passer à Vue 3. Apparemment, Vetur est pour Vue 2, Volar est pour Vue 3. https://www.reddit.com/r/vuejs/comments/pahxs4/whats_the_general_opinion_on_vetur_vs_volar/ . J'ai mis une tâche dans Trello pour ça.

Avec un peu de chance, le passage de Vue 2 à Vue 3 se fera sans trop de problèmes, parce que j'ai pas énormément de code pour l'instant.

Un dernier truc bizarre : les fichiers `gameExamples.js` et `gameSpecLoader.js` sont placés dans le même répertoire, ils ont la même extension, et contiennent le même type de donnée (du code javascript).

Et pourtant Volar ne les traite pas de la même manière. Pour `gameSpecLoader.js`, il met automatiquement une indentation à 2 espaces, et pour `gameExamples.js`, une indentation à 4 espaces. Je ne sais pas comment on le change, ni pourquoi ça fait ça.

Bien évidemment, l'indentation à 4 espaces fait râler ESLint, en plus de certaines lignes qui dépassent 120 caractères.

Ça m'embêterait de désactiver la règle des indentations juste pour un seul fichier. Et en plus, c'est pas vraiment un fichier contenant du javascript. Il contient des grandes chaînes de caractères constituant du python et du json. Donc pour ce fichier en particulier, on désactive ESLint (à l'aide d'un commentaire en première ligne). À terme (je sais juste pas à quel terme), ce fichier `gameExamples.js` sera amené à disparaître, et tout ce qu'il contient sera stocké dans un endroit un peu plus adapté.

Pfiou ! C'était pas simple de reprendre ce projet. Allez, au boulot !


## Modif linter suite à changement d'environnement de dev

Le 2023-01-09, je suis passé à Linux. J'ai dû réinstaller VSCode, mon environnement de dev, etc. Le tout est décrit en détail dans le fichier `passage_vue_3.md`.

Des tas de problèmes dû au linter se sont réglés tout seul, ne me demandez pas pourquoi ni comment. Je peux maintenant faire des boucles `for (... of ...)` sans que ça me gueule dessus, et les règles d'indentations bizarres décrites dans le chapitre précédent ne sont plus là. Et j'ai quand même un linter qui tient à peu près la route. C'est super, même si j'ai pas tout compris.

Le linter n'est plus désactivé pour `gameExamples.js`, et rien n'explose quand je lance `npm run lint`.


## Explications sur les tailles des canvas

Il y a deux tailles : la taille interne du canvas (en pixel) et la taille d'affichage dans la page (en pixel ou en autre chose).

La taille interne se définit avec les attributs HTML, la taille d'affichage se définit avec du CSS, comme d'habitude.

La mise à l'échelle entre les deux se fait toute seul, bien entendu. On peut la configurer avec du CSS, d'où le `image-rendering: pixelated;` qui se trouve dans mon code.

Source : https://webglfundamentals.org/webgl/lessons/webgl-resizing-the-canvas.html

Extrait :

> Here's an example of a canvas whose drawingbuffer is 10x15 pixels that is displayed 400x300 pixels on the page

> `<canvas id="c" width="10" height="15" style="width: 400px; height: 300px;"></canvas>`

Extraits de mes bouts de code, qui définissent la taille interne du canvas :

```
const canvasElem = this.$refs.game_canvas;
this.ctx_canvas = canvasElem.getContext('2d');
this.canvas_buffer = document.createElement('canvas');
this.ctx_canvas_buffer = this.canvas_buffer.getContext('2d');

this.canvas_width = this.nb_tile_width * this.tile_canvas_width;
this.canvas_height = this.nb_tile_height * this.tile_canvas_height;

const canvasElem = this.$refs.game_canvas;
canvasElem.width = this.canvas_width;
canvasElem.height = this.canvas_height;
this.canvas_buffer.width = this.canvas_width;
this.canvas_buffer.height = this.canvas_height;
```

Je dois le définir deux fois, pour l'objet `canvasElem` et pour l'objet `this.canvas_buffer`. J'utilise un buffer d'image interne pour dessiner les images de tile dessus, puis je balance tout le buffer dans le canvas. Pour que ce soit cohérent, ils doivent avoir tous les deux la même taille.

La taille d'affichage du canvas est définie à la fin de la fonction de la mort `handleResize`, avec ce bout de code : `this.$refs.game_canvas.style = ...`.

Ce bout de code redéfinit le CSS, et c'est bien normal.

Lien vers une autre source (qui explique pas grand chose) : https://www.w3schools.com/tags/att_canvas_width.asp .

Juste pour info : pour récupérer la taille rélle en pixel d'un élément HTML, telle qu'il est affiché dans la page : `elem.clientHeight` et `elem.clientWidth`.

