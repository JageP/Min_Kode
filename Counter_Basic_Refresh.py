# Counter

count = 0

# Initially count variable is set at 0, while True sets up the loop
# Meaning that the loop will continue until the break variable criteria
# Is met.
while True:
    count += 1

    # End loop if count is greater than 10

    if count > 100:
        break

    # Break Criteria is met when the count reaches 10, True is still True
    # But the break clause has been reached and the code stops.

    # Skip 5

    if count == 5:
        continue

    if count == 50:
        continue

    # You can insert code after the fact as long as it is properly indented.
    
    # When the counter reaches 5, it does not reach the print count
    # line and goes back to the top of the code and resumes counting
    #Therefore resulting in a non-print for the number 5.

    print(count)

input("\n\nPress any Key to Exit.")

# True needs to be CAPITALISED
