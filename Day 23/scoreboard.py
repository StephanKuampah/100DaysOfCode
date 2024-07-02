from turtle import *


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-225,265)
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f"Level:{self.level}",align="center" , font=FONT)

    def gameover(self):
         self.goto(0,0)
         self.write(f"Game Over",align="center",font=("Arial", 15 , "normal"))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update()
