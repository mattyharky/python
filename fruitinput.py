"""
Fruit input
    Get the number of apples used using the keyboard
    Get the number of pears used using the keyboard
    Get the cost of an apple using the keyboard
    Get the cost of a pear using the keyboard
    Work out how much fruit was used
    Work out the cost of all the fruit
    Work out how many pounds
    Work out how many pence
    Show the amount of fruit used
    Show the cost of the fruit in pence
    Show the cost of the fruit in pounds and pence
"""
try:
    print("How many apples used?")
    iApples = int(input())
    print("How many pears used?")
    iPears = int(input())
    print("What is the cost of an apple?")
    iAppleCost = int(input())
    print("What is the cost of a pear?")
    iPearCost = int(input())
    iFruitUsed = iApples + iPears
    iFruitCost = (iApples * iAppleCost) + (iPears * iPearCost)
    iFruitPounds = int(iFruitCost / 100)
    iFruitPence = iFruitCost - (iFruitPounds * 100)
    print("I used " + str(iFruitUsed) + " pieces of fruit")
    print("The cost of all the fruit was " + str(iFruitCost) + " pence")
    print("which is £" + str(iFruitPounds) + "." + str(iFruitPence))
except:
    print("You need to type in whole numbers only")


