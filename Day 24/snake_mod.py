from turtle import *

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    
    def __init__(self):
        self.parts = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add(position)
    

    def add(self,position):
        snake_parts = Turtle("square")
        snake_parts.color("white")
        snake_parts.penup()
        snake_parts.goto(position)
        self.parts.append(snake_parts)
    
    def extend(self):
        self.add(self.parts[-1].position())



    def move(self):
        for part in range(len(self.parts)-1, 0, -1):
            new_x = self.parts[part-1].xcor()
            new_y = self.parts[part-1].ycor()
            self.parts[part].goto(new_x, new_y)
        self.parts[0].forward(20)
    
    def up(self):
        if self.parts[0].heading() != DOWN:
            self.parts[0].setheading(UP)

    def down(self):
        if self.parts[0].heading() != UP:
            self.parts[0].setheading(DOWN)

    def left(self):
        if self.parts[0].heading() != RIGHT:
            self.parts[0].setheading(LEFT)

    def right(self):
        if self.parts[0].heading() != LEFT:
            self.parts[0].setheading(RIGHT)

    def return_snake(self):
        for part in self.parts:
            part.goto(9999,99999)
        self.parts.clear()
        self.create_snake()
