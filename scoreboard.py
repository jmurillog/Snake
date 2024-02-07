from tkinter import CENTER
from turtle import Turtle
import json


ALIGNEMENT = "center"
FONT = ('Courier', 24, 'normal')
HIGHEST_SCORE_PATH = r'highest_score.json'


try:
    with open(HIGHEST_SCORE_PATH, 'r') as f:
        highest_score = json.load(f)
except FileNotFoundError:
    print(f"Lo siento, el archivo {HIGHEST_SCORE_PATH} no existe.")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.goto(0,270)
        self.write(f"Score: {self.score}", align = ALIGNEMENT, font= FONT)


    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align = ALIGNEMENT, font= FONT)


    def highes_score(self):
        #If highest score
        self.goto(0,230)
        if not highest_score:
            highest_score["score"] = 0
        else:
            if self.score > highest_score["score"]:
                highest_score["score"] = self.score
                self.write(f"New high score: {highest_score['score']}", align = ALIGNEMENT, font= ('Courier', 20, 'normal'))
            else:
                self.write(f"Highest score: {highest_score['score']}", align = ALIGNEMENT, font= ('Courier', 20, 'normal'))

        json_object = json.dumps(highest_score, indent=1)
        with open(HIGHEST_SCORE_PATH, "w") as outfile:
            outfile.write(json_object)

    def print_highest_score(self):
        self.goto(0,230)
        self.write(f"Highest score: {highest_score['score']}", align = ALIGNEMENT, font= ('Courier', 20, 'normal'))