from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed(0)
        self.reset_player()
        self.left(90)


    def move_Up(self):
        y_position = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(), y=y_position)

    def reset_player(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False
