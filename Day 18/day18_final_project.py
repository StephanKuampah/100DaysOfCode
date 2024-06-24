import turtle
from turtle import *
import random 

turtle.colormode(255)
test = turtle.Turtle()
test.speed(0.5)
colors = [ (168, 76, 38), (206, 152, 104), (227, 214, 93), (65, 37, 25), (64, 87, 150), (125, 162, 200), (149, 31, 23), (153, 57, 80), (176, 150, 43), (134, 187, 160), (45, 42, 131), (135, 32, 46), (66, 120, 75), (213, 88, 60), (29, 27, 69), (197, 131, 160), (202, 82, 103), (63, 35, 45), (97, 157, 89), (162, 212, 171), (89, 109, 192), (72, 150, 172), (232, 174, 163), (32, 48, 28), (242, 217, 7), (176, 186, 219)]


def turn_left():
    test.left(90)
    test.penup()
    test.forward(50) 
    test.left(90)
    test.forward(500)
    test.right(180) 
    



def draw():
    for _ in range(10):
        test.dot(20,random.choice(colors))
        test.penup()
        test.forward(50)

test.left(225)
test.penup()
test.hideturtle()
test.forward(300)
test.left(-225)
test.pendown()





for _ in range(10):
    draw()
    turn_left() 


screen = Screen()
screen.exitonclick()
