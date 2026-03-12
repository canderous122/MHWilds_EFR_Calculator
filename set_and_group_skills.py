from weapon_classes import *

def blagongas_spirit(dmg, lvl):
    if lvl < 1 or lvl > 2:
        raise Exception("Invalid level")
    return dmg + (3 * lvl)

def ebony_odogarons_power(dmg, lvl):
    if lvl == 1:
        return dmg + 3
    elif lvl == 2:
        return dmg + 10
    else:
        raise Exception("Invalid level")
    
def xu_wus_vigor(dmg, lvl):
    if lvl == 1:
        return dmg + 15
    elif lvl == 2:
        return dmg + 25
    else:
        raise Exception("Invalid level")
    
def rey_daus_voltage():
    return True

def jin_dahaads_revolt(dmg, lvl):
    if lvl < 1 or lvl > 2:
        raise Exception("Invalid level")
    return dmg + (25 * lvl)

def leviathans_fury(aff):
    return aff + 15

def mizutsunes_prowess():
    return True