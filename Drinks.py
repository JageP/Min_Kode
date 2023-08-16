# Drinks

drinks = ("WINE", "BEER", "VODKA", "HOT CHEESE")
name = input("\n\nWhat is your name?\n\n")
uppercase_name = name.upper()

print("\n\nHello", uppercase_name, "\n\n")

print(drinks)
answer = input("\n\nHere are a list of drinks we have available, would you like one?\n\n")
answer_uppercase = answer.upper()

if answer_uppercase == "YES":
    drink_selection = input("\n\nWhat would you like to drink?\n\n")
    drink_selection_UC = drink_selection.upper()
else:print("Fuck off.")


if drink_selection_UC in drinks:
    print("\n\nHere is your", drink_selection_UC, "don't let it dribble down your face!")
else:print("We don't serve THAT filth here, we do serve other filth though")
