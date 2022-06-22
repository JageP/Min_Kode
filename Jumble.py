# Create a jumbled word
# Jumble is an empty string

import random

WORDS = ("cheese", "monkey", "fart", "goblin", "xylophone")
word = random.choice(WORDS)

correct = word

# WORDS is assigned to a list.
# word is a variable which gets assigned a value by the random module.

jumble = ""

# Jumble is an empty string

position = random.randrange(len(word))

# position is an number taken from the range of the length of the word

jumble += word[position]

# jumble gets a letter from a random position in the chosen word

# word = word[:position] + word[(position + 1):]

# Start Game

word = word[:position] + word[(position + 1):]

# word is a variable which constantly changes, it begins as a selection from
# WORDS, e.g Cheese, jumble gets the letter assigned to position, which means
# if the letter selected from cheese is S then jumble is equal to S and word
# becomes Cheee.

print("Welcome to Word Jumble")

print("The word is:", jumble)

guess = input("Take a guess")

while guess != correct and guess != "":
    print("Sorry that's not it.")
    position = random.randrange(len(word))
    jumble += word[position]
    print("The word is:", jumble)
    guess = input ("Your guess: ")

# When the user guesses the word and their guess is incorrect the the code
# pulls another letter from position in word and word loses another letter
# so in the example from earlier jumble would gain another letter and become
# SC and word would then be HEEE, this would then loop with every failed attempt
# until the jumble would be SEEHCE for example and the word would have no value.

if guess == correct:
        print("That's it! You guessed it!\n")

print("Thanks for playing.")

input("\n\n Press the Enter key to exit.")
