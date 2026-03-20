import turtle  # подключаем программу, которая умеет двигать черепашкой

def task1():
    # все размеры в пикселях - они очень маленькие!
    turtle.screensize(800, 800)  # задаем размер окна
    cell_size = 20  # размер клетки, чтобы было наглядно и удобно
    turtle.speed(5000)  # назначаем скорость черепашки
    turtle.tracer(50)  # ускорялка для черепашки -- она станем ебучим флешем!!!

    # рисуем себе координатную плоскость
    turtle.penup()  # поднимаем кисть, чтобы черепашка не рисовала за собой по своему пути
    for y in range(-12, 12):  # по размеру поля рисуем точечки
        for x in range(-12, 12):
            turtle.goto(x * cell_size, y * cell_size)  # переносим черепашку по координатам
            turtle.dot(4, "red")  # точка размером 4 пикселя красного цвета

    # идем по заданию
    turtle.goto(0, 0)  # перепестим черепашку в начальную позицию
    turtle.left(90)  # повернем ее головой вверх, как по условию
    turtle.pendown()  # опустим перо, чтобы она могла рисовать прямую

    for i in range(7):  # Повтори 7 раз:

        turtle.forward(10 * cell_size)  # Идти прямо 10 клеток
        # есть еще backward(count) -- назад

        turtle.right(120)  # Повернуть направо на 120 градусов

        if abs(turtle.pos()) == 0:  # модуль радиус-вектора черепашки
            break

    turtle.penup()  # поднимаем перо, чтобы она перестала рисовать прямую

    turtle.mainloop()  # чтобы сразу после рисования экран не выключился


def task2():
    turtle.screensize (800, 800)
    cell_size = 20
    turtle.tracer (50)

    turtle.penup()
    for y in range (-12, 12):
        for x in range (-12, 12) :
            turtle.goto(x * cell_size, y * cell_size)
            turtle.dot (4, "red")
    
    turtle.goto(0, 0)
    turtle.left(90)
    turtle.pendown()
    for i in range(1000):
        turtle.forward(5 * cell_size)
        turtle.right(45)
        turtle.backward(5 * cell_size)
        if abs(turtle.pos()) < 1:  # учитывает погрешность вычислений компа
            R = i + 1
            print (R)
            break
    turtle.penup ()
    turtle.mainloop()


def task3():
    turtle.screensize(800, 800)
    cell_size = 20
    turtle.tracer (50)

    turtle.penup()
    for y in range (-12, 12):
        for x in range (-12, 12) :
            turtle.goto(x * cell_size, y * cell_size)
            turtle.dot (4, "red")

    turtle.goto(0, 0)
    turtle.left(90)
    turtle.pendown()
    x, y = 0, 0  # начальные (текущие) координаты черепашки
    for i in range(20):
        turtle.goto((x + 4) * cell_size, (y + 3) * cell_size)
        # обновляем значения координат
        x += 4
        y += 3
        turtle.goto((x - 4) * cell_size, (y - 3) * cell_size)
        x -= 4
        y -= 3
        turtle.goto((x -12) * cell_size, (y - 5) * cell_size)
        x -= 12
        y -= 5
        turtle.goto((x + 12) * cell_size, (y + 5) * cell_size)
        x += 12
        y += 5
    turtle.penup()
    turtle.mainloop()


task3()
