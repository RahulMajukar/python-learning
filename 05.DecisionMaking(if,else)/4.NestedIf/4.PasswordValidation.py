password = "P@ssw0rd"

if len(password) >= 8:
    if any(char.isdigit() for char in password):
        if any(char.isupper() for char in password):
            if any(char.islower() for char in password):
                if any(char in "!@#$%^&*()-_+=<>?/" for char in password):
                    print("Password is strong")
                else:
                    print("Password should contain at least one special character")
            else:
                print("Password should contain at least one lowercase letter")
        else:
            print("Password should contain at least one uppercase letter")
    else:
        print("Password should contain at least one number")
else:
    print("Password is too short")
