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
names.append(atk1("name"))
names.append(def1("name"))

#################
### FUNCTIONS ###
#################

def gameselect():
    choice = input("\n1) Training\n"
                    "2) Quick\n"
                    "3) Normal\n"
                    "4) Ranked\n\n")
       
    if choice == "1":
        singlernd()
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
            choice = input(f"\n1) {names[0]}\n"
                           f"2) {names[1]}\n\n")
            
            if choice == "1":
                    atk1("view")
            elif choice == "2":
                    def1("view")
            elif choice == "3":
                    sys.exit()

############
### MAIN ###
############

print("\nWelcome to Besiegement!")

while exit != True:
    menu()