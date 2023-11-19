import turtle, time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Set up the turtle
t = turtle.Turtle()
t.speed(5)

# Draw a circle with radius 100
# t.circle(100)

# Draw a line of length 200
# t.forward(200)

# Draw a square of side 150
for i in range(0,4):
    t.forward(150)
    t.right(90)

time.sleep(20)
