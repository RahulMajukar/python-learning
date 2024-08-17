# The else block can be used to execute code if no exceptions are raised in the try block.

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError as e:
    print("You can't divide by zero!")
else:
    print("Division successful, result is:", result)
