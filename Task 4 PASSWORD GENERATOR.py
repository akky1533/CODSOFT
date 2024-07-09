import random

# Function to get user choice
def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors (or type 'quit' to exit): ").lower()
        if choice in ['rock', 'paper', 'scissors', 'quit']:
            return choice
        else:
            print("Invalid input. Please try again.")

# Function to get computer choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

# Function to print the result of a round
def print_result(user_choice, computer_choice, result):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")

# Function to play a single round
def play_round(user_score, computer_score):
    user_choice = get_user_choice()
    if user_choice == 'quit':
        return False, user_score, computer_score

    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    if result == "user":
        user_score += 1
    elif result == "computer":
        computer_score += 1

    print_result(user_choice, computer_choice, result)
    print(f"Current Scores - You: {user_score}, Computer: {computer_score}\n")
    return True, user_score, computer_score

# Main function to run the game
def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to the Rock-Paper-Scissors Game!")
    print("Instructions: Enter 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.\n")

    while True:
        continue_game, user_score, computer_score = play_round(user_score, computer_score)
        if not continue_game:
            print(f"Final Scores - You: {user_score}, Computer: {computer_score}")
            print("Thanks for playing! Goodbye!")
            break

# Start the game
play_game()