import time
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

#
# 1. Turtle's first steps
#
# t.forward(100)

#
# 2. Draw a square
#
# t.clear()
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)

#
# 3. Draw a square... using a loop!
#
# t.clear()
# for number in range(0, 4):
#     t.forward(100)
#     t.right(90)

#
# 4. Draw a triangle using a loop.
#
# t.clear()
# for number in range(0, 3):
#     t.forward(100)
#     t.right(120)

#
# 5. Write a function that will draw any shape.
#
# def drawShape(sides):
#     t.clear()
#     degrees = 360 / sides
#     for number in range(0, sides):
#         t.forward(100)
#         t.right(degrees)

#
# 6. Call the function!
#
# drawShape(3)
# drawShape(4)
# drawShape(6)
# drawShape(10)

#
# 7. Use an if-elif-else-statement
#
for number in range(0,5):
    time.sleep(1)
    direction = turtle.textinput("What way should Turtle turn?", "Type 'right' or 'left' and hit ok to make Turtle turn.")
    distance = turtle.numinput("How far should Turtle go?", "Enter a number from 25 to 250 to make Turtle move forward.", None, 25, 250)
    
    time.sleep(1)
    if (direction == "right"):
        t.right(90)
    elif (direction == "left"):
        t.left(90)
    else:
        t.right(45)
        t.left(90)
        t.right(45)
    
    time.sleep(1)
    t.forward(distance)



turtle.done()