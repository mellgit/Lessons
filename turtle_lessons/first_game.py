import turtle, random


def main():
    window = turtle.Screen()  # захват экрана чтобы не закрылось

    fun_border()
    fun_ball()

    window.mainloop()  # удержание открытого окна

def fun_border():
    border = turtle.Turtle()  # объявление
    border.speed(100)  # скорость
    border.up()  # поднять карандаш
    border.goto(300, 300)  # иди в точку 300 300
    border.down()  # опустить карандаш
    border.hideturtle()  # убрать курсор
    border.pensize(4)  # размер линии
    border.color('red')  # цвет
    border.goto(300, -300)
    border.goto(-300, -300)
    border.goto(-300, 300)
    border.goto(300, 300)


def fun_ball():
    # вторая функция
    ball = turtle.Turtle()  # объявление шарика в центре экрана
    ball.hideturtle()  # спрятать черепашку
    ball.shape('circle')  # прорисовка шарика
    ball.up()
    randx = random.randint(-290, 290)  # рандомная координата по x
    randy = random.randint(-290, 290)  # рандомная координата по y

    ball.goto(randx, randy)
    ball.showturtle()  # показать черепашку
    dx = 3  # координаты для движения черепашки
    dy = 2

    while True:
        x, y = ball.position()  # первая позиция черепашки
        if x + dx >= 300 or x + dx <= -300:  # чтобы черепашка не выходила за границы
            dx = -dx # изменение направления
        if y + dy >= 300 or y + dy <= -300:
            dy = -dy
        ball.goto(x + dx, y + dy)  # движение по координатам



if __name__ == '__main__':
    main()