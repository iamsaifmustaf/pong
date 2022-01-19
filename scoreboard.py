from turtle import Turtle, Screen
import sys
import time
import random

ALIGNTMENT = "center"
FONT = ("Courier", 60, "normal")



class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score_board()

    def update_score_board(self):
        self.goto(-100,200)
        self.write(self.l_score, align=ALIGNTMENT, font=FONT)
        self.goto(100,200)
        self.write(self.r_score, align=ALIGNTMENT, font=FONT)

    def increase_score_left(self):
        self.l_score += 1
        self.clear()
        self.update_score_board()


    def increase_score_right(self):
        self.r_score += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNTMENT, font=FONT)
        time.sleep(2)
        sys.exit(0)