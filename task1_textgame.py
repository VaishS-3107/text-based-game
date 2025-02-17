print("👻 Welcome to the Haunted House! 👻")
print("You wake up in a dark room with two doors: Left (L) and Right (R).")

choice1 = input("Which door do you choose? (L/R): ").strip().upper()

if choice1 == "L":
    print("\nYou enter a creepy library. A ghost whispers a riddle...")
    print("Riddle: I speak without a mouth and hear without ears. What am I?")
    answer = input("Your answer: ").strip().lower()

    if answer == "echo":
        print("The ghost nods and lets you pass. You find the exit! 🎉")
    else:
        print("The ghost screams! You're trapped forever! 👻")

elif choice1 == "R":
    print("\nYou step into a dark hallway. A vampire blocks your way!")
    action = input("Do you (F)ight or (R)un?: ").strip().upper()

    if action == "F":
        print("You bravely fight, but the vampire is too strong. You lose! 🧛‍♂️")
    else:
        print("You run and find a secret door leading outside. You escape! 🎉")

else:
    print("You hesitate for too long... The house consumes you! ☠️")
