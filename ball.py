from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()

#MOVE THE BALL
    def move(self):
        new_x = self.xcor() + 14
        new_y = self.ycor() + 14
        self.goto(new_x, new_y)