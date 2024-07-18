# Prompt the user for a number
age_str = input("Enter your age: ")

# Convert the input string to an integer
age = int(age_str)

# Perform some operation with the input
if age >= 18:
    print("You are an adult.")
else:
    print("You are not yet an adult.")
