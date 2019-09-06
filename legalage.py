"""
Legal age
    Get the age of the user using the keyboard
    If the age is less than 16
        Tell the user they cannot vote
    Else
        Tell the user they can vote
    If the age is less than 18
        Tell the user they cannot buy booze
    Else
        Tell the user they can buy booze
    If the age is greater than 99
        Tell the user that the Queen must have sent a birthday card to you
    Else
        Work out how many more years to wait for a birthday card from the Queen
        Show the user how many years to wait
"""
print("Enter your age")
try:
    iAge = int(input())
    if(iAge < 16):
        print("You cannot vote")
    else:
        print("You can vote")
    if(iAge < 18):
        print("You cannot buy booze")
    else:
        print("You can buy booze")
    if(iAge > 99):
        print("The Queen must have been sent you a birthday card")
    else:
        iYears = 100 - iAge
        print("You need to wait for " + str(iYears) + " years before the Queen sends you a birthday card")
except:
    print("You need to type in whole numbers for the age")



