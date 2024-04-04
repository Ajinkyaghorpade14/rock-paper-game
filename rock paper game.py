import random

def get_user_choice():
    """Get user input for their choice."""
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    """Determine the winner based on user and computer choices."""
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Play a single round of Rock-Paper-Scissors."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Your choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

# Play the game
play_game()
