# Example: Sum numbers until a negative number is entered
total = 0
while True:
    number = float(input("Enter a number (negative number to stop): "))
    if number < 0:
        break
    total += number
print(f"Total sum is: {total}")
