import random

names_list = ["Nigel", "Fartman 5000", "BO Boy", "Queefqueen"]

ages_list = ["320", "412", "900"]

genders_list = ["1", "2", "3"]

name = input("What is your name?")

age = input("How old are you?")

gender = input("What is your gender?")


print("Okay, so your name is", name, "you are", age, "years old. And you're a", gender)

input("Press any key to continue")

print("DID YOU KNOW: If you were living in the year 2100 your name would be", (random.choice(names_list)),
      "and you'd be", (random.choice(ages_list)), ",you know, becuase of Science" , "you'd probably be a", (random.choice(genders_list)))


