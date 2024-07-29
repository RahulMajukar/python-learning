# Example: Keep asking the user for input until they enter 'quit'
user_input = ''
while user_input != 'quit':
    user_input = input("Enter 'quit' to exit: ")
    print(f"You entered: {user_input}")
