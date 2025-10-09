
import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Tighter Spiral with Geometric Shapes")

# Create turtle object
spiral = turtle.Turtle()
spiral.speed(0)
spiral.width(2)
spiral.hideturtle()

# Define number of shapes and color settings
num_shapes = 150
hue = 0
colors = []

# Generate a list of colors using HSV color space
for i in range(num_shapes):
    colors.append(colorsys.hsv_to_rgb(hue, 1, 1))
    hue += 1 / num_shapes

# Draw tighter spiral pattern with geometric shapes
for i in range(num_shapes):
    r, g, b = colors[i]
    spiral.color(r, g, b)
    spiral.forward(i * 3)      # Smaller step for tighter spiral
    spiral.right(45)
    spiral.forward(i * 2)
    spiral.right(90)
    spiral.forward(i)
    spiral.right(45)
    spiral.forward(i * 0.5)
    spiral.right(89)           # Slightly less than 90 for tighter curve

# Keep the window open until clicked
screen.exitonclick()
