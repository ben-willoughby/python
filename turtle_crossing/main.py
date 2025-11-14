import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
game_over_sb = Scoreboard()

screen.listen()
screen.onkey(player.up, key="Up")

scoreboard.update()

cars = []

# for n in range(1,):
#     car = CarManager((random.randint(300, 1000), (random.randint(-200, 240))))
#     cars.append(car)

# max_cars = 15

game_refresh = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    game_refresh += 1
    # print(game_refresh % 6)

    dead = False

    # Generate cars
    if game_refresh % 6 == 0:
        car = CarManager((random.randint(300, 1000), (random.randint(-250, 250))))
        cars.append(car)
        # car.move()
        if car.xcor() < -300:
            cars.remove(car)
    for car in cars:
        car.move()
        if player.distance(car) < 30:
            # print("dead")
            # time.sleep(1)
            dead = True
            game_over_sb.game_over()
            screen.update()
            time.sleep(5)
            game_is_on = False
            # game_is_on = False
    # cars.append(CarManager((random.randint(-200, 280), (random.randint(-200, 240)))))
    # if dead:
        # game_over_sb.game_over()
        # time.sleep(1)
        # game_is_on = False


    player.win_check()

    if player.win_check():
        player.level_up()
        scoreboard.level_up()
        for car in cars:
            car.level_up()

    # if player.ycor() == player.FINISH_LINE_Y
