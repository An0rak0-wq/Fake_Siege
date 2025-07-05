# ACT 1: Fight requirements
---

### SCENE 1: 

Requirements for a fight:
1. Enemy(s)
2. Position

### SCENE 2:

For now, enemies will be static. By this, I mean that they will be assigned a room, and they will stay there for the duration of the round, or until they are killed.

Position is tricky. A map may need to be drawn (I really don't want to do this, I suck at maps) and fixed peeks may need to be created. There is a possibility for types of peek (ie hole in the wall or a window) to be generated in random locations around the map to make the game more engaging and replayable, but that will come further down the line.

### SCENE 3:

Example (for analysis):
> You enter the barricade. An enemy is on the stairs and open fire. 2TP are consumed going for cover, and 30 dmg taken

TP - tactical points. These are spent each turn in order to create some form of strategy

> 1) Run (0.5 TP)<br>
> 2) Peek (0.5 TP)<br>
> 3) Fire (1 TP)<br>
> 4) Peek and fire (3 TP)

Run - run away
Peek - see if the enemy is still there 
Fire - shoot
Peek and fire - look - and if the enemy is there, shoot

The adv to peek and fire is that it conserves ammo.

I'll get these scenarios broken down, with the hopes of getting something I can code.

---
# ACT 2: Entry
---

### SCENE 1:

Forget drone phase for now, action phase has begun. The function should look like this:

```python
def entry(loc):
```

It controls the entry into the building, and probably the entry into all rooms in the building just to keep code more compact. However, it may need to know if the player is outside or not, so that it can apply appropriate context, so let's add that.

```python
def entry(loc, out):
```

Let's take it as loc = 1a and out = True, where 1a is the code for the entrance (which will be connected to a title in a dictionary so the player gets given a name) and True means that the player is outside. The function is as follows:

```python
def entry("1a", True):
```

It should print a statement to the player, saying where they have entered.

```python
loc = "1a"
out = True

def entry(loc, out):
    print(f"You have entered {loc}")
```

### SCENE 2:

While that statement works, it gets very repetitive and boring, very quickly. But as I said, it works. As they say, don't fix what ain't broken. So we'll get to work on something else and refine it later.

Now, I believe it would be usefull to know if an enemy is in the location the player has entered. For simplicity's sake, lets say that entrance 1a (Which i shall now rename e1, e for entrance/exit and 1 as it is the first) leads into r1 (room 1). We need a way of knowing what entrance leads to what room. This can be managed within an array, which outputs whether the room is populated (boolean output) and by how many (integer output). It will need the room code, which I will sort out in another function in a latter scene/act. For now:

```python
def enmcheck(rmcd):
```

We now need a way of knowing where each enemy is. We can use a 2d array for this, which can store the operator name and room code

```python
enmloc = [["op1", "op2", "op3", "op4", "op5"]
          ["r1", "r2", "r3", "r4", "r5"]]
```

The function will have access to this, so now attention can be turned back to it. We first need to check if the room code is in the array.

```python
def enmcheck(rmcd):
    if rmcd in enmloc:
```

If the room code is in the array, we then need to get the index so we can get the operator(s) name(s).

```python
def enmcheck(rmcd):
    if rmcd in enmloc:
        index = enmloc.index(rmcd)
```

### SCENE 3:

After testing, I found that a 2d array is not working nicely. I've decided to change it to a dictionary.

```python
enmloc = {
    "op1": "r1",
    "op2": "r2",
    "op3": "r3",
    "op4": "r4",
    "op5": "r5",
}
```

And due to the loop I am using to get the key, I have decided that no operators will be generated into the same room as another. Here is the following loop: 

```python
for key, val in enmloc.items():
    if val == rmcd:
        print(key) 
```

So the function will now look like this

```python
def enmcheck(rmcd):
    for key, val in enmloc.items():
        if val == rmcd:
            print(key) 
```

But we do not want the key printed, we want it returned. And if it is returned empty, then we can return false for enemies in the room. Furthermore, we no longer need to return how many enemies populate the room, but we do need the operator name. We can reuse the function created in Operators.py to easily get the name.

```python
def enmcheck(rmcd):
    opnm = ""

    for key, val in enmloc.items():
        if val == rmcd:
            opnm = key

    if opnm == def1():
        opnm = def1("name")
        return True, opnm

    if opnm == "":
        return False, ""
```

I will now test this code.

### SCENE 4:

This code seems to run, so I wil keep it for now. Going back to the entry procedure, I can now have it feed the room code to enmcheck as follows

```python
def entry(loc, out):
    if out == True:
        if loc == "e1":
            enmpres, opnm = enmcheck("r1")
        #Continue for other entrances
```

The code is functioning, and will work for all cases (once these cases are added). I will add the entire program below before moving on to the next section.

```python
from Operators import *

enmloc = {
    "Citadel": "r1",
    "op2": "r2",
    "op3": "r3",
    "op4": "r4",
    "op5": "r5",
}

loc = input(": ")
out = True

def enmcheck(rmcd):
    opnm = ""

    for key, val in enmloc.items():
        if val == rmcd:
            opnm = key

    if opnm == def1("name"):
        opnm = def1("name")
        return True, opnm

    if opnm == "":
        return False, opnm
    
def entry(loc, out):
    if out == True:
        if loc == "e1":
            enmpres, opnm = enmcheck("r1")
            print(enmpres)
            print(opnm)
```

---
# ACT 3: PLAYER INTERACTION
---

### SCENE 1:

First off, I want to allow th player to pick their entrance. This will allow me to create more entrances, and therefore more rooms. The dictionary containing the entrance and room pairs will look similar to this:

```python
entrmpairs = {
    "e1": "r1",
    "e2": "r2",
    "e3": "r3"
}
```

Then, this can fed into the entry function.

```python
def entry(loc, out, enmloc, entrmpairs):
    #code
```

Note that enmloc is now a parameter.

The function needs to take input from the user to decide which room to "scan".

```python
def entry(loc, out, enmloc, entrmpairs):
    loc = input(f"1) {entrmpairs["e1"]}")
    if out == True:
```

### SCENE 2:

The player can now interact with the game so far as to pick their operator from the two available on each side, and to pick their entrance (which are yet to get names, so are still presented as room/entrance codes). Now, it is important that the player gets a message if an operator is there. For now, this should suffice. The message should look as follows:

> You enter {xyz}, and an enemy is there

After this, the player should be presented with two options:

> 1) Identify and take cover (2 TP)<br>
> 2) Take cover (1 TP)

From here, the program goes on to either tell the player the name of the operator or to set the players status to "safe" (I am planning to create three states for the player; safe, semi-same/partially safe or unsafe) and initiate the fight.

The program first need to decide whether to display the message for enemy presence. Currently, the program returns and prints True is an enemy is present and false if there isn't. Instead, there should be an if statement to handle this

```python
if enmpres == True:
    print(f"You enter through {loc} and an enemy is there.")

    choice = input("1) Identify and take cover (2 TP)\n"
                    "2) Take cover (1 TP)\n")
else:
    print(f"You enter through {loc}. There are no enemies.")

    choice = input("1) Move (0.5 TP)\n"
                    "2) Use ability (2 TP)\n"
                    "3) Take cover (1 TP)\n")
```

This adapts to where the player is so can be used universally.

### SCENE 3:

It's time for the big moment: considering the fights. Here is a list of stats required:
1. Health
2. TP
3. Primary & secondary weapons
4. Location
5. Status
6. Ammo

I think the best way to store this is as a 2 dimensional list, as follows:

```python
playerstats = [["Health", "TP", "Primary", "Secondary", "Location", "Status", "Ammo"], 
                [180, 5, "AR", "Handgun", "e1", "safe", 100]]
```

And the same can be done for the enemy's stats:

```python
enemystats = [["Health", "TP", "Primary", "Secondary", "Location", "Status", "Ammo"], 
                [180, 5, "AR", "Handgun", "e1", "safe", 100]]
```

These can be passed into the function, and from there all the info can be unpacked

```python
def fight(playerstats, enmystats):
```

Now, a turn system has to be put in place. A variable called turn will contain the name of which party is currently having its turn, and an if statement can be used to switch whose turn it is. A while loop keeps things running until an operator dies (For now this will be the only way to end a fight).

```python
def fight(playerstats, enmystats):
    while enemyalive == True and playeralive == True:
        if turn == "Player":
            #Allow the player to do there turn
        elif turn == "Enemy":
            #Allow the AS (Artificial Stupidity, as it will be dumb as rocks) to make (poor) decisions
```

The AS will, pretty much, always try to do the same thing. If the player is not safe, it will shoot. If the player is safe, it will peek and shoot (a new option that does not always work (every time a gun is fired, accuracy will be decided using random, but peek and shoot will have lower chances)). It will then use random to decide whether to take cover or not (probably around about a 50/50 chance).

```python
def fight(playerstats, enemystats):
    while enemyalive == True and playeralive == True:
        if turn == "Player":
            #Allow the player to have their turn
        elif turn == "Enemy":
            if playerstats[1][5] != "safe":
                peek_and_shoot({whatever variables go here})
            else:
                shoot({whatever variables go here})
```

### SCENE 4:

First, I'll look at shoot(), as it's more likely to come up. It will require:
1. Gun type
2. Ammo

If there is enough ammo, it wil go on to use random, but if not, will tell the enemy and which switch turn immediately

```python
else:
    gtype = random.choice(gun_types)
    if gtype == "Secondary":
        shoot(enemystats[1][2], enemystats[1][6])
    elif gtype == "Primary":
        shoot(enemystats[1][3], enemystats[1][6])
```

The ammo pool will be the total accumulation; i.e the ammo for the primary and secondary weapon combined.

The shoot() function, as seen above, will take two arguments, the name of the gun and the amount of ammo remaining. For now, I will have it print "shots fired" and subtract 1 from the ammo pool

```python
def shoot(gtype, ammo):
    print("Shots fired")
    ammo -= 1
    return ammo
```

This is a start, but in a fight scenarion is of no use whatsoever. It needs to deal damage. It will take in another argument, ophealth, which is the health of the operator who is getting shot at. It will, for now, decrease this by a flat amount of 10 HP, and return it.

```python
def shoot(gtype, ammo, ophealth):
    print("Shots fired")
    ammo -= 1
    ophealth -= 10
    return ammo, ophealth
```

Now I shall test this and see if it works as intended.

### SCENE 5:

It is all working, and I have it updating the lists until it reaches the player's death (as for now there is no way for the player to pick what they do). The AS picks between it's primary and secondary at random, which will play a part in changing both the amount of damage dealt and the accuracy. Now, I need to work on having a message printed, before then working on the player's interaction (where I will finally need to implemet the use of TP).

The message will be fairly standard, and the same each time.

>"{enemy name} shoots at you with their {gun name}, hitting you {hits} time(s) and dealing {damage} damage."

And if they decide to hide behind something:

>"{enemy name} is now {hidden} hidden"

The variable "hidden" will be either not, partially or completely, showing the player their likelihood of hitting the enemy. This will be factored into the equation that decides how many shots hit.

This means some new claculations need to be made, and some new variables need to be returned.

I will experiment with some possibilites.

### SCENE 6:

The calculations look as follows:

> hits = shots fired * gun accuracy * accuracy

Gun accuracy is a unique value, not so much accuracy but points that are unique to each weapon that changes the mult. For example, the AR has a weapon accuracy of 0.85. When 10 shots are fired at an operator who is not safe, there are 7 hits.
This goes down to 4 if the weapon is changed to an SMG.

Now damage must be calculated. This can be held within a 3rd section in the primaryguns/secondaryguns list.

The weapon lists look as such:

```python
primaryguns = [["AR", "SMG", "LMG", "Shotgun"],
               [0.85, 0.55, 0.95, 0.5],
               [3.5, 2.05, 5, 2.45]]

secondaryguns = [["Handgun", "Claws"],
                [0.85, 1.25],
                [3.45, 4.55]]
```

And by constructing another function, I can calculate the damage by multiplying hits by the weapon damage, and rounding it down.

Now, this new and improved damage system needs to update the operator's health. This should be rather simple.