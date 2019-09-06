print("Enter a string of text to convert to hexadecimal")
sString = input()
print("As individual characters to hexadecimal")
for loop in sString:
    print(format(ord(loop), "x") + " = " + loop)
bString = ""
print("As a single hexadecimal representation")
for loop in sString:
    bString = bString + format(ord(loop), "x")
print (bString)

