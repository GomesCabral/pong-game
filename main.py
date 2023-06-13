from turtle import Screen, Turtle

#SCREEN
my_screen = Screen()
my_screen.bgcolor('black')
my_screen.setup(width=800, height=600)
my_screen.title('Pong Game')

#TAKE OFF THE ANIMATION
my_screen.tracer(0)

#CREATE A PADDLE
paddle = Turtle()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(-380, 0)

#MOVE THE PADDLE
my_screen.listen()

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_x = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_x)

my_screen.onkey(go_up, 'Up')
my_screen.onkey(go_down, 'Down')


game_is_on = True

while game_is_on:
    my_screen.update()

my_screen.exitonclick()