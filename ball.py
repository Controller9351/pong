from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_mov=10
        self.y_mov = 10
        self.ball_speed=0.1

    def move(self):
        x_p=self.xcor()+self.x_mov
        y_p = self.ycor()+self.y_mov
        self.goto(x_p,y_p)



    def bounce_y(self):
        self.y_mov *=-1

    def bounce_x(self):
        self.x_mov *=-1
        self.ball_speed*=0.9

    def re_start(self):
        self.goto(0, 0)
        self.ball_speed=0.1
        self.bounce_x()



