"""
CSE 1110: Structured Programming
Variables
Example 1

"""

from turtle import setup, speed, pencolor, penup, pendown, left, forward, exitonclick

# Set the canvas size and turtle speed
setup(300, 300)
speed(1)

# Move turtle into position
penup()
left(90)
forward(100)
left(150)

# Draw a blue triangle
pencolor("blue")
pendown()
forward(200)
left(120)
forward(200)
left(120)
forward(200)

# Finished!
exitonclick()
