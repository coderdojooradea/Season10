import turtle, time

def draw_right_triangle(a, b):
    hypotenuse = (a**2 + b**2)**0.5
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.goto(0, 0)
    
    return hypotenuse

a = 100
b = 150

turtle.speed(1)
hypotenuse_length = draw_right_triangle(a, b)

print(f"The length of the hypotenuse is: {hypotenuse_length}")
time.sleep(20)