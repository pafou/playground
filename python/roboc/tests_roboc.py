"""
Test module for "roboc" program.

Type "python tests_roboc.py" to test
"""

# -*-coding:Utf-8 -*

import unittest

from game import check_game_name
from game import check_user_choice

class TestCheckGameName(unittest.TestCase):
    def test_check_game_name_ko(self):
        for name in ['Nom qui va pas car sur plusieurs mots',
                    'Nom-avec-des-tirets',
                    'Nomavec#',
                    'Nomavec%',
                    '']:
            self.assertFalse(check_game_name(name),name) 

    def test_check_game_name_ok(self):
        for name in ['Nomquiva',
                    'Nomquiva01',
                    'Nomqui_va',
                    '1namequiva4']:
            self.assertTrue(check_game_name(name),name) 

class TestCheckUserChoice(unittest.TestCase):
    def test_check_user_choice_ok(self):
        for user_choice in ['Q','N','E','S','W','I']:
            self.assertTrue(check_user_choice(user_choice),user_choice) 
        for user_choice in ['N','E','S','W']:
            for i in [1,24,3,5,99,432566]:
                my_user_choice = user_choice + str(i)
                self.assertTrue(check_user_choice(my_user_choice),my_user_choice) 
    def test_check_user_choice_ko(self):
        for user_choice in ['Q12','I2','S0','abc','a dd','ES','0','12O','4I6','%%']:
            self.assertFalse(check_user_choice(user_choice),user_choice) 

if __name__ == '__main__':
    unittest.main()
