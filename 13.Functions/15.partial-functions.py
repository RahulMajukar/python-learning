# Partial Functions
# Using functools.partial, you can fix a certain number of arguments of a function and generate a new function.

from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(4))  # Output: 8