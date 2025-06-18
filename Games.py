from Operators import *

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
            health, primary, secondary, special, name = atk1("get")

        return health, primary, secondary, special, name

def training():
    side = "def"
    health, primary, secondary, special, name = opsl(side)

    print(health)
    print(primary)
    print(secondary)
    print(special)
    print(name)

def quick():
    print("Quick")

def normal():
    print("Normal")

def ranked():
    print("Ranked")