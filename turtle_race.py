from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour:")
print(bet)
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y = -100
for colour in colours:
    turt = Turtle(shape="turtle")
    turt.penup()
    turt.color(colour)
    turt.goto(x=-230, y=y)
    y += 30
    all_turtles.append(turt)

if bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()