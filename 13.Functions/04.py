class Example:
    def display(self, a=None, b=None):
        if a is not None and b is not None:
            print(f"a: {a}, b: {b}")
        elif a is not None:
            print(f"a: {a}")
        else:
            print("No arguments provided")

obj = Example()
obj.display(10, 20)  # a: 10, b: 20
obj.display(10)      # a: 10
obj.display()        # No arguments provided
