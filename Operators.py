def overview(health, primary, secondary, special):
    print("\nOperator overview:\n"
          f"Health: {health}\n"
          f"Primary weapon: {primary}\n"
          f"Secondary weapom: {secondary}\n"
          f"Special: {special}\n")

def atk1(mde):
    health = "180"
    primary = "AR"
    secondary = "Handgun"
    special = "Increased Speed"
    name = "Surge"

    if mde == "view":
        overview(health, primary, secondary, special)
    elif mde == "name":
        return name

def def1(mde):
    health = "150"
    primary = "Shotgun"
    secondary = "Handgun"
    special = "Fortify Wall"
    name = "Citadel"

    if mde == "view":
        overview(health, primary, secondary, special)
    elif mde == "name":
        return name