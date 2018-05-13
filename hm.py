#-*- coding: utf-8 -*-

import os, stat, sys, re, fnmatch
import argparse
parser = argparse.ArgumentParser(description=
    """
    Help Me, find code samples in code source files.
    """,
                                 epilog=
    """
    
    #Examples:
        
        hm.py -t sub
    find tag "#sub" in all code files
        
        hm.py -k open
    find key word "open" in all code files
    """,
    formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("-t", "--tag", help="tag to find") # optional argument
parser.add_argument("-k", "--kw", help="key word") # optional argument

def hm_error(a_text):
    """
    Prints error messages in standard format, and exit(1)
    """
    print "Error in hm : {0} ; exit 1".format(a_text)
    exit(1)
    

if __name__ == '__main__':
    args = parser.parse_args() # arguments are parsed

    #Check args
    if (args.tag and args.kw):
        hm_error("Args check: must be -k or -t, but not both")
    if (not args.tag and not args.kw):
        hm_error("Args check: -k or -t mandatory")
    
    #Let'go. Checks are ok.

# tag & key word
tag = args.tag
kw = args.kw

# find code files
 
in_dir = '.'
pattern = '*.*' # not limited right now
file_list = []
 
# walk through directory
for d_name, sd_name, f_list in os.walk(in_dir):
    for file_name in f_list:
        if fnmatch.fnmatch(file_name, pattern): # Match search string
            file_list.append(os.path.join(d_name, file_name))

# search in code file
for file_name in file_list:
    file = open(file_name,"r") # file read
    good = "no" # default, need good="yes" to print result
    if (kw):
        rx = re.compile(re.escape(kw))
    elif (tag):
        rx = re.compile(r"\#" + re.escape(tag))
    
    for line in file:
        if (re.search(rx,line)): # search matches
            good = "yes"
            print ("\n\n** File: {}\n".format(file.name)) # print file name first
        elif (tag and re.search(r"\#\w",line)): # for tag research, print ends when another #\w is find
            good = "no"
        elif (kw): # for key word research, print stops if search does not find
            good = "no"
        if (good == "yes"):
            line = re.sub(r"\n", r"", line) # no \n in print result
            print line
    file.close()