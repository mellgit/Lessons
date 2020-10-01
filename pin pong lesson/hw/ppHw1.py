"""
    ТЗ
    Дан код, в котором реализованно весло А и его ограничения для его хода
    Необходимо:
    1 - реализовать весло В, задать ему необходимые характеристики 
    2 - написать ограничения для хода этого весла

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


# Main game loop
while True:
    wn.update()  # обновление экрана, работает только вместе с tracer
    

    # Paddle and scope
    if paddle_a.ycor()+60 > 290:
        paddle_a.sety(250)

    if paddle_a.ycor() - 60 < -290:
        paddle_a.sety(-250)
