###############
### IMPORTS ###
###############

from Operators import *
import random

####################
### DICTIONARIES ###
####################

enmloc = {
}

###############################
### VARIABLE INITIALISATION ###
###############################

loc = ""
out = True

#################
### FUNCTIONS ###
#################

def opsl(side):
    names = []

    if side == "atk":
        names.append(atk1("name"))
        choice = int(input(f"\n1) {names[0]}\n\n"))

        print(f"\nChosen operator - {names[choice - 1]}\n")

        if choice == 1:
            health, primary, secondary, special = atk1("get")

        return health, primary, secondary, special
    
    elif side == "def":
        names.append(def1("name"))
        choice = int(input(f"\n1) {names[0]}\n\n"))

        print(f"\nChosen operator - {names[choice - 1]}\n")

        if choice == 1:
            health, primary, secondary, special = atk1("get")

        return health, primary, secondary, special
    
def enmcheck(rmcd, enmloc):
    opnm = ""

    for key, val in enmloc.items():
        if val == rmcd:
            opnm = key

    if opnm == def1("name"):
        opnm = def1("name")
        return True, opnm
    elif opnm == atk1("name"):
        opnm = atk1("name")
        return True, opnm

    if opnm == "":
        return False, opnm
    
def entry(loc, out, enmloc):
    if out == True:
        if loc == "e1":
            enmpres, opnm = enmcheck("r1", enmloc)
            print(enmpres)
            print(opnm)

def training():
    side = "atk"

    if side == "def":
        health, primary, secondary, special = opsl(side)

        atkenmloc = {
            "Surge": "r1"
        }

        loc = "e1"
        out = True

        entry(loc, out, atkenmloc)
    else:
        health, primary, secondary, special = opsl(side)

        defenmloc = {
            "Citadel": "r1"
        }

        loc = "e1"
        out = True

        entry(loc, out, defenmloc)


def quick():
    print("Quick")

def normal():
    print("Normal")

def ranked():
    print("Ranked")