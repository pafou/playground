*** Code Mardown ***
*********************

# Titres
## Title 2
### Title 3
####  Title 4

# Paragraphes

Pour afficher un paragraphe, sautez deux ligne et de taper son texte. 
Un seul saut de ligne correspond à un retour chariot et pas à un changement de paragraphe.

# Retour à la ligne

Effectuer un saut de ligne simple dans votre texte markdown n’aura aucun effet sur le Export HTMLé. 
Sauf si vous terminez votre ligne par un double espace (ou plus que ça).
Un retour chariot sera alors exporté.  
Voilà (là j'ai fait un retour charriot)

# Italique et Gras

Italique : à mettre entre * : *italique*. Ou entre _ : _italique aussi_  
Gras : à mettre entre double * : **gras**. Ou entre double _ : __gras aussi__


# Les citations

Pour afficher un bloc de citation, commencez le paragraphe par un chevron fermant. Si votre bloc contient plusieurs lignes, vous pouvez faire des sauts de lignes à la main et toutes les ouvrir par un chevron fermant, mais ce n’est pas nécessaire. Ces bloc peuvent contenir d’autres éléments markdown comme des titres ou des listes.

> une citation est un paragraphe ouvert par un chevron fermant  
> qu'on peut mettre sur plusieurs lignes

# Listes

Pour afficher une liste, commencez la ligne par une astérisque * (marche aussi avec + et -).

* item avec *
* item avec *
* item avec *

# Les listes ordonnées

Pour afficher une liste ordonnée, commencez la ligne par un nombre suivit d’un point.
A noter : seule la numérotationdu premier point est important (marche aussi avec 1., 2., 25., 4....)


1. Item
2. Item
3. Item
4. Item

#Le bloc de code

Pour afficher un bloc de code, sautez deux lignes comme pour un paragraphe, puis indentez avec 4 espaces ou une tabulation. Dans le navigateur, la touche tabulation vous fait changer de champ et il n’est généralement pas possible de l’utiliser. Le bloc se terminera dès qu’il arrivera sur un ligne non indentée.


    ls -ltr /tmp
    pig/<language>/<projet>/<projet>.<ext>

#Le code inliné

Pour afficher du code dans une ligne, il faut l’entourer par des guillemets simples : (`).

Exemple, là j'ai du code : `ls -ltr /tmp`

#Les filets ou barres de séparation

Pour afficher un filet de séparation, entrez au moins 3 astérisques * sur une ligne entourée de sauts de ligne.

Saut de ligne :

***

#Les liens

Il y a deux façons d’afficher un lien. De manière automatique en encadrant un lien par des chevrons. Il est alors cliquable et affiche l’url indiquée entre chevrons.

<http://www.google.com>

Autre manière : en ajoutant des paramètres. Le texte à afficher est alors indiqué entre crochets suivi de l’adresse du lien entre parenthèses. Dans les parenthèses, à la suite du lien, on peut indiquer un titre entre guillemets. Ce titre sera affiché lors du survol du lien dans le navigateur. Il sera également lu par les navigateurs textuels pour les déficients visuels. Cette méthode est plus verbeuse lors de l’édition du document, mais plus élégante lors de sont export. Elle sera donc préférée à la première. 

    [google] (http://www.google.com "link to google")

  [google] (http://www.google.com "link to google")

#Les images

Pour afficher une image, commencez par un point d’exclamation. 
Puis indiquez le texte alternatif entre crochets. 
Ce dernier sera affiché si l’image n’est pas chargé et lu par les moteurs de recherche. 
Terminez par l’URL de l’image entre parenthèses. 
Cette URL peut être un lien vers le web ou un chemin local de ce type : /dossier_images/nom_de_mon_image.jpg. Après le lien vers l’image, il est possible d’ajouter un titre lu par les navigateurs textuels et affiché au survol de l’image par les autres.


    ![Google logo](https://www.google.fr/images/srpr/logo11w.png "google logo")

![Google logo](https://www.google.fr/images/srpr/logo11w.png "google logo")

#Les tableaux

Les tableaux n’existent pas dans la spécification markdown originale, mais ils sont présent dans la plupart des implémentations récentes. Et il ont vraiment une utilité très forte dans certains cas.

L’idée globale est de “dessiner” des colonnes en les entourant avec des pipes |. Le nombre de colonnes est défini dans la première ligne du tableau et vous devez pour chaque ligne avoir le même nombre de colonnes, même si certaines sont vides.

La première ligne sera votre en-tête. La seconde ligne sépare cet en-tête du corps du tableau et définit l’alignement du texte dans les colonnes. Elle ne contient que des tiret - et des deux points : sont utilisés pour définir cet alignement. Pas de : ou juste un à gauche signifie que le texte sera aligné à gauche. Si la ligne de - est entourée de 2 :, le texte sera centré et si un seul : est présent à droite de a ligne, le texte sera aligné à droite.

*** Code Mardown ***
*********************

    | Header 1      |     2 header    |   header 3 |
    | ------------- |: -------------: | ---------: |
    | 1 Online      |        1        |      value |
    | Line 2        |        2        |      value |
    | 3 Online      |        3        |      value |

| Header 1      |     2 header    |   header 3 |
| ------------- |: -------------: | ---------: |
| 1 Online      |        1        |      value |
| Line 2        |        2        |      value |
| 3 Online      |        3        |      value |

Vous pouvez avoir un tableau très propre comme dans l’exemple précédent pour mieux lire en mode édition. Mais ce n’est pas obligatoire. Les | en début et en fin de ligne sont optionnels. Il est possible d’imbriquer des éléments d’emphase ou de code dans les tableaux. Il n’y a besoin que d’un seul - par colonne pour la séparation entre l’en-tête et le corps du tableau.

    1 header | header 2 | 3 header
    - |:-: | -:
    line `1` | **1** | **_valeur_**
    Line 2 | 2 | *Value*

1 header | header 2 | 3 header
- |:-: | -:
line `1` | **1** | **_valeur_**
Line 2 | 2 | *Value*

#Échappement des caractères

antislash \\

\\ \* \` \- \_ \[\] \(\) \{\} \# \+ \. \!

#Séparer des blocs

Une petite chose peut se révéler agaçante : deux blocs consécutifs se verront fusionnés. 
Ce sera le cas de deux blocs de citation ou de code par exemple. 
Et ce quel que soit le nombre de lignes que vous sauterez. 
Une solution simple est d’ajouter des commentaires html entre deux blocs. 
La syntaxe des commentaire est la suivante : <!-- texte en commentaire -->;. 
Le texte sera ignoré par le navigateur. Votre commentaire peut tout à fait être vide.

> Citation 1

> Citation 2

> Citation 1
<!-- -->
> Citation 2
