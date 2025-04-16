print("🧠 Welcome to the Reverse Guess the Number Game!\n")
print("Think of a number between 1 and 100, and I will try to guess it.")

low = 1
high = 100
attempts = 0
feedback = ""

while feedback != "c":
    guess = (low + high) // 2
    attempts += 1
    print(f"\nIs your number {guess}?")
    feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

    if feedback == "h":
        high = guess - 1
    elif feedback == "l":
        low = guess + 1
    elif feedback == "c":
        print(f"\n🎉 I guessed your number in {attempts} attempts!")
    else:
        print("Please enter a valid response: 'h', 'l', or 'c'.")

