#-*- coding: utf-8 -*-

"""Pour tester la fonction unittest"""


import unittest
 
# Le code a tester doit être importable. 
# Ici on teste pig_classes (Classes ClasseScolaire et Eleve)
from pig_classes import *
 
# Cette classe est un groupe de tests. Son nom DOIT commencer
# par 'Test' et la classe DOIT heriter de unittest.TestCase.


class TestMethodeBonjour(unittest.TestCase):
 
    # Chaque méthode dont le nom commence par 'test_' est un test.
    def test_bonjour(self):
 
        element = bonjour()
 
        # test simple d'égalité.
        self.assertEqual(element, 'bonjour')


class TestClasseClasseScolaire(unittest.TestCase):
 
    # Initialise le test
    def setUp(self):
        """Initialisation des tests."""
        self.classe = ClasseScolaire('6.3')
        self.eleve1 = Eleve('Fruchon','Damien')
        self.eleve2 = Eleve('Cramique','Yohann')
        self.eleve3 = Eleve('Grigou','Laurent')

    # Teste qu'un élève ajouté fait bien partie de la classe
    def test_add_eleve(self):
        self.classe.ajout(self.eleve1)
         # test que l'élève est dans la classe
        self.assertIn(self.eleve1, self.classe.eleves)

    # Teste la moyenne de la classe
    def test_moyenne_classe(self):
        self.eleve1.moyenne = 8
        self.eleve2.moyenne = 12
        self.eleve3.moyenne = 1
        self.classe.ajout(self.eleve1)
        self.classe.ajout(self.eleve2)
        self.classe.ajout(self.eleve3)
 
        # test que l'élève est dans la classe
        self.assertEqual(self.classe.moyenne(), 7)

# Ceci lance le test si on execute le script directement.
if __name__ == '__main__':
    unittest.main()