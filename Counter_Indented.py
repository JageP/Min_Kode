#Counter

count = 0
while True:
    count += 1
    if count > 10:
        break
    if count == 5:
        continue
    print(count)


input("Press the Enter Key to exit")

# Count starts at 0
# While this is true, the program adds 1
# If count exceeds 10 then the program stops
# If count reaches 5, skip it.
# Print as the program loops.
