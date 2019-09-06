"""
Sum of five
    Set sum of number to zero
    Do the following 5 times
        Get a number using the keyboard
        Add the number to a sum of number
    Show the sum of the numbers to the user
"""
fSum = 0.0
for loop in range(1, 6): #1 to 5
    try:
        print("Enter a number")
        fNumber = int(input())
        fSum = fSum + fNumber
    except:
        print("You need to type in numbers so one less!")
print("The sum of numbers = " + str(fSum))






