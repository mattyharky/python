"""
Guess Random number
    Get a random number between 1 and 10
    While the guess number is not equal to the random number
        Get a guess number using the keyboard
        If the guess number and random number are the same
            Let the user know they are correct
        Show the random number to the user
"""
import random
iNumberOfGuesses = 0
iGuessNumber = 11
iRandomNumber = random.randint(1, 10)
while (iRandomNumber != iGuessNumber):
    print("Enter a guess number from 1 to 10")
    try:
        iGuessNumber = int(input())
        iNumberOfGuesses += 1
        if(iGuessNumber == iRandomNumber):
            print("you guessed correctly")
    except:
        print("You need to enter a whole number")
print("The random number was " + str(iRandomNumber))
print("It took you " + str(iNumberOfGuesses) + " guesses to get it correct")







