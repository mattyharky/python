"""
Average of six
    Set sum of number to zero
    Do the following 5 times
        Get a number using the keyboard
        Add the number to a sum of number
    Work out the average by dividing sum by 6
    Show the average of the numbers to the user
"""
fSum = 0.0
for loop in range(1, 7): #1 to 6
    try:
        print("Enter a number")
        fNumber = int(input())
        fSum = fSum + fNumber
    except:
        print("You need to type in numbers so one less!")
fAverage = fSum / 6
print("The average of numbers = " + str(fAverage))







