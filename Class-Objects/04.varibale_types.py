# Class vs. Instance Variables
# Class Variables: Shared across all instances of a class.
# Instance Variables: Unique to each instance.

class Circle:
    pi = 3.14  # Class variable

    def __init__(self, radius):
        self.radius = radius  # Instance variable
    
    def area(self):
        return Circle.pi * (self.radius ** 2)

circle1 = Circle(5)
circle2 = Circle(10)

print(circle1.area())
print(circle2.area())
