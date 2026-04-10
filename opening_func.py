from clear_func import clear
     
def opening():

    print("Welcome to the Monster Hunter Wilds effective raw calculator")
    print("This progam isn't completely accurate but its aim is to give you your highest possible damage possible under perfect conditions.")   
    print("Hopefully this is helpful in deciding what skills you should prioritise for the maximum possible DPS!")
    ans2 = input("Press ENTER to continue >>")

    if ans2 == "":
        clear()
    else:
        clear()
        print("What key did I ask you to press?..")
        print()

    i = 1
    while i == 1:    
        w_type = input("So to begin, what type of weapon are you using?  ").strip()

        clear()
        print("Now I need the attack power of the weapon, this is the stock value before any the type multiplier is applied or before any initial damage increase skills are applied.")
        print("Essentially how the number for the weapon appears in your equipment box.")
        print()
        dmg = input("Hopefully that made sense, so what is the attack power of your weapon?  ").strip()

        clear()
        print("Now, I need the affinity of your weapon, again before any additions by any skills, such as Critical Eye or Maximum Might.")
        print()
        aff = input("What is the affinity of your weapon?  ").strip()

        clear()
        shrp = input("Finally, I just need the colour sharpness of your weapon:  ").strip()

        clear()
        print("Thank you for completing that.")
        print()
        print(f"Now, just to clarify that we're on the same page, you're using a {w_type} with attack power {dmg}, with {aff}% affinity and {shrp} sharpness?")
        ans = input("Is this correct? (y/n)  ")
        
        if ans.lower().strip() == "y":
            return w_type, dmg, aff, shrp
        if ans.lower().strip() == "n":
            clear()
            continue
        else:
            raise Exception("Please input valid answer.")
        