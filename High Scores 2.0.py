# High Scores 2.0
# Demonstrates nested sequences.

scores = []

choice = None

while choice != "0":
    print(
        """

High Scores

0 - Quit
1 - List Scores
2 - Add a Score
"""
        )


    choice = input("Choice: ")
    print()

# Exit

    if choice == "0":
        print("Goodbye.")


# Display the highscore table

    elif choice == "1":
        print("High Scores\n")
        print("NAME\tScore")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

# Add a Score

    elif choice == "2":
        name = input("What is the players name?: ")
        score = int(input("What score did the player get?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]          # Keep only top 5 scores

# Some unknown choice

    else: print("Sorry but", choice, "Isn't a valid choice.")

input("\n\nPlease press any key to exit")
    

