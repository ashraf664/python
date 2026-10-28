import random
import string

def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols

    password = random.choice(letters) + random.choice(digits) + random.choice(symbols)
    password += ''.join(random.choice(all_chars) for _ in range(length - 3))
    password = ''.join(random.sample(password, len(password)))
    return password

while True:
    while True:
        try:
            user_input = input("Enter the desired password length : ")
            length = int(user_input)
            if length < 4:
                print(" Password length must be at least 4 to be secure.")
            else:
                break
        except ValueError:
            print(" Please enter a valid number.")
    
    password = generate_password(length)
    print("\n Your generated strong password is:")
    print(password)

    again = input("\nDo you want another password? (yes/no): ").strip().lower()
    if again == "no":
        print("Goodbye!")
        break
