import random

gamearray = []
numarray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
comparray = [2, 2, 2, 4]

for board_create in range(0, 16):
    picker = random.randrange(0, 3)
    if picker == 1:
        gamearray.append(comparray[picker])
    else:
        # gamearray.append(numarray[board_create])
        gamearray.append("*")

table_row_col = []  # a four digit holding slot for movement


def printboard():
    print("{}   {}   {}   {}".format(gamearray[0], gamearray[1], gamearray[2], gamearray[3]))
    print("{}   {}   {}   {}".format(gamearray[4], gamearray[5], gamearray[6], gamearray[7]))
    print("{}   {}   {}   {}".format(gamearray[8], gamearray[9], gamearray[10], gamearray[11]))
    print("{}   {}   {}   {}".format(gamearray[12], gamearray[13], gamearray[14], gamearray[15]))


def downarrow():
    col1 = []
    col2 = []
    col3 = []
    col4 = []
    for i in range(0, 16):
        if i % 4 == 0:
            col1.append(numarray[i])
        elif i % 4 == 1:
            col2.append(numarray[i])
        if i % 4 == 2:
            col3.append(numarray[i])
        elif i % 4 == 3:
            col4.append(numarray[i])
        else:
            print ("helloo")

    print (col1, col2, col3, col4)
    printboard()


def playermove():
    playermove = input('Move? WASD movement\n\n')
    playermove.upper()
    playermove = playermove.upper()
    if playermove == "S":
        print("Down")
        downarrow()
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
