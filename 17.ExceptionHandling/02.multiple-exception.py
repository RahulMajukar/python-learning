# You can handle multiple exceptions by specifying multiple except blocks.

# Example:

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError as e:
    print("That's not a valid number!")
except ZeroDivisionError as e:
    print("You can't divide by zero!")