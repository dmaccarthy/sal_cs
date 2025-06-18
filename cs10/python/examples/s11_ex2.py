"""
CSE 1120: Structured Programming
Conditional Statements
Example 2

"""

from math import sqrt

num = float(input("Please enter a number: "))
if num >= 0:
    root = sqrt(num)
    print(f"The square root of {num} is {root}.")
else:
    print("The number cannot be negative!")

# Try running this program with both positive and negative inputs
