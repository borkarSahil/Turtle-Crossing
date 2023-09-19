from turtle import Turtle
FONT = ('Arial', 15, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.lvl = 1
        self.goto(x=-280, y=250)
        self.display()

    def display(self):
        self.clear()
        self.write(arg=f"Level {self.lvl}", move=False, align="left", font=FONT)

    def increase_level(self):
        self.lvl += 1
        self.display()
