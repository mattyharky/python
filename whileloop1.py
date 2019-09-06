sQuit = "no"
iAcumulate = 0
while sQuit != "yes":
    iAcumulate += 1
    print("Acumulate is at " + str(iAcumulate) + ".\nDo you want to quit? {yes or no}")
    sQuit = input().lower()
print("All done")    

