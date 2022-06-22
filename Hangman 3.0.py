# Hangman Game 3.0 Bug Fixes

# I am currently experiencing a number of bugs.
# The hangman counter, 1, 2, 3, 4, does not cycle through with a wrong guess
# I now get unlimited guesses.
# When the word is guessed the last letter is AND is NOT in the word.

# Import
import random

# Here is the pictures which cycle through with each wrong guess, progressing
# 1 through 7.

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

# This is the maximum amount of turns you are allowed, it is equal to the length
# of the word minus 1.

WORDS = ("CHEESE", "MONKEY", "CAPITALISM", "DUCK", "FROMAGE", "CUNTS")

# Initializing Variables

word = random.choice(WORDS) # This function takes a word from the list above
# and sets the word to be guessed as well as the amount of guesses the user
# can make to find out what the word is.

so_far = "-" * len(word)# There is one dash for each letter in the word that is
# yet to be guessed.

wrong = 0 # This is the number of tries the player has made so far, beginning with 0.

used = [] # These are the letters already guessed.

print("Welcome to Hangman MOTHERFUCKER, YOU GON' LEARN TODAY!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("You've used the following letters:\n", used)
    print("So far the word is:\n", so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("You've already guess the letter", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper

    used.append(guess)

    if guess in word:
        print("\nYes!", guess, "is in the word!")

        # create a new so_far to include guess

        new = ""

        for i in range(len(word)):
            if guess == word[i]:
                new += guess
    
        else:
            new += so_far[i]
    so_far = new

else:
    print("Sorry,", guess, "isn't in the word.")
    wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("You've now been hanged.")

else:
    print("\nYou guessed it!, the word was :\n", word)

    input("\n\nPress the Enter Key to Exit.")


    
