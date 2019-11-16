import turtle
a = turtle.Turtle()
a.speed(0)
turtle.shape("turtle")
turtle.setposition(-100, -100)
turtle.penup()

turtle.goto(100, 100)
c = 1
turtle.pendown()
for i in range(360):
    a.forward(100)
    a.right(90)
    a.forward(1)
    if c % 2 == 0:
        a.color("black")
        print("black")
    else:
        print("red")

    a.penup()
    a.right(180)
    a.forward(1)
    a.left(90)
    a.pendown()
    a.forward(100)
    a.left(180)
    a.right(1)
    print(c)
    c = c + 1








turtle.done()
