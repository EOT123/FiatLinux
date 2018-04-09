print ("Welcome to blahdeblah")

mylocx = 0
mylocy = 0
myxandy = (mylocx, mylocy)
print ("you are standing at blah blah")
felixsword = False

locationstrue = [
    (-4, -4), (-3, -4), (-2, -4), (-1, -4), (0, -4), (1, -4), (2, -4), (3, -4),
    (-4, -3), (-1, -3), (1, -3),
    (-4, -2), (-3, -2), (-2, -2), (-1, -2), (1, -2), (3, -2), (4, -2),
    (-4, -1), (-2, -1), (1, -1), (2, -1), (3, -1),
    (-3, 0), (-2, 0), (-1, 0), (0, 0), (3, 0),
    (-2, 1), (0, 1), (2, 1), (3, 1), (4, 1),
    (-2, 2), (0, 2), (3, 2),
    (-3, 3), (-2, 3), (-1, 3), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
    (-4, 4), (-3, 4), (-1, 4), (1, 4), (3, 4)]
locationdict = {"lockbox": (-4, 0), "science lab": (-3, 0), "dark hallway": (-2, 0), "control room": (-1, 0),
                "main deck": (0, 0)}
myinventory = ["old book", "jug of water", "rusty key", "brass lamp"]
checker = myxandy in locationstrue


def help():
    print ("Valid commands in the game are: n,s,e,w - use lower case")


def loc():
    if myxandy == (-4, -4):
        print ("there is a giant waterfall here cascading into darkness")
    if myxandy == (-3, -4):
        print("you are in a room with a wet floor, you hear thundering water to the west, a door is on the south wall")
    if myxandy == (-2, -4):
        print("you are standing at -2,-4")
    if myxandy == (-1, -4):
        print("you are standing at -1, -4")
    if myxandy == (0, -4):
        print("you are standing at 0, -4")
    if myxandy == (1, -4):
        print("you are standing at 1,-4")
    if myxandy == (2, -4):
        print("you are standing at 2,-4")
    if myxandy == (3, -4):
        print("you are standing at 3,-4")

    if myxandy == (-4, -3):
        print("you are standing at -4,-3")
    if myxandy == (-1, -3):
        print("you are standing at -1, -3")
    if myxandy == (1, -3):
        print("you are standing at 1, -3")

    if myxandy == (-4, -2):
        print("you are standing at -4, -2")
    if myxandy == (-3, -2):
        print("you are standing at -3, -2")
    if myxandy == (-2, -2):
        print("you are standing at -2, -2")
    if myxandy == (-1, -2):
        print("you are standing at -1, -2")
    if myxandy == (1, -2):
        print("you are standing at 1, -2")
    if myxandy == (3, -2):
        print("you are standing at 3, -2")
    if myxandy == (4, -2):
        print("you are standing at 4, -2")

    if myxandy == (-4, -1):
        print("you are standing at -4, -1")
    if myxandy == (-2, -1):
        print("you are standing at -2, -1")
    if myxandy == (1, -1):
        print("you are standing at 1, -1")
    if myxandy == (2, -1):
        print("you are standing at 2, -1")
    if myxandy == (3, -1):
        print("you are standing at 3, -1")

    if myxandy == (-3, 0):
        print("you are standing at -3, 0")
    if myxandy == (-2, 0):
        print("you are standing at -2, 0")
    if myxandy == (-1, 0):
        print("you are standing at -1, 0")
    if myxandy == (0, 0):
        print("You are standing in a room with a door on the north wall and a door on the west.")
        print("There is a pocket knife here.")

    if myxandy == (1, 0):
        print("you are standing at 1, 0")
    if myxandy == (3, 0):
        print("you are standing at 3, 0")

    if myxandy == (-2, 1):
        print("you are standing at -2, 1")
    if myxandy == (0, 1):
        print("you are standing in a hallway that stretches out to the north and south")
    if myxandy == (2, 1):
        print("you are standing at 2, 1")
    if myxandy == (3, 1):
        print("you are standing at 3, 1")
    if myxandy == (4, 1):
        print("you are standing at 4, 1")

    if myxandy == (-2, 2):
        print("you are standing at -2, 2")
    if myxandy == (0, 2):
        print("you are standing in front of a door marked 'long hallway'")
    if myxandy == (3, 2):
        print("you are standing at 3, 2")

    if myxandy == (-3, 3):
        print("you are standing at -3,3")
    if myxandy == (-2, 3):
        print("you are standing at -2,3")
    if myxandy == (-1, 3):
        print("you are in a room, there is a locked door on the north wall")
    if myxandy == (0, 3):
        print("you are standing at the intersection of hallways heading off to the west, east, and south")
    if myxandy == (1, 3):
        print("you are standing at 1,3")
    if myxandy == (2, 3):
        print("you are standing at 2,3")
    if myxandy == (3, 3):
        print("you are standing at 3,3")
    if myxandy == (4, 3):
        print("you are standing at 4,3")

    if myxandy == (-4, 4):
        print("you are standing at -4,4")
    if myxandy == (-3, 4):
        print("you are standing at -3,4")
    if myxandy == (-1, 4):
        print("you are standing at -1, 4")
    if myxandy == (1, 4):
        print("you are standing at 1,4")
    if myxandy == (3, 4):
        print("you are standing at 3,4")


while True:
    myans = input(" ")
    if myans == "w":
        mylocx = mylocx - 1
        myxandy = (mylocx, mylocy)
        checker = myxandy in locationstrue
        if checker == True:
            loc()
        if checker == False:
            mylocx = mylocx + 1
            myxandy = (mylocx, mylocy)
            print("you can't do that")
    elif myans == "e":
        mylocx = mylocx + 1
        myxandy = (mylocx, mylocy)
        checker = myxandy in locationstrue
        if checker == True:
            loc()
        if checker == False:
            mylocx = mylocx - 1
            myxandy = (mylocx, mylocy)

            print("you can't do that")
    elif myans == "n":
        mylocy = mylocy + 1
        myxandy = (mylocx, mylocy)
        checker = myxandy in locationstrue
        if checker == True:
            loc()
        if checker == False:
            mylocy = mylocy - 1
            myxandy = (mylocx, mylocy)
            print("you can't do that")
    elif myans == "s":
        mylocy = mylocy - 1
        myxandy = (mylocx, mylocy)
        checker = myxandy in locationstrue
        if checker == True:
            loc()
        if checker == False:
            mylocy = mylocy + 1
            myxandy = (mylocx, mylocy)
            print("you can't do that")
    elif myans == "h":
        help()
    elif myans == "take pocket knife":
        myinventory.append("pocket knife")
        print (myinventory)
    elif myans == "loc":
        loc()
    elif myans == "inv":
        print (myinventory)
    else:
        print ("Not a command, Please use a valid key, type 'h' for help")
