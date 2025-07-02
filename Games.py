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
    "e3": "r3",
    "e4": "r4",
    "e5": "r5",
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
    elif opnm == def2("name"):
        return True, opnm    
    elif opnm == atk1("name"):
        return True, opnm
    elif opnm == atk2("name"):
        return True, opnm

    if opnm == "":
        return False, opnm
    
def entry(loc, out, enmloc):
    if out == True:

        if loc == "1":
            enmpres, enmname = enmcheck(entrmpairs[e1], enmloc)

            if enmpres == True:
                print(f"You enter through {e1} and an enemy is there.")

                choice = input("1) Identify and take cover (2 TP)\n"
                                "2) Take cover (1 TP)\n")
            else:
                print(f"You enter through {e1}. There are no enemies.")

                choice = input("1) Move (0.5 TP)\n"
                                "2) Use ability (2 TP)\n"
                                "3) Take cover (1 TP)\n")
        elif loc == "2":
            enmpres, enmname = enmcheck(entrmpairs[e2], enmloc)

            if enmpres == True:
                print(f"\nYou enter through {e2} and an enemy is there.\n")

                choice = input("\n1) Identify and take cover (2 TP)\n"
                                "2) Take cover (1 TP)\n")
            else:
                print(f"You enter through {e2}. There are no enemies.")

                choice = input("1) Move (0.5 TP)\n"
                                "2) Use ability (2 TP)\n"
                                "3) Take cover (1 TP)\n")
        elif loc == "3":
            enmpres, enmname = enmcheck(entrmpairs[e3], enmloc)

            if enmpres == True:
                print(f"You enter through {e3} and an enemy is there.")

                choice = input("1) Identify and take cover (2 TP)\n"
                                "2) Take cover (1 TP)\n")
            else:
                print(f"You enter through {e3}. There are no enemies.")

                choice = input("1) Move (0.5 TP)\n"
                                "2) Use ability (2 TP)\n"
                                "3) Take cover (1 TP)\n")

def singlernd():
    side = Side(sides)
    health, primary, secondary, special = opsl(side)

    enmloc = {"Surge": "r1", "Vortex": "r2"} if side == "def" else {"Citadel": "r1", "Bulwark": "r2"}

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