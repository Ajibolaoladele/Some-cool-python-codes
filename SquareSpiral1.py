#SquareSpiral1.py - Draws a square spiral

import turtle

t = turtle.Pen()

turtle.bgcolor('black')

for x in range(300):
    t.pencolor('red')
    t.forward(x)
    t.left(90)