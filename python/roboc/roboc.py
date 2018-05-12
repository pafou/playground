# -*-coding:Utf-8 -*

"""Main code for roboc. Should work in python V2 and in python V3.

   En preambule: pour eviter tout probleme d'accent, le code et les commentaires
   sont en anglais (a l'exception notable de ces premiers commentaires dont 
   l'objectif est d'expliquer comment fonctionne le code pour l'exercice
   Openclassrooms).
   
   NB : je suis passe au tout "sans accent" car le code fonctionnait super bien
   en Python 2, et, lors des tests Python 3, malgre "# -*-coding:Utf-8 -*"
   en debut de code : des erreurs sporadiques sont apparues...
   Du coup j'ai tout traduit en anglais. Mais ai tout de meme laisse ce
   premier paragraphe en francais, sans les accents :-(, pour tout expliquer
   en language natif :-).

   Alors voila :
   ce fichier, roboc.py, contient le code principal du jeu.
   Executez-le avec Python pour lancer le jeu : 
       
       "python roboc.py"
   
   Le code a ete concu pour fonctionner en Python V2 et Python V3 (il y a 
   quelques differences notables sur les inputs, les xrange... entre V2 et V3).
   Et comme je ne suis pas sur que vous ayez la bonne version de Python...
   
   Quelques points a savoir:
      - la "carte" (card) est un objet cree a partir de la lecture d'un fichier txt
      - une "partie" (game) est un objet compose de : 
          o la position de robot (abscisse + ordonnee)
          o une carte epuree de la position initiale du robot
      - chaque coup implique la sauvegarde de l'objet "partie"
      
    Fonctionnement du programme:
        - la liste des cartes et des jeux en cours est proposée
        - l'utilisateur peut au choix :
            o demarrer un nouveau jeu a partir d'une carte (auquel cas il doit donner 
              un nom au jeu)
            o reprendre une partie en cours
        - a tout moment, en tapant "I", l'utilisateur peut avoir les instructions de mouvement
          du robot
"""

import os
import pickle
import re
from sys import version_info #For python version detection

from card import *
from game import *

#Python version detection
if version_info[0] < 3: # (python 2)
    print ("Python V2 detected: {}.{}.{}".format(version_info[0],version_info[1],version_info[2]))
else: # (python 3)
    print ("Python V3 detected: {}.{}.{}".format(version_info[0],version_info[1],version_info[2]))


#Existing cards are loaded
cards = [] #List of cards object read from txt files found in "cards" directory
for file_name in os.listdir("cards"):
    if file_name.endswith(".txt"):
        path = os.path.join("cards", file_name)
        card_name = file_name[:-4].lower()
        with open(path, "r") as file:
            my_content = file.read()
            my_card = Card(card_name,my_content)
            cards.append(my_card) 

#Printing existing cards
print("Start a new game from card:")
for i, card in enumerate(cards):
    print("  {} - {}".format(i + 1, card.name))
nb_cards = len(cards)

#Loading existing games
for file_name in os.listdir("games"):
    path = os.path.join("games", file_name)
    my_game = Game()
    try:
        """Fetch a game object from the file."""
        with open(path, 'rb') as file:
            my_depickler = pickle.Unpickler(file)
            my_game = my_depickler.load()
        cards.append(my_game) #Add game in list "cards" (list of cards and of existing games)
    except:
        pass

#Printing games list
list_of_existing_games = []
print("Resume game in progress:")
if (nb_cards == len(cards)):
    print ("  no game in progress")
else:
    if version_info[0] < 3:
        for i in xrange(nb_cards, len(cards)): #xrange (python V2)
            print("  {} - {}".format(i + 1, cards[i].name))
            list_of_existing_games.append(cards[i].name)
    else:
        for i in range(nb_cards, len(cards)): #range (python V3)
            print("  {} - {}".format(i + 1, cards[i].name))
            list_of_existing_games.append(cards[i].name)
        
#User can now choose between "new game from cards" and "resume game"
while True:
    try:
        if version_info[0] < 3:
            user_choice = int(raw_input("Your choice: ")) #Must be an integer (python V2)
        else:
            user_choice = int(input("Your choice: ")) #Must be an integer (python V3)
        if not (1 <= user_choice <= len(cards)): #Must correspond to user_choice
            raise AnError
        break #Getting out from while loop
    except:
        print ("Oops! Not a valid choice. Try again...")

print ("Ok. Let's go with {}-{}".format(user_choice,cards[user_choice-1].name))

if (1 <= user_choice <= nb_cards): 
    #User has chosen a card -> we have to create a new game from this card
    #First, we ask for a name
    while True: # 
        if version_info[0] < 3: # (python 2)
            game_name = raw_input("Give a name to your new game (simple word please): ") #New game name
        else: # (python 3)
            game_name = input("Give a name to your new game (simple word please): ") #New game name
        if (game_name in list_of_existing_games):
            print ("Game {} already exists: you must choose another name.".format(game_name))
        elif check_game_name(game_name):
            break
        else:
            print ("Oops!  Game name must be a simple word please. Try again...")
    #Creation of a new game from card
    my_card = cards[user_choice-1]
    my_game = Game(game_name, my_card.robot_init_position, my_card.matrix)
    my_game.save()
elif (nb_cards < user_choice <= len(cards)):
    #User has chosen to resume a game
    my_game = cards[user_choice-1]

my_game.show()

while (user_choice != "Q"):
    user_choice = "bad choice by default" #Default choice: does not support check
    while not (check_user_choice(user_choice)):
        print ("(Type 'I' for instructions)")
        if version_info[0] < 3: # (python 2)
            user_choice = raw_input("What do you want to do? ")
        else: # (python 3)
            user_choice = input("What do you want to do? ")
        if not (check_user_choice(user_choice)):
            print ("Humm... {} is a bad choice. You should ask for instructions.".format(user_choice))
    print ("Your choice: {}".format(user_choice))
    regexp = r"^(?P<dir_to_go>['N','S','E','W'])(?P<nb_moves>\d*)$"
    #Only N, S, E, and W are allowed with an optional number (exemple N5)
    #I or Q alone can also be chosen
    m = re.match(regexp, user_choice)
    if (user_choice == "I"):
        show_instructions()
    elif (m):
        dir_to_go = m.group("dir_to_go")
        nb_moves = m.group("nb_moves")
        if (nb_moves == ""):
            nb_moves = 1
        nb_moves = int(nb_moves)
        my_exit = my_game.move_robot(dir_to_go,nb_moves)
        #my_exit is "EXIT" only when robot reaches "U"
        if (my_exit =="EXIT"):
            print ("""\n\t==> GREAT D2R2. You dit it! Game "{}" is over.\n""".format(my_game.name))
            my_game.delete()
            break
        else:
            #Game is saved and then printed to screen
            my_game.save()
            my_game.show()

print ("Bye bye Amigo. Looking forward to seeing you.")