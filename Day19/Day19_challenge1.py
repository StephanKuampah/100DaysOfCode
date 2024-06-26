from turtle import *


test = Turtle()
screen = Screen()


def move_forward():
    test.forward(10)

def move_backward():
    test.back(10)

def move_anticlockwise():
    test.left(10)

def move_clockwise():
    test.right(10)

def clear_screen():
    test.reset()


screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="d",fun=move_clockwise)
screen.onkey(key="a",fun=move_anticlockwise)
screen.onkey(key="c",fun=clear_screen)
screen.exitonclick()