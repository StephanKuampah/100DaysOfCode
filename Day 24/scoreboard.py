from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_highscore()
        self.penup()
        self.color("white")
        self.goto(0,275)
        self.update_scoreboard()
        self.hideturtle()

    def read_highscore(self):
        with open("data.txt", mode="r") as file:
            content = file.read()
            self.high_score = int(content)
            
    def write_highscore(self):
        with open("data.txt", mode="w") as file:
            self.high_score = self.score 
            score = self.high_score
            file.write(f"{score}")

        
    def reset_highscore(self):
        if self.score > self.high_score:
            self.write_highscore()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}:    : Highscore: {self.high_score}",align="center",font=("Arial", 15 , "normal"))
    # def game_over(self):
    #      self.goto(0,0)
    #      self.write(f"Game Over",align="center",font=("Arial", 15 , "normal"))
        
    def increase(self):
        self.score += 1
        self.update_scoreboard()

        