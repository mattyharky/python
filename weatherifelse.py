"""
Weather if else decision
    Get the type of weather using the keyboard (raining, sunny, frosty)
    If the weather is raining
        Tell the user to take an umbrella
    Else If the weather is sunny
        Tell the user to take some sunglasses
    Else If the weather is frosty
        Tell the user to take a scarf and gloves
    Else
        Tell the user they needed to type in raining or sunny or frosty
"""
print("What type of weather today? (raining, sunny or frosty only)")
sWeather = input().lower()
if sWeather == "raining":
    print("Take an umbrella")
elif sWeather == "sunny":
    print("Take some sunglasses")
elif sWeather == "frosty":
    print("Take a scarf and gloves")
else:
    print("You needed to type in either raining or sunny or frosty")




