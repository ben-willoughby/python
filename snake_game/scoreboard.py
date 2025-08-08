from turtle import Turtle

ALIGNMENT = "center"
FONT = "Arial"
FONT_SIZE = 24

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(arg=f"Score: {self.score}", move=True, align=ALIGNMENT, font=(FONT, FONT_SIZE, 'normal'))

    def update(self):
        self.score += 1
        self.clear()
        self.goto(0, 260)
        self.write(arg=f"Score: {self.score}", move=True, align=ALIGNMENT, font=(FONT, FONT_SIZE, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=True, align=ALIGNMENT, font=(FONT, FONT_SIZE, 'normal'))