'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X......3 X 2 X 1

factorial(n) = n * factorial(n-1)
'''

# Factorial Number 5!=5*4*3*2*1
# Number to find the factorial of
num = 5

# Initialize result
factorial = 1

# Calculate factorial
for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")