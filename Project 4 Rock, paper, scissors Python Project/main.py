import random

print("🎮 Welcome to Rock, Paper, Scissors!\n")

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(options)

    if user_choice not in options:
        print("❌ Invalid choice! Try again.\n")
        continue

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
