#This is where Matty Harkin maintains his python code for teaching purposes.
#This is a single line comment.
#The hash tag symbol is used to show the start of the comment.
#Any text to the right of the hash symbol is the comment.
#People use comments in code to inform the reader
#An example comment could be:
#Created by Matty Harkin 5th September 2019
"""
Any line that has three sets of double quote marks on it is the start
of a multi-line comment.
You can type in what ever you like and each line will be treated as a comment.
The multi-line comment ends when another set of three double quote marks are typed.
"""
#A variable is a place in computer memory that can hold and remember information
#Your brain's memory has variables as well
#Examples are your name, your age, your address
#Below are examples of variables in a computers memory
sMyForename = "Matthew"
sMySurname = "Harkin"
sMyNickname = "Matty"
sMyGamerTag = "Glassjaw"
#All of these variables have a small s at the start.
#This means they hold strings of text.
#Notice that all of the text after "  contain strings of text data
sMyAddress = "10 Main Street, Dumfries, DG2 7PR"
#The example above has lots of string of text data
#You are allowed to mix numbers with text but cannot do arithmetic on this
iAge = 49
iYearBorn = 1969
iThisYear = 2019
#All of these variables have a small i at the start.
#This means they hold integers which are also called whole numbers.
#No variable starting with an i can hold a decimal point
fThePrice = 2.99
fMyShoeSize = 11.5
#All of these variables have a small f at the start.
#This smeans they hold floating point numbers which are numbers with a decimal.
#No variables starting with an f can be just a whole number.
#They must have a decimal point.
print("Hello")
#The print command sends information to the screen.
#In our example we need print().
#Anything between ( and ) are sent to to the screen.
#So print("Hello") sends a string of text "Hello" to the screen.
print("My name is Matty")
#This example sends another string of text - in this case a sentence to the screen
print("I am 49 years old")
#This example sends another string of text, it even includes numbers BUT it is treated as string
print("My name is Matty\nI am 49 years old")
#This example has \n which means take a new line so the text will appear on two lines
print(sMyForename)
print(sMySurname)
print(sMyForename + sMySurname)
print(sMyForename + " " + sMySurname)
#The print commands look for the variables in memory and prints the contents
#The + sign allows you to print more than one thing at a time
#The + " " + places a space between the variables to show Matthew Harkin
print("My name is " + sMyForename + " " + sMySurname)
print(sMyGamerTag + " is my gamertag")

#Printing number does not work so you have to enclose them with str()
print("I am " + str(iAge) + " years old")
print("I was born in " + str(iYearBorn) + " and my shoe size is " + str(fMyShoeSize) + " UK")

#You can do arithmetic in code
#+ is to add
#- is to subtract
#* is to multiply
#/ is to divide
#% is to do modulus or remainder
#() anything within these are worked out first
#BDMAS is used Brackets, Division, Multiplication, Addition, Subtraction
iTotal = 0 + 1 + 2 + 3 + 4 + 5
print(iTotal)
iTotal = 20 + 20
print(iTotal)
iTotal = 100 - 10 - 5
print(iTotal)
iTotal = 20 + 20 - 10
print(iTotal)
iTotal = iTotal * 2
print(iTotal)
iTotal = iTotal / 10
print(iTotal)
iTotal = 100 / 9
print(iTotal)
#The value is suddenly floating point
iTotal = int(iTotal)
#The int() command turns a floating point into an integer
print(iTotal)
iTotal = 100 % 9
print(iTotal)
#Here the remainder of 100 / 9 is shown
iTotal = int((20 - 10) + ((20 / 5) * 2))
print(iTotal)
#As you can see we can do complex looking arithmetic
fAppleCost = 0.55
fPearCost = 0.60
fFruitCost = fAppleCost + fPearCost
print("The fruit cost £" + str(fFruitCost))
#This example uses arithmetic by adding two variables

