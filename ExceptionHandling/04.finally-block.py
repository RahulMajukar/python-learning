# The finally block contains code that is always executed, regardless of whether an exception was raised or not. It is often used for cleanup actions like closing files or releasing resources.

# Example:

try:
    f = open("sample.txt", "r")
    # Perform file operations
except FileNotFoundError as e:
    print("File not found!")
finally:
    f.close()
    print("File closed.")