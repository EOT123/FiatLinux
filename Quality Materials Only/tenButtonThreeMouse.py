import random
import sys
import turtle

a = turtle.Turtle()
b = turtle.Screen()
b.setup(width=.618, height=.618, startx=None, starty=None)
b.colormode(255)
b.mode("logo")
b.tracer(7, 0)
a.hideturtle()

colorr = random.randrange(0, 16)
colorg = random.randrange(0, 16)
colorb = random.randrange(0, 16)
b.bgcolor(colorr * 16, colorb * 16, colorg * 16)

a.setheading(00)
a.speed("fastest")


def eraseboardwithspace():
    turtle.reset()


def aa():
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.write("A keyboard drawing demonstration by Clay Jones",
                 move=False, align="center", font=("Arial", 32, "bold"))


def ss():
    turtle.pendown()
    circleheading = 0
    circleincrementer = random.randrange(30, 50)
    circlestep = 360 / circleincrementer
    turtle.showturtle()
    turtle.penup()
    tilemaker = random.randrange(2, 8)
    for sss in range(0, circleincrementer):
        turtle.tracer(0, 0)
        circleheading = circleheading + circlestep
        turtle.setheading(circleheading)
        turtle.forward(circleincrementer * 8)
        turtle.pendown()
        turtle.circle(turtle.distance(0, 0) * .02, 360, tilemaker)
        for ttt in range(1, 10):
            turtle.forward(random.randrange(-10, 10))
            forcemultiplier()
            turtle.penup()
            turtle.home()


def dd():
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.setheading(random.randrange(1, 3) * 60)
    for triangleRunner in range(1, random.randrange(400, 500)):
        turtleflipper = random.randrange(-2, 2)
        turtle.right(turtleflipper * 60)
        turtle.forward(random.randrange(-3, 5) * 30)


def ff():
    turtleturner = 90
    myxloc = turtle.xcor
    turtle.penup()
    turtle.setx(0)
    turtle.sety(0)
    turtle.setheading(random.randrange(0, 360))
    turtle.pendown()
    turtlecolorr = random.randrange(0, 16)
    turtlecolorg = random.randrange(0, 16)
    turtlecolorb = random.randrange(0, 16)
    turtle.color(turtlecolorr * 16, turtlecolorg * 16, turtlecolorb * 16)
    turtle.pencolor(turtlecolorr * 16, turtlecolorg * 16, turtlecolorb * 16)
    turtle.fillcolor(turtlecolorr * 16, turtlecolorg * 16, turtlecolorb * 16)
    for zzz in range(1, 1000):
        myXLoc = turtle.xcor()
        print(myXLoc)
        turtle.forward(random.randrange(1, 2))
        turtle.right(turtleturner)
        turtle.forward(random.randrange(1, 2) * turtle.distance(0, 0) + random.randrange(-30, 30))
        turtleturner = turtleturner * -1
        turtle.right(turtleturner)
        turtle.forward(random.randrange(1, 2))
        turtle.right(turtle.distance(0, 0) / random.randrange(1000, 2500))
        turtle.update()


def gg():
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.tracer(0, 0)
    turtle.setheading(random.randrange(-4, 4) * 45)
    turtlecolorr = random.randrange(0, 16)
    turtlecolorg = random.randrange(0, 16)
    turtlecolorb = random.randrange(0, 16)
    turtle.color(turtlecolorr * 16, turtlecolorg * 16, turtlecolorb * 16)
    turtle.pencolor(turtlecolorr * 16, turtlecolorg * 16, turtlecolorb * 16)
    turtle.fillcolor(turtlecolorr * 16, turtlecolorg * 16, turtlecolorb * 16)
    for triangleRunner in range(1, random.randrange(400, 500)):
        turtle.pensize(random.randrange(1, 8))
        turtleflipper = random.randrange(-2, 2)
        turtle.right(turtlflipper * 45)
        turtle.forward(random.randrange(-3, 5) * 45)
        turtle.update()


def hh():
    turtle.penup()
    turtle.tracer(0, 0)
    turtle.home()
    turtle.pendown()
    turtle.setheading(random.randrange(-1, 2) * 90)
    turtlecolorr = random.randrange(0, 16)
    turtlecolorg = random.randrange(0, 16)
    turtlecolorb = random.randrange(0, 16)
    turtle.color(turtlecolorr * 16, turtlecolorg * 16, turtlecolorb * 16)
    turtle.pencolor(turtlecolorr * 16, turtlecolorg * 16, turtlecolorb * 16)
    turtle.fillcolor(turtlecolorr * 16, turtlecolorg * 16, turtlecolorb * 16)
    for triangleRunner in range(1, random.randrange(400, 500)):
        turtle.pensize(random.randrange(1, 3))
        turtleflipper = random.randrange(-2, 2)
        turtle.right(turtleflipper * 90)
        turtle.forward(random.randrange(-10, 10) * 8)
        turtle.update()


def jj():
    yoffset = 5
    ycountdown = yoffset - 10
    turtle.pensize(1)
    turtle.pendown()
    turtlecolorr = random.randrange(0, 16)
    turtlecolorg = random.randrange(0, 16)
    turtlecolorb = random.randrange(0, 16)
    turtle.color(turtlecolorr * 16, turtlecolorg * 16, turtlecolorb * 16)
    turtle.pencolor(turtlecolorr * 16, turtlecolorg * 16, turtlecolorb * 16)
    turtle.fillcolor(turtlecolorr * 16, turtlecolorg * 16, turtlecolorb * 16)
    for something in range(0, 3):
        turtleturner = 2
        turtdist = turtle.distance(0, 0)
        turtle.circle(turtle.distance(0, 0) * .05, 360, random.randrange(3, 6))
        turtle.right(turtleturner)
        turtleturner = turtleturner + .2
        multirange = random.randrange(-2, 2)
        sizetracker = random.randrange(-20, 1)
        sizetracker02 = random.randrange(10, 20)
        circlemaker = random.randrange(-5, 10)
        turtle.pendown()
        yoffset = yoffset - ycountdown
        for times in range(0, multirange):
            turtle.pensize(turtdist * .005)
            turtle.forward(sizetracker)
            turtle.right(360 / multirange)
            turtle.backward(sizetracker02 * 5)
            turtle.circle(circlemaker)


def kk():
    turtle.home()
    turtle.pendown()
    righty = 45
    turtle.setheading(random.randrange(0, 360))
    for practicesquarerotation in range(1, 200):
        turtle.right(righty)
        turtle.forward(practicesquarerotation)
        print(practicesquarerotation)
        myxloc = turtle.xcor()
        if turtle.distance(0, 0) >= 200:
            turtle.home()
            practicesquarerotation = practicesquarerotation * -1
            righty = righty * -1
        if turtle.distance(200, -300) >= 300:
            mynewvar = myxloc * -1
            turtle.circle(turtle.distance(0, 0) / 10)
        if turtle.distance(0, 0) >= 300:
            turtle.home()
            turtle.circle(turtle.distance(0, 0) / 100)
        if practicesquarerotation % 200 == 0:
            turtle.Terminator(True)


def ll():
    pass


def fwd():
    turtle.forward(100)
    b.update()


def bck():
    turtle.backward(100)
    b.update()


def lft():
    turtle.left(90)
    b.update()


def rgt():
    turtle.right(90)
    b.update()


def forcemultiplier():
    b.tracer(8, 0)
    turtle.pensize(.1)
    polygonpicker = 200
    polysize = 360 / polygonpicker * 10
    polygonpicker = random.randrange(5, 10)
    turtlecolorr = random.randrange(0, 16)
    turtlecolorg = random.randrange(0, 16)
    turtlecolorb = random.randrange(0, 16)
    turtle.color(turtlecolorr * 16, turtlecolorg * 16, turtlecolorb * 16)
    turtle.pencolor(turtlecolorr * 16, turtlecolorg * 16, turtlecolorb * 16)
    turtle.fillcolor(turtlecolorr * 16, turtlecolorg * 16, turtlecolorb * 16)
    for polymaker in range(0, polygonpicker):
        turtle.begin_fill()
        turtle.forward(polysize)
        turtle.right(360 / polygonpicker)
    turtle.end_fill()
    b.update()


def shutdown():
    sys.exit()


def spc():
    turtle.reset()


def leftclick(btn, add):
    turtle.pensize(.2)
    turtle.tracer(0, 0)
    for i in range(0, 1):
        turtlecolorr = random.randrange(6, 254)
        turtlecolorg = random.randrange(6, 254)
        turtlecolorb = random.randrange(6, 254)
        turtle.color(turtlecolorr, turtlecolorg, turtlecolorb)
        turtle.pencolor(turtlecolorr, turtlecolorg, turtlecolorb)
        turtle.fillcolor(turtlecolorr, turtlecolorg, turtlecolorb)
        randomoriginallocatorx = random.randrange(-400, 400)
        randomoriginallocatory = random.randrange(-400, 400)
        randomoriginalheading = random.randrange(0, 360)
        stepperrotator = random.randrange(-1, 1, 2)
        stepperenlengthener = random.randrange(-5, 5)
        stepper03 = random.randrange(0, 500)
        turtle.penup()
        turtle.setx(randomoriginallocatorx)
        turtle.sety(randomoriginallocatory)
        turtle.setheading(randomoriginalheading)
        turtle.pendown()
        rstepper = (random.randrange(-10, 10))
        gstepper = (random.randrange(-10, 10))
        bstepper = (random.randrange(-10, 10))
        for getgoing in range(1, 10000):
            if stepper03 % 10 == 0:
                turtle.setx(random.randrange(-600, 600))
                stepper03 = stepper03 * -1
                stepperrotator = stepperrotator * -1
                leftclick(btn, add)
            turtlecolorr = int(turtlecolorr + (rstepper / 10))
            turtlecolorg = int(turtlecolorg + (gstepper / 10))
            turtlecolorb = int(turtlecolorb + (bstepper / 10))
            turtle.color(turtlecolorr, turtlecolorg, turtlecolorb)
            if turtlecolorr >= 250:
                turtlecolorr = turtlecolorr - 2
            if turtlecolorg >= 250:
                turtlecolorg = turtlecolorg - 2
            if turtlecolorb >= 250:
                turtlecolorb = turtlecolorb - 2
            if turtlecolorr <= 5:
                turtlecolorr = turtlecolorr + 2
            if turtlecolorg <= 5:
                turtlecolorg = turtlecolorg + 2
            if turtlecolorb <= 5:
                turtlecolorb = turtlecolorb + 2
            if getgoing % 1000 == 0:
                break
            print(turtlecolorr, turtlecolorg, turtlecolorb)
            turtle.forward(stepper03)
            turtle.backward(stepper03)
            turtle.right(stepperrotator * .09)
            stepper03 = stepper03 + stepperenlengthener
            turtle.update()


def middleclick(btn, add):
    currentheading = 0
    turtle.pendown()
    rightclick(btn, add)
    b.update()
    b.tracer(10, 0)
    turtle.setheading(currentheading)
    headingstepper = random.randrange(10, 60)
    intervalstepper = 360 / headingstepper
    turtle.home()
    for count in range(0, headingstepper):
        currentheading = currentheading + intervalstepper
        turtle.penup()
        turtle.home()
        turtle.setheading(currentheading)
        for circles in range(1, 10):
            turtle.penup()
            turtle.forward(intervalstepper * (headingstepper * -.1) + 1.25)
            jj()


def rightclick(btn, add):
    colorr = random.randrange(0, 16)
    colorg = random.randrange(0, 16)
    colorb = random.randrange(0, 16)
    b.bgcolor(colorr * 16, colorb * 16, colorg * 16)


b.onkeypress(aa, "A")
b.onkeypress(aa, "a")
b.onkeyrelease(eraseboardwithspace, "A")
b.onkeyrelease(eraseboardwithspace, "a")

b.onkey(ss, "S")
b.onkey(ss, "s")

b.onkey(dd, "D")
b.onkey(dd, "d")

b.onkey(ff, "F")
b.onkey(ff, "f")

b.onkey(gg, "G")
b.onkey(gg, "g")

b.onkey(hh, "H")
b.onkey(hh, "h")

b.onkey(jj, "J")
b.onkey(jj, "j")

b.onkey(kk, "K")
b.onkey(kk, "k")

b.onkey(ll, "L")
b.onkey(ll, "l")

b.onkey(fwd, "Up")
b.onkey(bck, "Down")
b.onkey(lft, "Left")
b.onkey(rgt, "Right")
b.onkey(spc, "space")
b.onkey(shutdown, "Escape")

b.onclick(leftclick, 1, True)
b.onclick(middleclick, 2, True)
b.onclick(rightclick, 3, True)

b.update()
b.listen()
b.mainloop()
