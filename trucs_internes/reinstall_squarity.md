# Réinstallation du projet squarity-code

Fait le 2024-04-25 (à peu près)

Parce que le disque dur de mon crétin de PC a crashé, alors il a fallu tout réinstallé de zéro.

Et j'ai tout fait à l'arrache, évidemment.

`recher@recher-ordi:~$ git`

```
    usage : git [--version] [--help] [-C <path>] [-c <name>=<value>]
              [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
              [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
              [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
              [--super-prefix=<path>] [--config-env=<name>=<envvar>]
              <command> [<args>]

    Ci-dessous les commandes Git habituelles dans diverses situations :
    [...]

```

`recher@recher-ordi:~$ cd Documents/`

`recher@recher-ordi:~/Documents$ cd personnel/`

`recher@recher-ordi:~/Documents/personnel$ git clone https://github.com/darkrecher/squarity-code.git`

```
    Clonage dans 'squarity-code'...
    remote: Enumerating objects: 1003, done.
    remote: Counting objects: 100% (418/418), done.
    remote: Compressing objects: 100% (228/228), done.
    remote: Total 1003 (delta 240), reused 359 (delta 184), pack-reused 585
    Réception d'objets: 100% (1003/1003), 11.08 Mio | 1.14 Mio/s, fait.
    Résolution des deltas: 100% (537/537), fait.
```

`recher@recher-ordi:~/Documents/personnel$ sudo apt install npm`

```
    [sudo] Mot de passe de recher :
    Lecture des listes de paquets... Fait
    Construction de l'arbre des dépendances... Fait
    Lecture des informations d'état... Fait
    Les paquets suivants ont été installés automatiquement et ne sont plus nécessaires :
      libwpe-1.0-1 libwpebackend-fdo-1.0-1
    Veuillez utiliser « sudo apt autoremove » pour les supprimer.
    Les paquets supplémentaires suivants seront installés :
      build-essential dpkg-dev fakeroot g++ g++-11 gcc gcc-11 gyp javascript-common libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl libasan6 libc-ares2 libc-dev-bin libc-devtools libc6-dev
      libcc1-0 libcrypt-dev libdpkg-perl libfakeroot libfile-fcntllock-perl libgcc-11-dev libitm1 libjs-events libjs-highlight.js libjs-inherits libjs-is-typedarray libjs-psl libjs-source-map libjs-sprintf-js
      libjs-typedarray-to-buffer liblsan0 libnode-dev libnode72 libnsl-dev libquadmath0 libssl-dev libstdc++-11-dev libtirpc-dev libtsan0 libubsan1 libuv1-dev linux-libc-dev lto-disabled-list make manpages-dev
      node-abab node-abbrev node-agent-base node-ansi-regex node-ansi-styles node-ansistyles node-aproba node-archy node-are-we-there-yet node-argparse node-arrify node-asap node-asynckit node-balanced-match
      node-brace-expansion node-builtins node-cacache node-chalk node-chownr node-clean-yaml-object node-cli-table node-clone node-color-convert node-color-name node-colors node-columnify node-combined-stream
      node-commander node-console-control-strings node-copy-concurrently node-core-util-is node-coveralls node-cssom node-cssstyle node-debug node-decompress-response node-defaults node-delayed-stream
      node-delegates node-depd node-diff node-encoding node-end-of-stream node-err-code node-escape-string-regexp node-esprima node-events node-fancy-log node-fetch node-foreground-child node-form-data
      node-fs-write-stream-atomic node-fs.realpath node-function-bind node-gauge node-get-stream node-glob node-got node-graceful-fs node-growl node-gyp node-has-flag node-has-unicode node-hosted-git-info
      node-https-proxy-agent node-iconv-lite node-iferr node-imurmurhash node-indent-string node-inflight node-inherits node-ini node-ip node-ip-regex node-is-buffer node-is-plain-obj node-is-typedarray
      node-isarray node-isexe node-js-yaml node-jsdom node-json-buffer node-json-parse-better-errors node-jsonparse node-kind-of node-lcov-parse node-lodash-packages node-log-driver node-lowercase-keys
      node-lru-cache node-mime node-mime-types node-mimic-response node-minimatch node-minimist node-minipass node-mkdirp node-move-concurrently node-ms node-mute-stream node-negotiator node-nopt
      node-normalize-package-data node-npm-bundled node-npm-package-arg node-npmlog node-object-assign node-once node-opener node-osenv node-p-cancelable node-p-map node-path-is-absolute node-process-nextick-args
      node-promise-inflight node-promise-retry node-promzard node-psl node-pump node-punycode node-quick-lru node-read node-read-package-json node-readable-stream node-resolve node-retry node-rimraf node-run-queue
      node-safe-buffer node-semver node-set-blocking node-signal-exit node-slash node-slice-ansi node-source-map node-source-map-support node-spdx-correct node-spdx-exceptions node-spdx-expression-parse
      node-spdx-license-ids node-sprintf-js node-ssri node-stack-utils node-stealthy-require node-string-decoder node-string-width node-strip-ansi node-supports-color node-tap node-tap-mocha-reporter
      node-tap-parser node-tar node-text-table node-time-stamp node-tmatch node-tough-cookie node-typedarray-to-buffer node-unique-filename node-universalify node-util-deprecate node-validate-npm-package-license
      node-validate-npm-package-name node-wcwidth.js node-webidl-conversions node-whatwg-fetch node-which node-wide-align node-wrappy node-write-file-atomic node-ws node-yallist nodejs nodejs-doc rpcsvc-proto
    Paquets suggérés :
      debian-keyring g++-multilib g++-11-multilib gcc-11-doc gcc-multilib autoconf automake libtool flex bison gcc-doc gcc-11-multilib gcc-11-locales apache2 | lighttpd | httpd glibc-doc bzr libjs-angularjs
      libssl-doc libstdc++-11-doc make-doc node-nyc
    Les NOUVEAUX paquets suivants seront installés :
      build-essential dpkg-dev fakeroot g++ g++-11 gcc gcc-11 gyp javascript-common libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl libasan6 libc-ares2 libc-dev-bin libc-devtools libc6-dev
      libcc1-0 libcrypt-dev libdpkg-perl libfakeroot libfile-fcntllock-perl libgcc-11-dev libitm1 libjs-events libjs-highlight.js libjs-inherits libjs-is-typedarray libjs-psl libjs-source-map libjs-sprintf-js
      libjs-typedarray-to-buffer liblsan0 libnode-dev libnode72 libnsl-dev libquadmath0 libssl-dev libstdc++-11-dev libtirpc-dev libtsan0 libubsan1 libuv1-dev linux-libc-dev lto-disabled-list make manpages-dev
      node-abab node-abbrev node-agent-base node-ansi-regex node-ansi-styles node-ansistyles node-aproba node-archy node-are-we-there-yet node-argparse node-arrify node-asap node-asynckit node-balanced-match
      node-brace-expansion node-builtins node-cacache node-chalk node-chownr node-clean-yaml-object node-cli-table node-clone node-color-convert node-color-name node-colors node-columnify node-combined-stream
      node-commander node-console-control-strings node-copy-concurrently node-core-util-is node-coveralls node-cssom node-cssstyle node-debug node-decompress-response node-defaults node-delayed-stream
      node-delegates node-depd node-diff node-encoding node-end-of-stream node-err-code node-escape-string-regexp node-esprima node-events node-fancy-log node-fetch node-foreground-child node-form-data
      node-fs-write-stream-atomic node-fs.realpath node-function-bind node-gauge node-get-stream node-glob node-got node-graceful-fs node-growl node-gyp node-has-flag node-has-unicode node-hosted-git-info
      node-https-proxy-agent node-iconv-lite node-iferr node-imurmurhash node-indent-string node-inflight node-inherits node-ini node-ip node-ip-regex node-is-buffer node-is-plain-obj node-is-typedarray
      node-isarray node-isexe node-js-yaml node-jsdom node-json-buffer node-json-parse-better-errors node-jsonparse node-kind-of node-lcov-parse node-lodash-packages node-log-driver node-lowercase-keys
      node-lru-cache node-mime node-mime-types node-mimic-response node-minimatch node-minimist node-minipass node-mkdirp node-move-concurrently node-ms node-mute-stream node-negotiator node-nopt
      node-normalize-package-data node-npm-bundled node-npm-package-arg node-npmlog node-object-assign node-once node-opener node-osenv node-p-cancelable node-p-map node-path-is-absolute node-process-nextick-args
      node-promise-inflight node-promise-retry node-promzard node-psl node-pump node-punycode node-quick-lru node-read node-read-package-json node-readable-stream node-resolve node-retry node-rimraf node-run-queue
      node-safe-buffer node-semver node-set-blocking node-signal-exit node-slash node-slice-ansi node-source-map node-source-map-support node-spdx-correct node-spdx-exceptions node-spdx-expression-parse
      node-spdx-license-ids node-sprintf-js node-ssri node-stack-utils node-stealthy-require node-string-decoder node-string-width node-strip-ansi node-supports-color node-tap node-tap-mocha-reporter
      node-tap-parser node-tar node-text-table node-time-stamp node-tmatch node-tough-cookie node-typedarray-to-buffer node-unique-filename node-universalify node-util-deprecate node-validate-npm-package-license
      node-validate-npm-package-name node-wcwidth.js node-webidl-conversions node-whatwg-fetch node-which node-wide-align node-wrappy node-write-file-atomic node-ws node-yallist nodejs nodejs-doc npm rpcsvc-proto
    0 mis à jour, 222 nouvellement installés, 0 à enlever et 3 non mis à jour.
    Il est nécessaire de prendre 71,7 Mo/72,0 Mo dans les archives.
    Après cette opération, 274 Mo d'espace disque supplémentaires seront utilisés.
    Souhaitez-vous continuer ? [O/n] O
    Réception de :1 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libc-dev-bin amd64 2.35-0ubuntu3.7 [20,3 kB]
    Réception de :2 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 linux-libc-dev amd64 5.15.0-105.115 [1 330 kB]
    Réception de :3 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 libcrypt-dev amd64 1:4.4.27-1 [112 kB]
    Réception de :4 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 rpcsvc-proto amd64 1.4.2-0ubuntu6 [68,5 kB]
    Réception de :5 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libtirpc-dev amd64 1.3.2-2ubuntu0.1 [192 kB]
    Réception de :6 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 libnsl-dev amd64 1.3.0-2build2 [71,3 kB]
    Réception de :7 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libc6-dev amd64 2.35-0ubuntu3.7 [2 100 kB]
    Réception de :8 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libcc1-0 amd64 12.3.0-1ubuntu1~22.04 [48,3 kB]
    Réception de :9 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libitm1 amd64 12.3.0-1ubuntu1~22.04 [30,2 kB]
    Réception de :10 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libasan6 amd64 11.4.0-1ubuntu1~22.04 [2 282 kB]
    Réception de :11 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 liblsan0 amd64 12.3.0-1ubuntu1~22.04 [1 069 kB]
    Réception de :12 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libtsan0 amd64 11.4.0-1ubuntu1~22.04 [2 260 kB]
    Réception de :13 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libubsan1 amd64 12.3.0-1ubuntu1~22.04 [976 kB]
    Réception de :14 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libquadmath0 amd64 12.3.0-1ubuntu1~22.04 [154 kB]
    Réception de :15 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libgcc-11-dev amd64 11.4.0-1ubuntu1~22.04 [2 517 kB]
    Réception de :16 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 gcc-11 amd64 11.4.0-1ubuntu1~22.04 [20,1 MB]
    Réception de :17 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 gcc amd64 4:11.2.0-1ubuntu1 [5 112 B]
    Réception de :18 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libstdc++-11-dev amd64 11.4.0-1ubuntu1~22.04 [2 101 kB]
    Réception de :19 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 g++-11 amd64 11.4.0-1ubuntu1~22.04 [11,4 MB]
    Réception de :20 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 g++ amd64 4:11.2.0-1ubuntu1 [1 412 B]
    Réception de :21 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 make amd64 4.3-4.1build1 [180 kB]
    Réception de :22 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 lto-disabled-list all 24 [12,5 kB]
    Réception de :23 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 dpkg-dev all 1.21.1ubuntu2.3 [922 kB]
    Réception de :24 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 build-essential amd64 12.9ubuntu3 [4 744 B]
    Réception de :25 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 libfakeroot amd64 1.28-1ubuntu1 [31,5 kB]
    Réception de :26 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 fakeroot amd64 1.28-1ubuntu1 [60,4 kB]
    Réception de :27 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 gyp all 0.1+20210831gitd6c5dd5-5 [238 kB]
    Réception de :28 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 javascript-common all 11+nmu1 [5 936 B]
    Réception de :29 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 libalgorithm-diff-perl all 1.201-1 [41,8 kB]
    Réception de :30 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 libalgorithm-diff-xs-perl amd64 0.04-6build3 [11,9 kB]
    Réception de :31 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 libalgorithm-merge-perl all 0.08-3 [12,0 kB]
    Réception de :32 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libc-devtools amd64 2.35-0ubuntu3.7 [29,0 kB]
    Réception de :33 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 libfile-fcntllock-perl amd64 0.22-3build7 [33,9 kB]
    Réception de :34 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-events all 3.3.0+~3.0.0-2 [9 734 B]
    Réception de :35 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-highlight.js all 9.18.5+dfsg1-1 [367 kB]
    Réception de :36 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-is-typedarray all 1.0.0-4 [3 804 B]
    Réception de :37 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-psl all 1.8.0+ds-6 [76,3 kB]
    Réception de :38 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-sprintf-js all 1.1.2+ds1+~1.1.2-1 [12,8 kB]
    Réception de :39 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-typedarray-to-buffer all 4.0.0-2 [4 658 B]
    Réception de :40 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libssl-dev amd64 3.0.2-0ubuntu1.15 [2 376 kB]
    Réception de :41 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libuv1-dev amd64 1.43.0-1ubuntu0.1 [130 kB]
    Réception de :42 http://fr.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 libnode72 amd64 12.22.9~dfsg-1ubuntu3.5 [10,8 MB]
    Réception de :43 http://fr.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 libnode-dev amd64 12.22.9~dfsg-1ubuntu3.5 [609 kB]
    Réception de :44 http://fr.archive.ubuntu.com/ubuntu jammy/main amd64 manpages-dev all 5.10-1ubuntu1 [2 309 kB]
    Réception de :45 http://fr.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 nodejs amd64 12.22.9~dfsg-1ubuntu3.5 [122 kB]
    Réception de :46 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-abab all 2.0.5-2 [6 578 B]
    Réception de :47 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-ms all 2.1.3+~cs0.7.31-2 [5 782 B]
    Réception de :48 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-debug all 4.3.2+~cs4.1.7-1 [17,6 kB]
    Réception de :49 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-yallist all 4.0.0+~4.0.1-1 [8 322 B]
    Réception de :50 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-lru-cache all 6.0.0+~5.1.1-1 [11,3 kB]
    Réception de :51 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-semver all 7.3.5+~7.3.8-1 [41,5 kB]
    Réception de :52 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-agent-base all 6.0.2+~cs5.4.2-1 [17,9 kB]
    Réception de :53 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-ansi-regex all 5.0.1-1 [4 984 B]
    Réception de :54 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-ansistyles all 0.1.3-5 [4 546 B]
    Réception de :55 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-aproba all 2.0.0-2 [5 620 B]
    Réception de :56 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-delegates all 1.0.0-3 [4 280 B]
    Réception de :57 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-inherits all 2.0.4-4 [3 468 B]
    Réception de :58 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-inherits all 2.0.4-4 [3 010 B]
    Réception de :59 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-core-util-is all 1.0.3-1 [4 066 B]
    Réception de :60 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-safe-buffer all 5.2.1+~cs2.1.2-2 [15,7 kB]
    Réception de :61 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-string-decoder all 1.3.0-5 [7 046 B]
    Réception de :62 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-process-nextick-args all 2.0.1-2 [3 730 B]
    Réception de :63 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-util-deprecate all 1.0.2-3 [4 202 B]
    Réception de :64 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-isarray all 2.0.5-3 [3 934 B]
    Réception de :65 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-readable-stream all 3.6.0+~cs3.0.0-1 [32,6 kB]
    Réception de :66 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-are-we-there-yet all 3.0.0+~1.1.0-1 [8 920 B]
    Réception de :67 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-arrify all 2.0.1-2 [3 610 B]
    Réception de :68 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-asap all 2.0.6+~2.0.0-1 [14,4 kB]
    Réception de :69 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-asynckit all 0.4.0-4 [10,6 kB]
    Réception de :70 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-builtins all 4.0.0-1 [3 860 B]
    Réception de :71 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-chownr all 2.0.0-1 [4 404 B]
    Réception de :72 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-fs.realpath all 1.0.0-2 [6 106 B]
    Réception de :73 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-wrappy all 1.0.2-2 [3 658 B]
    Réception de :74 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-once all 1.4.0-4 [4 708 B]
    Réception de :75 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-inflight all 1.0.6-2 [3 940 B]
    Réception de :76 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-balanced-match all 2.0.0-1 [4 910 B]
    Réception de :77 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-brace-expansion all 2.0.1-1 [7 458 B]
    Réception de :78 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-minimatch all 3.1.1+~3.0.5-1 [16,9 kB]
    Réception de :79 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-path-is-absolute all 2.0.0-2 [4 062 B]
    Réception de :80 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-glob all 7.2.1+~cs7.6.15-1 [131 kB]
    Réception de :81 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-graceful-fs all 4.2.4+repack-1 [12,5 kB]
    Réception de :82 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-mkdirp all 1.0.4+~1.0.2-1 [11,4 kB]
    Réception de :83 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-iferr all 1.0.2+~1.0.2-1 [4 610 B]
    Réception de :84 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-imurmurhash all 0.1.4+dfsg+~0.1.1-1 [8 510 B]
    Réception de :85 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-fs-write-stream-atomic all 1.0.10-5 [5 256 B]
    Réception de :86 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-rimraf all 3.0.2-1 [10,1 kB]
    Réception de :87 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-run-queue all 2.0.0-2 [5 092 B]
    Réception de :88 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-copy-concurrently all 1.0.5-8 [7 118 B]
    Réception de :89 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-move-concurrently all 1.0.1-4 [5 120 B]
    Réception de :90 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-escape-string-regexp all 4.0.0-2 [4 328 B]
    Réception de :91 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-indent-string all 4.0.0-2 [4 122 B]
    Réception de :92 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-p-map all 4.0.0+~3.1.0+~3.0.1-1 [8 058 B]
    Réception de :93 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-promise-inflight all 1.0.1+~1.0.0-1 [4 896 B]
    Réception de :94 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-ssri all 8.0.1-2 [19,6 kB]
    Réception de :95 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-unique-filename all 1.1.1+ds-1 [3 832 B]
    Réception de :96 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-cacache all 15.0.5+~cs13.9.21-3 [34,9 kB]
    Réception de :97 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-clean-yaml-object all 0.1.0-5 [4 718 B]
    Réception de :98 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-clone all 2.1.2-3 [8 344 B]
    Réception de :99 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-color-name all 1.1.4+~1.1.1-2 [6 076 B]
    Réception de :100 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-color-convert all 2.0.1-1 [10,2 kB]
    Réception de :101 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-colors all 1.4.0-3 [12,3 kB]
    Réception de :102 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-strip-ansi all 6.0.1-1 [4 184 B]
    Réception de :103 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-defaults all 1.0.3+~1.0.3-1 [4 288 B]
    Réception de :104 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-wcwidth.js all 1.0.2-1 [7 278 B]
    Réception de :105 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-columnify all 1.5.4+~1.5.1-1 [12,6 kB]
    Réception de :106 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-console-control-strings all 1.1.0-2 [5 428 B]
    Réception de :107 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-growl all 1.10.5-4 [7 064 B]
    Réception de :108 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-sprintf-js all 1.1.2+ds1+~1.1.2-1 [3 916 B]
    Réception de :109 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-argparse all 2.0.1-2 [33,2 kB]
    Réception de :110 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-esprima all 4.0.1+ds+~4.0.3-2 [69,3 kB]
    Réception de :111 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-js-yaml all 4.1.0+dfsg+~4.0.5-6 [62,7 kB]
    Réception de :112 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-lcov-parse all 1.0.0+20170612git80d039574ed9-5 [5 084 B]
    Réception de :113 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-log-driver all 1.2.7+git+20180219+bba1761737-7 [5 436 B]
    Réception de :114 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-is-plain-obj all 3.0.0-2 [3 994 B]
    Réception de :115 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-is-buffer all 2.0.5-2 [4 128 B]
    Réception de :116 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-kind-of all 6.0.3+dfsg-2 [8 628 B]
    Réception de :117 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-minimist all 1.2.5+~cs5.3.2-1 [9 434 B]
    Réception de :118 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-cssom all 0.4.4-3 [14,1 kB]
    Réception de :119 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-cssstyle all 2.3.0-2 [30,3 kB]
    Réception de :120 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-delayed-stream all 1.0.0-5 [5 464 B]
    Réception de :121 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-combined-stream all 1.0.8+~1.0.3-1 [7 432 B]
    Réception de :122 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-mime all 3.0.0+dfsg+~cs3.96.1-1 [38,1 kB]
    Réception de :123 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-mime-types all 2.1.33-1 [6 944 B]
    Réception de :124 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-form-data all 3.0.1-1 [13,4 kB]
    Réception de :125 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-events all 3.3.0+~3.0.0-2 [3 090 B]
    Réception de :126 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-https-proxy-agent all 5.0.0+~cs8.0.0-3 [16,4 kB]
    Réception de :127 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-iconv-lite all 0.6.3-2 [167 kB]
    Réception de :128 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-lodash-packages all 4.17.21+dfsg+~cs8.31.198.20210220-5 [166 kB]
    Réception de :129 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-stealthy-require all 1.1.1-5 [7 176 B]
    Réception de :130 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-punycode all 2.1.1-5 [9 902 B]
    Réception de :131 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-psl all 1.8.0+ds-6 [39,6 kB]
    Réception de :132 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-universalify all 2.0.0-3 [4 266 B]
    Réception de :133 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-tough-cookie all 4.0.0-2 [31,7 kB]
    Réception de :134 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-webidl-conversions all 7.0.0~1.1.0+~cs15.1.20180823-2 [27,5 kB]
    Réception de :135 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-commander all 9.0.0-2 [48,0 kB]
    Réception de :136 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-mute-stream all 0.0.8+~0.0.1-1 [6 448 B]
    Réception de :137 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-read all 1.0.7-3 [5 478 B]
    Réception de :138 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-ws all 8.5.0+~cs13.3.3-2 [49,5 kB]
    Réception de :139 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-jsdom all 19.0.0+~cs90.11.27-1 [446 kB]
    Réception de :140 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-fetch all 2.6.7+~2.5.12-1 [27,1 kB]
    Réception de :141 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-coveralls all 3.1.1-1 [14,2 kB]
    Réception de :142 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-mimic-response all 3.1.0-7 [5 430 B]
    Réception de :143 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-decompress-response all 6.0.0-2 [4 656 B]
    Réception de :144 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-diff all 5.0.0~dfsg+~5.0.1-3 [77,4 kB]
    Réception de :145 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-err-code all 2.0.3+dfsg-3 [4 918 B]
    Réception de :146 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-time-stamp all 2.2.0-1 [5 984 B]
    Réception de :147 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-fancy-log all 1.3.3+~cs1.3.1-2 [8 102 B]
    Réception de :148 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-signal-exit all 3.0.6+~3.0.1-1 [7 000 B]
    Réception de :149 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-foreground-child all 2.0.0-3 [5 542 B]
    Réception de :150 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-function-bind all 1.1.1+repacked+~1.0.3-1 [5 244 B]
    Réception de :151 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-has-unicode all 2.0.1-4 [3 948 B]
    Réception de :152 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-ansi-styles all 4.3.0+~4.2.0-1 [8 968 B]
    Réception de :153 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-slice-ansi all 5.0.0+~cs9.0.0-4 [8 044 B]
    Réception de :154 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-string-width all 4.2.3+~cs13.2.3-1 [11,4 kB]
    Réception de :155 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-wide-align all 1.1.3-4 [4 228 B]
    Réception de :156 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-gauge all 4.0.2-1 [16,3 kB]
    Réception de :157 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-end-of-stream all 1.4.4+~1.4.1-1 [5 340 B]
    Réception de :158 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-pump all 3.0.0-5 [5 160 B]
    Réception de :159 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-get-stream all 6.0.1-1 [7 324 B]
    Réception de :160 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-lowercase-keys all 2.0.0-2 [3 754 B]
    Réception de :161 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-json-buffer all 3.0.1-1 [3 812 B]
    Réception de :162 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-p-cancelable all 2.1.1-1 [7 358 B]
    Réception de :163 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-quick-lru all 5.1.1-1 [5 532 B]
    Réception de :164 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-got all 11.8.3+~cs58.7.37-1 [122 kB]
    Réception de :165 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-has-flag all 4.0.0-2 [4 228 B]
    Réception de :166 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-hosted-git-info all 4.0.2-1 [9 006 B]
    Réception de :167 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-ip all 1.1.5+~1.1.0-1 [8 140 B]
    Réception de :168 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-ip-regex all 4.3.0+~4.1.1-1 [5 254 B]
    Réception de :169 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-is-typedarray all 1.0.0-4 [2 072 B]
    Réception de :170 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-isexe all 2.0.0+~2.0.1-4 [6 102 B]
    Réception de :171 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-json-parse-better-errors all 1.0.2+~cs3.3.1-1 [7 328 B]
    Réception de :172 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-encoding all 0.1.13-2 [4 366 B]
    Réception de :173 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-jsonparse all 1.3.1-10 [8 060 B]
    Réception de :174 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-minipass all 3.1.6+~cs8.7.18-1 [32,9 kB]
    Réception de :175 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-npm-bundled all 1.1.2-1 [6 228 B]
    Réception de :176 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-osenv all 0.1.5+~0.1.0-1 [5 896 B]
    Réception de :177 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-validate-npm-package-name all 3.0.0-4 [5 058 B]
    Réception de :178 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-npm-package-arg all 8.1.5-1 [8 132 B]
    Réception de :179 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-object-assign all 4.1.1-6 [4 754 B]
    Réception de :180 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-opener all 1.5.2+~1.4.0-1 [6 000 B]
    Réception de :181 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-retry all 0.13.1+~0.12.1-1 [11,5 kB]
    Réception de :182 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-promise-retry all 2.0.1-2 [5 010 B]
    Réception de :183 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-promzard all 0.3.0-2 [6 888 B]
    Réception de :184 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-set-blocking all 2.0.0-2 [3 766 B]
    Réception de :185 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-slash all 3.0.0-2 [3 922 B]
    Réception de :186 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 libjs-source-map all 0.7.0++dfsg2+really.0.6.1-9 [93,9 kB]
    Réception de :187 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-source-map all 0.7.0++dfsg2+really.0.6.1-9 [33,6 kB]
    Réception de :188 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-source-map-support all 0.5.21+ds+~0.5.4-1 [14,2 kB]
    Réception de :189 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-spdx-license-ids all 3.0.11-1 [7 306 B]
    Réception de :190 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-spdx-exceptions all 2.3.0-2 [3 978 B]
    Réception de :191 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-spdx-expression-parse all 3.0.1+~3.0.1-1 [7 658 B]
    Réception de :192 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-spdx-correct all 3.1.1-2 [5 476 B]
    Réception de :193 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-stack-utils all 2.0.5+~2.0.1-1 [9 368 B]
    Réception de :194 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-supports-color all 8.1.1+~8.1.1-1 [7 048 B]
    Réception de :195 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-tap-parser all 7.0.0+ds1-6 [19,4 kB]
    Réception de :196 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-tap-mocha-reporter all 3.0.7+ds-2 [39,2 kB]
    Réception de :197 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-text-table all 0.2.0-4 [4 762 B]
    Réception de :198 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-tmatch all 5.0.0-4 [6 002 B]
    Réception de :199 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-typedarray-to-buffer all 4.0.0-2 [2 242 B]
    Réception de :200 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-validate-npm-package-license all 3.0.4-2 [4 252 B]
    Réception de :201 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-whatwg-fetch all 3.6.2-5 [15,0 kB]
    Réception de :202 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-write-file-atomic all 3.0.3+~3.0.2-1 [7 690 B]
    Réception de :203 http://fr.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 nodejs-doc all 12.22.9~dfsg-1ubuntu3.5 [2 411 kB]
    Réception de :204 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-abbrev all 1.1.1+~1.1.2-1 [5 784 B]
    Réception de :205 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-archy all 1.0.0-4 [4 728 B]
    Réception de :206 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-chalk all 4.1.2-1 [15,9 kB]
    Réception de :207 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-cli-table all 0.3.11+~cs0.13.3-1 [23,2 kB]
    Réception de :208 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-depd all 2.0.0-2 [10,5 kB]
    Réception de :209 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-nopt all 5.0.0-2 [11,3 kB]
    Réception de :210 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-npmlog all 6.0.1+~4.1.4-1 [9 968 B]
    Réception de :211 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-tar all 6.1.11+ds1+~cs6.0.6-1 [38,8 kB]
    Réception de :212 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-which all 2.0.2+~cs1.3.2-2 [7 374 B]
    Réception de :213 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-gyp all 8.4.1-1 [34,7 kB]
    Réception de :214 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-ini all 2.0.1-1 [6 528 B]
    Réception de :215 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-negotiator all 0.6.2+~0.6.1-1 [10,3 kB]
    Réception de :216 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-resolve all 1.20.0+~cs5.27.9-1 [20,7 kB]
    Réception de :217 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-normalize-package-data all 3.0.3+~2.4.1-1 [12,8 kB]
    Réception de :218 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-read-package-json all 4.1.1-1 [10,4 kB]
    Réception de :219 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 node-tap all 12.0.1+ds-4 [43,6 kB]
    Réception de :220 http://fr.archive.ubuntu.com/ubuntu jammy/universe amd64 npm all 8.5.1~ds-1 [894 kB]
    71,7 Mo réceptionnés en 19s (3 778 ko/s)
    Extraction des modèles depuis les paquets : 100%
    Sélection du paquet libc-dev-bin précédemment désélectionné.
    (Lecture de la base de données... 208646 fichiers et répertoires déjà installés.)

    [...]

    Paramétrage de node-gyp (8.4.1-1) ...
    Paramétrage de npm (8.5.1~ds-1) ...
    Traitement des actions différées (« triggers ») pour man-db (2.10.2-1) ...
    Traitement des actions différées (« triggers ») pour libc-bin (2.35-0ubuntu3.7) ...
```

`recher@recher-ordi:~/Documents/personnel$ npm version`

```
    {
      npm: '8.5.1',
      node: '12.22.9',
      v8: '7.8.279.23-node.56',
      uv: '1.43.0',
      zlib: '1.2.11',
      brotli: '1.0.9',
      ares: '1.18.1',
      modules: '72',
      nghttp2: '1.43.0',
      napi: '8',
      llhttp: '2.1.6',
      http_parser: '2.9.4',
      openssl: '1.1.1m',
      cldr: '40.0',
      icu: '70.1',
      tz: '2024a',
      unicode: '14.0'
    }
```

`recher@recher-ordi:~/Documents/personnel$ cd squarity-code/`

`recher@recher-ordi:~/Documents/personnel/squarity-code$ npm install`

```
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: '@vitejs/plugin-vue@4.2.3',
    npm WARN EBADENGINE   required: { node: '^14.18.0 || >=16.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: 'eslint-plugin-vue@9.17.0',
    npm WARN EBADENGINE   required: { node: '^14.17.0 || >=16.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: 'rollup@3.25.1',
    npm WARN EBADENGINE   required: { node: '>=14.18.0', npm: '>=8.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: 'vite@4.3.9',
    npm WARN EBADENGINE   required: { node: '^14.18.0 || >=16.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: 'vue-eslint-parser@9.3.1',
    npm WARN EBADENGINE   required: { node: '^14.17.0 || >=16.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    added 137 packages, and audited 138 packages in 5s
    29 packages are looking for funding
      run `npm fund` for details
    2 vulnerabilities (1 moderate, 1 high)
    To address all issues, run:
      npm audit fix
    Run `npm audit` for details.
```

`recher@recher-ordi:~/Documents/personnel/squarity-code$ npm audit fix`

```
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: '@vitejs/plugin-vue@4.2.3',
    npm WARN EBADENGINE   required: { node: '^14.18.0 || >=16.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: 'eslint-plugin-vue@9.17.0',
    npm WARN EBADENGINE   required: { node: '^14.17.0 || >=16.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: 'vue-eslint-parser@9.3.1',
    npm WARN EBADENGINE   required: { node: '^14.17.0 || >=16.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: 'vite@4.5.3',
    npm WARN EBADENGINE   required: { node: '^14.18.0 || >=16.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: 'rollup@3.29.4',
    npm WARN EBADENGINE   required: { node: '>=14.18.0', npm: '>=8.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    changed 7 packages, and audited 138 packages in 5s
    30 packages are looking for funding
      run `npm fund` for details
    found 0 vulnerabilities
```

`recher@recher-ordi:~/Documents/personnel/squarity-code$ git status`

```
    Sur la branche master
    Votre branche est à jour avec 'origin/master'.
```

`recher@recher-ordi:~/Documents/personnel/squarity-code$ sudo apt install nodejs`

```
    Lecture des listes de paquets... Fait
    Construction de l'arbre des dépendances... Fait
    Lecture des informations d'état... Fait
    nodejs est déjà la version la plus récente (12.22.9~dfsg-1ubuntu3.5).
    nodejs passé en « installé manuellement ».
    Les paquets suivants ont été installés automatiquement et ne sont plus nécessaires :
      libwpe-1.0-1 libwpebackend-fdo-1.0-1
    Veuillez utiliser « sudo apt autoremove » pour les supprimer.
    0 mis à jour, 0 nouvellement installés, 0 à enlever et 3 non mis à jour.
```

(fermeture du terminal et ouverture d'un autre terminal.)

**suppression du dossier squarity-code**

`recher@recher-ordi:~/Documents/personnel$ git clone https://github.com/darkrecher/squarity-code.git`

`recher@recher-ordi:~/Documents/personnel$ cd squarity-code`

**suppression du fichier package-lock.json**

`recher@recher-ordi:~/Documents/personnel/squarity-code$ npm install`

```
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: '@vitejs/plugin-vue@4.6.2',
    npm WARN EBADENGINE   required: { node: '^14.18.0 || >=16.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: 'vite@4.5.3',
    npm WARN EBADENGINE   required: { node: '^14.18.0 || >=16.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: 'eslint-plugin-vue@9.25.0',
    npm WARN EBADENGINE   required: { node: '^14.17.0 || >=16.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: 'vue-eslint-parser@9.4.2',
    npm WARN EBADENGINE   required: { node: '^14.17.0 || >=16.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    npm WARN EBADENGINE Unsupported engine {
    npm WARN EBADENGINE   package: 'rollup@3.29.4',
    npm WARN EBADENGINE   required: { node: '>=14.18.0', npm: '>=8.0.0' },
    npm WARN EBADENGINE   current: { node: 'v12.22.9', npm: '8.5.1' }
    npm WARN EBADENGINE }
    added 140 packages, and audited 141 packages in 16s
    31 packages are looking for funding
      run `npm fund` for details
    found 0 vulnerabilities
```

`recher@recher-ordi:~/Documents/personnel/squarity-code$ npm run dev`

```
    > squarity-code@0.0.0 dev
    > vite
    file:///home/recher/Documents/personnel/squarity-code/node_modules/vite/bin/vite.js:7
        await import('source-map-support').then((r) => r.default.install())
        ^^^^^
    SyntaxError: Unexpected reserved word
        at Loader.moduleStrategy (internal/modules/esm/translators.js:133:18)
        at async link (internal/modules/esm/module_job.js:42:21)
    recher@recher-ordi:~/Documents/personnel/squarity-code$
```

## Putain de nodejs, putain de npm, putain de framework front de zouzou

J'avais déjà rencontré le problème, il est dans un de mes logs précédents.

https://stackoverflow.com/questions/73048645/npm-run-dev-not-working-with-vite-laravel-9

Et voilà, maintenant je me retrouve à indiquer des liens stackoverflow contenant le mot "laravel". Si c'est pas malheureux cette misère.

`recher@recher-ordi:~/Documents/personnel/squarity-code$ sudo snap install curl`

```
    [sudo] Mot de passe de recher :
    curl 8.1.2 par Wouter van Bommel (woutervb) installé
```

`recher@recher-ordi:~/Documents/personnel/squarity-code$ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash`

```
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
    100 15916  100 15916    0     0  85631      0 --:--:-- --:--:-- --:--:-- 86032
    => Downloading nvm from git to '/home/recher/.nvm'
    => Clonage dans '/home/recher/.nvm'...
    remote: Enumerating objects: 365, done.
    remote: Counting objects: 100% (365/365), done.
    remote: Compressing objects: 100% (313/313), done.
    remote: Total 365 (delta 43), reused 166 (delta 26), pack-reused 0
    Réception d'objets: 100% (365/365), 365.08 Kio | 1.06 Mio/s, fait.
    Résolution des deltas: 100% (43/43), fait.
    * (HEAD détachée sur FETCH_HEAD)
      master
    => Compressing and cleaning up git repository
    => Appending nvm source string to /home/recher/.bashrc
    => Appending bash_completion source string to /home/recher/.bashrc
    => Close and reopen your terminal to start using nvm or run the following to use it now:
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

(Fermeture du terminal et ouverture d'un nouveau)

`recher@recher-ordi:~$ nvm -v`

```
    0.39.3
```

`recher@recher-ordi:~$ nvm install 16.20.1`

**ça marche pas.**

`recher@recher-ordi:~$ nvm ls`

```
    ->       system
    iojs -> N/A (default)
    node -> stable (-> N/A) (default)
    unstable -> N/A (default)
    lts/* -> lts/iron (-> N/A)
    lts/argon -> v4.9.1 (-> N/A)
    lts/boron -> v6.17.1 (-> N/A)
    lts/carbon -> v8.17.0 (-> N/A)
    lts/dubnium -> v10.24.1 (-> N/A)
    lts/erbium -> v12.22.12 (-> N/A)
    lts/fermium -> v14.21.3 (-> N/A)
    lts/gallium -> v16.20.2 (-> N/A)
    lts/hydrogen -> v18.20.2 (-> N/A)
    lts/iron -> v20.12.2 (-> N/A)
```

`recher@recher-ordi:~$ node --version`

```
    v12.22.9
```

## PUTAIN D'EMPAFFÉ DE SNAP !!

https://askubuntu.com/questions/1387141/curl-23-failure-writing-output-to-destination

**Faut pas installer curl avec snap !!! **

`recher@recher-ordi:~$ sudo snap remove curl`

```
    curl supprimé
```

`recher@recher-ordi:~$ sudo apt install curl`

```
    Lecture des listes de paquets... Fait
    Construction de l'arbre des dépendances... Fait
    Lecture des informations d'état... Fait
    Les paquets suivants ont été installés automatiquement et ne sont plus nécessaires :
      libwpe-1.0-1 libwpebackend-fdo-1.0-1
    Veuillez utiliser « sudo apt autoremove » pour les supprimer.
    Les NOUVEAUX paquets suivants seront installés :
      curl
    0 mis à jour, 1 nouvellement installés, 0 à enlever et 3 non mis à jour.
    Il est nécessaire de prendre 194 ko dans les archives.
    Après cette opération, 454 ko d'espace disque supplémentaires seront utilisés.
    Réception de :1 http://fr.archive.ubuntu.com/ubuntu jammy-updates/main amd64 curl amd64 7.81.0-1ubuntu1.16 [194 kB]
    194 ko réceptionnés en 0s (640 ko/s)
    Sélection du paquet curl précédemment désélectionné.
    (Lecture de la base de données... 221848 fichiers et répertoires déjà installés.)
    Préparation du dépaquetage de .../curl_7.81.0-1ubuntu1.16_amd64.deb ...
    Dépaquetage de curl (7.81.0-1ubuntu1.16) ...
    Paramétrage de curl (7.81.0-1ubuntu1.16) ...
    Traitement des actions différées (« triggers ») pour man-db (2.10.2-1) ...
```

(Fermeture du terminal et ouverture d'un nouveau)

`recher@recher-ordi:~/Documents/personnel/squarity-code$ nvm install 16.20.1`

```
    Downloading and installing node v16.20.1...
    Downloading https://nodejs.org/dist/v16.20.1/node-v16.20.1-linux-x64.tar.xz...
    ############################################################################################################################################################################################################ 100,0%
    Computing checksum with sha256sum
    Checksums matched!
    Now using node v16.20.1 (npm v8.19.4)
    Creating default alias: default -> 16.20.1 (-> v16.20.1)
```

`recher@recher-ordi:~/Documents/personnel/squarity-code$ nvm ls`

```
    ->     v16.20.1
             system
    default -> 16.20.1 (-> v16.20.1)
    iojs -> N/A (default)
    unstable -> N/A (default)
    node -> stable (-> v16.20.1) (default)
    stable -> 16.20 (-> v16.20.1) (default)
    lts/* -> lts/iron (-> N/A)
    lts/argon -> v4.9.1 (-> N/A)
    lts/boron -> v6.17.1 (-> N/A)
    lts/carbon -> v8.17.0 (-> N/A)
    lts/dubnium -> v10.24.1 (-> N/A)
    lts/erbium -> v12.22.12 (-> N/A)
    lts/fermium -> v14.21.3 (-> N/A)
    lts/gallium -> v16.20.2 (-> N/A)
    lts/hydrogen -> v18.20.2 (-> N/A)
    lts/iron -> v20.12.2 (-> N/A)
```

`recher@recher-ordi:~/Documents/personnel/squarity-code$ node --version`

```
    v16.20.1
```

`recher@recher-ordi:~/Documents/personnel/squarity-code$ npm install`

```
    up to date, audited 141 packages in 503ms
    31 packages are looking for funding
      run `npm fund` for details
    found 0 vulnerabilities
```

`npm run dev`

**ça marche !!**

`npm run build` semble marcher aussi, mais à vérifier quand on remettra en prod.

`recher@recher-ordi:~/Documents/personnel/squarity-code$ npm install --global @vue/cli`

```
    npm WARN deprecated source-map-url@0.4.1: See https://github.com/lydell/source-map-url#deprecated
    npm WARN deprecated resolve-url@0.2.1: https://github.com/lydell/resolve-url#deprecated
    npm WARN deprecated urix@0.1.0: Please see https://github.com/lydell/urix#deprecated
    npm WARN deprecated source-map-resolve@0.5.3: See https://github.com/lydell/source-map-resolve#deprecated
    npm WARN deprecated @babel/plugin-proposal-nullish-coalescing-operator@7.18.6: This proposal has been merged to the ECMAScript standard and thus this plugin is no longer maintained. Please use @babel/plugin-transform-nullish-coalescing-operator instead.
    npm WARN deprecated @babel/plugin-proposal-class-properties@7.18.6: This proposal has been merged to the ECMAScript standard and thus this plugin is no longer maintained. Please use @babel/plugin-transform-class-properties instead.
    npm WARN deprecated @babel/plugin-proposal-optional-chaining@7.21.0: This proposal has been merged to the ECMAScript standard and thus this plugin is no longer maintained. Please use @babel/plugin-transform-optional-chaining instead.
    npm WARN deprecated apollo-server-plugin-base@3.7.2: The `apollo-server-plugin-base` package is part of Apollo Server v2 and v3, which are now deprecated (end-of-life October 22nd 2023 and October 22nd 2024, respectively). This package's functionality is now found in the `@apollo/server` package. See https://www.apollographql.com/docs/apollo-server/previous-versions/ for more details.
    npm WARN deprecated apollo-server-errors@3.3.1: The `apollo-server-errors` package is part of Apollo Server v2 and v3, which are now deprecated (end-of-life October 22nd 2023 and October 22nd 2024, respectively). This package's functionality is now found in the `@apollo/server` package. See https://www.apollographql.com/docs/apollo-server/previous-versions/ for more details.
    npm WARN deprecated apollo-datasource@3.3.2: The `apollo-datasource` package is part of Apollo Server v2 and v3, which are now deprecated (end-of-life October 22nd 2023 and October 22nd 2024, respectively). See https://www.apollographql.com/docs/apollo-server/previous-versions/ for more details.
    npm WARN deprecated apollo-server-env@4.2.1: The `apollo-server-env` package is part of Apollo Server v2 and v3, which are now deprecated (end-of-life October 22nd 2023 and October 22nd 2024, respectively). This package's functionality is now found in the `@apollo/utils.fetcher` package. See https://www.apollographql.com/docs/apollo-server/previous-versions/ for more details.
    npm WARN deprecated apollo-reporting-protobuf@3.4.0: The `apollo-reporting-protobuf` package is part of Apollo Server v2 and v3, which are now deprecated (end-of-life October 22nd 2023 and October 22nd 2024, respectively). This package's functionality is now found in the `@apollo/usage-reporting-protobuf` package. See https://www.apollographql.com/docs/apollo-server/previous-versions/ for more details.
    npm WARN deprecated apollo-server-types@3.8.0: The `apollo-server-types` package is part of Apollo Server v2 and v3, which are now deprecated (end-of-life October 22nd 2023 and October 22nd 2024, respectively). This package's functionality is now found in the `@apollo/server` package. See https://www.apollographql.com/docs/apollo-server/previous-versions/ for more details.
    npm WARN deprecated subscriptions-transport-ws@0.11.0: The `subscriptions-transport-ws` package is no longer maintained. We recommend you use `graphql-ws` instead. For help migrating Apollo software to `graphql-ws`, see https://www.apollographql.com/docs/apollo-server/data/subscriptions/#switching-from-subscriptions-transport-ws    For general help using `graphql-ws`, see https://github.com/enisdenjo/graphql-ws/blob/master/README.md
    npm WARN deprecated shortid@2.2.16: Package no longer supported. Contact Support at https://www.npmjs.com/support for more info.
    npm WARN deprecated vue@2.7.16: Vue 2 has reached EOL and is no longer actively maintained. See https://v2.vuejs.org/eol/ for more details.

    added 853 packages, and audited 854 packages in 42s

    74 packages are looking for funding
      run `npm fund` for details

    6 vulnerabilities (1 moderate, 5 high)

    To address all issues (including breaking changes), run:
      npm audit fix --force

    Run `npm audit` for details.
```

`recher@recher-ordi:~/Documents/personnel/squarity-code$ vue --version`

```
    @vue/cli 5.0.8
```

`recher@recher-ordi:~/Documents/personnel/squarity-code$ npm run lint`

```
    > squarity-code@0.0.0 lint
    > eslint . --ext .vue,.js,.jsx,.cjs,.mjs --fix --ignore-path .eslintignore
    /home/recher/Documents/personnel/squarity-code/src/classes/gameEngine/Layer.js
      17:23  error  'multiplicatorX' is defined but never used               no-unused-vars
      17:39  error  'multiplicatorY' is defined but never used               no-unused-vars
      71:27  error  'timeNow' is defined but never used                      no-unused-vars
      72:8   error  'timeNow' is defined but never used                      no-unused-vars
      74:25  error  'timeNow' is defined but never used                      no-unused-vars
      107:11  error  'timeNowLayerBefore' is assigned a value but never used  no-unused-vars
      144:11  error  'timeNowLayerAfter' is assigned a value but never used   no-unused-vars
      151:15  error  'gobjId' is assigned a value but never used              no-unused-vars
      165:15  error  'gobjId' is assigned a value but never used              no-unused-vars
      175:15  error  'gobjId' is assigned a value but never used              no-unused-vars
      206:27  error  'timeNow' is defined but never used                      no-unused-vars
      209:8   error  'timeNow' is defined but never used                      no-unused-vars
      230:25  error  'timeNow' is defined but never used                      no-unused-vars
    /home/recher/Documents/personnel/squarity-code/src/classes/gameEngineV2.js
      159:14  error  Irregular whitespace not allowed  no-irregular-whitespace
      171:14  error  Irregular whitespace not allowed  no-irregular-whitespace
    ✖ 15 problems (15 errors, 0 warnings)
```

Ah, j'ai plein de trucs mal fichus dans mon code, mais au moins le linter marche (et du premier coup !!)

