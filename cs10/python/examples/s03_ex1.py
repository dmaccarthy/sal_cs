"""
CSE 1110: Structured Programming
Programming in Python
Example 1

"""

from turtle import setup, speed, pencolor, penup, pendown, left, circle, backward, forward, exitonclick

setup(600, 480)
speed(1)
penup()

backward(200)
left(45)
forward(100)

pencolor("red")
pendown()
circle(-200, 180)

exitonclick()
