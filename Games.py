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
sides = ["atk", "def"]

entrmpairs = {
    "e1": "r1",
    "e2": "r2",
    "e3": "r3"
}

e1 = "e1"
e2 = "e2"
e3 = "e3"

#################
### FUNCTIONS ###
#################

def Side(sides):
    return random.choice(sides)

def opsl(side):
    names = []

    if side == "atk":
        operators = [atk1, atk2]
    else:
        operators = [def1, def2]

    for op in operators:
        names.append(op("name"))

    if side == "atk":
        print("\nYou are on attack")

        for i, name in enumerate(names, start=1):
            print(f"{i}) {name}")

        choice = int(input("\nChoose your operator: "))

        print(f"\nChosen operator - {names[choice - 1]}\n")

        health, primary, secondary, special = operators[choice - 1]("get")
        
        return health, primary, secondary, special
    
    elif side == "def":
        print("\nYou are on defence")
        
        for i, name in enumerate(names, start=1):
            print(f"{i}) {name}")

        choice = int(input("\nChoose your operator: "))

        print(f"\nChosen operator - {names[choice - 1]}\n")

        health, primary, secondary, special = operators[choice - 1]("get")

        return health, primary, secondary, special
    
def enmcheck(rmcd, enmloc):
    opnm = ""

    for key, val in enmloc.items():
        if val == rmcd:
            opnm = key

    if opnm == def1("name"):
        return True, opnm
    
    elif opnm == atk1("name"):
        return True, opnm

    if opnm == "":
        return False, opnm
    
def entry(loc, out, enmloc):
    if out == True:
        if loc == "1":
            enmpres, opnm = enmcheck("r1", enmloc)
            print(enmpres)
            print(opnm)

def singlernd():
    side = Side(sides)
    health, primary, secondary, special = opsl(side)

    enmloc = {"Surge": "r1"} if side == "def" else {"Citadel": "r1"}

    loc = input(f" 1) {entrmpairs[e1]}\n "
                f"2) {entrmpairs[e2]}\n "
                f"3) {entrmpairs[e3]}\n ")

    out = True
    entry(loc, out, enmloc)

def quick():
    print("Quick")

def normal():
    print("Normal")

def ranked():
    print("Ranked")