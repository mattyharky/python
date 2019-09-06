import platform
import datetime
import re
import os
import shutil

#user defined functions
def doubler(no):
    print("Doubler")
    no = no * 2
    return no


#A single line comment
"""
Multiline comments
"""
age = 21 #int
Age = 22.22 #float
print("Age calculator")
print(age)
print(Age)
Age = "hi and welcome  " #str
print(Age)
joined = age + 50
print(joined)
print (type(joined))
print(Age + " " + str(joined))
print(Age[0] + Age[3] + " " + Age[0:4]) #0 to 3
print(Age.strip()) #removes whitespace at edges
print(len(Age))
print(Age.lower())
print(Age.upper())
print(Age.replace("h","Y"))
print(Age.replace("Yi","Pi"))
print(Age.split(" "))
print("Enter your age")
a = input()
#print str(a) + " is a good age to be"
if int(a) == 21:
    print ("your 21")
elif int(a) > 21:
    print ("Your 22 or more")
else:
    print ("your not 21")
towns = ["Dumfries", "Annan", "Gretna"]
#this is called a list but is an array
print (towns)
print(len(towns))
#raw_input ("Press\nANY KEY")
a, b, c = 1, 2, 3
print (a + b + c)
del a # cant dp this now print a
print (towns[0])
print (towns[0][2:])
print (towns[0]*3)
print (towns[0:3][3:])
#dictionary its like a database
d = {"name1": "matty", "age1": 21, "name2": "jimmy", "age2": 24}
dd = {}
dd["name1"] = "mark"
dd["name2"] = "jake"
print (d)
print (dd)
print (d["name2"])
print (dd.keys())
print (dd.values())
no = 20
c = chr(no) #convert integer to character
print (c)
#cc = unichr(no)
#print (cc)
print (hex(no))
print (oct(no))
c = "A"
no = ord(c)
print (no)
a = 7
b = 2
c = a // b
print (c)
c = a % b
print (c)
c = 5 ** 2 #to the power of 2
print (c)
a = 7.6
print (abs(a))
#print (ceil(a)) # ceil not defined
#print floor(a) #floor not defined
print (max(10, 13, 9, 7))
print (min(10, 13, 9, 7))
print (pow(4,2))
#print sqrt(99) sqrt not defined
#print choice(towns) #random from a list not def
#print choice(dd) #random from a dict not def
#print random() not def
#print randrange(1, 100, 1) not def
count = 0
for loop in "Matty":
    count += 1
    print(loop + str(count))
ages = [20,30,40,50,60,70,80]
for loop in ages:
    print(loop)
for loop in range(10): #0 to 9
    print (loop)
for loop in range(1, 11): #1 to 10
    print (loop)
number = 7    
print(doubler(number))
newnumber = doubler(number)
print("The new number is " + str(newnumber))
towns.append("Glasgow")
print(towns)
towns.remove("Annan")
print(towns)
towns.pop(1)
print(towns)
towns.append("Annan")
towns.append("Grenta")
#print(index("Annan"))
towns.sort()
print(towns)
#classes and objects
class student:
    surname = "undefined"
    forename = "undefined"
    course = "undefined"

class person:
        def __init__(self, surname, forename, course, passed):
            self.surname = surname
            self.forename = forename
            self.course = course
            self.passed = passed
        def completed(self):
            self.passed = "YES"
        def status(self):
            print(self.course + " - " + self.forename[0].upper() + " " + self.surname.upper() + " COMPLETE? " + self.passed)
print(student)
student1 = student
student1.surname = "Harkin"
student1.forename = "Matty"
student1.course = "STAFF"
print(student1.forename + " " + student1.surname + " " + student1.course)

person1 = person("Bloggs", "Joe", "SCCP", "NO")
print(person1.course + " - " + person1.forename[0].upper() + " " + person1.surname.upper() + " COMPLETE? " + person1.passed)
person1.completed()
print(person1.course + " - " + person1.forename[0].upper() + " " + person1.surname.upper() + " COMPLETE? " + person1.passed)
person2 = person("Doe", "Jane", "NCMP", "YES")
person2.status()
townsiter = iter(towns)
print(next(townsiter)) #is this useful?
myplatform = platform.system()
print (myplatform)
allnames = dir(myplatform)
print (allnames)
alldate = datetime.datetime.now()
print(alldate)
print("The year is " + str(alldate.year))
print("The day is " + str(alldate.day))
print("The month is " + str(alldate.month))
zero = ""
if ((alldate.minute) < 10):
    zero = "0"
print("The time is " + str(alldate.hour) + ":" + zero + str(alldate.minute) + alldate.strftime("%p") + " " + alldate.strftime("%A %B"))
fullname = "Matty Harkin Da Boss"
findspace = re.search("\s", fullname)
print("space is located at " + str(findspace.start()))
splitspaces = re.split("\s", fullname)
print(splitspaces)
splitspaces = re.split("\s", fullname, 2)
print(splitspaces)
replacetext = re.sub("a", "@", fullname)
print(replacetext)
anumber = 76
try:
    print("The value is " + 76)
except:
    print("Error")
filename = "myfile"
myfile = open(filename, "w") #a is append w is write
myfile.write(str(towns))
myfile.close()
myfile = open("myfile", "a") #a is append w is write
myfile.write(person1.forename + ",")
myfile.write(person1.surname + ",")
myfile.write(person1.course + ",")
myfile.close()
myfile = open("myfile", "r") #read
print(myfile.read())
myfile.close()
os.remove(filename)
if os.path.exists(filename):
    print("file exists")
else:
    print("file does not exist")
#os.mkdir("myfolder")
#os.rmdir("myfolder") butits it is empty
print(os.getcwd())
print(os.get_exec_path())
print(os.getegid())
print(os.geteuid())
print(os.getgroups())
print(os.getlogin())
print(os.getpid())
print(os.getuid())
print(os.uname())
print(os.uname().sysname)
print(os.uname().nodename)
print(os.uname().release)
print(os.uname().version)
print(os.uname().machine)
print(os.get_terminal_size())
print(os.get_terminal_size().columns)
print(os.get_terminal_size().lines)
print(os.listdir(os.getcwd()))
print(os.getcwd() + "/")
whatsinthedir = os.listdir(os.getcwd())
for loop in whatsinthedir:
    print(loop)
for loop in whatsinthedir:
    if os.path.isfile(loop):
        print(loop + " is a file")
    else:
        print(loop + " is a folder")
        os.rename(loop, loop + "-renamed")
        shutil.rmtree(loop + "-renamed")
        print(loop + "-renamed has been deleted")
os.system("ls -la")
print(os.cpu_count())















    














