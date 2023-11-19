import turtle
import math

wn = turtle.Screen()
wn.setworldcoordinates(0, -1, 360, 1)

sine_wave = turtle.Turtle()
sine_wave.speed('fastest')

# Draw the sine wave
for x in range(360):
    y = math.sin(math.radians(x))  # Convert degrees to radians
    sine_wave.goto(x, y)

wn.exitonclick()
