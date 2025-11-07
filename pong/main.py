from turtle import Screen
# from turtle import Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()

#
# r_paddle = Turtle()
# r_paddle.color("white")
# r_paddle.shape("square")
# r_paddle.shapesize(stretch_wid=5, stretch_len=1)
# r_paddle.penup()
# r_paddle.setposition(x=350,y=0)
#
#
# def up():
#     r_paddle.goto(x=r_paddle.xcor(),y=r_paddle.ycor() + 20)
#
# def down():
#     r_paddle.goto(x=r_paddle.xcor(), y=r_paddle.ycor() - 20)
#
#
screen.listen()
screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()


    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
#        print("hit")
        ball.bounce_x()
        ball.increase_speed()

    if ball.xcor() > 380: # left wins
        #print("right fail")
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380: # right wins
        ball.reset_position()
        scoreboard.r_point()

    # Detect collision with wall (bounce)
    # if ball going up right
    # if ball.ycor() > 290 and ball.xcor() > 0:
    #     # bounce in different direction (flip y, not x)
    #     ball.setheading(DOWNRIGHT)
    # elif ball.ycor() < -290 and ball.xcor() > 0:
    #     ball.setheading(UPRIGHT)
    # elif ball.ycor() > 290 and ball.xcor() < 0:
    #     ball.setheading(DOWNLEFT)
    # elif ball.ycor() < -290 and ball.xcor() < 0:
    #     ball.setheading((UPLEFT))





# screen.exitonclick()