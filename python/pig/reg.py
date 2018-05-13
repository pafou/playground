#-*- coding: utf-8 -*-
#re 
import re

file = open("fichier.txt","r") # file read for regexp

#sub #substitution
for line in file:
    # print ("Ligne :: {}".format(line)) # print line
    # print re.sub(r"(#)", r":)\1", line) # substitution of # with smiley :)#
    line = re.sub(r"\n", r"", line) # no \n
    # print(re.sub(r"id=(?P<id>[0-9]+)", r"id[\g<id>]", line)) # substitute id=(xx) with id[xx]]
    # print(re.sub(r"#(?P<tag>\w+)\W", r"TAG==[\g<tag>] ", line)) # substitute id=(xx) with id[xx]]

file.close()
#end
