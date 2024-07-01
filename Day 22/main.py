from turtle import *
from bat_model import *
from ball import *
import time
from scoreboard import *



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,  height=600)
screen.tracer(0)
screen.listen()



bat1 = Bat((350,0))
bat2 = Bat((-350,0))
ball = Ball()
scoreboard1 = Scoreboard((100,275))
scoreboard2 = Scoreboard((-100,275))
line = Turtle()
line.color("white")
line.penup()
line.goto(0,300)
line.right(90)
for _ in range(20):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)
    



screen.onkey(key= "Up", fun= bat1.moveup)
screen.onkey(key= "Down", fun= bat1.movedown)

screen.onkey(key= "w", fun= bat2.moveup)
screen.onkey(key= "s", fun= bat2.movedown)


game_on = True

while game_on:
    screen.update()
    ball.moveup()
    time.sleep(0.1)
    

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(bat1) < 50 and ball.xcor() > 320) or (ball.distance(bat2) < 50 and ball.xcor() < -320) :
        ball.bounce2()


    if ball.xcor() > 360:
        ball.refresh()
        scoreboard2.increase()
        
    if ball.xcor() < -360:
        ball.refresh()
        scoreboard1.increase()
    
    
    



   



screen.exitonclick()