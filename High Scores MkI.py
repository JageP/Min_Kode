# Demonstrate list methods
# High Scores

scores = []

# This is the first of the variables, it is an empty list as defined by []

choice = None

# Unaware of concept of None, research needed.

while choice != "0":
    print(
        """
    High Scores

    0 - Exit
    1 - Show Scores
    2 - Add a Score
    3 - Delete a Score
    4 - Sort Scores
    """
    )
    choice = input("Choice: ")

    print()

# Exit

    if choice == "0":
        print("Goodbye")

    elif choice == "1":
        print("High Scores")
        for score in scores:
            print(score)

    elif choice == "2":
        score = int(input("What score did you get?:"))
        scores.append(score)

# Remove a score

    elif choice == "3":
        score = int(input("Remove which score?:"))
    if score in scores:
        scores.remove(score)
    else:
        print(score, "isn't in high scores list.")

# Issues:
# As it stands the code spams the high score list.
# If scores are empty show "" later.
