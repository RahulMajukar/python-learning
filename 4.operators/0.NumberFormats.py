# Define a decimal number
decimal_number = 6

# Convert decimal to binary using format()
binary_representation = format(decimal_number, 'b')

# Print the binary representation
print("The binary representation of", decimal_number, "is", binary_representation)

# Convert binary to decimal using int() with base 2
converted_decimal_number = int(binary_representation, 2)

print(converted_decimal_number)