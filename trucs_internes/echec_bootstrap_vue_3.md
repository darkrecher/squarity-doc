## Ajout de Bootstrap (échec)

Ça n'a pas marché et je suis revenu en arrière après. Je laisse mes commandes ici pour la traçabilité, mais honnêtement, ce fichier de doc ne sert à rien.


On va relancer les mêmes commandes que en Vue 2. Avec du bol, ça va le faire.

Oups, ne pas oublier de se mettre dans le bon répertoire avant d'ajouter Vue dans le projet.

`cd ..`
`cd squarity-code/`

`npm install bootstrap-vue`

    npm WARN deprecated popper.js@1.16.1: You can find the new Popper v2 at @popperjs/core, this package is dedicated to the legacy v1

    added 15 packages, and audited 152 packages in 998ms

    30 packages are looking for funding
    run `npm fund` for details

    found 0 vulnerabilities

`npm install bootstrap`

    added 2 packages, changed 1 package, and audited 154 packages in 551ms

    32 packages are looking for funding
    run `npm fund` for details

    found 0 vulnerabilities

`vue add bootstrap-vue`

    Command 'vue' not found, but can be installed with:
    sudo snap install vue

**Fuck ! Bootstrap-Vue est pas compatible Vue 3**

https://bootstrap-vue.org/
https://www.techiediaries.com/vue-bootstrap/
https://bootstrap-vue.org/vue3

On essaiera avec Vuetify. Ça a l'air compatible Vue3, et il y a du responsive design dedans.

On va donc désinstaller tout le bordel qu'on vient d'installer.

(entre temps, installation de vue-cli, voir la doc principale)


`vue add bootstrap-vue`

    WARN  There are uncommitted changes in the current repository, it's recommended to commit or stash them first.
    ? Still proceed? Yes

    📦  Installing vue-cli-plugin-bootstrap-vue...

    added 1 package, removed 5 packages, and audited 150 packages in 1s

    31 packages are looking for funding
    run `npm fund` for details

    found 0 vulnerabilities
    ✔  Successfully installed plugin: vue-cli-plugin-bootstrap-vue

    ? Use babel/polyfill? Yes
    ? Use scss? No

    🚀  Invoking generator for vue-cli-plugin-bootstrap-vue...
    WARN  conflicting versions for project dependency "bootstrap":

        - ^5.3.0 injected by generator "undefined"
        - ^4.5.2 injected by generator "vue-cli-plugin-bootstrap-vue"

        Using newer version (^5.3.0), but this may cause build errors.
    📦  Installing additional dependencies...

    added 29 packages, removed 1 package, and audited 178 packages in 3s

    35 packages are looking for funding
    run `npm fund` for details

    found 0 vulnerabilities
    ⚓  Running completion hooks...

    ✔  Successfully invoked generator for plugin: vue-cli-plugin-bootstrap-vue

Démarrage du serveur avec `npm run dev`. Ça pète. J'ai plein de message d'erreurs comme ça.

    ✘ [ERROR] No matching export in "node_modules/vue/dist/vue.runtime.esm-bundler.js" for import "default"

        node_modules/portal-vue/dist/portal-vue.esm.js:13:7:
        13 │ import Vue from 'vue';

    {
    detail: undefined,
    id: '',
    location: {
        column: 7,
        file: 'node_modules/portal-vue/dist/portal-vue.esm.js',
        length: 3,
        line: 13,
        lineText: "import Vue from 'vue';",
        namespace: '',
        suggestion: ''
    },
    notes: [],
    pluginName: '',
    text: 'No matching export in "node_modules/vue/dist/vue.runtime.esm-bundler.js" for import "default"'
    }

bootstrap est donc un échec. On va tout virer, tout désinstaller et vraiment essayer de passer à Vuetify.


`npm uninstall bootstrap-vue`

    npm ERR! code ERESOLVE
    npm ERR! ERESOLVE could not resolve
    npm ERR!
    npm ERR! While resolving: portal-vue@2.1.7
    npm ERR! Found: vue@3.3.4
    npm ERR! node_modules/vue
    npm ERR!   peer vue@"^3.2.25" from @vitejs/plugin-vue@4.2.3
    npm ERR!   node_modules/@vitejs/plugin-vue
    npm ERR!     dev @vitejs/plugin-vue@"^4.2.3" from the root project
    npm ERR!   peer vue@"3.3.4" from @vue/server-renderer@3.3.4
    npm ERR!   node_modules/@vue/server-renderer
    npm ERR!     @vue/server-renderer@"3.3.4" from vue@3.3.4
    npm ERR!   2 more (vue-router, the root project)
    npm ERR!
    npm ERR! Could not resolve dependency:
    npm ERR! peer vue@"^2.5.18" from portal-vue@2.1.7
    npm ERR! node_modules/portal-vue
    npm ERR!   portal-vue@"^2.1.7" from bootstrap-vue@2.23.1
    npm ERR!   node_modules/bootstrap-vue
    npm ERR!   portal-vue@"^2.1.7" from the root project
    npm ERR!
    npm ERR! Conflicting peer dependency: vue@2.7.14
    npm ERR! node_modules/vue
    npm ERR!   peer vue@"^2.5.18" from portal-vue@2.1.7
    npm ERR!   node_modules/portal-vue
    npm ERR!     portal-vue@"^2.1.7" from bootstrap-vue@2.23.1
    npm ERR!     node_modules/bootstrap-vue
    npm ERR!     portal-vue@"^2.1.7" from the root project
    npm ERR!
    npm ERR! Fix the upstream dependency conflict, or retry
    npm ERR! this command with --force, or --legacy-peer-deps
    npm ERR! to accept an incorrect (and potentially broken) dependency resolution.
    npm ERR!
    npm ERR! See /home/wilfried/.npm/eresolve-report.txt for a full report.

    npm ERR! A complete log of this run can be found in:
    npm ERR!     /home/wilfried/.npm/_logs/2023-07-04T21_56_23_835Z-debug-0.log

Zut.

`npm uninstall bootstrap`

    npm ERR! code ERESOLVE
    npm ERR! ERESOLVE could not resolve
    npm ERR!
    npm ERR! While resolving: portal-vue@2.1.7
    npm ERR! Found: vue@3.3.4
    npm ERR! node_modules/vue
    npm ERR!   peer vue@"^3.2.25" from @vitejs/plugin-vue@4.2.3
    npm ERR!   node_modules/@vitejs/plugin-vue
    npm ERR!     dev @vitejs/plugin-vue@"^4.2.3" from the root project
    npm ERR!   peer vue@"3.3.4" from @vue/server-renderer@3.3.4
    npm ERR!   node_modules/@vue/server-renderer
    npm ERR!     @vue/server-renderer@"3.3.4" from vue@3.3.4
    npm ERR!   2 more (vue-router, the root project)
    npm ERR!
    npm ERR! Could not resolve dependency:
    npm ERR! peer vue@"^2.5.18" from portal-vue@2.1.7
    npm ERR! node_modules/portal-vue
    npm ERR!   portal-vue@"^2.1.7" from bootstrap-vue@2.23.1
    npm ERR!   node_modules/bootstrap-vue
    npm ERR!     bootstrap-vue@"^2.23.1" from the root project
    npm ERR!   portal-vue@"^2.1.7" from the root project
    npm ERR!
    npm ERR! Conflicting peer dependency: vue@2.7.14
    npm ERR! node_modules/vue
    npm ERR!   peer vue@"^2.5.18" from portal-vue@2.1.7
    npm ERR!   node_modules/portal-vue
    npm ERR!     portal-vue@"^2.1.7" from bootstrap-vue@2.23.1
    npm ERR!     node_modules/bootstrap-vue
    npm ERR!       bootstrap-vue@"^2.23.1" from the root project
    npm ERR!     portal-vue@"^2.1.7" from the root project
    npm ERR!
    npm ERR! Fix the upstream dependency conflict, or retry
    npm ERR! this command with --force, or --legacy-peer-deps
    npm ERR! to accept an incorrect (and potentially broken) dependency resolution.
    npm ERR!
    npm ERR! See /home/wilfried/.npm/eresolve-report.txt for a full report.

    npm ERR! A complete log of this run can be found in:
    npm ERR!     /home/wilfried/.npm/_logs/2023-07-04T21_56_56_145Z-debug-0.log

re zut.

Bon, j'ai bien fait de commiter juste avant. Y'a plus qu'à annuler toutes les modifs en cours dans git, et ça devrait aller.

C'est juste devenu le bordel dans mon répertoire node_modules, mais on s'en fout un peu.

Le projet remarche comme avant, c'est déjà ça.

Ça aurait quand même été plus simple que j'ai un message d'avertissement dès le début pour me dire que c'est pas compatible Vue 3 et que j'ai qu'à trouver une autre solution.

Gestion de package de zouzou, Front-end de zouzou.

