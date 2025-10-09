
import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Mandala Pattern")

# Create turtle object
mandala = turtle.Turtle()
mandala.speed(0)
mandala.width(2)
mandala.hideturtle()

# Function to draw a petal-like shape
def draw_petal(radius, angle):
    for _ in range(2):
        mandala.circle(radius, angle)
        mandala.left(180 - angle)

# Generate a colorful mandala pattern
num_layers = 36
hue = 0
for i in range(num_layers):
    mandala.color(colorsys.hsv_to_rgb(hue, 1, 1))
    draw_petal(100, 60)
    mandala.right(360 / num_layers)
    hue += 1 / num_layers

# Keep the window open until clicked
screen.exitonclick()
