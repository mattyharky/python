"""
Weather if decision
    Get the type of weather using the keyboard (raining, sunny, frosty)
    If the weather is raining
        Tell the user to take an umbrella
    If the weather is sunny
        Tell the user to take some sunglasses
    If the weather is frosty
        Tell the user to take a scarf and gloves
"""
print("What type of weather today? (raining, sunny or frosty only)")
sWeather = input().lower()
if sWeather == "raining":
    print("Take an umbrella")
if sWeather == "sunny":
    print("Take some sunglasses")
if sWeather == "frosty":
    print("Take a scarf and gloves")




