from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len= 0.5)
        self.goto(random.randint(-290,290), random.randint(-290,290))
        self.speed('fastest')

    def refresh(self):
        self.goto(random.randint(-290,290), random.randint(-290,290))

