import time
from turtle import Screen
from paddle import Paddle
from ball import Ball


#SCREEN
my_screen = Screen()
my_screen.bgcolor('black')
my_screen.setup(width=800, height=600)
my_screen.title('Pong Game')

#TAKE OFF THE ANIMATION
my_screen.tracer(0)

#CREATE A PADDLE
right_paddle = Paddle((380, 0))
left_paddle = Paddle((-380, 0))

#CREATE A Ball
ball = Ball()

#MOVE THE PADDLES
my_screen.listen()

#MOVE THE RIGHT PADDLE
my_screen.onkey(right_paddle.go_up, 'Up')
my_screen.onkey(right_paddle.go_down, 'Down')

#MOVE THE LEFT PADDLE
my_screen.onkey(left_paddle.go_up, 'w')
my_screen.onkey(left_paddle.go_down, 's')


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    ball.move()



my_screen.exitonclick()