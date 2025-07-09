import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0
    play_again = "yes"

    while play_again.lower() == "yes":
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        while user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            user_choice = input("Choose rock, paper, or scissors: ").lower()

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Score: You - {user_score}, Computer - {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()

if __name__ == "__main__":
    main()