import turtle

border = turtle.Turtle() # границы для мяча

ball = turtle.Turtle(shape='circle') # мячик

window = turtle.Screen() # окно

ball.speedY = 0 # скорость по Y
ball.speedX = 2 # скорость по X

gravitation = 0.1 # коэффицент скорости мяча

def main():
    border_ball_window()
    fun(ball)

def border_ball_window(): # конфигурауия окна, границ и мяча
    window.bgcolor('red')
    
    border.hideturtle()
    border.speed(0)
    border.pensize(5)
    border.up()
    border.goto(-250, 250)
    border.down()
    border.goto(-250, -250)
    border.goto(250, -250)
    border.goto(250,250)

    ball.up()
    ball.goto(0,200) # чтобы мяч начинал движение с более высокой позиции

    

def fun(ball):
    while True:
        # print(ball.speedY, ball.position())  # чтобы посмотреть значение по Y при прыжке
        ball.speedY = ball.speedY - gravitation  # изменение сскорости по Y
         # xcor() и ycor() - получение координат по y и x
        ball.goto(ball.xcor() + ball.speedX, ball.ycor() + ball.speedY)

        if ball.ycor() <= -250: # условие для отскока по координате Y
            ball.speedY = -ball.speedY
        if ball.xcor() >= 250 or ball.xcor() <= -250:
            ball.speedX = -ball.speedX


if __name__ == "__main__":
    main()

window.mainloop()