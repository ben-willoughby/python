from asyncio import wait_for
from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.005

        # self.speed(1)
        # self.setheading(UPRIGHT)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # self.forward(1)

    def bounce_y(self):
        self.y_move *= -1
        # self.setheading(direction)

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        time.sleep(1)
        self.move_speed = 0.005
        self.bounce_x()

    def increase_speed(self):
        self.move_speed *= 0.9




