import random
import string

def generate_password(length, complexity):
    if complexity == 'simple':
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choices(characters, k=length))
    elif complexity == 'strong':
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
    else:
        raise ValueError("Invalid complexity level. Choose 'simple' or 'strong'.")
    
    return password

def save_password(password, filename="passwords.txt"):
    with open(filename, "a") as file:
        file.write(password + "\n")

def password_generator():
    print("Welcome to CodSoft Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Invalid length. Please enter a positive integer.")
            return

        complexity = input("Enter the password complexity (simple/strong): ").lower()
        password = generate_password(length, complexity)
        print(f"Generated password: {password}")

        if input("Do you want to save this password? (yes/no): ").lower() == "yes":
            save_password(password)
            print("Password saved successfully!")

    except ValueError as e:
        print(f"Invalid input. {e}")

password_generator()