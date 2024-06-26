from turtle import *
import random

screen = Screen()
screen.setup(width=500,height=400)
bet = screen.textinput(title="Make a bet", prompt="Which turtle wins the race. Enter a color: ")

red = Turtle(shape="turtle")
blue = Turtle(shape="turtle")
yellow = Turtle(shape="turtle")
green = Turtle(shape="turtle")
purple = Turtle(shape="turtle")
orange = Turtle(shape="turtle")


red.color("red")
blue.color("blue")
yellow.color("yellow")
green.color("green")
purple.color("purple")
orange.color("orange")


red.penup()
blue.penup()
yellow.penup()
green.penup()
purple.penup()
orange.penup()


red.goto(x=-235,y= 100)
blue.goto(x=-235,y= 60)
green.goto(x=-235,y= 20)
yellow.goto(x=-235,y=-20)
purple.goto(x=-235,y=-60)
orange.goto(x=-235,y=-100)

all_turtles = [red,blue,green,yellow,purple,orange]


distance = [1,2,3,4,5]


def move():
    red.forward(random.choice(distance))
    blue.forward(random.choice(distance))
    green.forward(random.choice(distance))
    yellow.forward(random.choice(distance))
    purple.forward(random.choice(distance))
    orange.forward(random.choice(distance))



if bet:
    should_continue = True
else:
    should_continue = False
    print("You did not choose a turtle.")

while should_continue:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            should_continue = False
            winner = turtle.pencolor()
            if bet == winner:
                print(f"You Win, the winning turtle is {winner}.")
            else:
                print(f"You lose, the winning turtle is {winner}.")
    move()
    

screen = exitonclick()

