import turtle, time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Set up the turtle
t = turtle.Turtle()
t.speed(5)

def draw_triangle(nodes, color, turtle):
    t.fillcolor(color)
    t.up()
    t.goto(nodes[0][0], nodes[0][1])
    t.down()
    t.begin_fill()
    t.goto(nodes[1][0], nodes[1][1])
    t.goto(nodes[2][0], nodes[2][1])
    t.goto(nodes[0][0], nodes[0][1])
    t.end_fill()

def get_midpoint(point1, point2):
    midpoint = ((point1[0]+point2[0])/2, 
                (point1[1]+point2[1])/2 )
    return midpoint

def sierpinski(nodes, level, turtle):
    colors = ['blue', 'red', 'green', 'yellow', 'orange']
    draw_triangle(nodes, colors[level % len(colors)], t)
    if level > 0:
        sierpinski([nodes[0],
                   get_midpoint(nodes[0], nodes[1]),
                   get_midpoint(nodes[0], nodes[2])],
                   level-1, t)
        sierpinski([nodes[1],
                   get_midpoint(nodes[0], nodes[1]),
                   get_midpoint(nodes[1], nodes[2])],
                   level-1, t)
        sierpinski([nodes[2],
                   get_midpoint(nodes[2], nodes[1]),
                   get_midpoint(nodes[0], nodes[2])],
                   level-1, t)

level = 4
nodes = [(-200,-100), (0,200), (200,-100)]
# print(get_midpoint(nodes[0], nodes[1]))
sierpinski(nodes, level, t)

time.sleep(20)
