# Decorators
# Decorators are a powerful tool that allows you to modify the behavior of a function or method. They are functions that take another function as an argument and extend its behavior.
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("Display function ran")

display()
# Output:
# Wrapper executed this before display
# Display function ran
