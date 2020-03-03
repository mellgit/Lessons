# dfjhgkjsdhfg

# где x0,y0 - координаты произвольной точки
#
# Если все три значения одинакового знака, то точка внутри треугольника,
#
# если значение равно нулю, значит точка лежит на стороне треугольника
#
# В ином случае (если значения различные по знаку) , точка вне треугольника.
def first_task():
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))
    x3 = int(input("x3 = "))
    y3 = int(input("y3 = "))

    x = int(input(" x = "))
    y = int(input(" y = "))

    k = (x1 - x) * (y2 - y1) - (x2 - x1) * (y1 - y)
    m = (x2 - x) * (y3 - y2) - (x3 - x2) * (y2 - y)
    n = (x3 - x) * (y1 - y3) - (x1 - x3) * (y3 - y)

    if k >= 0 and m >= 0 and n >= 0 or k <= 0 and m <= 0 and n <= 0:
        print("True")
    else:
        print("False")

# Снежинка Коха
# ОТрезок делится на три части, центральный убираем и вместо этого ставим равносторонний треугольник и так далее

def third_task():
    import turtle # Для изображения для Снежинки Коха
    import sys
    turtle.shape('turtle')
    turtle.penup() # состояние рисования (движение ручки вверх)
    turtle.goto(-200, 0) # для бозначение координат в 2D(x,y) (маштабируемость)
    turtle.pendown() # толщина линии (движение ручки вниз)

    def Koch_Line(l, n):
        if n == 0:
            turtle.forward(l) # расстояние (проползти вперед n шагов)
            return
        l //= 3 # деление без остатка в меньшую сторону
        Koch_Line(l, n - 1)
        turtle.left(60) # угол поворота в градусах слева
        Koch_Line(l, n - 1)
        turtle.right(120) # угол поворота в градусах слева
        Koch_Line(l, n - 1)
        turtle.left(60)
        Koch_Line(l, n - 1)

    Koch_Line(400, 4)

    turtle.mainloop() # задержать окно на экране
    # l = 400 - расстояние (расстояние от точки а до точки б) (слева на право)
    # n = 4 - количество отрезанных отрезков


def second_task1():  # процедура - это метод или функция, но процедура не может возвращаться значение, те return
    x = [1, 2, 3, 4]
    for i in range(len(x)):
        print(x[i])


def second_task2(n):
    result = ''
    print(n, end=' ')
    # zip() может принимать любые типы итераций, такие как файлы, списки, кортежи, словари, наборы и т. д.
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman  # 9//2 = 4 ()
        n %= arabic  # остаток от деления (1050 - m; 1000 - запишет останется 50; 50 - l)
        # print('({}) {} => {}'.format(roman, n, result))

    print("->", result)

    return result


def main():
    first_task()
    # second_task1()
    # second_task2(20)
    # third_task()


main()
