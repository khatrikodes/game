# Rock, Paper, Scissors Game
import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    # User input
    user_choice = int(input("Your choice (1-3): "))

    if user_choice not in [1, 2, 3]:
        print("Invalid choice. Please select 1, 2, or 3.")
        return

    # Map user choice to string
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    user_pick = choices[user_choice]

    # Random computer choice
    computer_choice = random.randint(1, 3)
    computer_pick = choices[computer_choice]

    print(f"You chose: {user_pick}")
    print(f"Computer chose: {computer_pick}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("You lose!")

# Main program
if __name__ == "__main__":
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing Rock, Paper, Scissors! Goodbye!")
            break
