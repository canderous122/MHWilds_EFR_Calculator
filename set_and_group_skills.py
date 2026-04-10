from weapon_classes import *

# Set bonus skills ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

def omega_resonance(dmg, aff, lvl): # arr[0] is dmg, arr[1] is affinity
    if lvl == 1:
        return dmg+10, aff+20
    elif lvl == 2:
        return dmg+20, aff+40
    else:
        raise Exception("Invalid level")

def seregios_tenacity(dmg, lvl):
    if lvl == 2:
        return dmg * 1.035
    elif lvl == 1:
        return dmg
    else:
        raise Exception("Invalid level")
    
def gore_magalas_tyranny(dmg, aff, lvl): # arr[0] is dmg, arr[1] is aff, pairs with antivirus
    if lvl == 1:
        return dmg, aff + 15
    elif lvl == 2:
        return dmg + 15, aff + 15
    else:
        raise Exception("Invalid level")


# Group SKils ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def fortifying_pelt(dmg): # need to incorporate a way to say that this is after 2 faints
    return dmg * 1.2

def lords_fury(dmg):
    return dmg + 10

def lords_soul(dmg):
    return dmg * 1.05

