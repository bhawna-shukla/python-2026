import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer"""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    """Get user input and validate it"""
    while True:
        user_input = input("\nEnter your choice (rock/paper/scissors): ").lower().strip()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("❌ Invalid choice! Please enter rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game"""
    if user_choice == computer_choice:
        return "tie"
    
    # Define winning conditions
    winning_conditions = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_conditions[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, result):
    """Display the game result"""
    print(f"\n{'='*40}")
    print(f"Your choice: {user_choice.upper()}")
    print(f"Computer choice: {computer_choice.upper()}")
    print(f"{'='*40}")
    
    if result == "tie":
        print("🤝 It's a TIE!")
    elif result == "user":
        print("🎉 YOU WIN!")
    else:
        print("😢 YOU LOSE!")

def play_game():
    """Main game loop"""
    user_score = 0
    computer_score = 0
    
    print("🎮 Welcome to Rock, Paper, Scissors! 🎮")
    print("=" * 40)
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, result)
        
        # Update scores
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        
        # Display score
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")
        
        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            break
    
    # Final results
    print(f"\n{'='*40}")
    print("FINAL RESULTS")
    print(f"{'='*40}")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")
    
    if user_score > computer_score:
        print("🏆 You won the game! Congratulations!")
    elif computer_score > user_score:
        print("💻 Computer won the game!")
    else:
        print("🤝 It's a tie overall!")
    
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()


