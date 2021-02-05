import turtle, random  

border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.pensize(5)
border.up()
border.goto(-250, 250)
border.down()
border.goto(-250, -250)
border.goto(250, -250)
border.goto(250,250)

window = turtle.Screen()
window.bgcolor('yellow')

window.tracer(20)# для сложной графики - tracer

balls = []
count = 30
forms = ['circle', 'square', 'triangle', 'turtle']

for ball in range(count):
    ball = turtle.Turtle(shape=random.choice(forms)) # random.choice(forms) - рандомно выбирает форму черепашки
    red = random.random() # для разных цветов
    green = random.random()
    blue = random.random()
    ball.color(red,green,blue)
    ball.up()
    ball.goto(random.randint(-200,200),random.randint(100,250)) # чтобы мяч мог повиться в рандомной точке
    ball.speedY = 0
    ball.speedX = random.randint(-3,3) # скорость каждого мяча разная
    ball.angle = random.randint(-5, 5)
    ball.gravitation = random.randint(1,30)*0.01
    balls.append(ball)




while True:
    window.update()# для обновления экрана
    for ball in balls:
        ball.left(ball.angle) # для того чтобы фигура могла крутиться
        ball.speedY = ball.speedY - ball.gravitation
        ball.goto(ball.xcor() + ball.speedX, ball.ycor() + ball.speedY)

        if ball.ycor() <= -250:
            ball.sety(-250) # чтобы мячики не выходили за границу, те если ушел то установим сразу ему позицию
            ball.speedY = -ball.speedY

        if ball.xcor() >= 250 or ball.xcor() <= -250:
            ball.speedX = -ball.speedX
window.mainloop()