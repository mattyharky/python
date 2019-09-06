import os
import re
import sys
import pyautogui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        width, height = pyautogui.size()
        self.title = "IP Calculator"
        self.width = int(width) - 200
        self.height = int(height) - 200
        self.left = (int(width) / 2) - (self.width / 2)
        self.top = (int(height) / 2) - (self.height / 2)
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.labelIP = QLabel(self)
        self.labelIP.setText("Enter IP Address")
        self.labelIP.move(10, 10)
        self.editIP = QLineEdit(self)
        self.editIP.setMaxLength(15)
        self.editIP.setFixedWidth(200)
        self.editIP.move(150, 10)
        self.buttonCalculate = QPushButton(self)
        self.buttonCalculate.setText("Calculate")
        self.buttonCalculate.move(10,60)
        self.buttonCalculate.clicked.connect(self.buttonCalculateClicked)
        self.labelAnswer1 = QLabel(self)
        self.labelAnswer1.setText("Enter an IP Address and click Calculate")
        self.labelAnswer1.move(10, 120)
        self.labelAnswer1.setFixedWidth(300)
        self.labelAnswer1.height = 300
        self.labelAnswer1.setGeometry(10, 100, 300, 300)
        self.labelAnswer2 = QLabel(self)
        self.labelAnswer2.setText("")
        self.labelAnswer2.move(200, 120)
        self.labelAnswer2.setFixedWidth(300)
        self.labelAnswer2.height = 300
        self.labelAnswer2.setGeometry(200, 100, 300, 300)
        self.show()
        
    #@pyqtSlot()
    def buttonCalculateClicked(self):
        processIPAddress(self.editIP.text(), self)
    

    

#Display all of the results from the conversions
def displayResults(sIP1, sIP2, sIP3, sIP4, hIP1, hIP2, hIP3, hIP4, bIP1, bIP2, bIP3, bIP4, self):
    self.labelAnswer1.setText("Denary IP address\nDenary Broadcast\nDenary Subnet mask\nHexadecimal IP address\nHexadecimal Broadcast\nHexadecimal Subnet mask\nBinary IP address\nBinary Broadcast\nBinary Subnet mask")
    self.labelAnswer2.setText(sIP1 + "." + sIP2 + "." + sIP3 + "." + sIP4)
    self.labelAnswer2.setText(self.labelAnswer2.text() + "\n" + sIP1 + "." + sIP2 + "." + sIP3 + "." + str(255))
    self.labelAnswer2.setText(self.labelAnswer2.text() + "\n"+ str(255) + "." + str(255) + "." + str(255) + "." + str(0))
    self.labelAnswer2.setText(self.labelAnswer2.text() + "\n"+ hIP1 + "." + hIP2 + "." + hIP3 + "." + hIP4)
    self.labelAnswer2.setText(self.labelAnswer2.text() + "\n"+ hIP1 + "." + hIP2 + "." + hIP3 + "." + format(int(255), "x"))
    self.labelAnswer2.setText(self.labelAnswer2.text() + "\n"+ format(int(255), "x") + "." + format(int(255), "x") + "." + format(int(255), "x") + "." + format(int(0), "x"))
    self.labelAnswer2.setText(self.labelAnswer2.text() + "\n"+ bIP1 + "." + bIP2 + "." + bIP3 + "." + bIP4)
    self.labelAnswer2.setText(self.labelAnswer2.text() + "\n"+ bIP1 + "." + bIP2 + "." + bIP3 + "." + format(int(255), "b"))
    self.labelAnswer2.setText(self.labelAnswer2.text() + "\n"+ format(int(255), "b") + "." + format(int(255), "b") + "." + format(int(255), "b") + "." + format(int(0), "b"))

#Process the IP address by checking for valid values and converting into hexadecimal and binary values    
def processIPAddress(sIPAddress, self):
    ipList = re.split("\.", sIPAddress)
    if(len(ipList) < 4 or len(ipList) > 4):
        self.labelAnswer.setText("Not an IP address, only 3 dots allowed")
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
                            displayResults(sIP1, sIP2, sIP3, sIP4, hIP1, hIP2, hIP3, hIP4, bIP1, bIP2, bIP3, bIP4, self)
                        else:
                            self.labelAnswer.setText("IP4 is not in range from 0 to 255")
                    else:
                        self.labelAnswer.setText("IP3 is not in range from 0 to 255")
                else:
                    self.labelAnswer.setText("IP2 is not in range from 0 to 255")
            else:
                self.labelAnswer.setText("IP1 is not class C network range from 192 to 223")
        except:
            self.labelAnswer.setText("Make sure you enter an IP address")
        
#Code starts here
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())


