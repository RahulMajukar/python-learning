# Tuples in Python are immutable sequences, typically used to store collections of heterogeneous data.

# 1. Creating a tuple
t = (1, 2, 3, 4, 5)
print(t)  # Output: (1, 2, 3, 4, 5)

# 2. Accessing elements
print(t[0])  # Output: 1
print(t[-1])  # Output: 5

# 3. Slicing tuples
print(t[1:3])  # Output: (2, 3)
print(t[:3])   # Output: (1, 2, 3)
print(t[3:])   # Output: (4, 5)

# 4. Tuples are immutable, so we cannot change their elements
# t[0] = 10  # This would raise a TypeError

# 5. Creating a tuple with different data types
t2 = (1, "hello", 3.14, True)
print(t2)  # Output: (1, 'hello', 3.14, True)

# 6. Concatenating tuples
t3 = t + t2
print(t3)  # Output: (1, 2, 3, 4, 5, 1, 'hello', 3.14, True)

# 7. Repeating tuples
t4 = t * 2
print(t4)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# 8. Checking if an element exists in a tuple
print(3 in t)  # Output: True
print(10 in t)  # Output: False

# 9. Getting the length of a tuple
print(len(t))  # Output: 5

# 10. Finding the maximum and minimum elements
t5 = (5, 10, 15, 20, 25)
print(max(t5))  # Output: 25
print(min(t5))  # Output: 5

# 11. Converting a list to a tuple
lst = [1, 2, 3, 4, 5]
t6 = tuple(lst)
print(t6)  # Output: (1, 2, 3, 4, 5)

# 12. Converting a string to a tuple
s = "hello"
t7 = tuple(s)
print(t7)  # Output: ('h', 'e', 'l', 'l', 'o')

# 13. Tuple unpacking
a, b, c, d, e = t
print(a, b, c, d, e)  # Output: 1 2 3 4 5

# 14. Nested tuples
nested_t = (1, (2, 3), (4, 5, 6))
print(nested_t)  # Output: (1, (2, 3), (4, 5, 6))
print(nested_t[1])  # Output: (2, 3)
print(nested_t[1][0])  # Output: 2

# 15. Using tuples as keys in a dictionary (since tuples are hashable)
dict_t = {(1, 2): "a", (3, 4): "b"}
print(dict_t[(1, 2)])  # Output: a

# 16. Counting occurrences of an element in a tuple
t8 = (1, 2, 2, 3, 4, 4, 4)
print(t8.count(2))  # Output: 2
print(t8.count(4))  # Output: 3

# 17. Finding the index of an element in a tuple
print(t8.index(2))  # Output: 1
print(t8.index(4))  # Output: 4

# 18. Using the `sum` function with tuples (elements must be numbers)
t9 = (1, 2, 3, 4, 5)
print(sum(t9))  # Output: 15

# 19. Using the `sorted` function to sort elements (returns a list)
t10 = (5, 2, 3, 1, 4)
print(sorted(t10))  # Output: [1, 2, 3, 4, 5]

# 20. Using the `all` function to check if all elements are true
t11 = (True, True, False)
print(all(t11))  # Output: False

# 21. Using the `any` function to check if any element is true
print(any(t11))  # Output: True

# 22. Using the `enumerate` function to get index and value pairs
for index, value in enumerate(t):
    print(index, value)
# Output:
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5

# 23. Creating an empty tuple
empty_t = ()
print(empty_t)  # Output: ()

# 24. Creating a single-element tuple (notice the comma)
single_element_t = (1,)
print(single_element_t)  # Output: (1,)

# 25. Using `*` to gather remaining elements into a list in tuple unpacking
a, *b = t
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4, 5]

# 26. Using `*` to gather elements in nested tuple unpacking
nested_t2 = (1, 2, 3, 4, 5)
a, *b, c = nested_t2
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5

# 27. Converting a tuple to a list
t_to_list = list(t)
print(t_to_list)  # Output: [1, 2, 3, 4, 5]

# 28. Using `zip` with tuples to pair elements from multiple iterables
t11 = (1, 2, 3)
t12 = ('a', 'b', 'c')
zipped = zip(t11, t12)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# 29. Using the `in` operator to check for membership
print(3 in t)  # Output: True
print(10 in t)  # Output: False

# 30. Using a generator expression with a tuple
gen_t = (x * 2 for x in t)
print(tuple(gen_t))  # Output: (2, 4, 6, 8, 10)

# 1. Reversing a tuple
# Tuples can be reversed using slicing.
t = (1, 2, 3, 4, 5)
print(t[::-1])  # Output: (5, 4, 3, 2, 1)

# 2. Converting a tuple to a string
# You can use the str() function or join() method to convert a tuple to a string.
t = ('a', 'b', 'c')
print(str(t))  # Output: ('a', 'b', 'c')

# Using join for elements that are strings
t = ('hello', 'world')
print(' '.join(t))  # Output: hello world

# 3. Creating a tuple using the tuple() function
# You can create a tuple from any iterable using the tuple() function.
lst = [1, 2, 3, 4]
t = tuple(lst)
print(t)  # Output: (1, 2, 3, 4)

# 4. Tuple comprehension using generator expressions
# While tuples themselves do not support comprehension syntax, you can create tuples using generator expressions within tuple().
t = tuple(x**2 for x in range(5))
print(t)  # Output: (0, 1, 4, 9, 16)

# 5. Using the reversed function to reverse a tuple
# The reversed() function returns an iterator that accesses the given sequence in reverse order.
t = (1, 2, 3, 4, 5)
reversed_t = tuple(reversed(t))
print(reversed_t)  # Output: (5, 4, 3, 2, 1)

# 6. Comparing tuples
# Tuples can be compared lexicographically using comparison operators.
t1 = (1, 2, 3)
t2 = (1, 2, 4)
print(t1 < t2)  # Output: True

# 7. Sorting a list of tuples
# You can sort a list of tuples based on the elements of the tuples.
lst_of_tuples = [(3, 'c'), (1, 'a'), (2, 'b')]
sorted_lst = sorted(lst_of_tuples)
print(sorted_lst)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# 8. Using the * operator to unpack tuples
# You can use the * operator to unpack tuple elements when passing them to a function.
def add(a, b, c):
    return a + b + c

t = (1, 2, 3)
print(add(*t))  # Output: 6

# 9. Combining multiple tuples
# You can combine multiple tuples using the + operator.
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t_combined = t1 + t2
print(t_combined)  # Output: (1, 2, 3, 4, 5, 6)

# 10. Immutability of Tuples
# Tuples are immutable, which means once they are created, their elements cannot be modified. Attempting to do so will result in an error.
t = (1, 2, 3)
# t[0] = 4  # This would raise a TypeError: 'tuple' object does not support item assignment

# 11. Tuple of tuples
# Tuples can contain other tuples as elements, allowing for nested tuple structures.
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)  # Output: ((1, 2), (3, 4), (5, 6))

# 12. Tuple with single element
# To create a tuple with a single element, include a comma after the element.
single_element_tuple = (1,)
print(single_element_tuple)  # Output: (1,)
print(type(single_element_tuple))  # Output: <class 'tuple'>

# 13. Using tuples for multiple assignment
# Tuples can be used for multiple assignment, allowing for swapping values or unpacking.
a, b = 1, 2
a, b = b, a
print(a, b)  # Output: 2 1

# 14. Using the * operator for extended unpacking
# You can use the * operator to capture remaining items during unpacking.
a, *b, c = (1, 2, 3, 4, 5)
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5

# 15. Tuple with heterogeneous elements
# Tuples can store elements of different data types.
heterogeneous_tuple = (1, "hello", 3.14, True)
print(heterogeneous_tuple)  # Output: (1, 'hello', 3.14, True)

# 16. Creating a tuple
t = (1, 2, 3, 4, 5)
print(t)  # Output: (1, 2, 3, 4, 5)

# 17. Accessing elements
print(t[0])  # Output: 1
print(t[-1])  # Output: 5

# 18. Slicing tuples
print(t[1:3])  # Output: (2, 3)
print(t[:3])   # Output: (1, 2, 3)
print(t[3:])   # Output: (4, 5)

# 19. Tuples are immutable, so we cannot change their elements
# t[0] = 10  # This would raise a TypeError

# 20. Creating a tuple with different data types
t2 = (1, "hello", 3.14, True)
print(t2)  # Output: (1, 'hello', 3.14, True)

# 21. Concatenating tuples
t3 = t + t2
print(t3)  # Output: (1, 2, 3, 4, 5, 1, 'hello', 3.14, True)

# 22. Repeating tuples
t4 = t * 2
print(t4)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# 23. Checking if an element exists in a tuple
print(3 in t)  # Output: True
print(10 in t)  # Output: False

# 24. Getting the length of a tuple
print(len(t))  # Output: 5

# 25. Finding the maximum and minimum elements
t5 = (5, 10, 15, 20, 25)
print(max(t5))  # Output: 25
print(min(t5))  # Output: 5

# 26. Converting a list to a tuple
lst = [1, 2, 3, 4, 5]
t6 = tuple(lst)
print(t6)  # Output: (1, 2, 3, 4, 5)

# 27. Converting a string to a tuple
s = "hello"
t7 = tuple(s)
print(t7)  # Output: ('h', 'e', 'l', 'l', 'o')

# 28. Tuple unpacking
a, b, c, d, e = t
print(a, b, c, d, e)  # Output: 1 2 3 4 5

# 29. Nested tuples
nested_t = (1, (2, 3), (4, 5, 6))
print(nested_t)  # Output: (1, (2, 3), (4, 5, 6))
print(nested_t[1])  # Output: (2, 3)
print(nested_t[1][0])  # Output: 2

# 30. Using tuples as keys in a dictionary (since tuples are hashable)
dict_t = {(1, 2): "a", (3, 4): "b"}
print(dict_t[(1, 2)])  # Output: a

# 31. Counting occurrences of an element in a tuple
t8 = (1, 2, 2, 3, 4, 4, 4)
print(t8.count(2))  # Output: 2
print(t8.count(4))  # Output: 3

# 32. Finding the index of an element in a tuple
print(t8.index(2))  # Output: 1
print(t8.index(4))  # Output: 4

# 33. Using the `sum` function with tuples (elements must be numbers)
t9 = (1, 2, 3, 4, 5)
print(sum(t9))  # Output: 15

# 34. Using the `sorted` function to sort elements (returns a list)
t10 = (5, 2, 3, 1, 4)
print(sorted(t10))  # Output: [1, 2, 3, 4, 5]

# 35. Using the `any` and `all` functions with tuples
t11 = (0, 1, 2, 3)
print(any(t11))  # Output: True
print(all(t11))  # Output: False

# 36. Using the `zip` function to create tuples from multiple iterables
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
zipped = tuple(zip(lst1, lst2))
print(zipped)  # Output: ((1, 'a'), (2, 'b'), (3, 'c'))

# 37. Tuple with a single element (note the comma)
single_element_tuple = (1,)
print(single_element_tuple)  # Output: (1,)
print(type(single_element_tuple))  # Output: <class 'tuple'>

# 38. Creating an empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()
print(type(empty_tuple))  # Output: <class 'tuple'>
