import random

gamearray = []
numarray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
comparray = [2, 2, 2, 4]
col1 = []
col2 = []
col3 = []
col4 = []

for board_create in range(0, 16):  # populates board with mostly "*" and some 2s and 4s
    picker = random.randrange(0, 6)
    if picker == 1:
        gamearray.append(comparray[random.randrange(0, 4)])
    else:
        # gamearray.append(numarray[board_create])
        gamearray.append("*")


def printboard():
    print("{}   {}   {}   {}".format(gamearray[0], gamearray[1], gamearray[2], gamearray[3]))
    print("{}   {}   {}   {}".format(gamearray[4], gamearray[5], gamearray[6], gamearray[7]))
    print("{}   {}   {}   {}".format(gamearray[8], gamearray[9], gamearray[10], gamearray[11]))
    print("{}   {}   {}   {}".format(gamearray[12], gamearray[13], gamearray[14], gamearray[15]))


def downarrow(gamearray):
    check_if_spot_is_empty = []
    col1 = []
    col2 = []
    col3 = []
    col4 = []
    for i in range(8):
        if gamearray[i] == "*":
            check_if_spot_is_empty.append(gamearray[i])
            print ("true")
        else:
            check_if_spot_is_empty.append(gamearray[0])
            print ("false")
    print (check_if_spot_is_empty)

    for i in range(0, 16):
        if i % 4 == 0:
            col1.append(gamearray[i])
        elif i % 4 == 1:
            col2.append(gamearray[i])
        if i % 4 == 2:
            col3.append(gamearray[i])
        elif i % 4 == 3:
            col4.append(gamearray[i])
        else:
            pass

    newboardcalc(col1, col2, col3, col4)


def newboardcalc(col1, col2, col3, col4):
    print(col1, col2, col3, col4)
    printboard()


def playermove():
    playermove = input('Move? WASD movement\n\n')
    playermove.upper()
    playermove = playermove.upper()
    if playermove == "S":
        print("Down")
        downarrow(gamearray)
    elif playermove == "W":
        print("Up")
    elif playermove == "D":
        print("Right")
    elif playermove == "A":
        print("Left")
    else:
        print("Illegal move")


printboard()
while True:
    playermove()
    newboardcalc(col1, col2, col3, col4)
