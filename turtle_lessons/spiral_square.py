import turtle


def main():
    window = turtle.Screen()  # захват экрана чтобы не закрылось
    bob = turtle.Turtle()  # объявление черепашки
    bob.shape('turtle')  # форма черепашки
    bob.speed(100)  # скорость отрисовки

    figure_rotation(bob)  # функция рисование одной фигуры

    window.mainloop()  # удержание открытого окна


# рисование одной фигуры (квадрата)
def drawing_figure(bob, long):
    colors = ['red', 'green', 'blue', 'black']  # список цветов
    for i in range(4):
        bob.color(colors[i % 4])  # изменяется цвет
        bob.forward(long)  # путь черепахи
        bob.left(90)  # угол поворота
        long += 5  # увеличения длины одной стороны


# поворот фигуры
def figure_rotation(bob):
    long = 100  # изначальная длина стороны
    for i in range(40):
        drawing_figure(bob, long)  # функция рисованя фигуры
        bob.right(10)  # поворот на 10 градусов
        long += 5  # увеличения длины стороны одного квадрата


if __name__ == '__main__':
    main()
