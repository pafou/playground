#-*- coding: utf-8 -*-

"""
    List, create, update or delete files in /tmp/tmps/<env> directory.
   
    Environment is mandatory. It corresponds to dev, val, inf or fr.
   
    Actions are:
       * get: for listing files (output=json file)
          * if a primary key (corresponding to the name of the file) is given: list the file
          * without primary key: all files are listed
       * post: for creating a new file (input=json file) - the name of the file is provided in the json file
       * put: for updating an existing file (input=json file) - the name of the file is provided in the json file
       * delete: for delting an existing file -the name of the file is set with '-k' option
   
    Json file format is the following:
       
        {
          "env": "<env>",
          "mode": "0<nnn>",
          "name": "<name>"
        },

    where:
       * <env> is the environment (must correspond to environment given with '-e' option)
       * <nnn> is the mode of the file, must correspond to regex "[2,6,7][1-7]{2}" (examples: 0644, 0755, 0632...)
       * <name> is the name of the file (must correspond to regex "\w+")
    
    #Examples:
        
        python  tmps.py -e dev -a post -j '{"env":"dev","mode": "0644","name": "Maurice"}' 
    creates file Maurice, with mode "0644", for environment dev. File created is `/tmp/tmps/dev/Maurice`
        
        python tmps.py -e dev -a get 
    lists files in `/tmp/tmps/dev`
        
        python  tmps.py -e dev -a put -j '{"env":"dev","mode": "0755","name": "Maurice"}' -k Maurice 
    update file Maurice, with mode "0755", for environment dev.
        
        python  tmps.py -e dev -a delete -k Jean
    deletes file Maurice
"""
from __builtin__ import False

# for RORO
# full initialisation
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list_alphabet = list(alphabet)

max_size = int(raw_input("Give max size: "))

dict_alphabet = dict()

num = 1
for letter in list_alphabet:
    dict_alphabet[letter] = num
    if (num == max_size):
        break
    num += 1

print (dict_alphabet)

while True:
    user_choice = raw_input("Give a letter: ")
    if (user_choice in dict_alphabet):
        print ("Good letter")
        ind = dict_alphabet[user_choice]
        print "Letter: {0} ; Index: {1}".format(user_choice, ind)    
    elif (user_choice == "q"):
        print ("Bye kid")
        break
    else:
        print ("Shoot again!")
