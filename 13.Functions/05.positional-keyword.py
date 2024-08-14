# Positional Arguments: Arguments are matched by position.
# Keyword Arguments: Arguments are passed with parameter names, allowing out-of-order specification.

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

# Positional
display_info("Alice", 30)  # Output: Name: Alice, Age: 30

# Keyword
display_info(age=30, name="Alice")  # Output: Name: Alice, Age: 30
