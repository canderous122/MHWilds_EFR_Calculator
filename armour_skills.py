from weapon_classes import *

def resentment(dmg, lvl):
    if lvl > 5 or lvl <= 0:
        raise Exception("Invalid Level")
    return dmg + (5 * lvl)

def adernaline_rush(dmg, lvl):
    if lvl > 5 or lvl <= 0:
        raise Exception("Invalid Level")
    return dmg + 5 + (5 * lvl)

def peak_performance(dmg, lvl):
    if lvl > 5 or lvl <= 0:
        raise Exception("Invalid Level")
    elif lvl == 1:
        return dmg + 3
    elif lvl == 2:
        return dmg + 6
    elif lvl == 3:
        return dmg + 10
    elif lvl == 4:
        return dmg + 15
    elif lvl == 5:
        return dmg + 20
    

