from turtle import *
import random


test = Turtle()
test.shape("turtle")
colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown"]

def draw(n):
    for _ in range(n):
        angle = 360/n
        test.forward(100)
        test.right(angle)

for n in range(3,10):
    test.color(random.choice(colors))
    draw(n)






screen = Screen()
screen.exitonclick()