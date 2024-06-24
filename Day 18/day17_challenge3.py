from turtle import *
import random

test = Turtle()
test.shape("turtle")
screen = Screen()
screen.setup(width = 800 , height = 600)

colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown"]


angles = [0,90,180,270]


def direction():
    directions = ["left", "right"]
    direction = random.choice(directions)
    if direction == "left":
        return test.left(random.choice(angles))
    else:
        return test.right(random.choice(angles))

for _ in range(200):
    test.pensize(10)
    test.speed(0.4)
    test.color(random.choice(colors))
    direction()
    test.forward(30)
    

screen.exitonclick()
