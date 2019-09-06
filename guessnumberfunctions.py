#Random numbers need this
import random

iNumber = 0
iNumberOfGuesses = 0
iEnded = 0
sContinue = "Y"
while(sContinue.upper() == "Y"):
    iScore = 0
    iHighScore = 999
    sScore = "Score: "
    sHighScore = "High Score: "
    random.seed()                       #Seed a random number
    iNumber = random.randint(1, 100)    #between 1 and 100 inc
    print(iNumber)                      #show it to cheat
    iEnded = 0;
    iNumberOfGuesses = 0
    sHighScore = "High Score: "
    while(iEnded == 0):
        print("Enter your guess")
        sGuess = input()
        iNumberOfGuesses += 1
        iGuess = int(sGuess)
        if(iGuess == iNumber):
            print("You guessed correctly")
            print("It took you " + str(iNumberOfGuesses) + " guesses.")
            for iScore in range(iNumberOfGuesses):
                sScore = sScore + "*"
            iEnded = 1
            if(iNumberOfGuesses < iHighScore):
                iHighScore = iNumberOfGuesses
                print("high score " + str(iHighScore))
            for iScore in range(iHighScore):
                sHighScore = sHighScore + "*"
            print(sScore)
            print(sHighScore)
            print("Do you want to continue? Y or N only")
            sContinue = input()
        if(iGuess > iNumber):
            print("Too high")
        if(iGuess < iNumber):
            print("Too low")
        
