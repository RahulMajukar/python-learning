# Recursive Functions
# A function that calls itself to solve smaller instances of the same problem. Useful for tasks like traversing data structures.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120