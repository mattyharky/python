"""
Weather decision
    Get the state of the weather using the keyboard (good or bad only)
    If the weather is bad
        Stay at home
    If the weather is good
        Go for a walk
"""
print("What is the weather like? good or bad only")
sWeather = input().upper()
if sWeather == "BAD":
    print("I am staying at home")
if sWeather == "GOOD":
    print("I am going for a walk")




