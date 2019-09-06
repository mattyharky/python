"""
Guess Random number
    Get a random number between 1 and 10
    Get a guess number using the keyboard
    If the guess number and random number are the same
        Let the user know they are correct
    Show the random number to the user
"""
import random
iRandomNumber = random.randint(1, 10)
print("Enter a guess number from 1 to 10")
try:
    iGuessNumber = int(input())
    if(iGuessNumber == iRandomNumber):
        print("you guessed correctly")
    else:
        print("The random number was " + str(iRandomNumber))
except:
    print("You need to enter a whole number")







