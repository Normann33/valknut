#!/usr/bin/env python3

import turtle
turtle.shape('arrow')
turtle.width(3)

def little_triangle(x):
    turtle.forward(x)
    turtle.left(120)
    turtle.forward(x * 3)
    turtle.left(120)
    turtle.forward(x * 3)
    turtle.left(120)
    turtle.forward(x)
    turtle.left(60)
    turtle.forward(x)
    turtle.right(120)
    turtle.forward(x)

def big(x):
    turtle.forward(2 * x)
    turtle.right(120)
    turtle.forward(6 * x)
    turtle.right(120)
    turtle.forward(2 * x)
    turtle.right(60)
    turtle.forward(x)

x = 60

little_triangle(x)
turtle.left(180)
little_triangle(x)
turtle.left(180)
little_triangle(x)

turtle.left(60)
turtle.forward(x)
turtle.right(60)
turtle.penup()
turtle.forward(x)
turtle.pendown()

big(x)
turtle.left(180)
big(x)
turtle.left(180)
big(x)
turtle.penup()
turtle.back(20 * x)

turtle.mainloop()
