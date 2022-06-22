#Number Guessing Game

print("Welcome to the number guessing game.")

#Use the fucking closed parenthesis you moron, James!

print("I am thinking of a number between 1 and 100.")
print("Try to guess in as few attempts as possible.")

#Import the module or it won't fucking work.

import random

#Setting Initial Variables

the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# Make sure there are as many parentheses at the back
# As there are at the front of the line.

# Guessing Loop

while guess != the_number:
    if guess > the_number:
        print("Lower...")

        guess = int(input("Take a guess: "))
        tries += 1
        
    else:
            print("Higher...")

            guess = int(input("Take a guess: "))
            tries += 1

    if tries == 5:
        print("Game Over Twat, Let's try again")
        the_number = random.randint(1, 100)
        guess = int(input("Take a guess: "))
        tries = 1
        
        

print ("Well Done You total and utter cockend, it only took you..", tries, "tries, moron.")

# Without guess = int(input("Take a guess: "))
# tries += 1
# Program will just spam higher.
# Ask for more input on both possible outcomes
# Then the loop resets because the conditions haven't
# been met, once they have the program prints the 'congratulations'
# Look more into how to print variables in the middle of a sentence.
