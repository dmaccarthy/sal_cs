"""
CSE 1110: Structured Programming
Input & Output
Example 5

"""

from turtle import textinput, setup, speed, penup, pendown, pencolor, left, forward, exitonclick

# Ask for color
color = textinput("Color", "What color triangle do you want?")

# Assign canvas and triangle size
canvas_size = 300
sides = 3
side_length = 2 / sides * canvas_size

# Set the canvas size and turtle speed
setup(canvas_size, canvas_size)
speed(1)

# Move turtle into position
penup()
left(90)
forward(side_length / 2)
left(150)

# Draw a triangle
pencolor(color)
pendown()
for side in range(int(sides)):
    forward(side_length)
    left(360 / sides)

# Finished!
exitonclick()