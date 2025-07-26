import random
import string

def generate_password():
    try:
        length = int(input("Enter length for the password = "))

        if length <= 0:
            print("Length must be positive. Try Again")
            return
        
        print("\nSpecify the complexity requirements (y/n).")
        include_letters = input("Include letters (e.g. ABC, abc?) : ").lower().startswith('y')
        include_number = input("include num (e.g. 123 ?) : ").lower().startswith("y")
        include_symbols = input("Include symbols (e.g. !@# ?) : ").lower().startswith('y')


        characters = ""
        if include_letters:
            characters += string.ascii_letters
        if include_number:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation

        if not characters:
            print("\nSelect atleast 1 character type.")
            return
        
        password = ''.join(random.choice(characters) for i in range(length))

        print("\n----------------------------------")
        print(f"Generated password 🔐: {password}")
        print("----------------------------------")

    except ValueError:
        print("\nInvalid input! Try Again")

if __name__ == "__main__":
    generate_password()


