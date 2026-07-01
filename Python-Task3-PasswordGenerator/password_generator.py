import random
import string

print("=" * 40)
print("    RANDOM PASSWORD GENERATOR")
print("=" * 40)

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

        print("\nChoose character types:")
        upper = input("Include Uppercase letters? (y/n): ").lower()
        lower = input("Include Lowercase letters? (y/n): ").lower()
        digits = input("Include Numbers? (y/n): ").lower()
        symbols = input("Include Symbols? (y/n): ").lower()

        characters = ""

        if upper == "y":
            characters += string.ascii_uppercase

        if lower == "y":
            characters += string.ascii_lowercase

        if digits == "y":
            characters += string.digits

        if symbols == "y":
            characters += string.punctuation

        if len(characters) == 0:
            print("Please select at least one character type.\n")
            continue

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:")
        print(password)

        again = input("\nGenerate another password? (y/n): ").lower()

        if again != "y":
            print("\nThank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.\n")