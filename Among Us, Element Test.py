import random

print("Hello, Welcome to Among Us")
print("Text Edition")

characters_list = ["Meg", "James", "Beth", "Heather", "Marian", "George", "Martin", "Joanne"]
character = random.choice(characters_list)
murderer = random.choice(characters_list)


# Remove murdered character from characters_list
characters_list.remove(character)

print("the remaining characters are", characters_list,"!")
      
