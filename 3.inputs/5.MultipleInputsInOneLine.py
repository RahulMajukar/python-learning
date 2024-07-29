# Taking multiple inputs in one line
numbers = input("Enter three numbers separated by space: ").split()
num1 = int(numbers[0])
num2 = int(numbers[1])
num3 = int(numbers[2])

print(f"The numbers you entered are: {num1}, {num2}, {num3}")
