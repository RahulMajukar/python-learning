# Number to be reversed
num = 12345

# Initialize the reversed number
reversed_num = 0

# Process the number
while num > 0:
    # Get the last digit of the number
    last_digit = num % 10
    
    # Build the reversed number
    reversed_num = reversed_num * 10 + last_digit
    
    # Remove the last digit from the number
    num = num // 10

# Print the reversed number
print(reversed_num)  # Output: 54321
