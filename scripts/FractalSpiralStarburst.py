
import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Creative Fractal Spiral Starburst")

# Create turtle object
artist = turtle.Turtle()
artist.speed(0)
artist.width(2)
artist.hideturtle()

# Function to draw a fractal tree-like pattern
def draw_fractal_branch(t, branch_length, level):
    if level == 0:
        return
    t.forward(branch_length)
    t.left(30)
    draw_fractal_branch(t, branch_length * 0.7, level - 1)
    t.right(60)
    draw_fractal_branch(t, branch_length * 0.7, level - 1)
    t.left(30)
    t.backward(branch_length)

# Function to draw a star
def draw_star(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(144)

# Function to draw a spiral of stars
def draw_spiral_stars(t, num_stars):
    hue = 0
    for i in range(num_stars):
        t.color(colorsys.hsv_to_rgb(hue, 1, 1))
        draw_star(t, i * 2 + 10)
        t.right(15)
        t.forward(i * 2)
        hue += 1 / num_stars

# Function to draw a colorful spiral
def draw_colorful_spiral(t, num_turns):
    hue = 0
    for i in range(num_turns):
        t.color(colorsys.hsv_to_rgb(hue, 1, 1))
        t.forward(i * 3)
        t.right(59)
        hue += 1 / num_turns

# Draw fractal tree in the center
artist.penup()
artist.goto(0, -150)
artist.setheading(90)
artist.pendown()
artist.color("white")
draw_fractal_branch(artist, 100, 4)

# Draw spiral of stars around the fractal
artist.penup()
artist.goto(0, 0)
artist.setheading(0)
artist.pendown()
draw_spiral_stars(artist, 36)


# Keep the window open until clicked
screen.exitonclick()
