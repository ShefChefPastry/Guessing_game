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
        max_attempts = 10

    elif difficulty_rating == "Medium":
        max_number = 500
        max_attempts = 10

    else:
        max_number = 1000
        max_attempts = 10

    secret_number = random.randint(1, max_number)



    #random number generator
    attempts_made = 0
    won = False

    #first guess
    guess = get_guess(max_number)

    attempts_made += 1

    #Main guessing loop
    while guess != secret_number and attempts_made < max_attempts:

        if guess > secret_number:
            print("Too High! Try again")
        else:
            print("Too Low! Try again")

        attempts_remaining = max_attempts - attempts_made
        print ("Attempts Remaining:", attempts_remaining)

        #Get next guess
        guess = get_guess(max_number)
        
        
        attempts_made += 1


    if guess == secret_number:
        won = True
        print("Congratulations! You Win!")

    else:
        print("You Lost! Too many guesses.")
        print(f"The secret number was {secret_number}.")

    if attempts_made == 1:  
        print("It took you 1 attempt.") 
    else: 
        print("It took you", attempts_made, "attempts.") 

    return attempts_made, won


#games played and attempts made counter
games_played = 0
total_attempts = 0
best_score = None

while True:
    attempts, won = play_game()
    games_played += 1
    total_attempts += attempts
    average_attempts = total_attempts / games_played


    if won:
        if best_score is None:
            best_score = attempts

        elif attempts < best_score:
            best_score = attempts

    print("========== Statistics ==========")
    print("Games Played:", games_played)
    print("Attempts This Game:", attempts)
    print("Total Attempts:", total_attempts)
    print("Average Attempts:", average_attempts)
    print("================================")
    print("Your Best Score is:", best_score)

    restart = input("Would you like to play again? (y/n): ")

    if restart.lower() != "y":
        print("Thanks for playing!")
        break






