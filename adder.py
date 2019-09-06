"""
Adder
    Get a whole 1st number using the keyboard
    Get a whole 2nd number using the keyboard
    Work out the sum of the numbers (add them)
    Show the sum of the numbers
"""
try:
    print("Enter 1st number")
    i1stNumber = int(input())
    print("Enter 2nd number")
    i2ndNumber = int(input())
    iSumOfNumbers = i1stNumber + i2ndNumber
    print("The sum of the numbers = " + str(iSumOfNumbers))
except:
    print("You need to type in whole numbers only")


