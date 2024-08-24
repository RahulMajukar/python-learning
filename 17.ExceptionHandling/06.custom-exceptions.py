# You can create your own exceptions by subclassing the Exception class.

# Example:

class MyCustomError(Exception):
    pass

def test_custom_error(x):
    if x > 100:
        raise MyCustomError("Value is too large!")
        
try:
    test_custom_error(150)
except MyCustomError as e:
    print(e)