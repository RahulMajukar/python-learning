# Functions can return a value using the return statement.
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8


# Functions can return multiple values as a tuple.
def get_user_info():
    name = "John"
    age = 25
    return name, age

user_name, user_age = get_user_info()
print(user_name)  # Output: John
print(user_age)  # Output: 25
