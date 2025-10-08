import turtle
import colorsys

# Setup
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pensize(2)

# Number of shapes and hue settings
n = 36
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)  # rainbow color
    h += 0.005
    t.pencolor(c)
    t.forward(i * 3 / n + i)
    t.left(59)
    t.forward(i * 3 / n + i)
    t.left(59)
    t.forward(i * 3 / n + i)
    t.left(59)
    t.left(1)  # slowly rotate the entire pattern

turtle.done()
