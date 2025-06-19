### ACT 1: Fight requirements
---

##### SCENE 1: 

Requirements for a fight:
1. Enemy(s)
2. Position

##### SCENE 2:

For now, enemies will be static. By this, I mean that they will be assigned a room, and they will stay there for the duration of the round, or until they are killed.

Position is tricky. A map may need to be drawn (I really don't want to do this, I suck at maps) and fixed peeks may need to be created. There is a possibility for types of peek (ie hole in the wall or a window) to be generated in random locations around the map to make the game more engaging and replayable, but that will come further down the line.

##### SCENE 3:

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