from weapon_classes import *


def main1():
    i = 0
    while i < 1:
        x = input("Stop or keep going?")
        if x == "keep going".lower():
            continue
        elif x == "stop".lower():
            print("Stopping...")
            return
        else:
            print("invalid input, please try again")
            continue


def main2():
    i = 0
    list = []
    print(a)
    print("Add something to the list,'show' what you have so far, or 'stop' the program and present list?")
    while i < 1:
        print(" ")
        x = input("Input:")
        if x == "stop".lower():
            print("Stopping...")
            print("Generating list...")
            print(" ")
            print(list)
            return
        elif x == "show".lower():
            print(" ")
            print("Here's what you have so far:")
            print(" ")
            print(list)
        else:
            print(" ")
            print(f"adding {x} to the list :)")
            list.append(x)
            continue


a = "Monster Hunter Effective Raw Calculator!"

def main3():
    print("Let's configure your weapon")
    print(" ")
    name = input("whats the weapons name?")
    type = input("whats your weapons type?")
    print("")
    print(f"The name of the weapon is {name} and it is a {type}")
    print("")
    dmg = input("Whats the attack power of your weapon? ")
    aff = input("what is the affinity of your weapon? ")
    shrp = input("What colour sharpness is your weapon? ")
    print("")
    print(f"The attack power is {dmg} and the affinity is {aff}, with {shrp} sharpness")
    print("")
    rarity = input("What is the rarity of your weapon? ")
    elem = input("What element is your weapon? ")
    print("")
    print(f"Your weapon has is rarity {rarity} and has {elem} element")
    print("generating your weapon....")
    user_wpn = Weapon(name, weapon_type_id_inverse(type.lower()),dmg, aff, shrp, rarity, elem)
    print(user_wpn.repr())

main3()



