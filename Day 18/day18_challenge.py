from turtle import *

test = Turtle()
test.shape("turtle")
for _ in range(15):
    test.forward(10)
    test.penup()
    test.forward(6)
    test.pendown()
    



screen = Screen()
screen.exitonclick()