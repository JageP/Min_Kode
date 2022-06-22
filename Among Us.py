import random

print("Hello, Welcome to Basic Among Us")

characters_list = ["Meg", "James", "Beth", "Heather", "Marian", "George", "Martin", "Joanne"]
character = random.choice(characters_list)
murderer = random.choice(characters_list)
victims_list = []
murderer_list = []

murderer_list.append(murderer)
characters_list.remove(murderer)

characters_list_1 = characters_list + murderer_list

##print("The Murderer is...", murderer, "and this code works")
    ## This code has selected a murderer at random from the characters list

print("The characters in this game are...", characters_list_1,"!")

print("The Murderer has killed", character,"this round")

    ##MAKE SURE YOU CHECK BRACKETS!

    ##Remove murdered character from characters_list

victims_list.append(character)
characters_list.remove(character)


print("the remaining characters are", characters_list_1,"!\nThose who have died are", victims_list)


guess = input("Please guess who the murderer is! Using capitalisation where appropriate\n")

while guess not in characters_list_1:
    print("This person is not in the list, use Capitization as appropriate")
    guess = input("Guess who the Murderer is:\n")

characters_list_1.remove(guess)
victims_list.append(guess)



print("Your guess of", guess, "was taken outside and killed on your orders! Let's hope you're right")

if murderer in victims_list:
    print("Congratulations, you killed the murderer!")
else:
    print("Nope, you just killed an innocent person!")
    print("Remaining are", characters_list_1, "!")
    print("So far these people have killed", victims_list, "!")
    guess = input("Who else could it be?")
    if guess is not murderer:
        print("No! You killed another innocent! Guess again!")
        characters_list_1.remove(guess)
        victims_list.append(guess)
        print("So far", victims_list, "have been killed")
        guess = input("Who could it be?!")

# Always the last person on the list
# Characters can die twice for some reason
# Suicide is an option for the murderer
        
