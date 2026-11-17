'''
def verify_user(func):
    def wrapper():
        print("User verified")
        func()
    return wrapper
def log_transaction(func):
    def wrapper():
        print("Transaction logged")
        func()
    return wrapper

@verify_user
@log_transaction
def check_balance():
    print("Hey user!")
check_balance()
'''

'''
def login_required(func):
    def wrapper(*args):
        func(*args)
    return wrapper
def log_activity(func):
    def wrapper(*args):
        func(*args)
    return wrapper

@login_required
@log_activity
def start_exam(student):
    print(f"Exam started for {student}")
start_exam("Mokshitha")
'''

'''
def login_check(func):
    def wrapper(*args):
        print("Login verified")
        func(*args)
    return wrapper
def order_log(func1):
    def wrapper(*args):
        print("Order recorded")
        func1(*args)
    return wrapper

@login_check
@order_log
def place_order():
    print("Order placed successfully")
place_order()
'''

'''
def log_operation(func):
    def wrapper(*args, **kwargs):
        print("Operation started")
        result = func(*args, **kwargs)
        print("Operation completed")
        return result
    return wrapper

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

@log_operation
def calculate(operation, a, b):
    return operation(a,b)

operation = input("Enter your operation: ")
if operation == 'add':
    result = calculate(add, 10, 5)
elif operation == 'subtract':
    result = calculate(subtract, 10, 5)
elif operation == 'multiply':
    result = calculate(multiply, 10, 5)
print(result)

square = lambda x: x*x
double = lambda x: x*2
cube = lambda x: x**3

print(square(4))
print(double(5))
print(cube(6))
'''

'''
def dec(func):
    def wrapper(*args, **kwargs):
        print("Processing started")
        result = func(*args, **kwargs)
        print("Processing completed")
        return result
    return wrapper

@dec
def process_marks(marks, operation):
    for mark in marks:
        print(operation(mark))

grace = lambda x: x+5
double = lambda x: x*2
greater_than_40 = lambda x: x>40

marks = [35, 45, 50, 30]

process_marks(marks, grace)
process_marks(marks, double)
process_marks(marks, greater_than_40)
'''


'''
def order_logger(func):
    def wrapper(*args, **kwargs):
        print("Order processing")
        result = func(*args, **kwargs)
        return result
    return wrapper

def payment_check(func):
    def wrapper(*args, **kwargs):
        print("Payment verification completed")
        result = func(*args, **kwargs)
        return result
    return wrapper

@order_logger
@payment_check
def process_order(price, discount_function):
    return discount_function(price)

discount10 = lambda price: price-(price*10/100)
discount20 = lambda price: price-(price*20/100)
discount100 = lambda price: price-100

print(process_order(180, discount10))
print(process_order(200,discount20))
print(process_order(250, discount100))
'''

'''
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Notification started")
        result = func(*args, **kwargs)
        print("Notification sent")
        return result
    return wrapper

@decorator
def send_notification(message, formatter):
    return formatter(message)

uppercase = lambda message: message.upper()
lowercase = lambda message: message.lower()
add = lambda message: message + "!!!"

print(send_notification("Hello Dear", lowercase))
print(send_notification("Good Afternoon", uppercase))
print(send_notification("Nice to meet you", add))
'''

#doubt
'''
def decorator(func):
    def wrapper(*args, **kwargs):
        print


def transaction(amount, operation):
    return operation(amount)

deposit = lambda amount: amount+

operation = input("Enter your operation: ")

if operation == 1:
    result = transaction(180, deposit)
elif operation == 3:
    result = transaction(360, balance_update)
elif operation == 2:
    result = transaction(258, withdraw)
'''



'''
class BankAccount:
    bank_name = "ABC Bank"

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number

        if balance < 0:
            self.balance = 0
        else:
            self.balance = balance

print("Person1 Details: ")
person1 = BankAccount("Mokshitha Sadula", 348345427352, 8000)
print(person1.__dict__)
print(person1.account_holder)
print(person1.account_number)
print(person1.balance)
print()

print("Person2 Details: ")
person2 = BankAccount("Mahendra", 3456789767890, -180)
print(person2.__dict__)
print(person2.account_holder)
print(person2.account_number)
print(person2.balance)
'''

'''
class Student:
    college = "ABC College"

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no

        if marks<=0 and marks>=100:
            self.marks = 0
        else:
            self.marks = marks

obj1 = Student("Mokshitha", "22K81A0550", 835)
print(obj1.__dict__)

obj2 = Student("Yamuna", "22K881A04J1", 700)
print(obj2.__dict__)
'''
doubt
'''
class Employee:
    company = "TechCorp"
    employee_count = 0
    
    def __init__(self, name, department, salary, experience):
        self.name = name
        self.department = department
        
        if salary<
'''

doubt
'''
class Product:
    store = "ShopEasy"
    
    def __init__(self, name, price, quantity):
        
        
        product_details = Product{}
'''






















