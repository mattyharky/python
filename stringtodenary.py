print("Enter a string of text to convert to denary")
sString = input()
print("As individual characters to denary")
for loop in sString:
    print(format(ord(loop), "d") + " = " + loop)
bString = ""
print("As a single denary representation")
for loop in sString:
    bString = bString + format(ord(loop), "d")
print (bString)

