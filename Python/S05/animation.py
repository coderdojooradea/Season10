import turtle

win = turtle.Screen()
win.bgcolor("white")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.speed(0)
ball.goto(0, 0)

dx = 2
dy = 2

while True:
    x, y = ball.position()
    if x > 300 or x < -300:
        dx = -dx
    if y > 300 or y < -300:
        dy = -dy
    ball.goto(x + dx, y + dy)

win.mainloop()
