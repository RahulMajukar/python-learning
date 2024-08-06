# 1. Creating a set
# Sets are unordered collections of unique elements.
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# 2. Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()

# 3. Adding elements to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# 4. Adding multiple elements using update()
my_set.update([7, 8, 9])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 5. Removing elements using remove() (raises KeyError if the element is not present)
my_set.remove(9)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# 6. Removing elements using discard() (does not raise an error if the element is not present)
my_set.discard(8)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

# 7. Removing and returning an arbitrary element using pop()
removed_element = my_set.pop()
print(removed_element)  # Output: (arbitrary element from the set)
print(my_set)  # Output: (set without the removed element)

# 8. Clearing all elements from a set
my_set.clear()
print(my_set)  # Output: set()

# 9. Set length
my_set = {1, 2, 3, 4}
print(len(my_set))  # Output: 4

# 10. Checking membership with in
print(2 in my_set)  # Output: True
print(5 in my_set)  # Output: False

# 11. Set union using union() or |
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# 12. Set intersection using intersection() or &
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# 13. Set difference using difference() or -
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# 14. Set symmetric difference using symmetric_difference() or ^
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# 15. Checking if a set is a subset using issubset()
subset = {1, 2}
print(subset.issubset(set1))  # Output: True

# 16. Checking if a set is a superset using issuperset()
print(set1.issuperset(subset))  # Output: True

# 17. Set comprehension
squares = {x**2 for x in range(5)}
print(squares)  # Output: {0, 1, 4, 9, 16}

# 18. Converting a list to a set (removes duplicates)
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(list_with_duplicates)
print(unique_set)  # Output: {1, 2, 3, 4, 5}

# 19. Iterating through a set
for item in set1:
    print(item)  # Output: (each element of set1 on a new line)

# 20. Using the set() function to create a set from a string
string_set = set("hello")
print(string_set)  # Output: {'h', 'e', 'l', 'o'}

# 21. Using set as keys in a dictionary
dict_with_set_keys = {frozenset([1, 2]): "value"}
print(dict_with_set_keys)  # Output: {frozenset({1, 2}): 'value'}

# 22. Frozen sets (immutable sets)
frozen_set = frozenset([1, 2, 3, 4])
print(frozen_set)  # Output: frozenset({1, 2, 3, 4})

# 23. Creating a frozen set from a set
mutable_set = {1, 2, 3, 4}
frozen_set_from_set = frozenset(mutable_set)
print(frozen_set_from_set)  # Output: frozenset({1, 2, 3, 4})

# 24. Set difference update using difference_update()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
set1.difference_update(set2)
print(set1)  # Output: {1, 2}

# 25. Set intersection update using intersection_update()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print(set1)  # Output: {3, 4}

# 26. Set symmetric difference update using symmetric_difference_update()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 5}

# 27. Using set() with no arguments to create an empty set
empty_set = set()
print(empty_set)  # Output: set()

# 28. Using set() to convert other iterables (like dictionaries) to sets
dict_keys_set = set({'a': 1, 'b': 2})
print(dict_keys_set)  # Output: {'a', 'b'}

# 29. Using set to remove duplicates from a list
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_elements = list(set(list_with_duplicates))
print(unique_elements)  # Output: [1, 2, 3, 4, 5] (order may vary)

# 30. Set difference between two sets (example of different results)
set_a = {1, 2, 3}
set_b = {2, 3, 4}
diff = set_a - set_b
print(diff)  # Output: {1}

# 31. Set intersection between two sets (example of different results)
set_a = {1, 2, 3}
set_b = {2, 3, 4}
intersect = set_a & set_b
print(intersect)  # Output: {2, 3}

# 32. Symmetric difference between two sets (example of different results)
set_a = {1, 2, 3}
set_b = {2, 3, 4}
sym_diff = set_a ^ set_b
print(sym_diff)  # Output: {1, 4}

# 33. Set union of multiple sets
set1 = {1, 2}
set2 = {2, 3}
set3 = {3, 4}
union_all = set1 | set2 | set3
print(union_all)  # Output: {1, 2, 3, 4}
