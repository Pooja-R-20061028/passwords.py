import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character sets selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("=== Password Generator ===")
try:
    length = int(input("Enter password length: "))
    use_letters =raw_input("Include letters? (y/n): ").lower() =='y'
    use_numbers =raw_input("Include numbers? (y/n): ").lower() =='y'
    use_symbols =raw_input("Include symbols? (y/n): ").lower() =='y'

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print(password)

except ValueError:
    print("Please enter a valid number for password length.")
