person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key in person:
    print(key)


# print values:
for value in person.values():
    print(value)

# print key-value pair:
for key, value in person.items():
    print(f"{key}: {value}")