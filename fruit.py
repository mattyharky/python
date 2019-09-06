"""
Fruit
    Set the number of apples used
    Set the number of pears used
    Set the cost of an apple
    Set the cost of a pear
    Work out how much fruit was used
    Work out the cost of all the fruit
    Work out how many pounds
    Work out how many pence
    Show the amount of fruit used
    Show the cost of the fruit in pence
    Show the cost of the fruit in pounds and pence
"""
iApples = 5
iPears = 7
iAppleCost = 45
iPearCost = 55
iFruitUsed = iApples + iPears
iFruitCost = (iApples * iAppleCost) + (iPears * iPearCost)
iFruitPounds = int(iFruitCost / 100)
iFruitPence = iFruitCost - (iFruitPounds * 100)
print("I used " + str(iFruitUsed) + " pieces of fruit")
print("The cost of all the fruit was " + str(iFruitCost) + " pence")
print("which is £" + str(iFruitPounds) + "." + str(iFruitPence))


