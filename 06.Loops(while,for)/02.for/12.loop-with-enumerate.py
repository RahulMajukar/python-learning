# Using enumerate to get both the index and the value while iterating over a list.

colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Color at index {index} is {color}")



# Using enumerate with a custom start index.
letters = ["a", "b", "c", "d"]
for index, letter in enumerate(letters, start=1):
    print(f"{index}: {letter}")
