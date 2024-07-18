# Creating a list of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)  # Output: [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Creating a mixed list
mixed_list = [1, "apple", 3.14, True]
print(mixed_list)  # Output: [1, 'apple', 3.14, True]

#List Length
print(len(numbers))

#type()
print(type(numbers))

#Using the list() constructor to make a List:
myList = list(("apple", "banana", "cherry")) # note the double round-brackets
print(myList)

# Accessing elements by index
print(fruits[0])  # Output: 'apple'
print(fruits[1])  # Output: 'banana'

# Accessing elements from the end
print(fruits[-1])  # Output: 'cherry'


# Slicing the list
print(numbers[1:3])  # Output: [2, 3]
print(numbers[:3])   # Output: [1, 2, 3]
print(numbers[3:])   # Output: [4, 5]

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# Append Items
# To add an item to the end of the list, use the append() method:
# Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items
# To insert a list item at a specified index, use the insert() method.
# The insert() method inserts an item at the specified index:
# Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend List
# To append elements from another list to the current list, use the extend() method.
# Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
# Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# Modifying an element
numbers[2] = 10
print(numbers)  # Output: [1, 2, 10, 4, 5]


# Modifying an element
numbers[2] = 10
print(numbers)  # Output: [1, 2, 10, 4, 5]


# Removing an element by value
numbers.remove(10)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

# Removing an element by index
del numbers[1]
print(numbers)  # Output: [1, 3, 4, 5, 6]

# Popping an element (removes and returns the last element)
last_element = numbers.pop()
print(last_element)  # Output: 6
print(numbers)       # Output: [1, 3, 4, 5]

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Example2
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Concatenation
new_list = numbers + [7, 8, 9]
print(new_list)  # Output: [1, 3, 4, 5, 7, 8, 9]

# Repetition
repeated_list = fruits * 2
print(repeated_list)  # Output: ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']


# Using a for loop to iterate over a list
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry


# Checking if an element is in the list
print("banana" in fruits)  # Output: True
print("grape" in fruits)   # Output: False


# Sorting a list
numbers = [4, 1, 3, 2, 5]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4, 5]

# Reversing a list
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]


# Copying a list
numbers_copy = numbers.copy()
print(numbers_copy)  # Output: [5, 4, 3, 2, 1]
