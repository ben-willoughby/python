import colorgram
import turtle as t
from turtle import Turtle, Screen
import random

colours = colorgram.extract('image.jpg', 50)
#
# c_list = []
#
# for n in range(10):
#     colour_tuple = (colours[n].rgb.r,colours[n].rgb.g,colours[n].rgb.b)
#     c_list.append(colour_tuple)
#
#     # c_list.append(colours[n].rgb.r)
#     # c_list.append(colours[n].rgb.g)
#     # c_list.append(colours[n].rgb.b)
#
#
# print(c_list)

colour_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61), (59, 48, 37)]

tim = Turtle()

t.colormode(255)

tim.speed("fastest")

tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

def reset():
    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

def draw_dot():
    tim.pendown()
    tim.dot(20, random.choice(colour_list))
    tim.penup()
    tim.forward(50)

for _ in range(10):
    for _ in range(10):
        draw_dot()
    reset()

screen = Screen()
screen.exitonclick()