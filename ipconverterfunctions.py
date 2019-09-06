import os


#Get each IP address octet using the keyboard
def getIP(whichip):
    print("Enter IP " + whichip)
    sIP = input()
    return sIP


#Display all of the results from the conversions
def displayResults(sIP1, sIP2, sIP3, sIP4, hIP1, hIP2, hIP3, hIP4, bIP1, bIP2, bIP3, bIP4):
    os.system("clear")
    print("IP ADDRESS CONVERTER\n")
    print("Denary IP address      :" + sIP1 + "." + sIP2 + "." + sIP3 + "." + sIP4)
    print("Denary Broadcast       :" + sIP1 + "." + sIP2 + "." + sIP3 + "." + str(255))
    print("Denary Subnet mask     :" + str(255) + "." + str(255) + "." + str(255) + "." + str(0))
    print("Hexadecimal IP address :" + hIP1 + "." + hIP2 + "." + hIP3 + "." + hIP4)
    print("Hexadecimal Broadcast  :" + hIP1 + "." + hIP2 + "." + hIP3 + "." + format(int(255), "x"))
    print("Hexadecimal Subnet mask:" + format(int(255), "x") + "." + format(int(255), "x") + "." + format(int(255), "x") + "." + format(int(0), "x"))
    print("Binary IP address      :" + bIP1 + "." + bIP2 + "." + bIP3 + "." + hIP4)
    print("Binary Broadcast       :" + bIP1 + "." + bIP2 + "." + bIP3 + "." + format(int(255), "b"))
    print("Binary Subnet mask     :" + format(int(255), "b") + "." + format(int(255), "b") + "." + format(int(255), "b") + "." + format(int(0), "b"))


#Process the IP address by checking for valid values and converting into hexadecimal and binary values    
def processAddress(sIP1, sIP2, sIP3, sIP4):
    #192 to 223
    if(int(sIP1) > 191 and int(sIP1) < 224):
        #0 to 255
        if(int(sIP2) > -1 and int(sIP2) < 256):
            #0 to 255
            if(int(sIP3) > -1 and int(sIP3) < 256):
                if(int(sIP4) > -1 and int(sIP4) < 256):
                    hIP1 = format(int(sIP1), "x")
                    hIP2 = format(int(sIP2), "x")
                    hIP3 = format(int(sIP3), "x")
                    hIP4 = format(int(sIP4), "x")
                    bIP1 = format(int(sIP1), "b")
                    bIP2 = format(int(sIP2), "b")
                    bIP3 = format(int(sIP3), "b")
                    bIP4 = format(int(sIP4), "b")
                    displayResults(sIP1, sIP2, sIP3, sIP4, hIP1, hIP2, hIP3, hIP4, bIP1, bIP2, bIP3, bIP4)
                else:
                    print("IP4 is not in range from 0 to 255")
            else:
                print("IP3 is not in range from 0 to 255")
        else:
            print("IP2 is not in range from 0 to 255")
    else:
        print("IP1 is not class C network range from 192 to 223")


#Code starts here
os.system("clear")
sIP1 = getIP("1")
sIP2 = getIP("2")
sIP3 = getIP("3")
sIP4 = getIP("4")
processAddress(sIP1, sIP2, sIP3, sIP4)
