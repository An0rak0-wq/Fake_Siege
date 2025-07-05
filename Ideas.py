import random
import math

playerstats = [["Health", "TP", "Primary", "Secondary", "Location", "Status", "Ammo"], 
                [180, 5, "AR", "Handgun", "e1", "unsafe", 100]]

enemystats = [["Health", "TP", "Primary", "Secondary", "Location", "Status", "Ammo"], 
                [180, 5, "AR", "Handgun", "e1", "safe", 100]]

gun_types = ["Secondary", "Primary"]

primaryguns = [["AR", "SMG", "LMG", "Shotgun"],
               [0.85, 0.55, 0.95, 0.5],
               [3.5, 2.05, 5, 2.45]]

secondaryguns = [["Handgun", "Claws"],
                [0.85, 1.25],
                [3.45, 4.55]]

turn = "Enemy"

hidden = "not"

def shoot(gtype, ammo):
    ammo -= 1

    Hits = hits(gtype, 10, hidden)
    Dmg = dmg(Hits, gtype)

    return ammo, Dmg, Hits

def peek_and_shoot(gtype, ammo, ophealth):
    print(f"Peek and Shoot, {gtype}")
    print(f"{ophealth}")
    input()

def hits(gtype, shotsfired, hidden):
    if gtype in primaryguns[0]:
        if hidden == "not":
            accuracy = 0.85

            index = primaryguns[0].index(gtype)
            gunaccuracy = primaryguns[1][index]

            mult = gunaccuracy * accuracy

            hits = math.floor(shotsfired * mult)

            return hits

        elif hidden == "partially":
            accuracy = 0.65

            index = primaryguns[0].index(gtype)
            gunaccuracy = primaryguns[1][index]

            mult = gunaccuracy * accuracy

            hits = math.floor(shotsfired * mult)

            return hits

        elif hidden == "completely":
            accuracy = 0.45

            index = primaryguns[0].index(gtype)
            gunaccuracy = primaryguns[1][index]

            mult = gunaccuracy * accuracy

            hits = math.floor(shotsfired * mult)

            return hits

    elif gtype in secondaryguns[0]:
        if hidden == "not":
            accuracy = 0.65
        
            index = secondaryguns[0].index(gtype)
            gunaccuracy = secondaryguns[1][index]

            mult = gunaccuracy * accuracy

            hits = math.floor(shotsfired * mult)

            return hits

        elif hidden == "partially":
            accuracy = 0.65
        
            index = secondaryguns[0].index(gtype)
            gunaccuracy = secondaryguns[1][index]

            mult = gunaccuracy * accuracy

            hits = math.floor(shotsfired * mult)

            return hits
            
        elif hidden == "completely":
            accuracy = 0.65
        
            index = secondaryguns[0].index(gtype)
            gunaccuracy = secondaryguns[1][index]

            mult = gunaccuracy * accuracy

            hits = math.floor(shotsfired * mult)

            return hits
        
def msg(dmg, hits, gtype):
    print(f"The enemy shoots at you with their {gtype}, hitting you {hits} time(s) and dealing {dmg} damage\n")
            
def dmg(Hits, gtype):
    if gtype in primaryguns[0]:
        return math.floor(Hits * primaryguns[2][primaryguns[0].index(gtype)])
    elif gtype in secondaryguns[0]:
        return math.floor(Hits * secondaryguns[2][secondaryguns[0].index(gtype)])

def fight(playerstats, enemystats):
    playeralive = True
    enemyalive = True
    turn = "Enemy"

    while enemyalive == True and playeralive == True:
        if turn == "Player":
            print("#################")
            print("### YOUR TURN ###")
            print("#################")
            print()

            print(f"Your health: {playerstats[1][0]}")
            print(f"Your TP: {playerstats[1][1]}\n")

            choice = int(input("1. Shoot Primary (2 TP)\n"
                               "2. Shoot Secondary (2 TP)\n"
                               "3. Peek and Shoot Primary (4 TP)\n"
                               "4. Peek and Shoot Secondary (4 TP)\n\n"))
            turn = "Enemy"
            
        elif turn == "Enemy":
            print("\n##################")
            print("### ENEMY TURN ###")
            print("##################")
            print()

            if playerstats[1][5] != "safe":
                gtype = random.choice(gun_types)

                if gtype == "Primary":
                    ammo, dmg, hits = shoot(enemystats[1][2], enemystats[1][6])
                    enemystats[1][6] = ammo
                    playerstats[1][0] -= dmg
                    turn = "Player"

                    gun = enemystats[1][2]

                    msg(dmg, hits, gun)

                    if playerstats[1][0] <= 0:
                        playeralive = False

                elif gtype == "Secondary":
                    ammo, dmg, hits = shoot(enemystats[1][3], enemystats[1][6])
                    enemystats[1][6] = ammo
                    playerstats[1][0] -= dmg
                    turn = "Player"
                    gun = enemystats[1][3]

                    msg(dmg, hits, gun)

                    if playerstats[1][0] <= 0:
                        playeralive = False
            else:
                gtype = random.choice(gun_types)

                if gtype == "Primary":
                    peek_and_shoot(enemystats[1][2], enemystats[1][6], playerstats[1][0])
                elif gtype == "Secondary":
                    peek_and_shoot(enemystats[1][3], enemystats[1][6], playerstats[1][0])

fight(playerstats, enemystats)

print("Player is dead")