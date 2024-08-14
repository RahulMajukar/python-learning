# Generators
# Generators are special functions that return an iterable set of items, one at a time, in a special way.

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)
# Output:
# 5
# 4
# 3
# 2
# 1