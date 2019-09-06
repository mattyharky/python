iNumber = 7
iNumberOfGuesses = 0
iEnded = 0
iScore = 0
iHighScore = 999
sContinue = "Y"
sScore = "Score: "
sHighScore = "High Score: "
while(sContinue.upper() == "Y"):
    #Need to add in a random number between 1 to 100
    iEnded = 0;
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
        
