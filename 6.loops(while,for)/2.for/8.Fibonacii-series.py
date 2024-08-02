# Number of Fibonacci numbers to generate
n = 10

# Initialize the first two Fibonacci numbers
a, b = 0, 1

print("Fibonacci Series:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
