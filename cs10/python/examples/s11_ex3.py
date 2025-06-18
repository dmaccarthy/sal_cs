"""
CSE 1120: Structured Programming
Conditional Statements
Example 3

"""

age = float(input("Please enter your age: "))
if age < 12:
    print("You are too young to be admitted to this movie!")
elif age < 18:
    print("You must be accompanied by an adult!")
else:
    print("Enjoy the show!")
