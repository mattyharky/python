import os
import re
import sys
#from PyQt4 import QtGui
from PyQt5.QtWidgets import *

def showIPWindow():
    app = QApplication([])
    wid = QWidget()
    wid.setGeometry(100, 100, 400, 400)
    wid.setWindowTitle("IP Calculator")
    labelIP = QLabel(wid)
    labelIP.setText("Enter IP Address")
    labelIP.move(10, 10)
    editIP = QLineEdit(wid)
    editIP.setMaxLength(15)
    editIP.setFixedWidth(150)
    editIP.move(150, 10)
    editIP.textChanged.connect(editIPChanged)
    buttonCalculate = QPushButton(wid)
    buttonCalculate.setText("Calculate")
    buttonCalculate.move(10,60)
    buttonCalculate.clicked.connect(buttonCalculateClicked)
    wid.show()
    sys.exit(app.exec())

def editIPChanged():
    print("changed")
    print(wid.editIP.text())
    
def buttonCalculateClicked():
    print("clicked")
    #sIPAddress = wid.editIP.text()
    

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
def processIPAddress(sIPAddress):
    ipList = re.split("\.", sIPAddress)
    if(len(ipList) < 4 or len(ipList) > 4):
        print("Not an IP address, only 3 dots allowed")
    else:
        sIP1 = ipList[0]
        sIP2 = ipList[1]
        sIP3 = ipList[2]
        sIP4 = ipList[3]
        try:
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
        except:
            print("Make sure you enter an IP address")
        
#Code starts here
            """
os.system("clear")
if(len(sys.argv) == 2):
    sIPAddress = str(sys.argv[1])
    processIPAddress(sIPAddress)
else:
    print("A single IP address is expected")
"""

if __name__ == '__main__':
    showIPWindow()


