# Checking if all or any elements in a list meet a condition.
numbers = [1, 2, 3, 4, 5]
all_even = all(num % 2 == 0 for num in numbers)
any_even = any(num % 2 == 0 for num in numbers)
print(f"All even: {all_even}")
print(f"Any even: {any_even}")
