############
### INFO ###
############

#Here is where is will place any info that needs to be read before execution. This can also be found in the README.

###############
### IMPORTS ###
###############

import random
from Operators import *

###############################
### VARIABLE INITIALISATION ###
###############################

exit = False

#################
### FUNCTIONS ###
#################

def menu():
    print("\nWelcome to Besiegement!")
    choice = input("1) Play\n"
                   "2) Operators\n"
                   "3) Settings\n"
                   "4) Exit\n")
    
    if choice == "1":
            print("Play")
    elif choice == "2":
            print("Operators")
    elif choice == "3":
            print("Settings")
    elif choice == "4":
            print("Exit")

############
### MAIN ###
############


while exit != True:
    menu()