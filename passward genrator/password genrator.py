import random
import string

def generate_password(length):
    # Define the possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        # Prompt user for the desired password length
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Password length must be a positive integer.")
            return
        
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()