from turtle import Screen
import turtle
from food import Food
from snake import  Snake
from scoreboard import Scoreboard
import time
score=Scoreboard()
score.speed("fastest")
score.ht()
score.penup()
score.left(90)
score.forward(280)
score.right(90)
x=score.xcor()
y=score.ycor()
score.color('white')
score.write(f"score:{score.score}",move=False,align="right",font=("Arial",15,"normal"))
score.write(f"Highscore:{score.highscore}",move=False,align="left",font=("Arial",15,"normal"))
screen=Screen()
turtle.write("sc")
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake game")
snake=Snake()
food=Food()
turtle.onkeyrelease(snake.down,"Down")
turtle.onkeyrelease(snake.right,"Right")
turtle.onkeyrelease(snake.left,"Left")
turtle.onkeyrelease(snake.up,"Up")
turtle.listen()
game_is_on=True
while(game_is_on):
    screen.update()
    snake.move()
    screen.update()
    time.sleep(0.1)
    if(snake.head.distance(food)<15):
        screen.tracer(0)
        food.refresh()
        score.increment(x,y)
        if(score.score>int(score.highscore)):
            score.update_highscore()
        snake.extend()
        screen.update()
    if(snake.head.xcor()>280 or snake.head.ycor()<-280 or snake.head.xcor()<-280 or snake.head.ycor()>280):
        score.goto(0,0)
        score.write("GAME OVER", align="center", font=("Arial", 15, "normal"))
        game_is_on=False
    for segment in snake.l[1:]:
        if(snake.head.distance(segment)<10):
            game_is_on=False
            score.goto(0, 0)
            score.write("GAME OVER", align="center", font=("Arial", 15, "normal"))



screen.exitonclick()