###############
###############
###############
###############
###############
###############

answer = 2
count = 0

response = int(input("What is 1+1?"))

while response != 2:
    count += 1
    print("Try Again, you've only had", count, "try so far!")

    response = int(input("What is 1+1?"))
    count += 1

else:
    print("Yay, it was 2!")

    


