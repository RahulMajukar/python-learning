# Encapsulation
# Encapsulation is the process of wrapping data (attributes) and methods into a single unit, the class. It also restricts access to certain attributes and methods to protect data from being modified directly.
# Private Attributes: In Python, prefixing an attribute with an underscore (_) or double underscore (__) makes it private or protected, which means it should not be accessed directly outside the class.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300
