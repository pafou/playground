'''Full example with "argparse" module'''

#-*- coding: utf-8 -*-

#arg #argparse
import argparse

parser = argparse.ArgumentParser(description="description of my program") # parsing for managing arguments

parser.add_argument("echo", help="print what you typed for echo") # positional argument named echo (mandatory)
parser.add_argument("integ", help="print square of int", type=int) # positional argument named integ (mandatory, type forced to int)
parser.add_argument("--verbosity", help="increase output verbosity") # optional argument named verbosity (orgs.verbosity for the given *mandatory* value)
parser.add_argument("--turn_on", help="is True or False", action="store_true") # optional argument named turn_on (no value: args.turn_on set to True or False)
parser.add_argument("-s", "--short", help="can be short s or short", action="store_true") # optional argument named short (no value: True or False) ; can be "-s"
parser.add_argument("-a", "--action", choices=["get", "post", "delete", "put"], help="action to perform") # optional argument where possible values are limited
parser.add_argument("-d", "--defaut", choices=[0, 1, 2, 3], type=int, default='0', help="defaut set to default value 0 unless you give one") # optional argument where possible integer values are limited, and default value set to 0 
parser.add_argument("-m", "--mandatory", required=True, help="Mandatory argument") # mandatory argument


args = parser.parse_args() # arguments are parsed

print args.echo # value of echo is printed
print "Square of {0} is {1}".format(args.integ,args.integ**2)
if args.verbosity:
    print "verbosity turned on to {0}".format(args.verbosity)
if args.turn_on:
    print "turn_on turned to on"
if args.short:
    print "short (s) turned to on"
if args.action:
    print "action set to {0}".format(args.action)
print  "value of defaut is set to {0}".format(args.defaut)
