

def attack_boost(dmg, lvl):
    if lvl == 1:
        return dmg + 3
    elif lvl == 2:
        return dmg + 5
    elif lvl == 3:
        return dmg + 7
    elif lvl == 4:
        return (dmg * 1.02) + 8
    elif lvl == 5:
        return (dmg * 1.04) + 9
    else:
        raise Exception("Invalid level")

def offensive_guard(dmg, lvl):
    if lvl == 1:
        return dmg * 1.05
    elif lvl == 2:
        return dmg * 1.10
    elif lvl == 3:
        return dmg * 1.15
    else:
        raise Exception("Invalid level")

def critical_boost(dmg, lvl): #added at end once total affinity has been calculated, all aff and dmg calculations are seperate until final dmg is found at the end.
    if lvl == 1:
        return dmg * 1.28
    elif lvl == 2:
        return dmg * 1.31
    elif lvl == 3:
        return dmg * 1.34
    elif lvl == 4:
        return dmg * 1.37
    elif lvl == 5:
        return dmg * 1.4
    else:
        raise Exception("Invalid level")

def critical_eye(aff, lvl):
    if lvl == 1:
        return aff + 4
    elif lvl == 2:
        return aff + 8
    elif lvl == 3:
        return aff + 12
    elif lvl == 4:
        return aff + 16
    elif lvl == 5:
        return aff + 20
    else:
        raise Exception("Invalid level")

def critical_draw(aff, lvl):
    if lvl == 1:
        return aff + 50
    elif lvl == 2:
        return aff + 75
    elif lvl == 3:
        return aff + 100
    else:
        raise Exception("Invalid level") 
    
def handicraft(shrp, lvl):
    if lvl > 5:
        raise Exception("Invalid level")
    return shrp + (lvl * 10)

def burst(wpn, dmg, lvl): # going to come back to this once I have finalised the weapon classes
    pass

def punishing_draw(dmg, lvl): # make a sidenote for draw attacks
    if lvl == 1:
        return dmg + 3
    if lvl == 2:
        return dmg + 5
    if lvl == 3:
        return dmg + 7
    else:
        raise Exception("Invalid level")
    
def slicked_blade(): #gonna have to figure this one out
    pass
