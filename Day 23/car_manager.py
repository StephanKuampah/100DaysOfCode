from turtle import *
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.start_speed = STARTING_MOVE_DISTANCE
         
        
    def create_car(self):  
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y = random.randint(-260,260)
            new_car.goto(x=300,y=y)
            new_car.setheading(180)
            self.all_cars.append(new_car)
    
    def move(self):
        for car in self.all_cars:
            car.forward(self.start_speed)
    
    def increase_speed(self):
        self.start_speed += MOVE_INCREMENT
        self.move() 

    def return_to_start(self,new_car):
        if self.xcor() < -300:
          self.goto(x=300,y=new_car.y)
   
        
    