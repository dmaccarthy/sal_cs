"""
CSE 1120: Structured Programming
Loops
Example 1

"""

from random import uniform

num = uniform(0, 100)
while num <= 99:
    print(num)
    num = uniform(0, 100)
print(num)
