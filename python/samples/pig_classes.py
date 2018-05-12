#-*- coding: utf-8 -*-

"""Pour manipuler les classes.
   La classe principale s'appelle ClasseScolaire et regroupe des eleves qui sont 
   eux-memes geres par une classe Eleve
"""

def bonjour():
    '''Return 'bonjour' '''
    return 'bonjour'

class Eleve:
    """Classe definissant un eleve caracterise par :
    - son nom
    - son prenom
    - son age
    - sa moyenne de l'année"""
    
    def __init__(self, nom, prenom): # méthode constructeur
        """Constructeur Eleve. Sa moyenne est nlle au départ, et il a 12 ans."""
        self.nom = nom
        self.prenom = prenom
        self.age = 12
        self.moyenne = 0


class ClasseScolaire:
    """Classe definissant une classe d'élève :
    - id: son numéro au format n.m (exemple 6.3 pour 6ème3)
    - eleves: liste d'élèves (sous forme d'objet Eleves)
    
    Méthodes:
    - moyenne: moyenne de tous les élèves"""

    def ajout(self, eleve):
        """Add eleve in ClasseScolaire"""
        self.eleves.append(eleve)     

    def moyenne(self):
        """Calculate average"""
        moy = 0.0
        nb_eleves = len(self.eleves)
        if (nb_eleves > 0):
            for el in self.eleves:
                moy = moy + el.moyenne
            moy = (moy / nb_eleves)
        return moy
        
    def __init__(self, id): # méthode constructeur
        """Constructeur ClasseScolaire."""
        self.id = id
        self.eleves = []

# Joué si le fichier est exécuté.
if __name__ == '__main__':
    classe = ClasseScolaire('6.3')
    eleve1 = Eleve('Fruchon','Damien')
    eleve2 = Eleve('Cramique','Yohann')
    eleve3 = Eleve('Grigou','Laurent')
    eleve1.moyenne = 8
    eleve2.moyenne = 12
    eleve3.moyenne = 1
    classe.ajout(eleve1)
    classe.ajout(eleve2)
    classe.ajout(eleve3)
    print "Moyenne = {}".format(classe.moyenne())
    
