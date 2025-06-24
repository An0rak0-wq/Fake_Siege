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

entry(loc, out)