print ("opening instructions")

firstorsecond = input("would you like to go first? Enter Y or N")
if firstorsecond == "Y":
    print ("I will go second")
else:
    print ("I will go first")

numberofpiecesleft = 23
print ("there are 23 pieces. You may take 1, or 2, or 3")
while True:
    playertake = int(input("how many pieces will you take?"))
    numberofpiecesleft = numberofpiecesleft - playertake
    print ("there are " + str(numberofpiecesleft) + " left")
    computertake = numberofpiecesleft % 4
    print("I will take " + str(computertake))
    numberofpiecesleft = numberofpiecesleft - computertake
    print ("there are " + str(numberofpiecesleft) + " left")
    if numberofpiecesleft == 0:
        print("I win")
        break
