"""
    Реализовать бинды для движения весла А
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

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)


# Keyboard binding
wn.listen()  # ожидание ввода
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')


# Main game loop
while True:
    wn.update()  # обновление экрана, работает только вместе с tracer
    

    # Paddle and scope
    if paddle_a.ycor()+60 > 290:
        paddle_a.sety(250)

    if paddle_a.ycor() - 60 < -290:
        paddle_a.sety(-250)

    if paddle_b.ycor()+60 > 290:
        paddle_b.sety(250)

    if paddle_b.ycor() - 60 < -290:
        paddle_b.sety(-250)
