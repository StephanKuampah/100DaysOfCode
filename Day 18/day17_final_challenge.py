from turtle import *
import random

test = Turtle()
test.shape("turtle")
test.speed(0.5)

colors = ["Black","Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown"]

for circle in range(int(360/5)):
    test.color(random.choice(colors))
    test.circle(100)
    test.right(5)




screen = Screen()
screen.exitonclick()