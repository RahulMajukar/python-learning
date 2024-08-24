# Polymorphism
# Polymorphism allows objects of different classes to be treated as objects of a common superclass. It means "many forms" and is achieved through method overriding, where a child class provides a specific implementation of a method that is already defined in its parent class.

class Bird:
    def fly(self):
        return "Bird can fly"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies at low altitude"

class Eagle(Bird):
    def fly(self):
        return "Eagle flies at high altitude"

# Polymorphism in action
def show_flight(bird):
    print(bird.fly())

sparrow = Sparrow()
eagle = Eagle()

show_flight(sparrow)  # Output: Sparrow flies at low altitude
show_flight(eagle)    # Output: Eagle flies at high altitude
