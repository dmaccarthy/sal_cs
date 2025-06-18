"""
CSE 1120: Structured Programming
Formatted Output
Example 2

"""

from math import sqrt

num = float(input("What is your favourite number? "))
root = sqrt(num)
template = "The square root of {:.2f} is {:.2f}."
print(template.format(num, root))
