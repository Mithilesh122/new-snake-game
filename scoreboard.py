from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt","r") as file:
            self.highscore=file.read()

    def increment(self,x,y):
        self.score += 1
        self.clear()
        self.goto(x,y)
        self.write(f"score:{self.score}",move=False,align="right", font=("Arial", 15, "normal"))
        self.show_highscore()

    def update_highscore(self):
        self.highscore=self.score
        with open("data.txt","w") as file:
            file.write(f"{self.highscore}")
        self.show_highscore()
    def show_highscore(self):
        self.clear()
        self.write(f"score:{self.score}", move=False, align="right", font=("Arial", 15, "normal"))
        self.write(f"high score:{self.highscore}", move=False, align="left", font=("Arial", 15, "normal"))



