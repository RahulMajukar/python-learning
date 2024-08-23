class Dog:
    # Class attribute
    species = "Canine"
    
    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Milo", 5)

# Accessing attributes and methods
print(dog1.description())
print(dog2.species)
