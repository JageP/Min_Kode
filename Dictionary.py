# Dictionary
# How does a dictionary work?

geek = {"term" : "definition"}
choice = None
while choice != "0":

    print(
        """

Programming Translator

0 - Quit
1 - Look Up a Programming Term
2 - Add a Programming Term
3 - Redefine a Programming Term
4 - Delete a Programming Term
5 - Print All Collected Terms

"""
        )

    choice = input("Choice: ")
    print()

# Exit
    if choice == "0":
         print("Goodbye")
     # 0 must have "s either side

    elif choice == "1":
         term = input("What term do you want me to translate?: ")
         if term in geek:
             definition = geek[term]
             print("\n", term, "means", definition)
         else:
            print("\nSorry, I don't know", term)

    elif choice == "2":
        term = input("What term do you want me to add?: ")
        if term not in geek:
            definition = input("What is the definition?: ")
            geek[term] = definition
            print("\n", term, "has been added.")
        else:
            print("\nThat term already exists, try redifining it.")

    elif choice == "3":
        term = input("What word do you want to redefine?: ")
        if term in geek:
            definition = input("What the new definition?: ")
            geek[term] = definition
            print("\n", term, "has been redefined.")
        else:
            print("That term doesn't exist, try adding it!")

    elif choice == "4":
        term = input("What do you want me to delete?: ")
        if term in geek:
            del geek[term]
            print("Okay, that shits been deleted! Yolo!")
        else:
            print("\nImpossible", term, "doesn't exist you penis!")

    elif choice == "5":
        print(geek)

    else:
        print("Soz, but", choice, "isn't a choice!")
        input("Press any key to exit.")
        
            
