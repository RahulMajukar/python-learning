# You can provide default values for parameters. If a value isn’t provided when calling the function, the default value is used.
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Output: Hello, Guest!
greet("Bob")  # Output: Hello, Bob!
