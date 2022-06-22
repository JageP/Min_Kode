# Hangman Game

# Imports
import random

# Constants
HANGMAN = (
    """
1
    """,
    """
2
    """,
    """
3
    """,
    """
4
    """,
    """
5
    """,
    """
6
    """,
    """
7
    """)

MAX_WRONG = len(HANGMAN) - 1

WORDS = ("CHEESE", "MONKEY", "NIGEL", "FIAT", "BMW", "HUNDRED", "THOUSAND")

# Initialize Variables

word = random.choice(WORDS) # The word to be guessed

so_far = "-" * len(word) # One dash for each letter to be guessed

wrong = 0 # Number of wrong guesses player has made

used = []

print("Welcome to Hangman, Good Luck!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n\n", used)
    print("\nSo far, the word is:\n", so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess is used:
        print("You've already guessed the letter", guess)
        guess = input("Enter your Guess: ")
        guess = guess.upper

    used.append(guess)

    if guess in word:
        print("\nYes", guess, "is in the word.")

    # Create a new so_far to include guess

        new = ""

    for i in range(len(word)):
        if guess == word[i]:
            new += guess
        else:
            new += so_far[i]
    so_far = new

else:
    print("Sorry", guess, "Is not in word.")
    wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've now been hung!")

else:
    print("You guessed it.")

print("The word was", word)

input("Press any Key to Exit.")

# Known Bugs

# So far the code works, the HANGMAN variable does not progress through as it should, i.e the couning mechanism.
# Letter is not in word even if it was in the word but as the last guess

