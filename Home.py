############
### INFO ###
############

#Here is where is will place any info that needs to be read before execution. This can also be found in the README.

###############
### IMPORTS ###
###############

import random, sys
from Operators import *
from Games import *

######################
### INITIALISATION ###
######################

exit = False
names = []
opfunctions = [atk1, atk2, def1, def2]

for func in opfunctions:
    names.append(func("name"))

#################
### FUNCTIONS ###
#################

def gameselect():
    choice = input("\n1) Single Round\n"
                    "2) Quick\n"
                    "3) Normal\n"
                    "4) Ranked\n\n")
       
    if choice == "1":
        singlernd(side)
    elif choice == "2":
        quick()
    elif choice == "3":
        normal()
    elif choice == "4":
        ranked()

def menu():
    choice = input("\n1) Play\n"
                   "2) Operators\n"
                   "3) Exit\n\n")
    
    if choice == "1":
            gameselect()
    elif choice == "2":
        choice = input("\n1) Attack\n"
                       "2) Defense\n\n")
        
        if choice == "1":
            attack_operators = names[:len(names) // 2]
            print("\n##############")
            print("### ATTACK ###")
            print("##############")
            choice = int(input("\n" + "\n".join([f"{i + 1}) {name}" for i, name in enumerate(attack_operators)]) + "\n\n"))

            if choice == 1:
                atk1("view")
            elif choice == 2:
                atk2("view")
        
        elif choice == "2":
            defense_operators = names[len(names) // 2:]
            print("\n###############")
            print("### DEFENSE ###")
            print("###############")
            choice = int(input("\n" + "\n".join([f"{i + 1}) {name}" for i, name in enumerate(defense_operators)]) + "\n\n"))

            if choice == 1:
                def1("view")
            elif choice == 2:
                def2("view")



############
### MAIN ###
############

print("\nWelcome to Besiegement!")

while exit != True:
    menu()