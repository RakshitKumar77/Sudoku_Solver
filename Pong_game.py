import turtle

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Creating Left Paddle
leftpaddle= turtle.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)


# Paddle Right Paddle
rightpaddle= turtle.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# #Creating Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2			# speed
ball.dy = -0.2			# speed

# #creating pen for scorecard update
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


#moving the left paddle
def paddle_a_up():
    y = leftpaddle.ycor()
    y += 20
    leftpaddle.sety(y)

def paddle_a_down():
    y = leftpaddle.ycor()
    y += -20
    leftpaddle.sety(y)

#moving the right paddle#

def paddle_b_up():
    y = rightpaddle.ycor()
    y += 20
    rightpaddle.sety(y)

def paddle_b_down():
    y = rightpaddle.ycor()
    y += -20
    rightpaddle.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:    # top of the screen
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:   # bottom of the screen
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:  # right side of the screen
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player  B: {}". format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:  # left side of the screen
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player  B: {}". format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1