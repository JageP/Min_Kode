# Password Files

print("Exclusive Network")

security = 0

username = ""
while not username:
    username = input("Username\n")

password = ""
while not password:
    password = input("Password\n")

if username == "james" and password == "hvitr790":
    print("Hi James")
    security = 5

else:
    print("Login Failed\n", username, "and", password, "\nDo not satisfy Criteria, \nTerminal Shutdown")

input("Press any Key to Exit.")

# Elif's can be added for additional users, specifying Usernames and Passwords
# You can use as many Elifs as are required.
