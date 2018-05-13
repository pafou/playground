# playground
Contient tous les codes simples, exemples, didactiques ou 'cracra'.  
C'est à dire :

* codes simples : codes ne méritant pas un projet à eux seuls, et souvent destinés à être réutilisés dans des projets plus importants.
* codes exemples et didactiques : code dans lequel on retrouve des exemples simples de manipulation d'objets, de modules, de tests, de docs, de fonctions, de classes...
* codes cracra : (dits 'playground' : destinés à faire quelques test unitaires)

## Organisation 

Les codes sont classés ainsi : 

    playground/<language>/samples
                         /pig
                         /<projet 1>
                         /<projet 2>
                         /...

* `samples` contient des scripts exemple ;
* `pig` contient tous les petits scripts expérimentaux ;
* sous chaque projet, on retrouve un script généralement dénommé `<projet>.<ext>` ;
c'est le script principal du projet.

## Un script important
`hm.py` est un script qui permet de rechercher des exemples de code dans tous les codes.


    hm.py -t un_tag
permettra de chercher des bouts de code encadrés par `#un_tag` et un autre tag.


    hm.py -k un_mot_cle
permettra de chercher des bouts de code qui contiennent le mot clé `un_mot_cle`.

## Quelques exemples 
### `playground/python/samples/`
On y retrouve des tas de scripts simples décrivant le fonctionnement du langage python.

Le script principal `samples.py`est le script principal. Il se contente de lister les scripts présents dans le projet 'samples', et de donner une description de chacun des scripts.

### `playground/python/tmps/`
On y trouve le projet python 'tmps', écrit en python.

### `playground/python/pig/`
On y trouve tous les scripts cracras, expérimentaux, écrits en python.

### `playground/markdown/samples/`
On y trouve un texte `samples.md` qui donne un exemple simple pour comprendre le langage markdown.

## Franglais
La logique d'écriture est la suivante:

* Français : si c'est explicatif (comme ici)
* Anglais : pour tout le contenu du code, dont les **commentaires** (variables, fonctions, classes...).


