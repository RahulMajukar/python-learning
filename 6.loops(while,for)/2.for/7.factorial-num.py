# Factorial Number 5!=5*4*3*2*1
# Number to find the factorial of
num = 5

# Initialize result
factorial = 1

# Calculate factorial
for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")