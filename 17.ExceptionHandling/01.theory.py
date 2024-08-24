# Exception: An event that occurs during the execution of a program and disrupts the normal flow of the program's instructions.
# Error: A problem that typically arises due to incorrect logic or programming mistakes, often leading to an exception.

# The try and except Blocks
# Python uses try and except blocks to catch and handle exceptions.

# try block: Contains the code that might raise an exception.
# except block: Contains the code that runs if an exception is raised in the try block.

# Syntax:

# try:
#     # Code that may raise an exception
# except SomeException as e:
#     # Code to handle the exception



# try:  
    # Code block  
    # These statements are those which can probably have some error  
  
# except:  
    # This block is optional.  
    # If the try block encounters an exception, this block will handle it.  
  
# else:  
    # If there is no exception, this code block will be executed by the Python interpreter  
  
# finally:  
    # Python interpreter will always execute this code.  



# Example:
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
    
# o/p:Error occurred: division by zero

