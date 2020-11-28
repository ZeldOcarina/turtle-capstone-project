import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Game variables
game_is_on = True
add_auto_counter = 0

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Game initialization
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Game logic
while game_is_on:
    time.sleep(car_manager.move_speed)
    add_auto_counter += 1

    if add_auto_counter % 3 == 0:
        car_manager.create_car()

    for car in car_manager.cars:
        car.move()

        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()
            pass

        if player.ycor() >= 260:
            print(scoreboard.score)
            scoreboard.increase_score()
            player.reset_position()
            car_manager.increase_speed()
            print(car_manager.move_speed)

    screen.onkey(player.move, "Up")
    screen.update()

screen.exitonclick()
