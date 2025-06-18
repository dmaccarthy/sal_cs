"""
CSE 1120: Structured Programming
Formatted Output
Question 1

"""

from math import pi

print("Radius", "Circ", "Area")
for radius in range(1, 11):
    C = 2 * pi * radius
    A = pi * radius ** 2
    print(radius, C, A)
