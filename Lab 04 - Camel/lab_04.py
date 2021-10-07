"""

Random Number Guessing Game
"""
import random

def main():
    print("Welcome to Save Princess Peach!")
    print("""Mario has saved Princess Peach from angry Bowser. 
    Make it back safe to the castle before he snatches Princess Peach again.""")
print()
main()

# Variables
milestraveled = 0
thirst = 0
mariocar = 0
bowsertraveled = -20
yeti = 3
bowserbehind = 10
oasis = 0
done = False


# Start main loop
while not done:
    fullspeed = random.randrange(13, 25)
    moderatespeed = random.randrange(7, 15)
    print("""
    A. Drink from Yeti.
    B. Ahead at moderate speed.
    C. Ahead full speed.
    D. Stop for the night.
    E. Status check.
    F. Quit.""")
    user_choice = input("Your choice? ").upper()
    if user_choice.lower() == "f":
        done = True
        print("Bye!")

    elif user_choice.lower() == "e":
        print("Miles traveled: ", bowsertraveled)
        print("Drinks from Yeti: ", yeti)
        print("Mario's car has: ", mariocar, "amount of gas.")
        print("Bowser is ", bowserbehind, "miles behind you.")

    elif user_choice.lower() == "d":
        mariocar *= 0
        print("The car feels refreshed and has ", mariocar, "gallons of gas left.")
        bowsertraveled += random.randrange(10, 22)

    elif user_choice.lower() == "c":
        print("You traveled ", fullspeed, "miles!")
        milestraveled += random.randrange(2, 5)
        thirst += 2
        mariocar += random.randrange(2, 5)
        bowsertraveled += random.randrange(10, 18)
        oasis = random.randrange(4, 24)

    elif user_choice.lower() == "b":
        print("You traveled ", moderatespeed, "miles!")
        bowsertraveled += moderatespeed
        thirst += 2
        mariocar += 2
        bowsertraveled += random.randrange(8, 16)
        oasis = random.randrange(4, 24)

    elif user_choice.lower() == "a":
        if yeti == 0:
            print("You are out of water.")
        else:
            yeti -= 1
            thirst *= 0
            print("You have ", yeti, "drinks left and you are no longer thirsty.")

    if oasis == 21:
        mariocar *= 0
        thirst *= 0
        yeti = 3
        print("You found an oasis! After taking a drink you filled you yeti and your car is full on gas.")

    if  bowsertraveled <= 16:
        print("Bowser is close.")

    if milestraveled >= 210 and not done:
        print("You did it, you win!")
        done = True

    if bowsertraveled >= milestraveled:
        print("Bowser captured Peach.")
        print("You failed!")
        done = True
    if thirst > 7:
        print("You died of dehydration!")
        done = True

    if mariocar > 6 and mariocar >= 9 and not done:
        print("The car's fuel light turned on.")

    if mariocar > 9:
        print("Your car ran out of gas.")
        done = True
