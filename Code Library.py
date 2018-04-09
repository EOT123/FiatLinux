'''



########################################################################
My Code Library - Clay Jones
########################################################################
This is a series of small snippets of code that taught me something or help me remember how to do something specific.

TABLE
OF
CONTENTS
code
syntax and structure
variables
loops
random
numbers
tkinter
turtle
tips and tricks
colors
code
math
operations

########################################################################
CODE
SYNTAX
AND
STRUCTURE
########################################################################


CODE IN THE FOLLOWING STRUCTURE
Import
Initialize anything that needs to be initialized
Declare global variables
event handling
conditional statements
logic statements(can modify variables)
graphics rendering
update display

tip: Dont use global variables when possible.keep things contained within the function

TIP: M. KENNEDY TIP - KEEP LOGIC AND UI COMPONENTS SEPERATED.

########################################################################
VARIABLES
########################################################################

Python
5
data
types − numbers, strings, lists, tuples, dictionaries

a
tuple is a
list
but
with many less features and uses less memory than a list
print(x, y) - returns
x and y as a
tuple

########################################################################
LOOPS
########################################################################

# prints a range of numbers from 1 to 10, checks to see if the number is odd or even
# for loop, range, print, functions, if statement, else statement, modulus
for nummy in range(1, 10):
    check = nummy % 2
    if check == 0:
        print("your number is " + str(nummy) + "; so it's even")
    else:
        print("your number is " + str(nummy) + "; so it's odd")
########################################################################
# prints out odd numbers between 1 and 21
for numer in range(1, 21):
    modCheck = (numer % 2)
    if modCheck != 0:
        print(numer)
########################################################################
# prints out all the numbers from 1 to 100 in binary
for x in range(1, 100):
    binaree = (bin(x))
    print(binaree)
########################################################################
# Code that creates a screen and draws repeating turtle patterns
import math
import turtle
import os

turtle = turtle.Turtle()
claysScreen = turtle.Screen()
claysScreen.screensize(canvwidth=100, canvheight=100)
claysScreen.bgcolor("black")

turtleMoveLength01 = 21
turtleMoveLength02 = 45
turtle.pen(fillcolor="white", pencolor=("white"), pensize=.1)
turtle.speed("fastest")
turtle.tracer(10)
turtle.color("lightgray")
turtle.shape("circle")
turtle.hideturtle()

for number in range(1, 1000):
    turtle.hideturtle()
    turtle.forward(turtleMoveLength01 * 3)
    turtle.left(145)
    turtleMoveLength01 += .15
    turtleMoveLength02 += -1
    turtle.pen(fillcolor="white", pencolor=("white"), pensize=.2)
    # turtle.setpos(width / 2, height / 2)
    if turtleMoveLength01 >= 10:
        turtleMoveLength01 = -10
    if turtleMoveLength01 <= -10:
        turtleMoveLength02 = 10

    for number in range(1, 200):
        turtle.forward(turtleMoveLength01 / 2.5)
        turtle.left(turtleMoveLength02 * .1977)
        turtleMoveLength02 -= -.19

########################################################################
# creates a red and yellow star
from turtle import *

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
########################################################################
# Unfinished Brick Wall - While loops
import turtle
import random

b = turtle.Screen()
a = turtle.Turtle()

b.setup(width=1.0, height=1.0, startx=None, starty=None)
turtle.speed("fastest")
b.tracer(0, 0)
turtle.setheading(0)
turtle.pu()
turtle.setx(-960)
turtle.sety(-480)
turtle.pd()


def whereInX():
    global meeyo
    meeyo = turtle.xcor()
    return (meeyo)


def whereInY():
    global yuyo
    yuyo = turtle.ycor()
    return (yuyo)


def drawBrick():
    for halfBrick in range(0, 2):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    turtle.forward(100)


for ww in range(1, 21):
    for xx in range(1, 25):
        yy = 50
        drawBrick()
        whereInX()
        whereInY()
        if meeyo >= 980:
            if ww % 2 != 0:
                turtle.setx(-960)
                turtle.sety(yuyo + 50)
            else:
                turtle.setx(-890)
                turtle.sety(yuyo + 50)

turtle.update()
b.mainloop()
########################################################################
# WRAPAROUND - while loops and conditional statements
# like pacman, the turtle leaves one side and returns on the other side

import turtle
import random

x = 0
turtle01 = turtle.Turtle()
screen01 = turtle.Screen()
turtle01.speed("fastest")
turtle.tracer(0, 0)
while True:
    print(x)
    turtle.setx(x)
    screen01.update()
    x += (random.randrange(-2, 2))
    if x >= 255:
        x = -255
    if x <= -255:
        x = 255

screen01.mainloop()

########################################################################
RANDOM
NUMBERS
########################################################################
import random

# for bell curves (standard deviations)
# for a mean of 100 with a standard deviation of five
# the first number indicates the middle of the cluster
# the smaller the second number, the tighter the grouping
for i in range(10):
    print(random.normalvariate(100, 1))
########################################################################
# die roll
for i in range(10):
    print(random.randint(1, 6))
########################################################################
# pick an element from a list
outcomes = ["mage", "cleric", "paladin", "warrior", "archer", "rogue", "hunter", "druid"]
for i in range(8):
    print(random.choice(outcomes))

########################################################################
TKINTER
########################################################################
# Uses tkinter makes a frame with buttons
# tkinter, root, frame, .pack(), .mainloop
from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
button1 = Button(topFrame, text="Submit", fg="black", )
button2 = Button(topFrame, text="Donkey", fg="black", )
button3 = Button(topFrame, text="Yahoo", fg="black", )
button4 = Button(bottomFrame, text="Little More", fg="red", )
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
root.mainloop()

########################################################################

# builds a tkinter frame with a button that tallies mouse clicks
from tkinter import *

x = 0


def hello(event):
    global x
    x = x + 1
    print(x)


def quit(event):
    print("Double Click, so let's stop")
    import sys;
    sys.exit()


widget = Button(None, text='Mouse Clicks')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit)
widget.mainloop()

########################################################################

# Creates 4 arrows to control turtle that draws rainbow lines and random circles
import turtle
import tkinter
import sys
import random

screen01 = turtle.Screen()
turtle01 = turtle.Turtle()

convXtoInt = 0
convYtoInt = 0
r = 0
g = 0
b = 0
size = 1

turtle.colormode(255)
turtle01.hideturtle()
turtle.tracer(1, 0)
turtle01.speed("fastest")
turtle.shapesize(2)
turtle.setheading(90)


def randomColorGenerator(r, g, b):
    metoo = random.randrange(120, 130)
    turtle.color(metoo + random.randrange(-120, 120), 255 - (metoo + random.randrange(-120, 120)),
                 255 - (metoo + random.randrange(-120, 120)))


def randomSizeGenerator(size):
    turtle.pensize(random.randrange(1, 10))
    turtle.shapesize(random.randrange(1, 3))


def gottago():  # this kills everthing by hitting escape
    sys.exit()


def f():  # forward function and reports x and y position
    randomColorGenerator(r, g, b)
    turtle.forward(50)
    forcemultiplier = random.randrange(-10, 10)
    for ii in range(1, random.randrange(-7, 7)):
        turtle.forward(50)
        randomSizeGenerator(size)
        for cir in range(-2, 2):
            turtle.circle(random.randrange(-10, 10) * cir)
            turtle.left(cir)
            turtle.right(cir)
            randomColorGenerator(forcemultiplier / 20, forcemultiplier / 20, forcemultiplier / 20)
        whereInX()
        whereInY()


def l():  # left turn
    turtle.left(90)


def r():  # right turn
    turtle.right(90)


def b():  # backward function and reports position
    turtle.backward(50)
    whereInX()
    whereInY()


def whereInX():  # assigns and prints variable of x position
    whereInX = turtle.xcor()
    print("x position = " + str(whereInX))
    convXtoInt = int(whereInX)
    return whereInX


def whereInY():  # assigns and prints variable of x position
    whereInY = turtle.ycor()
    print("y position = " + str(whereInY))
    print("")
    return whereInY


if whereInX() >= 400:
    turtle.setx(400)
if whereInX() <= -400:
    turtle.setx(-400)
if whereInY() >= 400:
    turtle.sety(400)
if whereInY() <= -400:
    turtle.sety(-400)


def rightBorder():
    turtle.setx(200.0)


print(whereInX())
screen01.listen()

screen01.onkey(l, "Left")
screen01.onkey(f, "Up")
screen01.onkeypress(f, "Up")
screen01.onkey(r, "Right")
screen01.onkey(b, "Down")
screen01.onkey(gottago, "Escape")
screen01.exitonclick()
turtle.Terminator()

screen01.mainloop()

########################################################################
TURTLE
TIPS
AND
TRICKS
########################################################################


########################################################################
COLORS
CODE
########################################################################
# converts r,g,b (0,255) to hexidecimal and draws the screen in that color

import random
import turtle

hex001 = random.randrange(0, 255)
hex002 = random.randrange(0, 255)
hex003 = random.randrange(0, 255)
a001 = (format(hex001, '02X'))
a002 = (format(hex002, '02X'))
a003 = (format(hex003, '02X'))
mycolor = ("#" + (a001 + a002 + a003))
print(mycolor)
screen01 = turtle.Screen()
turtle01 = turtle.Turtle()
screen01.bgcolor(mycolor)
print(format(255, '#04X'))
screen01.mainloop()

########################################################################

# Color Fader - fades colors in and out

import turtle
import random
import sys
import time

screen01 = turtle.Screen()
turtle01 = turtle.Turtle()

screen01.colormode(255)

redInit = random.randrange(0, 255)
redCyc = random.randrange(-2, 2)
greenInit = random.randrange(0, 255)
greenCyc = random.randrange(-2, 2)
blueInit = random.randrange(0, 255)
blueCyc = random.randrange(-2, 2)

# screen01.bgcolor(redInit, greenInit, blueInit)
while True:
    screen01.bgcolor(redInit, greenInit, blueInit)
    redInit = redInit + redCyc
    greenInit = greenInit + greenCyc
    blueInit = blueInit + blueCyc
    time.sleep(.01)
    print(redInit, redCyc, greenInit, greenCyc, blueInit, blueCyc)
    if (redInit) <= 0:
        time.sleep(.01)
        redInit = 252
    elif (redInit) >= 252:
        time.sleep(.01)
        redInit = 0
    elif (greenInit) <= 0:
        time.sleep(.01)
        greenInit = 252
    elif (greenInit) >= 252:
        time.sleep(.01)
        greenInit = 0
    elif (blueInit) <= 0:
        time.sleep(.01)
        blueInit = 252
    elif (blueInit) >= 252:
        time.sleep(.01)
        blueInit = 0
    elif (blueInit) <= 0:
        time.sleep(.01)
        blueInit = 252
    else:
        print("yadoneitnow")


def timeToFly():
    sys.exit()


screen01.listen()
screen01.onkey(timeToFly, "Up")
# screen01.onkey(numberGetter, "Down")
screen01.exitonclick()
screen01.mainloop()

########################################################################
MATH
OPERATIONS
########################################################################
# An experiment with modulus to determine colors
import turtle
import random

b = turtle.Screen()
a = turtle.Turtle()
b.bgcolor("black")
b.setup(width=.5, height=0.5, startx=None, starty=None)
xpos = 1
ypos = -1
headingMaker = -1
turtle.color("black", "yellow")
turtle.tracer(10, 0)
for xx in range(1, 20):
    for i in range(-200, 200, 1):
        turtle.begin_fill()
        turtle.setx(xpos + random.randrange(0.0, 10.0))
        turtle.goto(xpos * 100, xpos * -10)
        turtle.end_fill()
        turtle.forward(100 * (i / 200))
        turtle.left(-90)
        turtle.circle(100, 2, 2)
        # turtle.setheading(headingMaker+180)
        # turtle.circle (headingMaker*180,headingMaker*i*10,50)
        # headingMaker=headingMaker*-1

        if i % 5 == 0:
            i = i * -i
            turtle.color("purple")
            turtle.left(i * i)
        elif i % 2 == 0:
            i = i * -i
            turtle.color("blue")
            turtle.left(i * i)
        elif i % 3 == 0:
            i = i * -i
            turtle.color("red")
            turtle.left(i * i)
        elif i % 7 == 0:
            i = i * -i
            turtle.color("white")
            turtle.left(i * i)
        elif i % 11 == 0:
            i = i * -i
            turtle.clear()
            turtle.left(i * i)
        elif i % 4 == 0:
            i = i * -i
            turtle.clear()
            turtle.left(i * i)
        else:
            turtle.color("black", "yellow")
    if i >= 190:
        i = -200
turtle.update
b.mainloop()

########################################################################
'''
