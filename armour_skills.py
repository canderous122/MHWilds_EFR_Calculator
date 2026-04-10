from weapon_classes import *

def resentment(dmg, lvl):
    if lvl > 5 or lvl <= 0:
        raise Exception("Invalid level")
    return dmg + (5 * lvl)

def adernaline_rush(dmg, lvl):
    if lvl > 5 or lvl <= 0:
        raise Exception("Invalid level")
    return dmg + 5 + (5 * lvl)

def peak_performance(dmg, lvl):
    if lvl == 1:
        return dmg + 3
    elif lvl == 2:
        return dmg + 6
    elif lvl == 3:
        return dmg + 10
    elif lvl == 4:
        return dmg + 15
    elif lvl == 5:
        return dmg + 20
    else:
        raise Exception("Invalid level")
    
def counterstrike(dmg, lvl):
    if lvl == 1:
        return dmg + 10
    elif lvl == 2:
        return dmg + 15
    elif lvl == 3:
        return dmg + 25
    else:
        raise Exception("Invalid level")
    
def weakness_exploit(aff, lvl): 
    if lvl == 1:
        return aff + 5
    elif lvl == 2:
        return aff + 10
    elif lvl == 3:
        return aff + 15
    elif lvl == 4:
        return aff + 20
    elif lvl == 5:
        return aff + 30
    else:
        raise Exception("Invalid level")
    
def maximum_might(aff, lvl):
    if lvl > 3 or lvl <= 0:
        raise Exception("Invalid level")
    return aff + (10 * lvl)

def agitator(dmg, aff, lvl): 
    if lvl == 1:
        return dmg + 4, aff + 3
    if lvl == 2:
        return dmg + 8, aff + 5
    if lvl == 3:
        return dmg + 12, aff + 7
    if lvl == 4:
        return dmg + 16, aff + 10
    if lvl == 5:
        return dmg + 20, aff + 15


def latent_power(aff, lvl):
    if lvl < 1 or lvl > 5:
        raise Exception("Invalid level")
    return aff + (10 * lvl)

def burst(type, dmg, lvl): 
    if type == WeaponType.GREAT_SWORD or type == WeaponType.HUNTING_HORN:
        if lvl > 5 or lvl <= 0:
            raise Exception("Invalid level")
        return dmg + (2 * lvl)
    
    elif type == WeaponType.BOW or type == WeaponType.HEAVY_BOWGUN or type == WeaponType.LIGHT_BOWGUN:
        if lvl > 5 or lvl <= 0:
            raise Exception("Invalid level")
        return dmg + lvl
            
    else:
        match lvl:
            case 1:
                return dmg + 8
            case 2:
                return dmg + 10
            case 3:
                return dmg + 12
            case 4:
                return dmg + 15
            case 5:
                return dmg + 18
            

def heroics(dmg, lvl):
    if lvl == 1:
        return dmg
    elif lvl == 2:
        return dmg * 1.05
    elif lvl == 3:
        return dmg * 1.05
    elif lvl == 4:
        return dmg * 1.1
    elif lvl == 5:
        return dmg * 1.3
    else:
        raise Exception("Invalid level")