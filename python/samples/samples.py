#-*- coding: utf-8 -*-

# CONDITIONS
a = 5
b = 12
if a>0: # Si a est superieur a 0
    print(a," est superieur a 0.")
    if b<5:
        print("b est plus petit que 5")
    elif b==5:    
        print("b est egal a 5")
    else:
        print("b est plus grand que 5") 

if a>=2 and a<=8:
    print("a est dans l'intervalle.")
else:
    print("a n'est pas dans l'intervalle.")
    
annee=1600

while annee<1634:
    print(annee)
    if annee%4!=0:
        print("annee non multiple de 4 : non bissextile")
    else:
        if annee%100==0:
            if annee%400==0:
                print("annee multiple de 100 et de 400 : bissextile")
            else:
                print("annee multiple de 100 mais pas de 400 : non bissextile")
        else:
            print("annee non muliple de 100 : bissextile")
    annee += 1        
        
nb = 7 # On garde la variable contenant le nombre dont on veut la table de multiplication
i = 0 # C'est notre variable compteur que nous allons incrementer dans la boucle

while i < 10: # Tant que i est strictement inferieure a 10
    print(i + 1, "*", nb, "=", (i + 1) * nb)
    i += 1 # On incremente i de 1 a chaque tour de boucle


def table(nb, maxi):
    i = 0
    while i < maxi: # Tant que i est strictement inferieure a la variable max,
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

table(25,32)

def tablemax(nb, maxi=10):
    """Fonction affichant la table de multiplication par nb
    de 1*nb a max*nb
    
    (max >= 0)"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

help(tablemax)

def fonc(a=1, b=2, c=3, d=4, e=5):
    """fonc avec des valeurs par defaut -> c'est genial"""
    print("a =", a, "b =", b, "c =", c, "d =", d, "e =", e)
    
help(fonc)
fonc(b=3)

def carre(valeur):
    return valeur * valeur
print("carre de 3", carre(3))

ajout = lambda x,y: x+y

print (ajout(2,3))

from mon_package import mon_module
mon_module.ma_fonction("Yes man t'es un dieu, tu as imprime depuis une fonction dant un module")

help(mon_module)

import json

mon_fichier = open("fichier.json", "r")
contenu = mon_fichier.read()
print ("FICHER\n")
print (contenu)
print ("DUMPS\n")
print(json.dumps(contenu))
print ("REPR de LOADS\n")
obj = json.loads(contenu)
print(repr(obj))
mon_fichier.close()

import subprocess  

x = subprocess.Popen(["/Users/pascalfoucher/git/iac/test.bash", "ok"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print ("\nCODE RETOUR OK:",x.wait())
print ("sortie standard", x.stdout.read())
print ("erreurs : ",x.stderr.read())


x = subprocess.Popen(["/Users/pascalfoucher/git/iac/test.bash", "NA"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print ("\nCODE RETOUR NA:",x.wait())
print ("sortie standard", x.stdout.read())
print ("erreurs : ",x.stderr.read())


x = subprocess.Popen(["/Users/pascalfoucher/git/iac/test.bash", "ofdsk"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print ("\nCODE RETOUR KO:",x.wait())
print ("sortie standard", x.stdout.read())
print ("erreurs : ",x.stderr.read())

#STRING
# les string sont non modifiables
ma_chaine = """j'aime les string"""
print (ma_chaine[0:7] + "les cacahuetes")
print (ma_chaine.upper())

#LISTES et TUPLES
ma_liste = ["a", "b", "c"]
print (ma_liste)
print (ma_liste[2]) # 3eme element de la liste
ma_liste.append("d") # ajout de d en dernier
ma_liste.insert(2, 'c') # On insere 'c' a l'indice 2
ma_liste += [8, 9, 10] # ajout d'une liste a la fin
print (ma_liste)
del ma_liste[2] # on supprime le 3eme element
ma_liste.remove("c") # on retire la valeur c de la liste
print (ma_liste)
for i, elt in enumerate(ma_liste):
    print("A l'indice {} se trouve {}.".format(i, elt))
tuple_vide = ()
tuple_non_vide = (1,) # est equivalent a ci dessous
tuple_non_vide = 1,
tuple_avec_plusieurs_valeurs = (1, 2, 5) 
print (tuple_avec_plusieurs_valeurs)
print (ma_chaine.split(" "))
ma_liste = ['Bonjour', 'a', 'tous']
print (" ".join(ma_liste))

#parametres
def afficher(*parametres, sep=' ', fin='\n'):
    """Fonction chargee de reproduire le comportement de print.
    
    Elle doit finir par faire appel a print pour afficher le resultat.
    Mais les parametres devront deja avoir ete formates. 
    On doit passer a print une unique chaîne, en lui specifiant de ne rien mettre a la fin :

    print(chaine, end='')"""
    
    # Les parametres sont sous la forme d'un tuple
    # Or on a besoin de les convertir
    # Mais on ne peut pas modifier un tuple
    # On a plusieurs possibilites, ici je choisis de convertir le tuple en liste
    parametres = list(parametres)
    # On va commencer par convertir toutes les valeurs en chaîne
    # Sinon on va avoir quelques problemes lors du join
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    # La liste des parametres ne contient plus que des chaînes de caracteres
    # A present on va constituer la chaîne finale
    chaine = sep.join(parametres)
    # On ajoute le parametre fin a la fin de la chaîne
    chaine += fin
    # On affiche l'ensemble
    print(chaine, end='')

afficher("salut les cocos")

#Comprehension de liste
liste_origine = [0, 1, 2, 3, 4, 5]
print ([nb * nb for nb in liste_origine])

#SORT
inventaire = [
     ("pommes", 22),
     ("melons", 4),
     ("poires", 18),
     ("fraises", 76),
     ("prunes", 51),
]

# On change le sens de l'inventaire, la quantite avant le nom
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit,qtt in inventaire]
print (inventaire_inverse)
# On n'a plus qu'a trier dans l'ordre decroissant l'inventaire inverse
# On reconstitue l'inventaire trie
inventaire = [(nom_fruit, qtt) for qtt,nom_fruit in sorted(inventaire_inverse, reverse=True)]
print (inventaire)

#SYNTAXE 
une_liste = []
un_tuple = ()
un_dictionnaire = {}

type(une_liste)
type(un_tuple)
type(un_dictionnaire)

#DICTIONNAIRES
fruits = {"pommes":21, "melons":3, "poires":31}
for cle, valeur in fruits.items():
    print("La cle {} contient la valeur {}.".format(cle, valeur))
    
#Transformer un dictionnaire en parametres nommes d'une fonction

parametres = {"sep":" >> ", "end":" -\n"}
print("Voici", "un", "exemple", "d'appel", **parametres)

#FICHIERS
import os
print (os.getcwd())

mon_fichier = open("/tmp/fichier.txt", "w") # r=read, w=write, a=append + (option) b=binaire
mon_fichier.write("Premier test d'ecriture dans un fichier via Python\n")
mon_fichier.close()

with open("/tmp/fichier.txt","r") as un_fichier:
    texte = un_fichier.read()
    print (texte)
    
#PICKLE
import pickle
#Enregistrer un objet dans un fichier
score = {
   "joueur 1":    5,
   "joueur 2":   35,
   "joueur 3":   20,
   "joueur 4":    2,
}
with open('/tmp/donnees', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score)
#Recuperer nos objets enregistres
with open('/tmp/donnees', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere = mon_depickler.load()
print(score_recupere)


#:Classes - attributs de classes
# les noms de classes sont CamelCase (vs. snake_case)
class Personne:
    """Classe definissant une personne caracterisee par :
    - son nom
    - son prenom
    - son âge
    - son lieu de residence"""

    
    objets_crees = 0 # Le compteur vaut 0 au depart
    def __init__(self, nom): # Notre methode constructeur
        """Constructeur de notre classe. Chaque attribut va être instancie
        avec une valeur par defaut... original
        et A chaque fois qu'on cree un objet, on incremente le compteur"""
        Personne.objets_crees += 1 # attribut de classe incremente a chaque creation
        
        self.nom = nom
        self.prenom = "Jean" # Quelle originalite
        self.age = 33 # Cela n'engage a rien
        self.lieu_residence = "Paris"

ma_personne = Personne("Durand")
ma_personne.age = 45
print (ma_personne.nom, ma_personne.prenom)

ma_personne = Personne("Djai")
ma_personne = Personne("Flou")

print(Personne.objets_crees, "objets crees\n") # impression de l'attribut de classe

#: methodes de classe 
class Compteur:
    """Cette classe possede un attribut de classe qui s'incremente a chaque
    fois que l'on cree un objet de ce type"""

    
    objets_crees = 0 # Le compteur vaut 0 au depart
    def __init__(self):
        """A chaque fois qu'on cree un objet, on incremente le compteur"""
        Compteur.objets_crees += 1
    def combien(cls):
        """Methode de classe affichant combien d'objets ont ete crees"""
        print("Jusqu'a present, {} objets ont ete crees.".format(
                cls.objets_crees))
    combien = classmethod(combien)
    
#: methodes statiques 
class Test:
    """Une classe de test tout simplement"""
    def afficher():
        """Fonction chargee d'afficher quelque chose"""
        print("On affiche la même chose.")
        print("peu importe les donnees de l'objet ou de la classe.")
    afficher = staticmethod(afficher)
    

#: les proprietes
# les proprietes permettent de definir des fonctions d'acces aux attributs  (lecture, ecriture, suppression ou help)
# exemple avec des fonctions d'acces a lieu de residence
class Gens:
    """Classe definissant une personne caracterisee par :
    - son nom ;
    - son prenom ;
    - son âge ;
    - son lieu de residence"""

    
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._lieu_residence = "Paris" # Notez le souligne _ devant le nom
    def _get_lieu_residence(self):
        """Methode qui sera appelee quand on souhaitera acceder en lecture a
        l'attribut 'lieu_residence'"""
        
        
        print("On accede a l'attribut lieu_residence !")
        return self._lieu_residence
    def _set_lieu_residence(self, nouvelle_residence):
        """Methode appelee quand on souhaite modifier le lieu de residence"""
        print("Attention, il semble que {} demenage a {}.".format( \
                self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence
    # On va dire a Python que notre attribut lieu_residence pointe vers une
    # propriete
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)

jean = Gens("Micado", "Jean")
jean.lieu_residence
# affichera : On accede a l'attribut lieu_residence ! 'Paris'
jean.lieu_residence = "Berlin"
# affichera : Attention, il semble que Jean demenage a Berlin.

class MqQueue:
    """MqQueue : objet file MQ caracterisee par :
    - un alias
    - un type (QL, QR, QLD, QRD)
    - un environnement (DEV, INF, VAL, FR)
    - une profondeur"""

    
    def json(self):
        return json.dumps(self.__dict__)

    def json_print(self):
        json_out = "{\n"
        for cle in self.__dict__:
            json_out = json_out + "    \"" + cle + "\": \"" + str(self.__dict__[cle]) + "\",\n"
        json_out = json_out + "}\n"
        return json_out

    def __init__(self):
        """Constructeur de la classe."""
        self.alias = "vide"
        self.type = "vide" 
        self.env = "vide" 
        self.deep = 12

mq = MqQueue()
mq.alias = "VPMOGA"
mq.type = "QL"
mq.env = "VAL"

mon_json = mq.json_print()
print(mon_json)

mon_fichier = open("/tmp/mq.json", "w") # r=read, w=write, a=append + (option) b=binaire
mon_fichier.write(mon_json)
mon_fichier.close()

with open("/tmp/mq.json","r") as un_fichier:
    texte = un_fichier.read()
    print (texte)

print (mq.json())
