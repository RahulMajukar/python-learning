# Iterating over two lists simultaneously using zip.
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")