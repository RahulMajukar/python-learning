#  Anonymous Functions Using lambda, map(), filter(), and reduce()
# lambda is used for small functions.
# map() applies a function to all items in an input list.
# filter() creates a list of elements for which a function returns true.
# reduce() applies a rolling computation to sequential pairs of values.


from functools import reduce

# Using map()
squared = list(map(lambda x: x ** 2, [1, 2, 3, 4]))
print(squared)  # Output: [1, 4, 9, 16]

# Using filter()
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print(evens)  # Output: [2, 4]

# Using reduce()
sum_all = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(sum_all)  # Output: 10