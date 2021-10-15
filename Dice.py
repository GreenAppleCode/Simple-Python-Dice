import random

def dice():
    Sides = input("How many sides would you like the dice to have?: ")
    Amount_of_Dice = input("How many dice would you like to roll?: ")
    Amount_of_Dice = int(Amount_of_Dice)
    Sides = int(Sides)
    counter = 0
    while counter < Amount_of_Dice:
        dice2 = random.randint(1, Sides)
        print(dice2)
        counter = counter + 1
    yorn = input("Do you want to roll again(y/n): ")
    if yorn == "y":
        dice()
    elif yorn == "Y":
        dice()
    elif yorn == "n":
        print("Alright, have a nice day!")
        exit()
    elif yorn == "N":
        print("Alright, have a nice day!")
        exit()
    else:
        print("Invalid Syntax, Closing Program...")
        exit()
dice()