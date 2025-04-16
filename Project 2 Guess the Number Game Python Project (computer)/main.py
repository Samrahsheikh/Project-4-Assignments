import random

print("🎲 Welcome to the Guess the Number Game!\n")
print("I'm thinking of a number between 1 and 100. Can you guess it?\n")

# Generate a random number
secret_number = random.randint(1, 100)
guess = None
attempts = 0

# Game loop
while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! 📉 Try again.\n")
        elif guess > secret_number:
            print("Too high! 📈 Try again.\n")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} tries.")
    except ValueError:
        print("Please enter a valid number! ❌\n")
