import turtle, time

def vicsek_fractal(x, y, side, depth):
    if depth == 0:
        draw_square(x, y, side)
    else:
        new_side = side / 3
        # Middle square
        vicsek_fractal(x, y, new_side, depth - 1)
        # Corner squares
        vicsek_fractal(x - side / 2, y - side / 2, new_side, depth - 1)
        vicsek_fractal(x - side / 2, y + side / 2, new_side, depth - 1)
        vicsek_fractal(x + side / 2, y - side / 2, new_side, depth - 1)
        vicsek_fractal(x + side / 2, y + side / 2, new_side, depth - 1)

def draw_square(x, y, side):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(side)
        turtle.right(90)

t = turtle.Turtle()
my_win = turtle.Screen()
t.speed('fastest')

vicsek_fractal(0, 0, 200, 3)
time.sleep(5)
