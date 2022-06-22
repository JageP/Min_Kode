# Instructions
# Demonstrates Programmer-Created Functions

X = "X"
O = "O"
EMPTY = ""
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
    """Display Game Instructions."""
    print(
        """
Welcome to this shit, here are the number relevant to the spaces on a noughts and crosses board

0 ¦ 1 ¦ 2
----------
3 ¦ 4 ¦ 5
----------
6 ¦ 7 ¦ 8

Learn that shit, play this shit.
"""
)

# Main
print("Instructions")
instructions()

input("Press any key to continue.")

# def instructions(): - this line tells the computer that the block of code that follows
# is the definition of the function instructions, this means whenever the function instructions
# is called, this block of code follows.

