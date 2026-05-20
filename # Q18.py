# Q18. Password Strength Checker

def check_password(password):

    if (len(password) >= 8 and
        any(char.isdigit() for char in password) and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password)):
        return "Strong Password"

    return "Weak Password"

pwd = input("Enter password: ")
print(check_password(pwd))