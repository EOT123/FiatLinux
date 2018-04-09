'''how can you make a list and have your code check the list for an item and report if it 
is there or not'''

xpos = 0
ypos = 0
print("Welcome to the simple map game - use N,S,E, and W to move")
while True:
    if xpos == 0 and ypos == 0:
        print("You are standing at the end of a long road")
    if xpos == 1 and ypos == 0:
        print("You are heading West down a road, ahead in the distance there is a house")
    if xpos == 2 and ypos == 0:
        print("You are standing in front of a big house")
    if xpos == 3 and ypos == 0:
        print("You force the door open and you can see only darkness ahead")
    if xpos == 4 and ypos == 0:
        print("You are standing in darkness, the light of outside is behind you")
    if xpos == 5 and ypos == 0:
        print("You are paralyzed with fear and cannot go on without light")
    mylatestmove = input("wHERE DO YOU WANT TO GO NOW")
    if mylatestmove == "W":
        xpos = xpos + 1
    if mylatestmove == "w":
        xpos = xpos + 1
    if mylatestmove == "E":
        xpos = xpos - 1
    if mylatestmove == "e":
        xpos = xpos - 1

    else:
        print("")
