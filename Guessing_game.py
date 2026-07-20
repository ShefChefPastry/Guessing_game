#ok my first game in python 7/17/2026 @7:45PM


# program display
print("===============")
print("Number Guessing Game") 
print("===============")
input("PRESS ENTER TO START")


# character selection
name = input("Enter Player Name: ")
print("Welcome to my first game in Python,",name,"!")


# random number generator
import random

play_again = "yes"
while play_again == "yes":
    secret_number = random.randint(1, 100)
    guess = int(input("Enter a number between 1-100: "))
    while guess != secret_number:
        if guess > secret_number:
            print("Too High! Try again")
        else:
            print("Too Low! Try again")
        guess = int(input("Enter a number: "))

    print("Congratulations! You Win!")
    play_again = input("Play again? (yes/no): ").strip().lower()

print("Thanks for playing,", name, "!")
