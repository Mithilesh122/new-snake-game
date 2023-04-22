from turtle import Turtle
from snake import Snake
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

        randx = random.randint(-280, 280)
        randy = random.randint(-280, 280)
        self.goto(randx, randy)
        self.refresh()
    def refresh(self):
        randx = random.randint(-280, 280)
        randy = random.randint(-280, 280)
        self.goto(randx, randy)

