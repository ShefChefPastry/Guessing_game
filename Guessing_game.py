#ok my first game in python 7/17/2026 @7:45PM
import random

def get_guess(max_number):
    while True:
        try:
            guess = int(input(f"Enter a number between 1 and {max_number}: "))

            if guess < 1 or guess > max_number:
                print(f"Invalid number! Please choose a number between 1 and {max_number}.")
                continue

            return guess
        
        except ValueError:
            print("Please enter a whole number.")



def play_game():


# program display
    print("===============")
    print("Number Guessing Game") 
    print("===============")
    input("PRESS ENTER TO START")


# character selection
    name = input("Enter Player Name: ")
    print(f"Welcome to my first game in Python, {name}!")


# choose your difficulty rating
    difficulty_rating = input("Choose difficulty (Easy, Medium, or Hard): ")

    while(
    difficulty_rating != "Easy"
    and difficulty_rating != "Medium"
    and difficulty_rating != "Hard"
    ):
     print("Invalid difficulty.") 
     difficulty_rating = input("Please enter Easy, Medium, or Hard: ")

    if difficulty_rating == "Easy":
        max_number = 100
        secret_number = random.randint(1, max_number)
    elif difficulty_rating == "Medium":
        max_number = 500
        secret_number = random.randint(1, max_number)
    elif difficulty_rating == "Hard":
        max_number = 1000
        secret_number = random.randint(1, max_number)



    #random number generator
    attempts_made = 0

    #first guess
    guess = get_guess(max_number)

    attempts_made += 1

    #Main guessing loop
    while guess != secret_number:

        if guess > secret_number:
            print("Too High! Try again")
        else:
            print("Too Low! Try again")

        #Get next guess
        guess = get_guess(max_number)
        
        
        attempts_made += 1


    print("Congratulations! You Win!")

    if attempts_made == 1:  
        print("It took you 1 attempt.") 
    else: 
        print("It took you", attempts_made, "attempts.") 

while True:
    play_game()

    restart = input("Would you like to play again? (y/n): ")

    if restart.lower() != "y":
        print("Thanks for playing!")
        break






