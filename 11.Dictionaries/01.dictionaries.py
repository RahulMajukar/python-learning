# 1. Creating a dictionary
# Dictionaries are collections of key-value pairs.
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# 2. Accessing values
# Values can be accessed using their corresponding keys.
print(my_dict["name"])  # Output: John

# 3. Adding or updating a key-value pair
my_dict["email"] = "john@example.com"
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'john@example.com'}

# 4. Removing a key-value pair using del
del my_dict["age"]
print(my_dict)  # Output: {'name': 'John', 'city': 'New York', 'email': 'john@example.com'}

# 5. Removing a key-value pair using pop()
email = my_dict.pop("email")
print(email)  # Output: john@example.com
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}

# 6. Removing all items using clear()
my_dict.clear()
print(my_dict)  # Output: {}

# 7. Checking if a key exists using in
my_dict = {"name": "John", "age": 30}
print("name" in my_dict)  # Output: True
print("email" in my_dict)  # Output: False

# 8. Iterating through a dictionary
for key in my_dict:
    print(key, my_dict[key])
# Output:
# name John
# age 30

# 9. Iterating through keys
for key in my_dict.keys():
    print(key)
# Output:
# name
# age

# 10. Iterating through values
for value in my_dict.values():
    print(value)
# Output:
# John
# 30

# 11. Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value)
# Output:
# name John
# age 30

# 12. Creating a dictionary with dict()
new_dict = dict(name="Alice", age=25, city="Boston")
print(new_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Boston'}

# 13. Creating a dictionary with fromkeys()
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(default_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# 14. Using get() to access a value
age = my_dict.get("age")
print(age)  # Output: 30
email = my_dict.get("email", "Not Found")
print(email)  # Output: Not Found

# 15. Using setdefault() to get a value or set it if the key does not exist
city = my_dict.setdefault("city", "Unknown")
print(city)  # Output: Unknown
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'Unknown'}

# 16. Updating a dictionary with another dictionary
update_dict = {"age": 31, "email": "john@example.com"}
my_dict.update(update_dict)
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'Unknown', 'email': 'john@example.com'}

# 17. Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 18. Nested dictionaries
nested_dict = {
    "person1": {"name": "John", "age": 30},
    "person2": {"name": "Alice", "age": 25}
}
print(nested_dict)  # Output: {'person1': {'name': 'John', 'age': 30}, 'person2': {'name': 'Alice', 'age': 25}}

# 19. Accessing nested dictionary values
print(nested_dict["person1"]["name"])  # Output: John

# 20. Using the copy() method to copy a dictionary
copy_dict = my_dict.copy()
print(copy_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'Unknown', 'email': 'john@example.com'}

# 21. Using dict() constructor to create a dictionary from a list of tuples
list_of_tuples = [("name", "Bob"), ("age", 22)]
dict_from_tuples = dict(list_of_tuples)
print(dict_from_tuples)  # Output: {'name': 'Bob', 'age': 22}

# 22. Using the keys() method to get all keys
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'city', 'email'])

# 23. Using the values() method to get all values
values = my_dict.values()
print(values)  # Output: dict_values(['John', 31, 'Unknown', 'john@example.com'])

# 24. Using the items() method to get all key-value pairs
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'John'), ('age', 31), ('city', 'Unknown'), ('email', 'john@example.com')])

# 25. Merging dictionaries using the | operator (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = dict1 | dict2
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# 26. Merging dictionaries using the |= operator (Python 3.9+)
dict1 |= dict2
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

# 27. Using the popitem() method to remove and return the last inserted key-value pair
last_item = my_dict.popitem()
print(last_item)  # Output: ('email', 'john@example.com')
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'Unknown'}

# 28. Using a dictionary as a counter
from collections import defaultdict
counter = defaultdict(int)
for char in "mississippi":
    counter[char] += 1
print(counter)  # Output: defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})

# 29. Using defaultdict to handle missing keys
d = defaultdict(lambda: "Not Present")
d["a"] = 1
print(d["a"])  # Output: 1
print(d["b"])  # Output: Not Present

# 30. OrderedDict (remembers the insertion order, available in collections module)
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
print(ordered_dict)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
