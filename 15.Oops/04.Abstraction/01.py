# 5. Abstraction
# Abstraction hides the complexity of the system and exposes only the essential features. In Python, abstraction can be achieved using abstract base classes (ABCs), which define abstract methods that must be implemented by subclasses.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(10, 20)
print(rect.area())  # Output: 200