# Hero's Inventory
# Shows lists

#create a list with some items and display with a for loop

inventory = ["Axe", "Leather Armour", "Roundshield", "Supplies"]
print("Your Items:")
for item in inventory:
    print(item)

input("\nPress the enter key to continue.")

# Get the length of the list
print("You have", len(inventory), "items in your possession.")

input("\nPress the enter key to continue.")

# Test for membership with in

if "Supplies" in inventory:
    print("You live to fight another day.")
else:
    print("Game Over, You died.")

# Display a slice

start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("\nEnter the index number to end a slice: "))

print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

input("\nPress the enter key to continue")

# Concatenating Two Lists

chest = ["Gold", "Gems"]

print("You find a chest which contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to continue.")

# Assign by index

print("You trade your Leather Armour for a Crossbow.")
inventory[1] = "Crossbow"
print("Your inventory us now:")
print(inventory)

# Assign by slice number

print("You trade your Gold and Gems for an orb of future telling.")
inventory[4:6] = ["Orb of Future Telling"]
print("Your inventory is now:")
print(inventory)

input("\nPress the Enter key to continue.")

# Deleting an list element

print("In a great battle, you Roundshield is splintered and destroyed.")
del inventory[2]
print("Your inventory is now:")
print(inventory)

# Deleting a list slice

print("Your Crossbow and Axe are stolen by thieves.")
del inventory[:2]
print("Your inventory is now:")
print(inventory)
