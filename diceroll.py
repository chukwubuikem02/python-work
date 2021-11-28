import random 
randomList = [1,3,6]
roll = random.choice(randomList)
print(roll)


if roll == 6:
    print ("Awesome, Move to the next step")
if roll == 3:
    print("You missed, Roll again")
if roll == 1:
    print("drop the dice")