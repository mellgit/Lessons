import turtle, random, time

def main():
    
    window = turtle.Screen()
    fun2(window)
    window.mainloop()


def chooseRandomColor():
    red = random.random()
    green = random.random()
    blue = random.random()
    return red, green, blue

def fun2(window):
    while True:
        
        window.bgcolor(chooseRandomColor())
        time.sleep(1)

if __name__ == "__main__":
    main()


