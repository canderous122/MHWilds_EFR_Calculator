from enum import Enum


class WeaponType(Enum):
    GREAT_SWORD = "great sword"
    LONG_SWORD = "long sword"
    SWORD_AND_SHEILD = "sword and sheild"
    DUAL_BLADES = "dual blades"
    HAMMER = "hammer"
    HUNTING_HORN = "hunting horn"
    LANCE = "lance"
    GUNLANCE ="gunlance"
    SWITCH_AXE = "switch axe"
    CHARGE_BLADE = "charge blade"
    INSECT_GLAIVE = "insect glaive"
    BOW = "bow"
    LIGHT_BOWGUN = "light bowgun"
    HEAVY_BOWGUN = "heavy bowgun"

def weapon_type_id(x):
    match x:
        case WeaponType.GREAT_SWORD:
            return "Great Sword"
        case WeaponType.LONG_SWORD:
            return "Long Sword"
        case WeaponType.SWORD_AND_SHEILD:
            return "Sword & Sheild"
        case WeaponType.DUAL_BLADES:
            return "Dual Blades"
        case WeaponType.HAMMER:
            return "Hammer"
        case WeaponType.HUNTING_HORN:
            return "Hunting Horn"
        case WeaponType.LANCE:
            return "Lance"
        case WeaponType.GUNLANCE:
            return "Gunlance"
        case WeaponType.SWITCH_AXE:
            return "Switch Axe"
        case WeaponType.CHARGE_BLADE:
            return "Charge Blade"
        case WeaponType.INSECT_GLAIVE:
            return "Insect Glaive"
        case WeaponType.BOW:
            return "Bow"
        case WeaponType.LIGHT_BOWGUN:
            return "Light Bowgun"
        case WeaponType.HEAVY_BOWGUN:
            return "Heavy Bowgun"

def weapon_type_id_inverse(x):
    match x:
        case "great sword":
            return WeaponType.GREAT_SWORD 
        case "long sword":
            return WeaponType.LONG_SWORD 
        case "sword and sheild":
            return WeaponType.SWORD_AND_SHEILD
        case "dual blades":
            return WeaponType.DUAL_BLADES
        case "hammer":
            return WeaponType.HAMMER
        case "hunting horn":
            return WeaponType.HUNTING_HORN
        case "lance":
            return WeaponType.LANCE
        case "gunlance":
            return WeaponType.GUNLANCE
        case "switch axe":
            return WeaponType.SWITCH_AXE
        case "charge blade":
            return WeaponType.CHARGE_BLADE
        case "insect glaive":
            return WeaponType.INSECT_GLAIVE
        case "bow":
            return WeaponType.BOW
        case "light bowgun":
            return WeaponType.LIGHT_BOWGUN
        case "heavy bowgun":
            return WeaponType.HEAVY_BOWGUN



class Weapon:
    def __init__(self, name, type, atk_pwr, aff, shrp, rarity,elem=0):
        self.name = name
        self.type = type
        self.atk_pwr = atk_pwr
        self.aff = aff
        self.shrp = shrp
        self.rarity = rarity
        self.elem = elem
        
        

    def repr(self):
        return f"This is a {weapon_type_id(self.type)} with attack power {self.atk_pwr} and affinity of {self.aff}% called {self.name}"


