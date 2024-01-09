import string
import random

def password_generator():
    print("Welcome to the password generator!")
    length = int(input("Enter the desired length of the password: "))
   
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = "".join(random.choice(characters) for _ in range(length))
    
    print(f"Your password is: {password}")

if __name__ == "__main__":
    password_generator()
