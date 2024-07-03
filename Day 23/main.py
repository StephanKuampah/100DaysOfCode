import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

        




screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    cars.create_car()
    cars.move()
    time.sleep(0.1)
    screen.update()
    

    if player.ycor() > 280:
        scoreboard.increase_level()
        player.player_refresh()
        cars.increase_speed()
    
    for car in cars.all_cars:
        if  car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameover()

    



screen.exitonclick()
