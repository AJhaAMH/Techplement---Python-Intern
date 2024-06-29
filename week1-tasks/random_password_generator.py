import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character type must be selected")
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def get_user_preferences():
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special symbols? (y/n): ").strip().lower() == 'y'
    
    return length, use_uppercase, use_lowercase, use_numbers, use_special

def main():
    length, use_uppercase, use_lowercase, use_numbers, use_special = get_user_preferences()
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
        print("Generated password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
