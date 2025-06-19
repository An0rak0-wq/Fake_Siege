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
> "You enter the barricade. An enemy is on the stairs and open fire. 2TP are consumed going for cover, and 30 dmg taken"

TP - tactical points. These are spent each turn in order to create some form of strategy

> "1) Run (0.5 TP)
> "2) Peek (0.5 TP)
> "3) Fire (1 TP)
> "4) Peek and fire (3 TP)"

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