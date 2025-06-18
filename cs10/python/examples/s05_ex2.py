"""
CSE 1110: Structured Programming
Variables
Example 2

"""

from turtle import setup, speed, pencolor, penup, pendown, left, forward, exitonclick


# Assign canvas and triangle size
canvas_size = 300
side_length = 2 / 3 * canvas_size

# Set the canvas size and turtle speed
setup(canvas_size, canvas_size)
speed(1)

# Move turtle into position
penup()
left(90)
forward(side_length / 2)
left(150)

# Draw a blue triangle
pencolor("blue")
pendown()
forward(side_length)
left(120)
forward(side_length)
left(120)
forward(side_length)

# Finished!
exitonclick()
