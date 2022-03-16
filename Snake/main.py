from turtle import Screen,Turtle
from snake import Snake
from food import Food
from score_tracker import Score


from random import randint
import time
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor('black')
screen.title("Welcome to Snake Game!")
screen.tracer(0)

snake = Snake()
snake.speed('fast')
food = Food()
score = Score()

def turn_left():
    snake.turn_left()

def turn_right():
    snake.turn_right()


screen.listen()
score.display_score()

snake.reset_snake()

def end_game():
    score.endgame = True

screen.onkey(end_game,  "Up")

while not score.endgame:
    score.display_high_score()
    while not snake.hit_wall() and not snake.hit_its_body():
        time.sleep(0.1)
        screen.update()
        screen.onkey(fun= turn_left,key= 'Left')
        screen.onkey(fun= turn_right, key= 'Right')
        snake.movement()
        if snake.segments[0].distance(food.pos()) < 15:
            food.refresh()
            snake.add_segment()
            score.add_score()
            score.display_score()

    score.reset_highscore()

    snake.clear_snake()
    snake.reset_snake()
    food.refresh()

screen.exitonclick()




