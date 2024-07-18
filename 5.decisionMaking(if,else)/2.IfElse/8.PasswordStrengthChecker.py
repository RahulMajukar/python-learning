password = "mypassword"

if len(password) < 6:
    print("Password is too short")
elif not any(char.isdigit() for char in password):
    print("Password should contain at least one number")
elif not any(char.isupper() for char in password):
    print("Password should contain at least one uppercase letter")
else:
    print("Password is strong")
