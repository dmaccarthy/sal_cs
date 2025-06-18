"""
CSE 1120: Structured Programming
Formatted Output
Example 4

"""

from math import sqrt

num = float(input("What is your favourite number? "))
root = sqrt(num)
print(f"The square root of {num:.2f} is {root:.2f}.")

# This also works!!
print(f"The square root of {num:.2f} is {sqrt(num):.2f}.")
