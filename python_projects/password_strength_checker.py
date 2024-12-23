def is_strong_password(password):
    """This function checks if the password is strong or not"""
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False
    return True

password = input("Enter your password: ")
if is_strong_password(password):
    print("Strong Password")
else:
    print("Weak Password")
    print("Password must be at least 8 characters long, contain at least one digit, one lowercase letter, one uppercase letter, and one special character.")
    