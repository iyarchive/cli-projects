while True:

    password = input("Input a password: ")

    if len(password) <8:
        print("Password must be at least 8 characters long.")

    elif not any(character.isdigit() for character in password):
        print("Username must contain at least one number.")

    else:
        break
