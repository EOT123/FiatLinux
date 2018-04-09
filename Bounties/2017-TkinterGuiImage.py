import pygame

pygame.init()
from tkinter import *

app = Tk()
app.title('')

T = Text(app, height=2, width=30)
T.pack()
T.insert(END, "craft\nwith buttons\n")

topFrame = Frame(app)
topFrame.pack()
bottomFrame = Frame(app)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 001", fg='red')
button2 = Button(topFrame, text="Button 002", fg='yellow')
button3 = Button(topFrame, text="Button 003", fg='green')
button4 = Button(topFrame, text="Button 004", fg='blue')

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)

fname = Canvas(bg='black', height=1920, width=1080)
fname.pack(side=TOP)

image1 = PhotoImage(file='python.png')
image = fname.create_image(50, 40, anchor=NW, image=image1)
fname.pack()


def leftclick(event):
    print('left')


def middleclick(event):
    print('middle')


def rightclick(event):
    print('right')


frame = Frame(app, width=200, height=0)
frame.bind('<Button-1>', leftclick)
frame.bind('<Button-2>', middleclick)
frame.bind('<Button-3>', rightclick)

frame.pack()

app.mainloop()
