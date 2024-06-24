from turtle import Turtle, Screen 

test = Turtle()
test.shape("turtle")
test.color("coral")
for _ in range(4):
    test.forward(100)
    test.left(90)



screen = Screen()
screen.exitonclick() 

import heroes
print(heroes.gen())