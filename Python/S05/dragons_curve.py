import turtle

def dragon_curve(t, iterations, length=120, is_right=True):
    if iterations == 0:
        t.forward(length)
    else:
        t.right(45 if is_right else -45)
        dragon_curve(t, iterations - 1, length / 2 ** 0.5, True)
        t.left(90 if is_right else -90)
        dragon_curve(t, iterations - 1, length / 2 ** 0.5, False)
        t.right(45 if is_right else -45)

t = turtle.Turtle()
my_win = turtle.Screen()
t.speed('fastest')
t.up()
t.goto(-50, 0)
t.down()
dragon_curve(t, 10)  # Change the second argument for more iterations
my_win.exitonclick()


