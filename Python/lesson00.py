# Automatic Dice Roller
# Written by Jacksper

from random import randint

print ("Automatic Dice Roller")
roll_again = input("Do you want to roll?")



if roll_again == "y":
    while roll_again == "y":
        print (randint(1,6))
        roll_again = input("Roll Again?")


if roll_again == "n":
        print ("Okay Game Over")
        

