import random

characters_list = ["Meg", "James", "Beth", "Heather", "Marian", "George", "Martin", "Joanne"]
character = random.choice(characters_list)
murderer = random.choice(characters_list)
victims_list = []

print("The Murderer is...", murderer, "and this code works")
    ## This code has selected a murderer at random from the characters list

print("The characters in this game are...", characters_list,"!")

print("The Murderer", murderer, "has killed", character,"this round")

    ##MAKE SURE YOU CHECK BRACKETS!

    ##Remove murdered character from characters_list
victims_list.append(character)
characters_list.remove(character)


print("the remaining characters are", characters_list,"!\nThose who have died are", victims_list)


guess = input("Please guess who the murderer is! Using capitalisation where appropriate")

characters_list.remove(guess)

print("Your guess of", guess, "was taken outside and killed on your orders! Let's hope you're right")

if murderer not in characters_list:
    print("Congratulations, you killed that bitch!")
else:
    print("Nope, you just killed an innocent person!")
    print("Remaining are", characters_list, "!")
    guess = input("Who else could it be?")
        
