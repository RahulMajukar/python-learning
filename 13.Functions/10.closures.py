# Closures
# A closure is a nested function that remembers the environment in which it was created, even after the outer function has finished executing.

def outer_function(text):
    def inner_function():
        print(text)
    return inner_function

my_func = outer_function("Hello, Closure!")
my_func()  # Output: Hello, Closure!
