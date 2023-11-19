import turtle

class GeometriFigures:
    def __init__(self):
        #Set up the screen
        self.screen = turtle.Screen()
        self.screen.bgcolor("white")

        #Create turtle
        self.t = turtle.Turtle()
        self.t.speed(3)

    def display(self):
        self.t.hideturtle()

    def draw_square(self, side_length, 
                    orientation='left'):
        for _ in range(4):
            self.t.forward(side_length)
            if orientation=='right':
                self.t.right(90)
            else:
                self.t.left(90)

    def draw_cross(self, side_length, 
                    orientation='left'):
        for _ in range(4):
            self.t.forward(side_length)
            if orientation=='right':
                self.t.right(90)
                self.t.forward(side_length)
                self.t.left(90)
                self.t.forward(side_length)
                self.t.left(90)
            else:
                self.t.left(90)
                self.t.forward(side_length)
                self.t.right(90)
                self.t.forward(side_length)
                self.t.right(90)

    def draw_star(self, sides, side_length):
        if sides <=4:
            print("Error. Shape is not drawable.")
        else:
            for _ in range(sides):
                self.t.forward(side_length)
                self.t.right(180-180/sides)

    def draw_polygon(self, sides, side_length):
        if sides <=4:
            print("Error. Shape is not drawable.")
        else:
            for _ in range(sides):
                self.t.forward(side_length)
                self.t.right(360/sides)

    def turn_right(self, angle):
        self.t.right(angle)
