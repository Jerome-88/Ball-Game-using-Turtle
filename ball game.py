import turtle

wn = turtle.Screen()
wn.title("game1")
wn.bgcolor("blue")
wn.setup(width=1000, height=800)
wn.tracer()
#score
score_a=0
score_b=0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=3)
paddle_a.color("orange")
paddle_a.penup()
paddle_a.goto(-490, 0)

#paddleB
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=3)
paddle_b.color("orange")
paddle_b.penup()
paddle_b.goto(490, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("orange")
ball.penup()
ball.goto(0, 0)
ball.dx=7
ball.dy=7

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,360)
pen.write("a:0  B:0", align="center", font=("normal"))

#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)


    #keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#main game loop
while True:
    wn.update()

#ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border
    if ball.ycor()>390:
        ball.sety(390)
        ball.dy*=-1
    
    if ball.ycor()<-390:
        ball.sety(-390)
        ball.dy*=-1

    if ball.xcor()>490:
        ball.goto(0,0)
        ball.dx*=-1
        score_a += 1
        pen.clear()
        pen.write("a:{}  B:{}".format(score_a, score_b), align="center", font=("normal"))

    if ball.xcor()<-490:
        ball.goto(0,0)
        ball.dy*=-1
        score_b += 1
        pen.clear()
        pen.write("a:{}  B:{}".format(score_a, score_b), align="center", font=("normal"))


#pedal
    if (ball.xcor()>450 and ball.xcor()<460) and(ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50):
        ball.setx(450)
        ball.dx *= -1

    if (ball.xcor()<-450 and ball.xcor()>-460) and(ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50):
        ball.setx(-450)
        ball.dx *= -1


