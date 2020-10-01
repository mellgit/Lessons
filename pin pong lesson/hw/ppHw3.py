"""
    Написать счет - при помощи черепашки pen
    1 - создать черепашку pen
    2 - методом speed задать значение 0 для быстрой отрисовки
    3 - задать белый цвет
    4 - поднять pen чтобы он за собой не оставлял следов
    5 - перемастить pen на координаты 0,260
    6 - метод write вписать ("Player A: 0  Player B: 0", align='center', font=('Courier', 24, 'bold')) для красивого шрифта
    7 - стереть черепашку
"""


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

# Pen###############################


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
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Paddle and scope
    if paddle_a.ycor()+60 > 290:
        paddle_a.sety(250)

    if paddle_a.ycor() - 60 < -290:
        paddle_a.sety(-250)

    if paddle_b.ycor()+60 > 290:
        paddle_b.sety(250)

    if paddle_b.ycor() - 60 < -290:
        paddle_b.sety(-250)
