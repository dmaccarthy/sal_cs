"""
CSE 1110: Structured Programming
Comments & Docstrings
Example 1

"""

from turtle import setup, speed, pencolor, penup, pendown, left, forward, backward, exitonclick

# Set the canvas size, turtle speed, and pen color
setup(600, 480)
speed(1)
pencolor("red")

# Move turtle into position
penup()
backward(200)
left(45)

# Start drawing
pendown()
forward(200)

# Finished!
exitonclick()
