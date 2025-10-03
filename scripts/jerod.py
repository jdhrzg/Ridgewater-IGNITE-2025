import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

t.right(-90)
t.penup()
t.backward(250)
t.pendown()

# the acute angle between
# the base and branch of the Y
angle = 30

# function to plot a Y
def drawY(size, level):   

    if level > 0:
        turtle.colormode(255)
        
        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        t.pencolor(0, 255 // level, 0)
        
        # drawing the base
        t.forward(size)

        t.right(angle)

        # recursive call for
        # the right subtree
        drawY(0.8 * size, level-1)
        
        t.pencolor(0, 255//level, 0)
        
        t.left( 2 * angle )

        # recursive call for
        # the left subtree
        drawY(0.8 * size, level-1)
        
        t.pencolor(0, 255//level, 0)
        
        t.right(angle)
        t.forward(-size)
         
        
drawY(150, 12)

turtle.done()