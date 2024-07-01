from turtle import *

    
    

class Bat(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
            

    def moveup(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), y = new_y)

    def movedown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), y=new_y)



