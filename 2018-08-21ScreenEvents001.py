import turtle # imports the turtle library
import random # imports the random library

scr = turtle.Screen() # goes into turtle library and calls screen function
trt = turtle.Turtle() # creates turtle
scr.tracer(10,0)
trt.color("black",'blue')
def littledraw():
    myx = random.randrange(-200,200)
    myy = random.randrange(-200,200)
    randsize = random.randrange(5,20)
    trt.penup()
    trt.goto(myx,myy)#sends turtle to random x and
    trt.pendown()
    trt.begin_fill()
    trt.circle(randsize)
    trt.circle(100)
    trt.end_fill()
'''
Short Comment
'''
scr.listen() # readies screen events
scr.update()# refreshes the screen
scr.onkey(littledraw, "a")
scr.mainloop() #keeps screen looping

