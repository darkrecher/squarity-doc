# Passage à Vue 3

## Réinstallation de nodejs et npm

npm et node ont déjà été installé sur ma toute belle machine Linux Ubuntu. (Voir doc de mise en prod).

`node -v`
v12.22.9
`npm -v`
8.5.1

`npm init vue@latest`

Ça marche pas bien.

    Need to install the following packages:
    create-vue@latest
    Ok to proceed? (y) y
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: 'create-vue@3.7.1',
    npm WARN EBADENGINE   required: { node: '>=v16.20.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    /home/recher/.npm/_npx/2f7e7bff16d1c534/node_modules/create-vue/outfile.cjs:4663
    const isFeatureFlagsUsed = typeof (argv.default ?? argv.ts ?? argv.jsx ?? argv.router ?? argv.pinia ?? argv.tests ?? argv.vitest ?? argv.cypress ?? argv.nightwatch ?? argv.playwright ?? argv.eslint) === "boolean";
                                                    ^

    SyntaxError: Unexpected token '?'
        at wrapSafe (internal/modules/cjs/loader.js:915:16)
        at Module._compile (internal/modules/cjs/loader.js:963:27)
        at Object.Module._extensions..js (internal/modules/cjs/loader.js:1027:10)
        at Module.load (internal/modules/cjs/loader.js:863:32)
        at Function.Module._load (internal/modules/cjs/loader.js:708:14)
        at Function.executeUserEntryPoint [as runMain] (internal/modules/run_main.js:60:12)
        at internal/main/run_main_module.js:17:47
    npm ERR! code 1
    npm ERR! path /home/recher/Documents/personnel/squarity/squarity-code
    npm ERR! command failed
    npm ERR! command sh -c create-vue

    npm ERR! A complete log of this run can be found in:
    npm ERR!     /home/recher/.npm/_logs/2023-06-22T21_12_20_065Z-debug-0.log

Il faut installer nvm, pour pouvoir ensuite mettre node à jour.

`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash`

    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
    100 15916  100 15916    0     0   138k      0 --:--:-- --:--:-- --:--:--  138k
    => Downloading nvm from git to '/home/recher/.nvm'
    => Cloning into '/home/recher/.nvm'...
    remote: Enumerating objects: 360, done.
    remote: Counting objects: 100% (360/360), done.
    remote: Compressing objects: 100% (306/306), done.
    remote: Total 360 (delta 40), reused 170 (delta 28), pack-reused 0
    Receiving objects: 100% (360/360), 219.83 KiB | 1.62 MiB/s, done.
    Resolving deltas: 100% (40/40), done.
    * (HEAD detached at FETCH_HEAD)
    master
    => Compressing and cleaning up git repository

    => Appending nvm source string to /home/recher/.bashrc
    => Appending bash_completion source string to /home/recher/.bashrc
    => Close and reopen your terminal to start using nvm or run the following to use it now:

    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

`nvm --version`
0.39.3

La commande `nvm ls` ne donne rien d'intéressant. La commande `nvm ls-remote` liste toutes les versions disponibles de node. Ça fait un gros tas de trucs.

`nvm install 16.20.1`

    Downloading and installing node v16.20.1...
    Downloading https://nodejs.org/dist/v16.20.1/node-v16.20.1-linux-x64.tar.xz...
    ########################################################################################################################################### 100,0%
    Computing checksum with sha256sum
    Checksums matched!
    Now using node v16.20.1 (npm v8.19.4)
    Creating default alias: default -> 16.20.1 (-> v16.20.1)

`nvm ls`

    ->     v16.20.1
            system
    default -> 16.20.1 (-> v16.20.1)
    iojs -> N/A (default)
    unstable -> N/A (default)
    node -> stable (-> v16.20.1) (default)
    stable -> 16.20 (-> v16.20.1) (default)
    lts/* -> lts/hydrogen (-> N/A)
    lts/argon -> v4.9.1 (-> N/A)
    lts/boron -> v6.17.1 (-> N/A)
    lts/carbon -> v8.17.0 (-> N/A)
    lts/dubnium -> v10.24.1 (-> N/A)
    lts/erbium -> v12.22.12 (-> N/A)
    lts/fermium -> v14.21.3 (-> N/A)
    lts/gallium -> v16.20.1
    lts/hydrogen -> v18.16.1 (-> N/A)

`node --version`
v16.20.1

## Création d'un nouveau projet Vue 3

`npm init vue@latest`

Vue.js - The Progressive JavaScript Framework

✔ Project name: … squarity-code
✔ Add TypeScript? … *No* / Yes
✔ Add JSX Support? … *No* / Yes
✔ Add Vue Router for Single Page Application development? … No / *Yes*
✔ Add Pinia for state management? … *No* / Yes
✔ Add Vitest for Unit Testing? … *No* / Yes
✔ Add an End-to-End Testing Solution? › *No*
✔ Add ESLint for code quality? … No / *Yes*
✔ Add Prettier for code formatting? … *No* / Yes

Scaffolding project in /home/recher/Documents/personnel/squarity/squarity-code/squarity-code...

Done. Now run:

  cd squarity-code
  npm install
  npm run dev

Tout a été créé dans un répertoire "squarity-code/squarity-code". C'est relou. On déplace tout un répertoire au-dessus, en espérant que ça fasse pas tout péter.

`mv squarity-code/* .`

`pwd`
~/Documents/personnel/squarity/squarity-code

`ll`

    total 48
    drwxrwxr-x 7   4096 juin  22 23:40 ./
    drwxrwxr-x 5   4096 juin  19 22:43 ../
    drwxrwxr-x 8   4096 juin  22 23:31 .git/
    -rw-rw-r-- 1    230 juin  19 22:43 .gitignore
    -rw-rw-r-- 1    331 juin  22 23:35 index.html
    drwxrwxr-x 4   4096 juin  22 23:00 old_project_vue2/
    -rw-rw-r-- 1    471 juin  22 23:35 package.json
    drwxrwxr-x 2   4096 juin  22 23:35 public/
    -rw-rw-r-- 1    706 juin  22 23:35 README.md
    drwxrwxr-x 3   4096 juin  22 23:40 squarity-code/
    drwxrwxr-x 6   4096 juin  22 23:35 src/
    -rw-rw-r-- 1    309 juin  22 23:35 vite.config.js

`npm install`

    added 135 packages, and audited 136 packages in 14s

    28 packages are looking for funding
    run `npm fund` for details

    found 0 vulnerabilities

`npm run dev`

    VITE v4.3.9  ready in 203 ms

    ➜  Local:   http://localhost:5173/
    ➜  Network: use --host to expose
    ➜  press h to show help

Ça fonctionne, on voit le site par défaut.


## Réintégration de tout mon code dans ce nouveau projet.

Au départ, il suffit de remettre le component principal (GameBoard) dans la vue principale (HomeView). Et il faut aussi copier les fichiers de l'ancien projet dans le nouveau.

Concrètement, c'est pas si simple. Il y a plein de choses qui changent (en particulier, on n'utilise plus le mot-clé `require`).

Je vais pas tout décrire, mais il suffit de voir le code du nouveau projet.

Première version, qui affiche des trucs, mais pas le jeu. Commit : a7f6d40982, du repository squarity-code.

Le chargement du fichier `pyodide.js` ne se fait pas. C'est normal, il manque un plugin. J'avais pris ce truc : https://www.npmjs.com/package/vue-plugin-load-script

Let's go !

`npm install --save vue-plugin-load-script@^2.x.x`

    added 1 package, and audited 137 packages in 2s

    28 packages are looking for funding
    run `npm fund` for details

    2 moderate severity vulnerabilities

    To address all issues, run:
    npm audit fix

    Run `npm audit` for details.

`npm audit`

    # npm audit report

    word-wrap  *
    Severity: moderate
    word-wrap vulnerable to Regular Expression Denial of Service - https://github.com/advisories/GHSA-j8xg-fqg3-53r7
    fix available via `npm audit fix`
    node_modules/word-wrap
    optionator  0.8.3 - 0.9.1
    Depends on vulnerable versions of word-wrap
    node_modules/optionator

    2 moderate severity vulnerabilities

    To address all issues, run:
    npm audit fix

On fera les fix après. Déjà faut que ça marche.

Ça marche pas immédiatement. Mais après quelques modifs dans le code, tout va bien. Je vois le jeu du sorcier et le jeu de H2O dans l'interface !!

`npm audit fix`

    added 1 package, removed 1 package, changed 1 package, and audited 137 packages in 806ms

    28 packages are looking for funding
    run `npm fund` for details

    found 0 vulnerabilities

OK. Il reste encore plein de trucs à régler (bootstrap, responsive, le router, ...). Mais avec ce commit : 5b504f0c, les jeux fonctionnent.


## Ajout de Bootstrap (échec)

C'était pas une bonne idée. Je l'ai enlevé juste après.

Pour plus de détail, voir doc `echec_boostrap_vue_3.md`


## Vue-cli

Faudrait aussi installer le vue-cli. Un truc que j'aurais dû faire depuis le début.

`npm install --global @vue/cli`

    npm WARN deprecated source-map-url@0.4.1: See https://github.com/lydell/source-map-url#deprecated
    npm WARN deprecated urix@0.1.0: Please see https://github.com/lydell/urix#deprecated
    npm WARN deprecated resolve-url@0.2.1: https://github.com/lydell/resolve-url#deprecated
    npm WARN deprecated source-map-resolve@0.5.3: See https://github.com/lydell/source-map-resolve#deprecated
    npm WARN deprecated apollo-server-plugin-base@3.7.2: The `apollo-server-plugin-base` package is part of Apollo Server v2 and v3, which are now deprecated (end-of-life October 22nd 2023). This package's functionality is now found in the `@apollo/server` package. See https://www.apollographql.com/docs/apollo-server/previous-versions/ for more details.
    npm WARN deprecated apollo-server-env@4.2.1: The `apollo-server-env` package is part of Apollo Server v2 and v3, which are now deprecated (end-of-life October 22nd 2023). This package's functionality is now found in the `@apollo/utils.fetcher` package. See https://www.apollographql.com/docs/apollo-server/previous-versions/ for more details.
    npm WARN deprecated apollo-datasource@3.3.2: The `apollo-datasource` package is part of Apollo Server v2 and v3, which are now deprecated (end-of-life October 22nd 2023). See https://www.apollographql.com/docs/apollo-server/previous-versions/ for more details.
    npm WARN deprecated apollo-reporting-protobuf@3.4.0: The `apollo-reporting-protobuf` package is part of Apollo Server v2 and v3, which are now deprecated (end-of-life October 22nd 2023). This package's functionality is now found in the `@apollo/usage-reporting-protobuf` package. See https://www.apollographql.com/docs/apollo-server/previous-versions/ for more details.
    npm WARN deprecated apollo-server-errors@3.3.1: The `apollo-server-errors` package is part of Apollo Server v2 and v3, which are now deprecated (end-of-life October 22nd 2023). This package's functionality is now found in the `@apollo/server` package. See https://www.apollographql.com/docs/apollo-server/previous-versions/ for more details.
    npm WARN deprecated apollo-server-types@3.8.0: The `apollo-server-types` package is part of Apollo Server v2 and v3, which are now deprecated (end-of-life October 22nd 2023). This package's functionality is now found in the `@apollo/server` package. See https://www.apollographql.com/docs/apollo-server/previous-versions/ for more details.
    npm WARN deprecated subscriptions-transport-ws@0.11.0: The `subscriptions-transport-ws` package is no longer maintained. We recommend you use `graphql-ws` instead. For help migrating Apollo software to `graphql-ws`, see https://www.apollographql.com/docs/apollo-server/data/subscriptions/#switching-from-subscriptions-transport-ws    For general help using `graphql-ws`, see https://github.com/enisdenjo/graphql-ws/blob/master/README.md
    npm WARN deprecated apollo-server-core@3.12.0: The `apollo-server-core` package is part of Apollo Server v2 and v3, which are now deprecated (end-of-life October 22nd 2023). This package's functionality is now found in the `@apollo/server` package. See https://www.apollographql.com/docs/apollo-server/previous-versions/ for more details.
    npm WARN deprecated apollo-server-express@3.12.0: The `apollo-server-express` package is part of Apollo Server v2 and v3, which are now deprecated (end-of-life October 22nd 2023). This package's functionality is now found in the `@apollo/server` package. See https://www.apollographql.com/docs/apollo-server/previous-versions/ for more details.

    added 864 packages, and audited 865 packages in 41s

    66 packages are looking for funding
    run `npm fund` for details

    21 vulnerabilities (16 moderate, 5 high)

    To address issues that do not require attention, run:
    npm audit fix

    To address all issues (including breaking changes), run:
    npm audit fix --force

    Run `npm audit` for details.

Ça met un gros bazar, comme d'hab'.

`vue --version`

    @vue/cli 5.0.8

Youpi.


## Ajout de Vuetify

Inspiration : https://vuetifyjs.com/en/getting-started/installation/

`npm add vuetify`

    added 1 package, removed 41 packages, and audited 138 packages in 15s

    29 packages are looking for funding
    run `npm fund` for details

    found 0 vulnerabilities

Il faut faire quelques modifs dans le code pour que la gestion du responsive design fonctionne comme avant. En gros : écrire `v-col` et `v-row` au lieu de `b-col` et `b-row`.

Commit : 41b094cb, du repository squarity-code.

