# -*-coding:Utf-8 -*

"""This module contains "Card" class."""


class Card:
    """Transition object between a file and a card.
       A card is defined by a name and "matrix".
       
       Attributes:
        - name: string containing the name of the card
        - matrix: 2 dimensional object composed of a list of lists
          containing characters.
    """
    
    def show(self):
        """Print the card."""
        for line in self.matrix:
            print (''.join(line))
        
    def __init__(self, name, text_from_file):
        """Card construction.
           self.matrix is initialized from the content of the file.
           self.robot_init_position is a list containing robot coordinates.
        """
        self.name = name
        ordi = 0 #Ordinate of robot position
        self.matrix = [] #Initialization of the list 
        lines = text_from_file.split("\n") #Card is split in lines
        for line in lines:
            #For each line, a list of characters is created.
            my_list = list(line)
            absc = 0 #Abscissa of robot position
            for char in my_list:
                if (char == 'X'):
                    try:
                        #Check if self.robot_init_position exists
                        type(self.robot_init_position)
                    except AttributeError:
                        #self.robot_init_position does not exist: we create it
                        self.robot_init_position = [absc,ordi]
                        my_list[absc]=" " #X in the matrix is replaced by " "
                        
                    else:
                        print ("Error: robot does not exist anymore on the card.")
                        exit(1)
                absc +=1
            #Then, list of characters is stored in list 'matrix'
            self.matrix.append(my_list)
            ordi += 1

    def __repr__(self):
        return "<Card {}>".format(self.name)
