import turtle

def koch_curve(t, iterations, length=200):
    if iterations == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, iterations - 1, length)
        t.left(60)
        koch_curve(t, iterations - 1, length)
        t.right(120)
        koch_curve(t, iterations - 1, length)
        t.left(60)
        koch_curve(t, iterations - 1, length)

t = turtle.Turtle()
my_win = turtle.Screen()
t.up()
t.goto(-100, 50)
t.down()
for i in range(3):
    koch_curve(t, 5, 300)  # Change the second argument for more complexity
    t.right(120)
my_win.exitonclick()


