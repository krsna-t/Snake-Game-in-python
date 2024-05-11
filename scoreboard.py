from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("/home/krishna/Documents/python/day20_21snakegame/data.txt") as data:
            self.highscore=int(data.read())
        self.color("white")
        self.penup()        
        self.goto(0,270) 
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High score:{self.highscore}",align="center",font=("Courier",15,"normal"))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center",font=("Courier",25,"normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
            with open("/home/krishna/Documents/python/day20_21snakegame/data.txt",mode="w") as data:
                data.write(f"{self.highscore}")  
        self.score=0
        self.update_scoreboard()


    def increase_score(self):
        self.score +=1

        self.update_scoreboard()          


        

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    