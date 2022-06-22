# Tuples
# What the fuck is a tuple?

# Create a tuple with some items and display with a for loop

inventory = ("Sword",
             "Armour",
             "Shield",
             "Cheese")

# Inventory is a tuple, it has many values, all indented.

print("Your Items:\n")
for item in inventory:
    print(item)

# Use singular and plural terms where necessary

# Get the length of a tuple

print("\nYou have", len(inventory), "items in your possession")

input("\nPress The Enter Key To Continue")

#To get the length of a tuple use len, make sure it's in the correct format.

# Testing whether a variable is present

if "Cheese" in inventory:
    print("\nYou just ate a fuckload of cheese.")

# Display one item through an index


############################################################################
#  index = int(input("\nEnter the index number for item in inventory: "))  #
#  print("At index", index, "is", inventory[index])                        #
############################################################################

# Displaying a slice, for whatever reason.

start = int(input("Enter the index number to begin a slice: "))
finish = int(input("Enter the index number to end a slice: "))
print("Inventory[", start, ":" , finish, "] is", end=" ")
print(inventory[start:finish])

# Q: Why do we use square brackets for this?

# You can splice strings in order to create a new sub-string, more on that
# Later, let's crack on with this shit.

# You can add tuples together and create a new value for a variable i.e Inventory
# By creating a new tuple with new values and using += (Concatenating)
