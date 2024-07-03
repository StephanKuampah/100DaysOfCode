from turtle import *
import time
from snake_mod import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake: ")
screen.tracer(0)
start = screen.textinput(title= "Welcome to snake", prompt="Do you want to start the game? Type 'yes' or 'no'")





snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(key= "Up", fun= snake.up)
screen.onkey(key= "Down" , fun= snake.down)
screen.onkey(key= "Left", fun= snake.left)
screen.onkey(key= "Right", fun= snake.right)

if start == 'yes':
    game_on = True
else:
    game_on =False
    print("You did not start game")

while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.parts[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()
    
    if (snake.parts[0].xcor() < -280) or (snake.parts[0].xcor() > 280) or (snake.parts[0].ycor() < -280) or (snake.parts[0].ycor() > 280):
            snake.return_snake()
            scoreboard.reset_highscore()
            # new_start = screen.textinput(title= "Welcome to snake", prompt="Do you want to start the game? Type 'yes' or 'no'")
            # if new_start == 'yes':
            #      game_on = True
            # else:
            #      game_on = False
            #      scoreboard.game_over()
        
               

           
            
    for parts in snake.parts[1:]:
         if snake.parts[0].distance(parts) < 10 :
                snake.return_snake()
                scoreboard.reset_highscore()
                # new_start = screen.textinput(title= "Welcome to snake", prompt="Do you want to start the game? Type 'yes' or 'no'")
                # if new_start == 'yes':
                #     game_on = True
                # else:
                #     game_on = False
                #     scoreboard.game_over()
            









screen.exitonclick()