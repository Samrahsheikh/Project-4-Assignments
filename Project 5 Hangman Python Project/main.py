import random

# Hangman stages
stages = [
    '''
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    ''',
    '''
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / 
       -
    ''',
    '''
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |      
       -
    ''',
    '''
       --------
       |      |
       |      O
       |     \\|
       |      |
       |     
       -
    ''',
    '''
       --------
       |      |
       |      O
       |      |
       |      |
       |     
       -
    ''',
    '''
       --------
       |      |
       |      O
       |    
       |      
       |     
       -
    ''',
    '''
       --------
       |      |
       |      
       |    
       |      
       |     
       -
    '''
]

# Word list should be a list of separate words (you had a single string!)
words = ['apple', 'banana', 'grapes', 'orange', 'peach']

# Randomly choose a word
chosen_word = random.choice(words)
word_display = ['_'] * len(chosen_word)
guessed_letters = []
attempts = len(stages) - 1  # 6 attempts (0 index is final hangman)

print("Welcome to Hangman!")
print("Guess the fruit name!")

# Main game loop
while attempts > 0 and '_' in word_display:
    print('\n' + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Correct!")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("Wrong guess!")
        print(stages[attempts])
        attempts -= 1
        print(f"Attempts left: {attempts}")

# End of game
if '_' not in word_display:
    print("\nYou guessed it right! The word was:", chosen_word)
else:
    print(stages[0])
    print("\nGame Over! The correct word was:", chosen_word)
