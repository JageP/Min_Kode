# Receive and Return Program
# Demonstrates Parameters and Return Values

def display(message):
    print(message)

def give_me_five():
    five = 5
    return five # replaced numeric

def ask_yes_no(question):
    """Ask a Yes/No Question."""
    reponse = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

display("Here's a message for you.\n")

number = give_me_five()
print("Here's what I got from give_me_five():", number)

answer = ask_yes_no("\nPlease Enter 'y' or 'n': ")

print("Thanks for entering:", answer)

input("\n\nPress the enter key to exit.")
