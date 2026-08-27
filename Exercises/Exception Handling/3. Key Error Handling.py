# Exercise 3: Key Error Handling
# Problem Statement: Given a dictionary of country capitals, ask the user to enter a country name and print the corresponding capital. If the country is not in the dictionary, catch the KeyError and display a helpful message.
capitals = {"France": "Paris", "Japan": "Tokyo", "Brazil": "Brasilia"}
try:
    c = input("enter a country name: ")
    cap = capitals[c]
    print(f"{c}'s capital is : {cap}")
except KeyError:
    print(f"{c} not found in the dictionary")
