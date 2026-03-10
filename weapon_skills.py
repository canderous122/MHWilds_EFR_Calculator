from weapon_classes import *

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

def critical_draw(aff, lvl): # On the sidenote for draw attacks
    if lvl == 1:
        return aff + 50
    elif lvl == 2:
        return aff + 75
    elif lvl == 3:
        return aff + 100
    else:
        raise Exception("Invalid level") 
    
def handicraft(shrp, lvl):
    if lvl > 5 or lvl <= 0:
        raise Exception("Invalid level")
    return shrp + (lvl * 10)


def punishing_draw(dmg, lvl): # make a sidenote for draw attacks
    if lvl == 1:
        return dmg + 3
    if lvl == 2:
        return dmg + 5
    if lvl == 3:
        return dmg + 7
    else:
        raise Exception("Invalid level")
    
def slicked_blade(aff, lvl): #bool checks for if bubbleblight is possible, although could also just fight a mizu so it should always be true. 
    if lvl == 1:
        return aff + 7
    elif lvl == 2:
        return aff + 14
    elif lvl == 3:
        return aff + 21
    else:
        raise Exception("Invalid level")

def power_stone(dmg):
    return dmg + 30

def darkside(dmg):
    return dmg + 22

def synergy(aff, bool): #bool is only true if resonance is lvl 2
    if bool:
        return aff + 25
    else:
        return aff + 15
    
def omega_resonance(dmg, aff, lvl): # arr[0] is dmg, arr[1] is affinity
    if lvl == 1:
        return [dmg+10, aff+20]
    elif lvl == 2:
        return [dmg+20, aff+40]
    else:
        raise Exception("Invalid level")

def grillmaster(aff):
    return aff + 10

def bludgeoner(dmg, lvl):
    if lvl == 1:
        return dmg * 1.05
    elif lvl == 2:
        return dmg * 1.1
    elif lvl == 3:
        return dmg * 1.1
    else:
        raise Exception("Invalid level")
    
def ambush(dmg, lvl): #Can also get its own catergory and link in with draw attack scaling
    if lvl < 1 or lvl > 3:
        raise Exception("Invalid level")
    return dmg + (dmg * 0.05 * lvl)

def antivirus(aff, lvl): #Will need to check that gore magalas tyranny is up to level two for this to proc
    if lvl == 1:
        return aff + 3
    if lvl == 2:
        return aff + 6
    if lvl == 3:
        return aff + 15