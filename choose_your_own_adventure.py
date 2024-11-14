name = input("What is your name? ")

print("Welcome to the Choose Your Own Adventure Game " + name + "!")
print("You are a hero in a world full of danger and adventure.")
print("Your goal is to find the treasure and escape the forest.")
print("You start on a dirt road that has ended at a river. You have three choices to make:")
print("1. Go left")
print("2. Go right")
print("3. Swim across the river")
print("Which choice will you make?")

choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    print("You have chosen to go left.")
    print("You have found the treasure but it is being guarded by a cyclops.")
    print("you have three choices to make:")
    print("1. Attack the cyclops")
    print("2. Run away")
    print("3. Try to sneak past the cyclops")
    choice = input("Enter 1, 2, or 3: ")
    if choice == "1":
        print("You have chosen to attack the cyclops.")
        print("You have been killed by the cyclops.")
    elif choice == "2":
        print("You have chosen to run away.")
        print("The cyclops chases you until you can't run anymore and you die.")
    elif choice == "3":
        print("You have chosen to sneak past the cyclops.")
        print("The cyclops caught you and killed you.")
        
elif choice == "2":
    print("You have chosen to go right.")
    print("You have been attacked by a monster and were injured.")
    print("You have three choices to make:")
    print("1. Fight the monster")
    print("2. Run away and try to treat your wounds")
    print("3. Use a healing potion")
    choice = input("Enter 1, 2, or 3: ")
    if choice == "1":
        print("You have chosen to fight the monster.")
        print("You have been killed by the monster.")
    elif choice == "2":
        print("You have chosen to run away and try to treat your wounds.")
        print("You successfully escaped the monster, but your wounds became infected and you died")
    elif choice == "3":
        print("You have chosen to use a healing potion.")
        print("You have been healed and restored to full strength.")
        
elif choice == "3":
    print("You have chosen to swim across the river.")
    print("You have been drowned in the river and died.")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")