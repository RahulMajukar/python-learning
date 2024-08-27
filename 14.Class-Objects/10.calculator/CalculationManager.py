from Calculator import Calculator

class CalculationManager:
    def __init__(self, calculator_instance):
        self.calculator = calculator_instance  # Store the instance of Calculator

    def perform_operations(self, x, y):
        print(f"Addition of {x} and {y}: {self.calculator.add(x, y)}")
        print(f"Subtraction of {x} and {y}: {self.calculator.subtract(x, y)}")
        print(f"Multiplication of {x} and {y}: {self.calculator.multiply(x, y)}")
        print(f"Division of {x} and {y}: {self.calculator.divide(x, y)}")

# Create an instance of Calculator
calc = Calculator()

# Create an instance of CalculationManager and pass the Calculator instance to it
manager = CalculationManager(calc)

# Perform operations using the methods from Calculator
manager.perform_operations(10, 5)
