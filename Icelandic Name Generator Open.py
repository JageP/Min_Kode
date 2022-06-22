#Icelandic Name Generator

import random

# num = 10
# for x in range(num):
# This is to repeat the code as many times as required.
# Requires indentation.

name = ["Jón", "Sigurður", "Guðmundur", "Gunnar", "Ólafur", "Einar", "Kristján",
"Magnús", "Stefán", "Jóhann", "Björn", "Arnar", "Árni", "Bjarni", "Helgi",
"Halldór", "Pétur", "Daníel", "Kristinn", "Ragnar", "Hvitr"]

places = ["Hordaland", "Raumsdalr", "Finnmark", "Uppsala", "Nidaros",
"Jamtaland", "Heidmark", "Lappland"]

birthplace = (random.choice(places))

career_list = ["Viking", "Village Idiot", "Fisherman"]

career = (random.choice(career_list))

# Use [] For lists.

viking_firstname = (random.choice(name))

viking_lastname =  (random.choice(name))

viking_fullname = viking_firstname + ' ' + viking_lastname + "son"

# Use + ' ' + to add a space in between variables

print("Here is your randomly generated Icelandic Name:", viking_fullname)

print("Your name is", viking_firstname, "your father's name was", viking_lastname)
print("You were born in", birthplace, "and you're a", career)

