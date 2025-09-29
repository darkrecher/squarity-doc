# Configuration DNS

## Config initiale avec GoDaddy

Achat des noms de domaine `squarity.fr` et `squariti.fr` par le site GoDaddy.fr. J'avais pris "squariti" au cas où des gens l'écriraient avec une faute.

Il y avait une simple redirection (HTTP 301) vers la vraie url où est hébergé le site : `squarity.pythonanywhere.com`.

Les "bookmarks" `#fetchez_githubgist_` permettant d'indiquer où récupérer le jeu en cours étaient conservés au moment de la redirection.

Par exemple, l'url `http://squarity.fr/#fetchez_githubgist_darkrecher/dd5cd1e7c59eb19f71609c5b074881c1/raw/unstable-isotopes`

était correctement redirigée vers `https://squarity.pythonanywhere.com/#fetchez_githubgist_darkrecher/dd5cd1e7c59eb19f71609c5b074881c1/raw/unstable-isotopes`

Le jeu s'affichait correctement, mais il y avait des défauts embarrassants :

 - Pas de HTTPS. `https://squarity.fr` ne fonctionnait pas, même si la redirection amenait au final vers un site en HTTPS.
 - Les sous-répertoires après le nom de domaine ne fonctionnaient pas. `http://squarity.fr/machin` menait vers une page 404 de GoDaddy.

Les sous-répertoires non gérés sont vraiment devenus un problème lorsque le site a eu une vraie structure avec plusieurs pages. Les jeux sont censés être à l'url `https://squarity.fr/game/#fetchez_githubgist_xxxx`. Le sous-répertoire `/game` a été ajouté, pour ne pas se mélanger avec la page d'accueil. Mais cette url ne fonctionnait pas.


## Configuration actuelle

(Config réalisée avec l'aide d'une IA, parce que je suis pas très doué en DNS).

GoDaddy ne gère pas les redirections avec des sous-répertoires. Il faut utiliser un service supplémentaire : CloudFlare.

C'est lourdingue, car ça fait une dépendance supplémentaire (GoDaddy, CloudFlare, pythonanywhere, github pour stocker les jeux). Mais je n'ai pas trouvé d'autres solutions.

GoDaddy reste le "gérant principal" de squarity.fr, mais on peut le configurer pour "sous-traiter" la gérance à un autre service. Ça se fait avec les champs DNS de type "NS".

Description des champs NS (source: https://www.cloudflare.com/fr-fr/learning/dns/dns-records/dns-ns-record/ )

> NS signifie « Nameserver » (serveur de noms), et l'enregistrement du serveur de noms indique quel serveur DNS fait autorité pour ce domaine (c'est-à-dire quel serveur contient les enregistrements DNS réels). Fondamentalement, les enregistrements NS indiquent à Internet où aller pour trouver l'adresse IP d'un domaine. Un domaine comporte souvent plusieurs enregistrements NS qui peuvent indiquer des serveurs de noms principaux et secondaires pour ce domaine. Sans enregistrements NS correctement configurés, les utilisateurs ne pourront pas charger un site web ou une application.

### Config GoDaddy

La config se trouve (à peu près) dans le menu "Nom de domaine / DNS / Serveurs de nom".

Par défaut, deux champs "NS" sont configurés, permettant à GoDaddy de gérer tous les champs DNS de squarity.fr. Je ne me souviens plus de leurs noms, ils commencent par "ns1" et "ns2". Dans tous les cas, il est possible de remettre ces valeurs par défaut.

Pour déléguer la gestion à CloudFlare, il faut modifier ces champs NS en y mettant les valeurs demandées par CloudFlare. Pour squarity.fr, il s'agit de :

 - `ganz.ns.cloudflare.com`
 - `melissa.ns.cloudflare.com`

Lorsque ces champs sont redéfinis dans GoDaddy, on ne peut plus rien configurer d'autres (à part remettre les valeurs de NS par défaut). C'est normal.

**Attention, la nouvelle config n'est pas instantanément prise en compte. Il faut attendre quelques dizaines de minutes, voire plus. C'est le temps que tous les serveurs DNS de l'internet prennent en compte la nouvelle config.**

On peut le vérifier en allant sur des sites comme "whois". Les infos DNS affichées sont supposées changer.

Tant que ce n'est pas pris en compte, on ne peut rien configurer chez CloudFlare.

### Config CloudFlare

Menu "DNS / Records".

Si c'est correctement propagé, on doit voir les bons champs NS dans la partie "Nameservers".

Il faut ensuite définir les autres records. La config actuelle a 3 records:

 - type: A, name: `squarity.fr`, IPv4 address: 192.0.2.1, status: Proxied (case cochée), TTL: Auto
 - type: A, name: `www`, IPv4 address: 192.0.2.1, status: Proxied (case cochée), TTL: Auto
 - type: CNAME, name: `_domainconnect`, Target: `_domainconnect.gd.domaincontrol.com`, status: Proxied (case cochée), TTL: Auto

Ensuite, il faut aller dans le menu "Rules - Overview" et rajouter une règle, à partir d'un template de redirection.

 - Redirect rules,
   - name: (ce qu'on veut)
   - match: Custom filter expression
 - When incoming requests match...
   - field: Hostname
   - operator: equals
   - value: `squarity.fr`
 - Then...
   - type: Dynamic
   - expression: `concat("https://squarity.pythonanywhere.com", http.request.uri.path)`
   - status: 301
 - Place at
   - order: first

Ensuite, menu "DNS - Settings". Activer "DNSSEC".

Je ne me souviens plus exactement ce qu'il faut faire, mais c'est assez simple, les directives ne sont pas loin. En gros, il faut copier-coller ce que demande CloudFlare dans les champs "DS Record", "Digest", etc.

Pour finir, il faut attendre encore quelques minutes pour que tout soit pris en compte, et ça marche.

Rappelons que le service fourni par CloudFlare est gratuit (je ne sais même pas comment ils font).

### Fonctionnement actuel

HTTP et HTTPS fonctionnent tous les deux pour `squarity.fr`.

Tous les sous-répertoires fonctionnent, y compris quand il y en a plusieurs. `http://squarity.fr/machin/truc` redirige vers `https://squarity.pythonanywhere.com/machin/truc`.

Les bookmarks fonctionnent aussi, comme avant. Et la combinaison sous-répertoires + bookmarks fonctionne aussi.

Par contre, l'url est réécrite, comme dans la config d'avant. `squarity.fr` n'apparaît plus dans la barre d'adresse du navigateur, on a `squarity.pythonanywhere.com` à la place. Ça peut poser problème pour les gens qui partagent des jeux et qui copie-collent l'url à partir de leur navigateur.

Je ne sais pas comment faire pour que l'url reste en `squarity.fr`. Je crois qu'il faut acheter un abonnement à pythonanywhere. On verra ça plus tard.

Et donc, à partir de maintenant, pour partager les jeux, il faut utiliser des urls qui commencent par `https://squarity.fr/game/#fetchez_githubgist_`, même si ça change après dans la barre d'adresse.

La méthode pour construire une url de partage d'un jeu est décrite dans la doc utilisateur: `user_manual/share_your_game.md`.

Au passage, j'ai abandonné le domaine `squariti.fr`. En essayant de comprendre tout ce bazar, j'ai cru qu'il fallait complètement abandonner la gestion d'un domaine sur GoDaddy, pour que CloudFlare puisse le gérer correctement. Ça ne marche pas comme ça, heureusement que j'ai testé avec le domaine `squariti`.

Quand on abandonne un domaine sur GoDaddy, c'est "no refund" et il faut le racheter. On verra plus tard si ça vaut le coup. Le plus important est de ne pas avoir perdu `squarity.fr`.


