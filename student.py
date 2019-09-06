"""
Student
    Set the number of males in the class
    Set the number of females in the class
    Set the average age of males in the class
    Set the average age of females in the class
    Set the maximum age in the class
    Set the minimum age in the class
    Work out how many people are in the class
    Work out the difference between the maximum and minimum age in the class
    Work out the difference between the number of males and females in the class
    Show how many people are in the class
    Show the difference between the maxium and minimum age in the class
    Show the difference between the number of males and females in the class
"""
iNumberOfMales = 9
iNumberOfFemales = 2
iAverageAgeOfMales = (17 + 16 + 18 + 20 + 22 + 37 + 17 + 16 + 26) / iNumberOfMales
iAverageAgeOfFemales = (17 + 32) / iNumberOfFemales
iMaximumAge = 37
iMinimumAge = 16
iNumberOfPeople= iNumberOfMales + iNumberOfFemales
iAgeDifference = iMaximumAge - iMinimumAge
iMaleToFemaleDifference = iNumberOfMales - iNumberOfFemales
print("The number of people in the class are " + str(iNumberOfPeople))
print("The difference between " + str(iMaximumAge) + " max age and " + str(iMinimumAge) + " min age is " + str(iAgeDifference))
print("The difference in numbers between " + str(iNumberOfMales) + " males and " + str(iNumberOfFemales) + " females is " + str(iMaleToFemaleDifference))


