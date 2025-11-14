import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle


class CarManager(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.penup()
        self.setposition(position)
        self.color(random.choice(COLORS))
        self.speed = MOVE_INCREMENT

    def move(self):
        new_x =self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())

    def level_up(self):
        self.speed += 2

# car = CarManager((random.randint(-200, 280), (random.randint(-200, 240))))