'''6. Create a class in a module that uses private attributes and
@property / @setter decorators. Import the class into another module and
show how encapsulation protects the data while still allowing controlled access.'''

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance")
