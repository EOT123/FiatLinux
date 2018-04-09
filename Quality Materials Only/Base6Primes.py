import turtle

turtlemaker = turtle.Turtle()
screenmaker = turtle.Screen()
screenmaker.tracer(0, 0)

turtle02 = turtle.Turtle()
turtle03 = turtle.Turtle()
turtle04 = turtle.Turtle()
turtle02.hideturtle()
turtle03.hideturtle()
turtle04.hideturtle()
turtle02.penup()
turtle03.penup()
turtle04.penup()
turtle02.speed("fastest")
turtle03.speed("fastest")
turtle04.speed("fastest")
turtle02.goto(-645, 470)
turtle03.goto(-930, 470)
turtle04.goto(-135, 470)
turtle02.write("BASE 12", align="left", font=100)
turtle03.write("BASE 06", align="left", font=100)
turtle04.write("BASE 36", align="left", font=100)
turtlemaker.pencolor("red")
screenmaker.update()


def turtleredbox():
    turtbeginx = -650
    for fins in range(0, 12):
        turtlemaker.penup()
        turtlemaker.goto(turtbeginx, 467)
        turtlemaker.setx(turtbeginx)
        turtbeginx = turtbeginx + 30
        turtlemaker.pendown()
        for final in range(1, 50):
            turtlemaker.forward(30)
            turtlemaker.right(90)
            turtlemaker.forward(15)
            turtlemaker.right(90)
            turtlemaker.forward(30)
            turtlemaker.right(90)
            turtlemaker.forward(15)
            turtlemaker.backward(15)
            turtlemaker.right(90)
            screenmaker.update()


def turtleredboxii():
    turtbeginx = -935
    for fins in range(0, 6):
        turtlemaker.penup()
        turtlemaker.goto(turtbeginx, 467)
        turtlemaker.setx(turtbeginx)
        turtbeginx = turtbeginx + 30
        turtlemaker.pendown()
        for final in range(1, 50):
            turtlemaker.forward(30)
            turtlemaker.right(90)
            turtlemaker.forward(15)
            turtlemaker.right(90)
            turtlemaker.forward(30)
            turtlemaker.right(90)
            turtlemaker.forward(15)
            turtlemaker.backward(15)
            turtlemaker.right(90)
            screenmaker.update()


def turtleredboxiii():
    turtbeginx = -139
    for fins in range(0, 36):
        turtlemaker.penup()
        turtlemaker.goto(turtbeginx, 467)
        turtlemaker.setx(turtbeginx)
        turtbeginx = turtbeginx + 30
        turtlemaker.pendown()
        for final in range(1, 50):
            turtlemaker.forward(30)
            turtlemaker.right(90)
            turtlemaker.forward(15)
            turtlemaker.right(90)
            turtlemaker.forward(30)
            turtlemaker.right(90)
            turtlemaker.forward(15)
            turtlemaker.backward(15)
            turtlemaker.right(90)
            screenmaker.update()
            turtlemaker.hideturtle()


turtleredboxii()
turtleredbox()
turtleredboxiii()

xloc2 = -935
yloc2 = 400
for num in range(1, 294):
    turtle.penup()
    turtle.setx(xloc2)
    turtle.sety(yloc2)
    xloc2 = xloc2 + 30
    prime = True
    if num % 6 == 0:
        turtle.penup()
        xloc2 = -935
        yloc2 = yloc2 - 15
    for i in range(2, num):
        turtle.penup()
        turtle.goto(xloc2 + 50, yloc2)
        turtle.pendown()
        if (num % i == 0):
            prime = False
    if prime:
        turtle.penup()
        turtle.goto(xloc2, yloc2 + 50)
        turtle.pendown()
        turtle.setx(xloc2)
        turtle.write(num, font=45, align="right")

xloc = -650
yloc = 400
turt02distance = 50

for num in range(1, 588):
    turtle.penup()
    turtle.setx(xloc)
    turtle.sety(yloc)
    xloc = xloc + 30
    prime = True
    if num % 12 == 0:
        turtle.penup()
        xloc = -650
        yloc = yloc - 15
    for i in range(2, num):
        turtle.penup()
        turtle.goto(xloc + 50, yloc)
        turtle.pendown()
        if (num % i == 0):
            prime = False
    if prime:
        turtle.penup()
        turtle.goto(xloc, yloc + 50)
        turtle.pendown()
        turtle.setx(xloc)
        turtle.write(num, font=45, align="right")

xloc3 = -136
yloc3 = 400
for num in range(1, 1760):
    turtle.penup()
    turtle.setx(xloc3)
    turtle.sety(yloc3)
    xloc3 = xloc3 + 30
    prime = True
    if num % 36 == 0:
        turtle.penup()
        xloc3 = -136
        yloc3 = yloc3 - 15
    for i in range(2, num):
        turtle.penup()
        turtle.goto(xloc3 + 50, yloc3)
        turtle.pendown()
        if (num % i == 0):
            prime = False
    if prime:
        turtle.penup()
        turtle.goto(xloc3, yloc3 + 50)
        turtle.pendown()
        turtle.setx(xloc3)
        turtle.write(num, font=45, align="right")

screenmaker.mainloop()
