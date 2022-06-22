# Losing Battle Program
# Demonstrating the Infinite Loop

import random

print("The cashier is surrounded by an army of evil Karens.")
print("Their disgusting hair cuts stretch beyond the horizon")
print("The cashier loads his shotgun and prepares for the fight of his life\n")

# New line to split the following threads

health = 10
karens = 0
dice = [1,2,3,4,5,6]
damage = random.choice(dice)

# How to get the script to re-run a random integer?
# Random is no defined
# While Health != 0, this means unless the counter stops specifically on 0 the script will carry on to the minuses.

while health > 0: #When health is less than 0
    karens += 1
    health -= damage

# This line above with indents runs as one line
# All of this is linked together
# And flows as one command, true false progression.

    print("The cashier fires the shotgun and kills an evil Karen,"\
          "but takes", damage, "damage points.\n Your character has", health,"points of health left")

print("The cashier fought valiantly and killed", karens, "Karens.")
print("But alas, your hero is no more.")
