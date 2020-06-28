# Apprentissage de Vue

(sans TypeScript)

## asynchrone, async, await

Je m'étais toujours mélangé les pinceaux avec ces trucs.

Voici un lien vers une explication qui tient la route : https://openclassrooms.com/fr/courses/5543061-ecrivez-du-javascript-pour-le-web/5577676-gerez-du-code-asynchrone

Merci !!


## Tilesets sympa

Pour un peu tout et n'importe quoi

https://opengameart.org/content/2d-sci-fi-platformer-tileset-16x16
https://opengameart.org/content/classic-rpg-tileset
https://opengameart.org/content/wang-3-edge-walkways-tileset
https://opengameart.org/content/tiny16-tileset
https://opengameart.org/content/top-sci-fi-cga-tileset
https://opengameart.org/content/steampunk-brick-new-connecting-tileset-16x16
https://opengameart.org/content/dungeon-tileset

https://opengameart.org/users/buch


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

