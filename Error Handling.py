#11 NOVEMBER
'''1• Create a class Person whose constructor takes age as an argument. Raise a
ValueError if the age is less than 0.'''
'''
class Person:
    def __init__(self, age):
        if age<0:
            raise ValueError("Age cannot be negative")
        self.age = age

#obj = Person(-21)
obj = Person(20)
print(obj.age)
'''

'''2• Write a function named find_length(obj) that uses a loop to calculate the length
of the given object without using the built-in len() function. The function should 
return the calculated length if the object is iterable. If a non-iterable object such
as an integer is passed, the function should raise and handle a TypeError, and print 
an appropriate error message explaining what happens when an integer is sent as input.'''
'''
def find_length(obj):
    c=0
    try:
        if isinstance(obj,(str,list,tuple)):
            for x in obj:
                c += 1
            return c
        elif isinstance(obj):
            for k,v in obj.items():
                c += 1
            return c
        else:
            raise TypeError("Obj must be string, list, tuple, dict")    #to raise the error
    # to handle the error
    except TypeError as e:
        #to handle the error
        print("Error:", e)
        print("Integer is not an iterable object.")

find_length(1234567)    #to handle the error
#print(find_length(1234567)) #if you want to raise an error.
'''

'''3• Create a class Student with an attribute marks. Implement a method 
set_marks(marks) that raises a ValueError if marks are not in the range 0 to 
100.'''
'''
class Student:
    #def __init__(self, marks):
    #    self.marks = marks

    def set_marks(self, marks):
        if marks<0 or marks>100:
            raise ValueError("Invalid Marks")
        self.marks = marks

s = Student()
s.set_marks(38)
#s.set_marks(-26)
#s.set_marks(128)
print(s.marks)
'''

'''4• Create a custom exception named InvalidAgeError. Create a class Voter with a 
method check_eligibility(age) that raises this exception if age is less than 18.'''
'''
class InvalidAgeError(Exception):
    pass

class Voter:
    def check_eligibility(self, age):
        if age<18:
            raise InvalidAgeError("Age is Invalid")
        self.age = age
        print("Eligible to vote", self.age)
v = Voter()
v.check_eligibility(25)
#v.check_eligibility(15)
#v.check_eligibility(-22)
print(v.age)
'''

'''5• Create a class BankAccount with an attribute balance. Implement a method 
withdraw(amount) that raises an exception if the withdrawal amount is greater 
than the available balance.'''
'''
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount>self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

b = BankAccount(2000)
b.withdraw(250)
print(b.balance)
'''

'''6• Create a class PasswordValidator with a method validate(password). Raise an 
exception if the password length is less than 8 characters.'''
'''
class PasswordValidator:
    def validate(self, password):
        if len(password) < 8:
            #raise
            raise ValueError("Required more characters")
        self.password = password

pv = PasswordValidator()
#pv.validate("")
pv.validate("mokshitha@112345678")
#pv.validate("mok@11")
print(pv.password)
'''

'''7• Create a class UserInput with a method get_integer(value). Handle ValueError 
and TypeError using separate except blocks.'''
'''
class UserInput:
    def get_integer(self, value):
        try:
            num = int(value)
            print(num)
        except ValueError as v:
            print("ValueError: Invalid integer value")
        except TypeError as t:
            print("TypeError: Invalid data type")

u = UserInput()
u.get_integer("123")
u.get_integer("abc")
u.get_integer(None)
'''

'''8• Create a base class Shape with a method area() that raises NotImplementedError. 
Create a child class Rectangle that overrides and implements the area method. '''
'''
class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented in child class") #if you raise error it will print

class Rectangle(Shape):
    #pass #Error
    def area(self):
        print("area")
r = Rectangle()
r.area()
'''

'''9• Create a class Service with a method that calls another method which raises an exception. 
Catch and handle the exception in the Service class. '''
'''
class Service:
    def m1(self):
        try:
            self.m2()
        except ValueError as e:
            print("Error handled:", e)

    def m2(self):
        raise ValueError("Something wrong")
s = Service()
s.m1()
#s.m2() #raises exception
'''

'''10• Create a class Transaction with a method process() that uses try, except, and 
finally blocks to ensure a cleanup message is always printed. '''
'''
class Transaction:
    def process(self):
        try:
            num = int("abc")
            print(num)
        except ValueError as v:
            print("Invalid transaction")
        finally:
            print("Cleanup completed. You are done")

t = Transaction()
t.process()
'''

'''11• Create a class LoginSystem with a method login(password) that raises an exception 
for an incorrect password and handles the exception outside the class. '''
'''
class LoginSystem:
    def login(self, password):
        if password=="Python21":
            raise ValueError("Incorrect password")
        print("Login successful")

l = LoginSystem()
try:
    l.login("Python")
    #l.login("Python21")
except ValueError as e:
    print("Error:", e)
'''