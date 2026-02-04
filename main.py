from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s=Screen()
s.setup(height=600,width=800)
s.title("Pong")
s.bgcolor("black")
st_wid=5
s.tracer(0)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
sc=Scoreboard()



s.listen()
s.onkey(r_paddle.go_up,"Up")
s.onkey(r_paddle.go_down,"Down")

s.onkey(l_paddle.go_up,"w")
s.onkey(l_paddle.go_down,"s")




game_is_on=True

while game_is_on:
    time.sleep(ball.ball_speed)
    s.update()
    ball.move()

# detection collision
    if ball.ycor()>280or ball.ycor()<-280:
        ball.bounce_y()


# detection collision with left paddle
    if ball.distance(r_paddle) < 50  and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320 :
        ball.bounce_x()

#   misses paddle
    if ball.xcor()>380 :
        ball.re_start()
        sc.r_point()
    elif ball.xcor()<-380:
        ball.re_start()
        sc.l_point()



s.exitonclick()
