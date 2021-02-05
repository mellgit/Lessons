import turtle

speed = 5


def main():
    global window
    window = turtle.Screen()

    global pen
    pen = turtle.Turtle()

    # window.onkey(функция, клавиша) - события

    window.onkey(moveUp, "Up")
    window.onkey(moveDown, "Down")  # движение вниз
    window.onkey(moveLeft, "Left")
    window.onkey(moveRight, "Right")
    window.onkey(change, "space") # скрыть черепашку

    window.onkey(speedUp, "q") # увеличить скороть 
    window.onkey(speedDown, "g") # уменишить скорость

    window.listen()
    window.mainloop()


def moveUp():
    # в пизошн лежит кортеж
    x = pen.position()[0]
    y = pen.position()[1]
    pen.setposition(x, y+5)


def moveDown():
    x = pen.position()[0]
    y = pen.position()[1]
    pen.setposition(x, y-speed)


def moveLeft():
    x = pen.position()[0]
    y = pen.position()[1]
    pen.setposition(x-speed, y)


def moveRight():
    x = pen.position()[0]
    y = pen.position()[1]
    pen.setposition(x+speed, y)


def change():
    if pen.isvisible():  # если черепашка видна
        pen.up()
        pen.hideturtle()
    else:
        pen.down()
        pen.showturtle()


def speedUp():
    global speed
    speed += 1


def speedDown():
    global speed
    speed = max(0, speed-1)# проверка на отрицательную скорость


if __name__ == "__main__":
    main()
