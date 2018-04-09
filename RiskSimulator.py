import random

playerfunds = 100

print("-----------------------------------------")
print("      Gambling and Risk Simulation")
print("-----------------------------------------")
print("you will start off with 100 dollars.")
print ("you will roll two dice and you can bet any amount you want and choose your bet")

print ("rolling a 7 gives you seven dollars")
print ("rolling doubles, doubles your bet")
print ("everything else costs you 2 bucks")

while True:
    print('You have ${}'.format(playerfunds))
    betamount = int(input('how much would you like to bet?'))
    print('you bet {}'.format(betamount))
    randomroll01 = random.randrange(1, 6)
    randomroll02 = random.randrange(1, 6)
    randrolltot = randomroll01 + randomroll02
    print ('you rolled a {} and a {} totalling {}'.format(randomroll01, randomroll02, randrolltot))
    if randomroll01 == randomroll02:
        playerfunds = playerfunds + (betamount * 2)
    elif randrolltot == 7:
        playerfunds = playerfunds + betamount + 7

    else:
        playerfunds = playerfunds - 2 - betamount
