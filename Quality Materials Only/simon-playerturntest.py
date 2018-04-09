import random
import turtle

scr = turtle.Screen()
scr.tracer(10, 0)

simon_move_list = []
player_move_list = []


# make gamboard
def createbuttons():
    turtlemover = turtle.Turtle()
    redbutton = turtle.Turtle()
    redbutton.color('red')
    redbutton.shape('square')
    redbutton.shapesize(10)
    redbutton.goto(110, 110)
    bluebutton = turtle.Turtle()
    bluebutton.color('blue')
    bluebutton.shape('square')
    bluebutton.shapesize(10)
    bluebutton.goto(110, -110)
    greenbutton = turtle.Turtle()
    greenbutton.color('green')
    greenbutton.shape('square')
    greenbutton.shapesize(10)
    greenbutton.goto(-110, 110)
    yellowbutton = turtle.Turtle()
    yellowbutton.color('yellow')
    yellowbutton.shape('square')
    yellowbutton.shapesize(10)
    yellowbutton.goto(-110, -110)
    scr.update()


def turtlemover(btn, add):
    myxcor = int(turtle.xcor())
    myycor = int(turtle.ycor())
    turtle.goto(myxcor, myycor)
    turtle.write('x={}\ny={}'.format(myxcor, myycor), move=False, align='center', font=('Arial', 20, 'normal'))
    scr.update()
    # make and record button presses
    if myxcor <= 0 and myycor >= 0:
        print('green')
        player_move_list.append(1)
    if myxcor > 0 and myycor > 0:
        print('red')
        player_move_list.append(2)
    if myxcor <= 0 and myycor <= 0:
        print('yellow')
        player_move_list.append(3)
    if myxcor > 0 and myycor < 0:
        print('blue')
        player_move_list.append(4)
    print(player_move_list)


def gameloop():
    while True:
        simons_turn = True
        # generate simon's moves
        # record simon's moves
        simon_makes_move = random.randrange(1, 5)
        simon_move_list.append(simon_makes_move)
        playermove = input('what is your combo?')
        playermoveint = int(playermove)

        for simoncycler in range(0, len(simon_move_list)):
            print(simon_move_list[simoncycler])
            if simon_move_list[simoncycler] == 1:
                print('green')
            elif simon_move_list[simoncycler] == 2:
                print('red')
            elif simon_move_list[simoncycler] == 3:
                print('yellow')
            elif simon_move_list[simoncycler] == 4:
                print('blue')
            else:
                print("invalid")

        simons_turn = True


# game logic
# if players moves are same as simon continue
# if players moves take too long beep an error and repeat
# if players moves are wrong beep an error and repeat.
turtle.penup()
scr.onclick(turtle.goto)
scr.onclick(turtlemover, 1, True)
scr.listen()
createbuttons()
gameloop()
scr.mainloop()
