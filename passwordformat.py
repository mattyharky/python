"""
Password format
    Show the password rules and ask for a password
    Get a password using the keyboard
    Set valid values to False for all rules
    if the password does meet all of the rules
        Inform the user that the password is valid
    Else
        Inform the user that the password is invalid
"""
bValid = False
bLength = False
bUpper = False
bLower = False
bNumber = False
bSymbol = False
print("The password rules\n\n1. Length of 8 minimum\n2. Must contain at least one upper case letter\n3. Must contain at least one lower case letter\n4. Must contain at least one number\n5. Must contain at least one symbol")
#Get the password using the keyboard
sPassword = input()
if(len(sPassword) >= 8):
    bLength = True
else:
    bLength = False
#Check for an upper case
for loop in sPassword:
    if(loop.isupper() == True):
        bUpper = True
#Check for an lower case
for loop in sPassword:
    if(loop.islower() == True):
        bLower = True
#Check for a number
for loop in sPassword:
    try:
        number = int(loop)
        bNumber = True
    except:
        bNothing = False
#Check for a symbol
for loop in sPassword:
    iAscii = ord(loop)
    if(iAscii >= 123 and iAscii <= 126) or (iAscii >= 91 and iAscii <= 96) or (iAscii >= 58 and iAscii <= 64) or (iAscii >= 33 and iAscii <= 47):
        bSymbol = True
#Let the user know if the password format is valid or not
if(bValid == True and bLength == True and bUpper == True and bLower == True and bNumber == True and bSymbol = True):
    print("Valid password")
else:
    print("Invalid password")
