from turtle import *

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_parts = Turtle("square")
            snake_parts.color("white")
            snake_parts.penup()
            snake_parts.goto(position)
            self.snake.append(snake_parts)
    
    def move(self):
        for part in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[part-1].xcor()
            new_y = self.snake[part-1].ycor()
            self.snake[part].goto(new_x, new_y)
        self.snake[0].forward(20)
    
    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)