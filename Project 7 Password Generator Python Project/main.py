import random
import string

def generate_password(length):
    # Ensure password length is at least 8 for security
    if length < 8:
        print("Password should be at least 8 characters long for security.")
        return None

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + symbols

    # Randomly select characters for the password
    password = random.sample(all_characters, length)

    # Ensure at least one character from each set is included
    if any(c in lowercase for c in password) and any(c in uppercase for c in password) and any(c in digits for c in password) and any(c in symbols for c in password):
        return ''.join(password)
    else:
        print("Password doesn't meet security requirements, regenerating...")
        return generate_password(length)  # Recursively generate if the password doesn't meet the criteria

# Ask the user for the length of the password
password_length = int(input("Enter the desired password length (at least 8): "))
password = generate_password(password_length)

# Display the generated password
if password:
    print(f"Generated Password: {password}")
