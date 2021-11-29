import random

randomList = [1,2,3,4,5,6]
roll = random.choice(randomList)

name = input ("Welcome to CodeHub_AfricaTech games, Input your name to start: ")
about = input ("Are you ready to roll, Daniel: ")
rolling = input ("Alright, enter ROLL to start: ")

print (roll)

if roll == 6:
    print ("Awesome, Move to the next step")
if roll == 5:
    print ("So close, Roll again")
if roll == 4:
    print ("Roll again")
if roll == 3:
    print("You missed, Roll again")
if roll == 2:
    print ("Roll again")
if roll == 1:
    print("drop the dice")
