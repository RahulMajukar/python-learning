# Higher-Order Functions
# A higher-order function is a function that either takes another function as an argument or returns a function.

def apply_func(func, value):
    return func(value)

result = apply_func(lambda x: x**2, 4)
print(result)  # Output: 16
