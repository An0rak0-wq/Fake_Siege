import random

playerstats = [["Health", "TP", "Primary", "Secondary", "Location", "Status", "Ammo"], 
                [180, 5, "AR", "Handgun", "e1", "unsafe", 100]]

enemystats = [["Health", "TP", "Primary", "Secondary", "Location", "Status", "Ammo"], 
                [180, 5, "AR", "Handgun", "e1", "safe", 100]]

gun_types = ["Secondary", "Primary"]

turn = "Enemy"

def shoot(gtype, ammo, ophealth):
    ammo -= 1
    ophealth -= 10
    print(f"Shoot, {gtype}")
    print(f"{ophealth}")
    input()
    return ammo, ophealth

def peek_and_shoot(gtype, ammo, ophealth):
    print(f"Peek and Shoot, {gtype}")
    print(f"{ophealth}")
    input()

def fight(playerstats, enemystats):
    playeralive = True
    enemyalive = True
    turn = "Enemy"

    while enemyalive == True and playeralive == True:
        if turn == "Player":
            print("Player's turn")
            input()
            turn = "Enemy"
            
        elif turn == "Enemy":
            if playerstats[1][5] != "safe":
                gtype = random.choice(gun_types)

                if gtype == "Primary":
                    ammo, health = shoot(enemystats[1][2], enemystats[1][6], playerstats[1][0])
                    enemystats[1][6] = ammo
                    playerstats[1][0] = health
                    turn = "Player"

                    if playerstats[1][0] <= 0:
                        playeralive = False

                elif gtype == "Secondary":
                    ammo, health = shoot(enemystats[1][3], enemystats[1][6], playerstats[1][0])
                    enemystats[1][6] = ammo
                    playerstats[1][0] = health
                    turn = "Player"

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