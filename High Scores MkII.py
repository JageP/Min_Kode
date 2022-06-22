# Demonstrate list methods
# High Scores

scores = []

choice = None

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

# Everything within the menu is indented underneath the menu, which
# keeps the loop going, when it was not indented the menu was being
# spammed continuously because of a break in the code, if there is no
# indentation then the code will run from the top, without further
# instructions, once it reaches a break.

# Exit

    if choice == "0":
        print("Goodbye")

    elif choice == "1":
        print("High Scores")
        for score in scores:
            print(score)

# Elif choice 1 was printing as a list view horizontally, using
# for score in scores print(score) it now prints in vertically.

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

# If and else needed to be indented below choice 3, otherwise there is
# a syntax error for elif choice ==  4

# Sort Scores

    elif choice == "4":
        scores.sort(reverse=True)
        for score in scores:
            print(score)

# I added in for score in scores print score after choice ==4 for a score
# list to be printed immidiately after the execution of choice == 4
# Although I need to understand the code (for score in scores print score)


# Unknown choice

    else:
        print("Sorry, but", choice, "isn't a valid choice.")
        
