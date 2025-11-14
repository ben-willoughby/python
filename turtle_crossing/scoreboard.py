FONT = ("Courier", 24, "normal")
from turtle import Turtle
import time


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        # self.game_over = False

    def update(self):
        self.clear()
        self.goto(-200,250)
        self.write("Level: " + str(self.level),align="center", font=FONT)


    def level_up(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)
        # time.sleep(1)