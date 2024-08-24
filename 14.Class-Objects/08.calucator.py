# Static methods in Python are methods that belong to the class rather than any object instance. They do not access or modify the class state, meaning they do not have access to the class (cls) or instance (self) variables. Static methods are defined using the @staticmethod decorator.

class MathOperations:
    # Static method to perform addition
    @staticmethod
    def add(a, b):
        return a + b

    # Static method to perform subtraction
    @staticmethod
    def subtract(a, b):
        return a - b

    # Static method to perform multiplication
    @staticmethod
    def multiply(a, b):
        return a * b

    # Static method to perform division
    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Division by zero is undefined!"
        return a / b

# Using the static methods without creating an instance of the class
print(MathOperations.add(10, 5))        # Output: 15
print(MathOperations.subtract(10, 5))   # Output: 5
print(MathOperations.multiply(10, 5))   # Output: 50
print(MathOperations.divide(10, 5))     # Output: 2.0
print(MathOperations.divide(10, 0))     # Output: Division by zero is undefined!
