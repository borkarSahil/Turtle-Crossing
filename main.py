# TODO : MOVE THE TURTLE WITH KEYPRESS
# TODO : CREATE AND MOVE THE CARS
# TODO : DETECT COLLISION WITH CAR
# TODO : DETECT WHEN TURTLE REACHES THE OTHER SIDE
# TODO : CREATE A SCOREBOARD

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Class Objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(key="Up", fun=player.move_Up)
screen.onkeypress(key="Up", fun=player.move_Up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False

    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.reset_player()
        car_manager.increase_speed()



screen.exitonclick()