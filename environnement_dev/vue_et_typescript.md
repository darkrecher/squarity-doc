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
    C:\Users\recher\AppData\Roaming\npm\npm -> C:\Users\recher\AppData\Roaming\npm\node_modules\npm\bin\npm-cli.jsC:\Users\recher\AppData\Roaming\npm\npx -> C:\Users\recher\AppData\Roaming\npm\node_modules\npm\bin\npx-cli.js+ npm@6.14.5
    added 435 packages from 873 contributors in 21.238s
    λ npm -v
    6.14.5

