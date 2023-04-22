DOWN=270
UP=90
LEFT=180
RIGHT=0
from turtle import Turtle
class Snake:
    def __init__(self):
        self.l = []
        for i in range(3):
            self.l.append(Turtle("square"))
        self.head=self.l[0]
        self.s = 0
        for i in self.l:
            i.speed("fastest")
            i.penup()
            i.color("white")
            xcor = i.xcor()
            i.setx(xcor - self.s)
            self.s += 20
        self.head.speed("fastest")
    def extend(self):
        self.l.append(Turtle("square"))
        self.l[-1].color("white")
        self.l[-1].speed("fastest")
        self.l[-1].penup()
        self.l[-1].hideturtle()
        self.l[-1].goto(self.l[-2].xcor()-30,self.l[-2].ycor()-30)
        self.l[-1].showturtle()



    def move(self):
        for i in range(len(self.l) - 1, 0, -1):
            xc = self.l[i - 1].xcor()
            yc = self.l[i - 1].ycor()
            self.l[i].goto(xc, yc)
        self.l[0].forward(20)
    def up(self):
        if(self.l[0].heading()!=DOWN):
          self.l[0].setheading(90)

    def down(self):
        if (self.l[0].heading() != UP):
          self.l[0].setheading(270)
    def right(self):
        if(self.l[0].heading()!=LEFT):
          self.l[0].setheading(0)
    def left(self):
        if(self.l[0].heading()!=RIGHT):
          self.l[0].setheading(180)
