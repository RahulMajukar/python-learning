# Looping through a list using a for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry


# Looping through a list using a for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry


# Looping through a list using a while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
# Output:
# apple
# banana
# cherry


# Using list comprehension to loop and print
[print(fruit) for fruit in fruits]
# Output:
# apple
# banana
# cherry


# Looping through list using range and len
for i in range(len(fruits)):
    print(fruits[i])
# Output:
# apple
# banana
# cherry


# Nested loop example with two lists
colors = ["red", "yellow", "green"]
for fruit in fruits:
    for color in colors:
        print(f"{fruit} is {color}")
# Output:
# apple is red
# apple is yellow
# apple is green
# banana is red
# banana is yellow
# banana is green
# cherry is red
# cherry is yellow
# cherry is green


# Looping through two lists in parallel using zip
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "dark red"]

for fruit, color in zip(fruits, colors):
    print(f"{fruit} is {color}")
# Output:
# apple is red
# banana is yellow
# cherry is dark red


# Looping with conditional statements
for fruit in fruits:
    if "a" in fruit:
        print(fruit)
# Output:
# apple
# banana
