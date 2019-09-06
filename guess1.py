iNumber = 7
print("Enter your guess ")
sGuess = input()
iGuess = int(sGuess)
if(iGuess == iNumber):
    print("You guessed correctly")
if(iGuess > iNumber):
    print("Too high")
if(iGuess < iNumber):
    print("Too low")
