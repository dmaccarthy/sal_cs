"""
CSE 1120: Structured Programming
Loops
Example 2

"""

from random import randint

roll = None
while roll != 7:
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    roll = die1 + die2
    if roll == 2:
        print("Snake eyes!")
    elif roll == 12:
        print("Boxcars!")
    else:
        print(f"You rolled a {roll}.")
