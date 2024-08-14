# Sometimes, you may not know how many arguments a function will receive. Use *args to handle this.
def sum_numbers(*args):
    return sum(args)

result = sum_numbers(1, 2, 3, 4)
print(result)  # Output: 10


#Arbitrary Keyword Arguments (**kwargs)
# Use **kwargs when you want to pass a variable number of keyword arguments.

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
