# Validating integer input
while True:
    try:
        age = int(input("Enter your age (must be a whole number): "))
        break  # Exit loop if input is valid integer
    except ValueError:
        print("Invalid input! Please enter a valid whole number.")

print(f"Your age is: {age}")
