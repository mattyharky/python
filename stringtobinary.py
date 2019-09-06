print("Enter a string of text to convert to binary")
sString = input()
print("As individual characters to binary")
for loop in sString:
    print(format(ord(loop), "b") + " = " + loop)
bString = ""
print("As a single binary representation")
for loop in sString:
    bString = bString + format(ord(loop), "b")
print (bString)

