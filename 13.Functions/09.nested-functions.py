# Nested Functions
# Functions can be defined inside other functions. The inner function is only accessible from the outer function.
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from inner function!")  # Output: Hello from inner function!
