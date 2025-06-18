############
### INFO ###
############

#Here is where is will place any info that needs to be read before execution. This can also be found in the README.

###############
### IMPORTS ###
###############

import random
from Operators import *

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

def menu(wt):
    choice = input("\n1) Play\n"
                   "2) Operators\n"
                   "3) Exit\n\n")
    
    if choice == "1":
            print("Play")
    elif choice == "2":
            choice = input(f"\n1) {names[0]}\n"
                           f"2) {names[1]}\n\n")
            
            if choice == "1":
                   atk1("view")
            elif choice == "2":
                   def1("view")

    elif choice == "3":
            print("Exit")

############
### MAIN ###
############

print("\nWelcome to Besiegement!")

while exit != True:
    menu()