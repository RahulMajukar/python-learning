# You can manually raise an exception using the raise keyword.

# Example:

def check_age(age):
    if age < 18:
        raise ValueError("You must be 18 or older!")
    else:
        print("Age verified.")
        
try:
    check_age(15)
except ValueError as e:
    print(e)