from turtle import Turtle,Screen
# from noconflict import makecls
import random
import time

class Snake(Turtle):
    # __metaclass__ = makecls()

    def __init__(self):

        super().__init__()
        self.screen = Screen()

    def reset_snake(self):
        self.segments = []
        self.segments.clear()
        self.number_of_segments = len(self.segments)
        starting_position = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_position:
            new_segment = Turtle(shape='square')
            new_segment.penup()
            new_segment.goto(position)
            new_segment.color('white')
            new_segment.speed('slow')
            self.segments.append(new_segment)
        # head = self.segments[0]

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        count = self.number_of_segments - 1
        new_segment.goto(2 * self.segments[count].xcor() - self.segments[count - 1].xcor(),
                         2 * self.segments[count].ycor() - self.segments[count - 1].ycor())
        new_segment.color('white')
        new_segment.speed('slowest')
        self.segments.append(new_segment)

    def turn_left(self):
        self.segments[0].left(90)

    def turn_right(self):
        self.segments[0].right(90)

    def hit_wall(self):
        if abs(self.segments[0].xcor()) > 290 or abs(self.segments[0].ycor()) > 290:

            return True
        else:
            return False

    def hit_its_body(self):
        for i in range(1,len(self.segments)):
            if self.segments[0].pos() == self.segments[i].pos():

                return True
        return False

    def movement(self):
        for i in range(len(self.segments) -1 , 0, -1):
            self.segments[i].setpos(self.segments[i - 1].pos())
        self.segments[0].fd(20)

    def clear_snake(self):
        for segment in self.segments:
            segment.hideturtle()
