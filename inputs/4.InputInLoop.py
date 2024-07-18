# Prompt the user to enter numbers until they enter 'done'
numbers = []
while True:
    num_str = input("Enter a number (or 'done' to finish): ")
    if num_str.lower() == 'done':
        break
    num = float(num_str)
    numbers.append(num)

# Display the numbers entered by the user
print("Numbers entered:", numbers)
