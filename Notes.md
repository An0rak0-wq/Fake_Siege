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
    "op1": "rm1",
    "op2": "rm2",
    "op3": "rm3",
    "op4": "rm4",
    "op5": "rm5",
}
```

And due to the loop I am using to get the key, I have decided that no operaotrs will be generated into the same room as another. Here is the following loop: 

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