import turtle
turtle.screensize(1000, 1000)
cell_size = 20
turtle.tracer(50)

turtle.penup()
for x in range(-14, 14):
    for y in range(-14, 14):
        turtle.goto(x * cell_size, y * cell_size)
        turtle.dot(4, "red")
        
turtle.goto(0, 0)
turtle.left(90)
turtle.pendown()

for i in range(3):
    turtle.forward(12 * cell_size)
    turtle.right(90)
    turtle.forward(6 * cell_size)
    turtle.right(90)

turtle.penup()

turtle.forward(5 * cell_size)
turtle.right(90)
turtle.forward(1 * cell_size)
turtle.left(90)

turtle.pendown()

for i in range(5):
    turtle.forward(10 * cell_size)
    turtle.right(90)
    turtle.forward(14 * cell_size)
    turtle.right(90)
turtle.penup()
turtle.mainloop()
