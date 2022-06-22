# Receive and Return Program
# Demonstrates Parameters and Return Values

import random

def display(message):
    print(message)

def give_me_five():
    five = 5
    return random.randrange(10) + 1

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

display("Here's a message for you!")

number = give_me_five()
print("High():", number, "!")

answer = ask_yes_no("\nPlease answer 'y' or 'n': ")

print("Thanks for entering:", answer)

input("\n\nPress the Enter Key to exit.")