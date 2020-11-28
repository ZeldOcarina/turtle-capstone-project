from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# width=600 height=600

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def make_car(self):
        self.showturtle()
        self.resizemode('user')
        self.shapesize(stretch_wid=1, stretch_len=2, outline=None)
        self.shape('square')
        self.color(random.choice(COLORS))
        self.penup()

    def move(self):
        self.setheading(180)
        self.forward(10)


def set_random_position(car):
    x_pos = 260
    y_pos = random.randrange(-200, 280, 40)
    car.goto(x_pos, y_pos)


class CarManager(Car):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_speed = 0.1

    def create_car(self):
        car = Car()
        car.make_car()
        set_random_position(car)
        self.cars.append(car)

    def increase_speed(self):
        self.move_speed *= 0.8
