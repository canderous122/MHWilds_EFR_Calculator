import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Then use it before each input prompt:
clear()
name = input("Enter your name: ")

clear()
age = input("Enter your age: ")

clear()
print(f"Hello {name}, you are {age} years old!")