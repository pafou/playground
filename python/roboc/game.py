# -*-coding:Utf-8 -*

"""This module contains Game class.
   A Game is composed of:
      - a robot: coordinates of the robot (a list : [abscissa, ordinate])
      - a matrix: it's a card, without robot
"""

import os
import pickle
import re
from sys import version_info #python version detection


def show_instructions():
    """Print instructions."""
    print ("""Instructions:
     I: instructions
     Q: quit
     S[n] : robot goes "South", for n steps (n is optional and must be an integer)
     N[n] : robot goes "North", for n steps (n is optional and must be an integer)
     W[n] : robot goes "West", for n steps (n is optional and must be an integer)
     E[n] : robot goes "East", for n steps (n is optional and must be an integer)
    """)
    
def check_game_name(game_name):
    """Check that the name of the game is a word (^\w+$)"""
    regexp = r"(^\w+$)"
    if re.match(regexp, game_name):
        return True
    else:
        return False

def check_user_choice(user_choice):
    """Check that user choice is an authorized choice: I, Q, E<n>, W<n>, N<n> or S<n>"""
    regexp = r"(^['Q','I']$)"
    regexp2 = r"(^['N','S','E','W']\d*$)"
    regexp3 = r"(^['N','S','E','W']0$)"
    if (re.match(regexp, user_choice) or re.match(regexp2, user_choice)
        and not re.match(regexp3, user_choice)):
        return True
    else:
        return False
    
class Game:
    """Class corresponding to a game.
       
       Attributes:
       - name : game name.
       - robot : list [absc, ordi]
       - matrix : list of lists from a matrix file, without robot
       Invariable attributes:
       - __path : path where games are stored
       - __max_absc : abscissa max (robot cannot go beyond)
       - __max_ordi : ordinate max (robot cannot go beyond)
       
       Moving:
       Coordinates of the robot are calculated like this:
           0-->abscissa
           |
           v ordinate
       
       When it goes South, ordinate = ordinate + 1
       When it goes North, ordinate = ordinate - 1
       When it goes West, abscissa = abscissa - 1
       When it goes East, abscissa = abscissa + 1
    """

    def save(self):
        """Save a game in a file. File name is game name."""
        saved_file = os.path.join(self.__path, self.name)
        with open(saved_file, 'wb') as file:
            my_pickler = pickle.Pickler(file)
            my_pickler.dump(self)

    def delete(self):
        """Delete a game by deleting file containing game."""
        saved_file = os.path.join(self.__path, self.name)
        os.remove(saved_file)

    def check_robot_move(self, absc, ordi):
        """Check if robot move is possible: wall ? matrix extremities...
        Return alert_message if move is not possible"""
        if (absc > self.__max_absc or ordi > self.__max_ordi):
            return "Robot cannot go beyond card frontier."
        elif (self.get_matrix_value(absc,ordi) == "O"):
            return "Robot cannot cross a wall (O)."
        elif (self.get_matrix_value(absc,ordi) == "U"):
            return ("EXIT")

    def get_matrix_value(self, absc, ordi):
        """Return character corresponding to coordinates [absc][ordi]"""
        o = 0 #Ordinate
        for line in self.matrix:
            a = 0 #Abscissa
            for car in line:
                if ([a,o] == [absc,ordi]):
                    return car
                a += 1
            o += 1

    def move_robot(self,dir_to_go,nb_moves):
        """Move robot <nb_moves> times to direction <dir_to_go>."""
        if version_info[0] < 3:
            for i in xrange(1, nb_moves+1): #xrange (python V2)
                alert_message = self.unit_robot_move(dir_to_go)
                if (alert_message is not None):
                    if (alert_message == "EXIT"):
                        return (alert_message)
                    else:
                        print ("\n\t--> Robot stopped because: {}\n".format(alert_message))
                        break
        else:
            for i in range(1, nb_moves+1): #range (python V3)
                alert_message = self.unit_robot_move(dir_to_go)
                if (alert_message is not None):
                    if (alert_message == "EXIT"):
                        return (alert_message)
                    else:
                        print ("\n\t--> Robot stopped because: {}\n".format(alert_message))
                        break

    def unit_robot_move(self,dir_to_go):
        """Unit robot move (N, S, E or W direction).
        check if the new position can be taken by the robot.
        If yes, the robot moves.
        If no, the robot does not move and the function sends an alert."""
        new_absc = self.robot[0]
        new_ordi = self.robot[1]
        if (dir_to_go == "S"):
            new_ordi = self.robot[1] + 1
        elif (dir_to_go == "N"):
            new_ordi = self.robot[1] - 1
        elif (dir_to_go == "W"):
            new_absc = self.robot[0] - 1
        elif (dir_to_go == "E"):
            new_absc = self.robot[0] + 1
        alert_message = self.check_robot_move(new_absc,new_ordi)
        if (alert_message is not None): #there is a problem
            return alert_message
        else: #It is ok: move the robot
            self.robot = [new_absc,new_ordi]

    def show(self):
        """Print the game.
           Consists in printing the matrix + an "X" where robot is
        """
        ordi = 0 #Ordinate of robot position
        for line in self.matrix:
            absc = 0 #Abscissa of robot position
            list_to_print = []
            for car in line:
                if ([absc,ordi] == self.robot):
                    list_to_print.append("X")
                else:
                    list_to_print.append(car)
                absc += 1
            print (''.join(list_to_print))
            ordi += 1


    def __init__(self, name='empty', robot=[0,0], matrix=[['X']]):
        """In case there is no argument, default values are (empty, [0,0] and [['X']])."""
        self.name = name
        self.robot = robot
        self.matrix = matrix
        self.__max_absc = 100000
        self.__max_ordi = 0
        for line in self.matrix:
            self.__max_ordi += 1 
            self.__max_absc = min(self.__max_absc,len(line))
        self.__path = "games"
        if not os.path.exists(self.__path):
                os.makedirs(self.__path)