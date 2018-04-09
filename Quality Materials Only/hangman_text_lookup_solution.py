import csv

import numpy


def newGame():  # Only runs once when the program is kicked off
    drawHangman(0)  # the full hangman is drawn when guesses left hit 0.  So this draws the full hangman
    print('Welcome to Hangman\n')
    newGameParameters()  # Passing focus to the next function which determines the parameters for the game


def newGameParameters():  # This function will determine parameters for the game.  Number of guesses, and difficulty
    global totalPenaltyNumber  # This var will hold the number of penalties the user wants to play with
    global gameDifficulty  # this var will hold the difficulty level
    global dictionaryFile
    totalPenaltyNumber = 0
    gameDifficulty = ''
    while totalPenaltyNumber < 5 or totalPenaltyNumber > 10:  # will force the user to choose between 5 and 10.  if they choose anything else it will loop back
        totalPenaltyNumber = input('How many missed guesses will you allow yourself?\nYou can do 5 through 10.\n')
        if totalPenaltyNumber.isnumeric():  # check to ensure the user entered a number
            totalPenaltyNumber = int(
                totalPenaltyNumber)  # if it was a number, changes the var from a string to an integer (since all user input defaults to string)
        else:
            print(
                'That was not a number')  # if the input was not a number, sets the input back to 0 and loops back until they input between 5 and 10
            totalPenaltyNumber = 0
    while gameDifficulty != 'EASY' and gameDifficulty != 'MED' and gameDifficulty != 'HARD':  # using while loop so if user enters anything except easy, med, or hard, will loop back
        gameDifficulty = input('''How difficult would you like the game?
        EASY = 2-4 letters
        MED = 5-7 letters
        HARD = 8 or more letters
        ''').upper()
    if gameDifficulty == 'HARD':  # if user chose hard, then sets the dictionary file variable to the *hard.csv which has longer words in it
        dictionaryFile = 'dictionaryHard.csv'
    elif gameDifficulty == 'MED':  # if user chose med, then sets the dictionary file variable to the *med.csv which has words 5-7 letters long in it
        dictionaryFile = 'dictionaryMed.csv'
    else:
        dictionaryFile = 'dictionaryEasy.csv'  # if user chose easy, then sets the dictionary file variable to the *easy.csv which has words 3-4 letters long in it
    resetUserSession()  # moves focus to the resetUserSession function


def resetUserSession():  # This function sets the number of incorrect guesses left and sets the previously used list.  If a brand new game...
    global incorrectGuessesLeft  # then these are being set for the first time.  However, if the user chooses to play again and not reset...
    global previousUserInput  # their parameters, the restart comes here to reset these variables for another game
    incorrectGuessesLeft = totalPenaltyNumber  # sets the number of incorrect guesses to be the same as how many penalties the user stated in the parameter function
    previousUserInput = []  # set the previous user input to NULL.  If the first time through the game, then doing doing much other than declaring var as list
    getNewWord()  # sends focus to the function to get a new random word from the csv files


def getNewWord():  # this function chooses a new word from one of the csv files
    global chosenWord  # this variable will hold the word as just a string (ex: 'MUTANT')
    global chosenWordAsList  # this variable will hold the word as a list of letters (ex: ['M','U','T','A','N','T'])
    global wordAsListToShow  # this variable will hold the word as it shows onscreen during the guessing, starts as all underscores (ex:  ['_','_','_','_','_','_'] )
    global lengthOfWord  # this variable will hold the length of the word.  Useful to set up loops for the correct number of passes
    chosenWordAsList = []
    wordAsListToShow = []
    lengthOfWord = 0
    rowCount = 0
    wordList = []
    with open(dictionaryFile,
              'r') as inputFile:  # uses the dictionaryFile variable which is holding whichever csv was set by the difficulty parameter
        sourceDictionary = csv.reader(inputFile)
        for currentRow in sourceDictionary:  # loops through all the rows (each row is one word) in the csv file
            word = currentRow[0]  # says that the column we want is in position [0]
            wordList.append(
                word)  # wordList is a list variable.  As the for loop goes through each row and reads the word, it appends the word into the wordList variable
            rowCount = rowCount + 1  # this is getting a rowCount to use as a parameter for the random function
    randomChoice = numpy.random.randint(0,
                                        rowCount)  # chooses a random number between 0 and the number of rows in the csv file
    chosenWord = wordList[
        randomChoice]  # uses the random number to choose a index in the wordList list, essentially choosing a random word from the list
    lengthOfWord = len(chosenWord)  # puts the length of the word into a variable for use in future loops
    for letter in range(
            lengthOfWord):  # sets up a loop for the correct number of passes to create an underscore variable
        wordAsListToShow.append(
            '_')  # creates a variable that is will show an underscore for each letter in the chosen word
    print('Your word has been chosen\n\n')
    chosenWordAsList = list(chosenWord)  # creates a list variable that holds the word as a list
    '''
    Now holding the word in a variable - chosenWord  (ex:  'mutant' )
    the word as a list in a variable - chosenWordAsList  (ex:  ['M','U','T','A','N','T'] )
    the word to show (which has underscores) as a variable - wordAsListToShow   (ex:  ['_','_','_','_','_','_'] )
    '''
    # print(' '.join(chosenWordAsList))              #this prints out the word chosen for debugging purposes.  For a real game, comment this line so that the word does not print
    getUserInput()  # sends focus to the user input function


def getUserInput():  # this function handles the user input / guessing function
    global userInput
    print('You have', incorrectGuessesLeft,
          'guesses left')  # prints how many guesses they have left.  If a guess it correct, it does not detract from this number
    print('So far you have guessed the following:')
    print(' '.join(
        previousUserInput))  # prints all the letters they have guessed so far, first time through the function, nothing is printed
    print('\n')
    print(' '.join(wordAsListToShow))  # prints the underscored word
    userInput = input('choose a letter\n').upper()  # asks for a guess from the user
    checkForPreviousUse(userInput)  # sends focus to the function to check for previous user input


def checkForPreviousUse(
        userInput):  # this function adds all user guesses to a list to keep track of what they have guessed so far
    previousUseCount = 0  # resets the flag to 0
    for value in previousUserInput:  # loops through the list variable that is holding all previous user input
        if value == userInput:  # if the most recent user input is equal to any of the previous inputs...
            previousUseCount = 1  # sets the flag to 1
    if previousUseCount == 1:  # if the flag is 1 let the user know that they have entered this before...
        print('You have used that entry before, choose something else.\n')
        getUserInput()  # and ask for their input again by going  back to the user input function
    elif previousUseCount == 0:  # if the flag is 0, then they have not used this input before...
        previousUserInput.append(userInput)  # add this most recent input to the previous input list...
        testUserInput(userInput)  # move to the testing function


def testUserInput(
        userInput):  # this function tests whether the letter guessed in the input is in the word, or if they correctly guessed the whole word
    global incorrectGuessesLeft
    correctGuess = 0  # resets the guess flag to 0
    for letter in range(
            lengthOfWord):  # sets up a loop for the correct number of passes (the number of letters in the word)
        if userInput == chosenWordAsList[
            letter]:  # for each pass checks if the user input is equal to the value in the variable that is holding the word as a list
            correctGuess = 1  # if any of the letters match, sets the flag to 1
    if userInput == chosenWord:  # first check is if the input matches the word (this is the variable holding the actual string word, not the list)
        print('nice guess!')
        gameWon()  # if the strings match, go to the game won function
    elif correctGuess == 1:  # if any of the letters matched in the loop above, then the flag was set to 1, so this is indicates a correct guess
        substituteLetterForUnderscore()  # since the guess was correct, go to the function that will substitue letters for underscores
        print('Yes,', userInput, 'is in the word.')
        if chosenWordAsList == wordAsListToShow:  # if this last user input completed the word, so that the word list variable is equal to the underscore variable...
            print('that does it!')
            gameWon()  # go to the game won function
        getUserInput()  # after the correct guess has substituted letters, and the game is not yet won, go back to user input function for another guess
    elif correctGuess == 0:  # if the flag is 0, then the letter was not matched, so the guess was incorrect
        incorrectGuessesLeft = incorrectGuessesLeft - 1  # subtract 1 from the number of guesses the user has left
        drawHangman(
            incorrectGuessesLeft)  # go to the draw hangman function which will draw the appropriate text according to how many guesses are left
        print(userInput, 'not in word, incorrect guess.')
        if incorrectGuessesLeft == 0:  # check if the number of guesses is 0, if it is 0...
            gameLost()  # go to the game lost function
        getUserInput()  # if the game is not yet lost, go to the user input function to get another guess


def substituteLetterForUnderscore():  # this function runs if a letter was guessed correctly, so it will substite the letter for an underscore
    for letter in range(
            lengthOfWord):  # sets up the loop for the correct number of passes (the number of letters in the word)
        if userInput == chosenWordAsList[
            letter]:  # for each pass checks if the user input is equal to the value in the variable that is holding the word as a list
            del wordAsListToShow[
                letter]  # if the letter matches, then it deletes the underscore according to the index position in the list variable...
            wordAsListToShow.insert(letter,
                                    userInput)  # then inserts the letter into the index posiition it just deleted
    return


def gameWon():  # this function indicates that the game was won
    drawHangman(-1)
    print('Congratuations, you won the game')
    print('The word was', chosenWord)
    wantToPlayAgain()  # sends the user to the function that asks if they want to play again


def gameLost():  # this function indicates that the game was lost
    print('Oooo, sorry, you lost the game')
    print('The word was', chosenWord)
    wantToPlayAgain()  # sends the user to the function that asks if they want to play again


def wantToPlayAgain():  # function that runs after the game has been won or lost.  Asks if the user wants to play again
    playAgain = input('Do you wish to play again?\n YES or NO\n').upper()
    if playAgain == 'YES':  # if the user wants to play again..
        setNewGameParameters = input(
            'Do you wish to reset your game parameters?\n Number of incorrect guesses and difficulty?\n YES or NO\n').upper()
        if setNewGameParameters == 'YES':  # asks if they want to reset their parameters (number of guesses, easy/med/hard)
            newGameParameters()  # if they do, it sends focus back to the newGameParameters function
        else:
            resetUserSession()  # if they do not, focus is sent to reset their session variables (number of guesses left, letters previously used)
    elif playAgain == 'NO':  # if the user does not want to play again, exits the program
        print('Thanks for playing')
        exit()
    else:
        print(
            'Command not recognized')  # if the user enters anything except YES or NO, will continue to loop them until they answer correctly
        wantToPlayAgain()


def drawHangman(
        incorrectGuessesLeft):  # this function draws the hangman according to how many guesses are left in the game
    if incorrectGuessesLeft == -1:  # not possible to get -1 incorrect guesses, just used to print a winning game picture
        print('''
           ===========
           ||/       
           ||     ________
           ||    |_ WOOT!_|     
           ||       |/
           ||      ()
           ||      \|/
           ||       |
           ||      / 
        ,,,||,,,,,,,,,,,,,,
        ''')
    elif incorrectGuessesLeft == 0:  # if 0 guess are left in the game, then the game is over, this is the full picture
        print('''
           ===========
           ||/       |
           ||       ()
           ||       \|/
           ||        |
           ||      ,/ \,
           ||
           ||
           ||
        ,,,||,,,,,,,,,,,,,,
        ''')
    elif incorrectGuessesLeft == 1:
        print('''
           ||/       |
           ||       ()
           ||       \|/
           ||        |
           ||      ,/ \,
           ||
           ||
           ||
        ,,,||,,,,,,,,,,,,,,
        ''')
    elif incorrectGuessesLeft == 2:
        print('''
           ||       ()
           ||       \|/
           ||        |
           ||      ,/ \,
           ||
           ||
           ||
        ,,,||,,,,,,,,,,,,,,
        ''')
    elif incorrectGuessesLeft == 3:
        print('''
           ||       \|/
           ||        |
           ||      ,/ \,
           ||
           ||
           ||
        ,,,||,,,,,,,,,,,,,,
        ''')
    elif incorrectGuessesLeft == 4:
        print('''
           ||        |
           ||      ,/ \,
           ||
           ||
           ||
        ,,,||,,,,,,,,,,,,,,
        ''')
    elif incorrectGuessesLeft == 5:
        print('''
           ||      ,/ \,
           ||
           ||
           ||
        ,,,||,,,,,,,,,,,,,,
        ''')
    elif incorrectGuessesLeft == 6:
        print('''
           ||
           ||
           ||
        ,,,||,,,,,,,,,,,,,,
        ''')
    elif incorrectGuessesLeft == 7:
        print('''
           ||
           ||
        ,,,||,,,,,,,,,,,,,,
        ''')
    elif incorrectGuessesLeft == 8:
        print('''
           ||
        ,,,||,,,,,,,,,,,,,,
        ''')
    elif incorrectGuessesLeft == 9:
        print('''
           ,,,||,,,,,,,,,,,,,,
           ''')
    return  # returns focus back to wherever it came from


newGame()
