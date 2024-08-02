# Number to check
num = 12321

# Store the original number for comparison
original_num = num

# Initialize the reversed number
reversed_num = 0

# Reverse the number
while num > 0:
    last_digit = num % 10
    reversed_num = reversed_num * 10 + last_digit
    num = num // 10

# Check if the original number is equal to the reversed number
if original_num == reversed_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")
