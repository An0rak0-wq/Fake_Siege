from Operators import *

enmloc = {
    "Citadel": "r1",
    "op2": "r2",
    "op3": "r3",
    "op4": "r4",
    "op5": "r5",
}

entrmpairs = {
    "e1": "r1",
    "e2": "r2",
    "e3": "r3"
}

e1 = "e1"
e2 = "e2"
e3 = "e3"

loc = e1
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
        if loc == "1":
            enmpres, opnm = enmcheck("r1")
            print(enmpres)
            print(opnm)

loc = input(f"1) {entrmpairs[e1]} ")

entry(loc, True)