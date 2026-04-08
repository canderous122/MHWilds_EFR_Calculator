import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
print("Welcome to the Monster Hunter Wilds effective raw calculator")
print("This progam isn't completely accurate but its aim is to give you your highest possible damage possible under perfect conditions.")
print("Hopefully this is helpful in deciding what skills you should prioritise for the maximum possible DSP!")

w_type = input("So to begin, what type of weapon are you using?")

clear()
print("Now I need the attack power of the weapon, this is the stock value before any the type multiplier is applied or before any initial damage increase skills are applied.")
print("Essentially how the number for the weapon appears in your equipment box.")
dmg = input("Hopefully that made sense, so what is the attack power of your weapon?")

clear()
print("Now, I need the affinity of your weapon, again before any additions by any skills, such as Critical Eye or Maximum Might.")
aff = input("What is the affinity of your weapon?")

clear()
shrp = input("Finally, I just need the colour sharpness of your weapon:")

clear()
print("Thank you for completing that.")
print(f"Now, just to clarify that we're on the same page, you're using a {w_type} with attack power {dmg}, with {aff}% affinity and {shrp} sharpness?")