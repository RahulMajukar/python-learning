# Example: Find the largest number entered
largest = None
while True:
    number = float(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    if largest is None or number > largest:
        largest = number
print(f"The largest number entered is: {largest}")
