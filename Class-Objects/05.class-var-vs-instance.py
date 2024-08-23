class Counter:
    # Class variable (shared across all instances)
    class_count = 0
    
    def __init__(self):
        # Instance variable (unique to each instance)
        self.count = 0
        
        # Increment instance variable
        self.count += 1
        # Increment class variable
        Counter.class_count += 1
        
        print(f"Instance count: {self.count}, Class count: {Counter.class_count}")

# Creating objects
c1 = Counter()  # Instance count: 1, Class count: 1
c2 = Counter()  # Instance count: 1, Class count: 2
c3 = Counter()  # Instance count: 1, Class count: 3


# Instance Variable (self.count):
# This variable is initialized to 0 each time a new instance of the Counter class is created.
# It is incremented by 1 in the constructor (__init__), so each instance has its own count starting from 1.
# Class Variable (Counter.class_count):
# This variable is shared across all instances of the class.
# It is incremented by 1 each time a new instance is created, so it keeps track of the total number of Counter objects created.