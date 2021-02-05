import turtle
import random


def main():
    bob = turtle.Turtle()

    bob.speed(100)
    bob.color('yellow')  # цвет черепашки

    window = turtle.Screen()
    window.bgcolor('black')  # цвет звезды
    window.setup(700, 500)  # размер экрана

    rand_stars(bob)

    window = turtle.Screen()
    window.bgcolor('black')  # цвет звезды
    window.setup(700, 500)  # размер экрана

    window.mainloop()


def rand_stars(bob):
    for i in range(40):
        x = random.randint(-310, 310)
        y = random.randint(-210, 210)
        bob.up()
        bob.setposition(x, y)
        bob.down()
        n = random.randint(5, 10)
        long = random.randint(20, 30)
        star_fun(bob, n, long)
        bob.hideturtle()


def star_fun(bob, n, long):
    bob.begin_fill()  # Надо вызвать перед рисунком фигуры с цветом внутри

    if n % 2 != 0:
        for i in range(n):
            bob.forward(long)
            angle = n // 2 * 360 / n  # нахождение одного угла звезды
            bob.right(angle)
    bob.end_fill()  # Надо вызвать после рисунка фигуры с цветом внутри


if __name__ == "__main__":
    main()
