from opening_func import opening
from skill_calculation_func import calculation
from clear_func import clear

def main():
    w_type, dmg, aff, shrp = opening()

    dmg, aff, draw_dmg, draw_aff, ambush_dmg = calculation(w_type, float(dmg), float(aff))

    mult = shrp_calc(shrp)

    clear()
    print("Now, all the values have been calculated, I present to you:")
    print("")
    print(f"You're max effective raw attack power on your {w_type} is {int(dmg)}.")
    print("")
    print(f"The affinity of your {w_type} is {aff}%")
    print("")
    print(f"With a sharpness of {shrp}, your attack power is multiplied by {mult} to give {mult*dmg}.")
    print("")
    if draw_dmg != dmg and draw_aff != aff:
        print("I've also worked out the attack power and affinity for draw attacks.")
        print(f"On draw attacks, your {w_type} has an attack power of {int(draw_dmg)} and affinity of {draw_aff}%")
        print("")
    if ambush_dmg != dmg:
        print(f"Finally, theres also the case of draw attacks that are boost by ambush, the attack power on these are {int(ambush_dmg)}.")

    print("")
    ans = input("Press ENTER to continue>> ")
    if ans != "":
        clear()
        print("And what key was that?")

    print("")
    print("Thank you for using this small cli tool, I enjoyed creating it! In the future I'll try to add to it, add the ability for configs so you can save loadouts and so on, maybe add a database of armour and weapons. There are a lot of things I decided not to do to bring the scale of the project down, so who knows what I may add.")
    print("")
    print(f"Here are your final stats: Attack Power:{int(dmg)} , Affinity:{aff}%")


def shrp_calc(shrp):
    if shrp.lower() == 'red':
        mult = 0.5
    if shrp.lower() == 'orange':
        mult = 0.75
    if shrp.lower() == 'yellow':
        mult = 1
    if shrp.lower() == 'green':
        mult = 1.05
    if shrp.lower() == 'blue':
        mult = 1.2
    if shrp.lower() == 'white':
        mult = 1.32
    if shrp.lower() == 'purple':
        mult = 1.39
    return mult



main()