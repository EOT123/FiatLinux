print("--------------------------------------------")
print("           Welcome to blahdeblah")
print("--------------------------------------------")

mylocx = 0
mylocy = 0
myxandy = (mylocx, mylocy)
print("you are standing at blah blah")
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
    print("Valid commands in the game are: n,s,e,w - use lower case")


def loc():
    pass


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
        print(myinventory)
    elif myans == "loc":
        loc()
    elif myans == "inv":
        print(myinventory)
    else:
        print("Not a command, Please use a valid key, type 'h' for help")
