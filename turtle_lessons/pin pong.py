import turtle
import random


wn = turtle.Screen()
wn.title('Pin-Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)  # трассировка

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(5, 1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(5, 1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx = random.randint(0, 50)*0.01
ball.dy = random.randint(0, 50)*0.01

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align='center',
          font=('Courier', 24, 'bold'))
pen.hideturtle()

# Score
score_a = 0
score_b = 0


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()  # ожидание ввода
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


# Main game loop
while True:
    wn.update()  # обновление экрана, работает только вместе с tracer
    # Moving Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # проверка по у границ для мяча
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy = -ball.dy

    # Score A Player
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -ball.dx
        score_a += 1
        pen.clear()  # очистка предыдущего счета
        pen.write(f"Player A: {score_a}  Player B: {score_b}",
                  align='center', font=('Courier', 24, 'bold'))

    # Score B Player
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = -ball.dx
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}",
                  align='center', font=('Courier', 24, 'bold'))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(340)
        ball.dx = -ball.dx

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        ball.dx = -ball.dx

    # Paddle and scope
    if paddle_a.ycor()+60 > 290:
        paddle_a.sety(250)

    if paddle_a.ycor() - 60 < -290:
        paddle_a.sety(-250)

    if paddle_b.ycor()+60 > 290:
        paddle_b.sety(250)

    if paddle_b.ycor() - 60 < -290:
        paddle_b.sety(-250)
