###############
### IMPORTS ###
###############

from Operators import *
import random

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
            health, primary, secondary, special, name = atk1("get")

        return health, primary, secondary, special, name
    
    elif side == "def":
        names.append(def1("name"))
        choice = int(input(f"\n1) {names[0]}\n\n"))

        print(f"\nChosen operator - {names[choice - 1]}\n")

        if choice == 1:
            health, primary, secondary, special = atk1("get")

        return health, primary, secondary, special
    
def fight(vsop, plop, side):
    if side == "def":
        if vsop == "Surge":
            enmHealth, enmPrimary, enmSecondary, enmSpecial = atk1("get")

        print(enmHealth)
        print(enmPrimary)
        print(enmSecondary)
        print(enmSpecial)

def training():
    side = "def"
    health, primary, secondary, special = opsl(side)

    if side == "def":
        atkenm = ["Surge"]
        num = random.randint(0, (len(atkenm)-1))
        enmNm = atkenm[num]

def quick():
    print("Quick")

def normal():
    print("Normal")

def ranked():
    print("Ranked")