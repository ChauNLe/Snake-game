import time
from turtle import Turtle, Screen


class Score(Turtle):

    def __init__(self):
        self.score = 0
        high_score_history = open("high_score.txt")
        self.high_score = int(high_score_history.read())
        high_score_history.close()
        self.endgame = False

        self.display = Turtle()
        self.display.hideturtle()
        self.display.color('white')
        self.display.penup()
        self.display.goto(200, 250)

        self.display_highscore = Turtle()
        self.display_highscore.hideturtle()
        self.display_highscore.color('white')
        self.display_highscore.penup()
        self.display_highscore.goto(-280, 250)


    def add_score(self):
        self.score += 1

    def display_score(self):

        # self.display.pendown()
        self.display.clear()
        self.display.write(arg=f'Current score: {self.score}',move= False, align='center', font= 8)

    def reset_highscore(self):
        display_new_highscore = Turtle()
        display_new_highscore.hideturtle()
        display_new_highscore.color('white')
        if self.score >= self.high_score:
            # self.high_score=self.score
            # high_score_history.truncate(0)
            with open("high_score.txt",'w') as high_score_history:
                high_score_history.write(f"{self.score}")
            with open('high_score.txt') as high_score_history:
                self.high_score = int(high_score_history.read())
            display_new_highscore.write(f"NEW HIGH SCORE: {self.high_score}", False, 'center', 8)
            time.sleep(2)
            display_new_highscore.clear()
        else:
            display_new_highscore.write("GAME OVER", False, 'center', 8)
            time.sleep(2)
            display_new_highscore.clear()
        self.score=0
        self.display_score()

    def display_high_score(self):

        # self.display.pendown()
        self.display_highscore.clear()
        self.display_highscore.write(arg=f'High score: {self.high_score}', move=False, align='left', font=8)

    def game_over(self):
        self.display.penup()
        self.display.goto(0,0)
        self.display.write("GAME OVER", False, align= 'center', font = 12)
