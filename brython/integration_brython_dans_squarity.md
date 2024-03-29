# Particularités de Brython


## Conservation des variables

En python normal :

    λ python
    Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> c = 12
    >>> truc = compile("print('avant', c);c += 1;print('apres', c)", "paf", "exec")
    >>> exec(truc)
    avant 12
    apres 13
    >>> print("valeur final de c :", c)
    valeur final de c : 13
    >>> exit()

La valeur de c est conservée.

Dans brython :

On met le même code dans un fichier :

    c = 12
    truc = compile("print('avant', c);c += 1;print('apres', c)", "paf", "exec")
    exec(truc)
    print("valeur final de c :", c)

On obtient ceci dans la console :

    avant 12
    apres 13
    valeur final de c : 12

La valeur de la variable c n'est pas conservée dans le scope global !

Il y a peut-être une petite différence (mais je vois pas ce que ça changerait) : Le test dans brython a été inséré dans la méthode d'une classe.

Heureusement, lorsqu'on utilise des variables membres, la valeur est conservée.

    class Machin():
        def fonction(self):
            self.c = 12
            truc = compile("print('avant', self.c);self.c += 1;print('apres', self.c)", "paf", "exec")
            exec(truc)
            print("valeur final de self.c :", self.c)

On obtient ça dans la console :

    avant 12
    apres 13
    valeur final de self.c : 13

Le reste fonctionne :

 - Initialisation de la variable dans une fonction, utilisation/modification dans une autre, via un compile.
 - Exécution successive de la même méthode de classe, via des appels successifs à une fonction python dans du javascript.

À chaque fois les valeurs des variables membres, dans la classe, sont conservées. Donc tout va bien, ouf !

Il faudra donner comme consigne aux utilisateurs de mettre les variables qu'ils veulent conserver dans self. Mais c'est déjà plus ou moins le cas en temps normal, avec les tiles et les gamobj. Donc tout va bien.


## Passage à Pyodide

L'exécution de code python par Brython est vraiment trop lente. TODO : ajouter dans ce repository le résultat de mon benchmark brython/pyodide.

De plus, avec pyodide, le lancement d'un code python via le javascript est beaucoup plus simple. Et la librairie standard est disponible immédiatement.

Inconvénient : Pyodide est très lent à démarrer au début. Il faut télécharger 20 Mo de js et de wasm, ça peut prendre plusieurs dizaines de secondes (mais ça se met en cache) Ensuite, il faut initialiser la VM-wasm python. Ça prend quelques secondes, et ça doit être refait à chaque rechargement de la page web.

**Architecture Decision Record** : on vire Brython et on met Pyodide à la place.

TODO : décrire les liens entre pyodide et le reste de mon code.

