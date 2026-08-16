#5-August
##FUNCTION DECORATORS:
#Ex1
'''
def decor(x):
    def inner(name):
        if name=='Sunny':
            print("Hello Sunny Bad Morning")
        else:
            x(name)
    return inner

#decorfunction = decor(wish)

#@decor #annotation
def wish(name):
    print("Hello", name, "good Evening")
wish('Durga')
wish('Ravi')
wish('Sunny')
#decorfunction('Sunny')
'''

#Ex2
'''
def smartdivision(func):
    def inner(a, b):
        if b==0:
            print("We can't divide with zero")
            return
        else:
            return func(a, b)
    return inner

@smartdivision
def division(a, b):
    return a/b

print(division(10,2))
print(division(10, 5))
print(division(10, 0))
'''

#Date: 6-AUGUST
#Q1
'''
def decorator(func):
    def wrapper():
        print("System starting")
        #func()
        print("System started successfully")
    return wrapper

def start_system():
    print("Hello")
started = decorator(start_system)
started()
'''

#Q2
'''
def decorator(func):
    def wrapper():
        print("Welcome!")
        func()
        print("Goodbye!")
    return wrapper
def show_message():
    print("hi")
msg = decorator(show_message)
msg()
'''

#Q3
'''
def decorator(func):
    def wrapper():
        print("Payment Initiated")
        print("Payment Successful")
    return wrapper
def make_payment():
    print("Pay 100rs")

paying = decorator(make_payment)
paying()
'''

#8-AUGUST
#Q1
''' Create a function place_order(item)
    Write a decorator that prints:
    * “Function started” before execution
    * “Function ended” after execution'''
'''
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        func()
        print("Function ended")
    return wrapper

def place_order(item):
    print("Hi")
place_order = decorator(place_order)
print(place_order())
'''

#Q2
''' Create a function greet(name)
    Write a decorator that adds:
    * “Welcome!” before
    * “Have a nice day!” after'''

'''
def decor(func):
    def wrapper(*args, **kwargs):
        print("Welcome!")
        func(*args)
        print("Have a nice day!")
    return wrapper

@decor
def greet(name):
    print("My name is", name)
#greet = decor(greet)
greet("Mokshitha")
'''

#Q3
''' Create a function transfer_money()
    Write a decorator that prints:
    * “Transaction started”
    * “Transaction successful” / “Transaction failed”
'''

'''
def decorator(func):
    def wrapper():
        print("Transaction started")
        func()
        print("Transaction successful")
    return wrapper

@decorator
def transfer_money():
    print("Hello")
#transfer_money = decorator(transfer_money)
transfer_money()
'''


#Q1
''' Create a function get_message() 
    that returns "hello user". 
    Write a decorator using @ syntax 
    that converts the output to uppercase.'''

'''
def decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@decorator
def get_message():
    return "hello user"
#get_message = decorator(get_message)
print(get_message())
'''

#Q2
''' Create a function get_number() that returns 10
    Use a decorator to return double the value.'''

'''
def decor(func):
    def wrapper():
        result = func()
        return result * 2
    return wrapper

@decor
def get_number():
    return 10
print(get_number())
'''

#Q3
''' Create a function place_order(item)
    Use a decorator to print:
    * “Order process started”
    * “Order process completed”'''

'''
def decor(func):
    def wrapper(*args):
        print("Order process started")
        func(*args)
        print("Order process completed")
    return wrapper

@decor
def place_order(item):
    print("hi")
place_order("Straightener")
'''

#Q4
''' Create a function login(username)
    Use a decorator to print:
    * “Authenticating user…”
    * “Login successful”'''

'''
def decor(func):
    def wrapper(*args):
        print("Authenticating User")
        func(*args)
        print("Login successful")
    return wrapper

@decor
def login(username):
    print("Hey")
login("Mokshitha")
'''

#Q5
''' Create a function send_message(msg)
    Use a decorator to print:
    * “Sending message…”
    * “Message sent”'''

'''
def decor(func):
    def wrapper(*args):
        print("Sending Message")
        func(*args)
        print("Message sent")
    return wrapper

@decor
def send_message(msg):
    print("Hi")
send_message("Good Morning!")
'''

#Q6
''' Create a function add(a, b)
    Use a decorator to print:
    * “Calculating sum…”
    * “Calculation done”'''

'''
def decorator(func):
    def wrapper(*args):
        print("Calculating sum")
        func(*args)
        print("Calculation done")
    return wrapper

@decorator
def add(a, b):
    print(a+b)
    return a+b
add(2, 5)
'''

#Q7
''' Create a function apply_discount(price)
    Use a decorator to print:
    * “Applying discount…”
    * “Discount applied”'''

'''
def deecor(func):
    def wrapper(*args):
        print("Applying discount")
        func(*args)
        print("Discount Applied")
    return wrapper

@deecor
def apply_discount(price):
    print("Hello")
apply_discount(500)
'''

#AUGUST 10
'''
from functools import wraps
def dec1(func):
    @functools.wraps(func)
    def wrap1(*args, **kwargs):
        print("hi")
        func(*args, **kwargs)
    return wrap1
def dec2(func):
    def wrap2(*args, **kwargs):
        func(*args, **kwargs)
        print("bye")
    return wrap2

#@dec1
#@dec2
def say_name(name):
    print("My name is", name)

#say_hello=dec1(say_name)
x = dec1(say_name)
x("Mokshitha")

#say_hello=dec2(say_name)
y=dec2(say_name)
y("Sadula")

#say_hello=dec2(say_name)
#say_name=wrap1
z=dec2(x)
z("Moksh")

#say_name(dec2(dec1(say_name)
print(z.__name__)    #o/p: wrap2
print(say_name.__name__)    #o/p: wrap2
'''



'''
def m1():
    print("hi")
print(m1.__name__)  #o/p: m1
'''

#11 AUGUST
#Q1
''' A banking application has a function check_balance(). 
    Create two decorators: verify_user, 
    which prints "User verified", and log_transaction, 
    which prints "Transaction logged". 
    Apply both decorators to check_balance() and 
    display "Balance displayed" from the original function.'''

'''
def verify_user(func):
    def wrapper(*args):
        print("User Verified")
        func(*args)
    return wrapper

def log_transaction(func):
    def wrapper():
        print("Transaction logged")
        func()
    return wrapper


@verify_user
@log_transaction
def check_balance():
    print("Balance Displayed")

check_balance()
'''

#Q2
''' An online examination system has a function start_exam(student). 
    Before allowing the student to start the exam, 
    the system must verify the student’s login and 
        then log the exam activity. 
    Create two decorators, login_required and log_activity, 
        and apply both decorators to start_exam(). 
    The function should finally display "Exam started for <student>".'''


'''
def login_required(func):
    def wrapper(*args):
        print("Logged in")
        func(*args)
    return wrapper

def log_activity(func):
    def wrapper(*args):
        print("Exam scheduled")
        func(*args)
    return wrapper

@login_required
@log_activity
def start_exam(student):
    print("Exam started for student", student)

start_exam("Mokshitha")
'''


#Q3
''' An online shopping application has a function place_order(). 
    Create two decorators: login_check to print "Login verified" and
        order_log to print "Order recorded". 
    Apply both decorators to place_order() and 
    display "Order placed successfully" from the original function.'''

'''
def login_check(func):
    def wrapper(*args):
        print("Login Verified")
        func()
    return wrapper

def order_log(func):
    def wrapper(*args):
        print("Order recorded")
        func()
    return wrapper

@login_check
@order_log
def place_order():
    print("Successful")

place_order()
'''



#14 AUGUST (Decorators Mixed with Funcs, Lambdas, FunReferences)
            #Decorators Questions
#Q1
''' Create functions add(a, b), 
    subtract(a, b) and multiply(a, b).
    Create a function calculate(operation, a, b) that 
    accepts a function reference and 
    performs the selected operation.

    Use lambda functions to perform:
    * Square of a number
    * Cube of a number
    * Double of a number

    Add a decorator log_operation that prints "Operation started" 
    before execution and "Operation completed" after execution.'''

'''
def log_operation(func):
    def wrapper(*args, **kwargs):
        print("Operation Started")
        result = func(*args, **kwargs)
        print("Operation Completed")
        return result
    return wrapper

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def multiply(a, b):
    return a*b

@log_operation
def calculate(operation, a, b):
    return operation(a, b)
print(calculate(add, 10, 5))  #if you are calling it only once, then the decorator prints operation started & completed only once
print()
print(calculate(sub, 8, 3))
print()
print(calculate(multiply,3, 5))
print()

square = lambda x: x * x
cube = lambda x: x ** 3
double = lambda x: x * 2

print(square(5))
print(cube(8))
print(double(7))
'''


#Q2
''' Create a function process_marks(marks, operation) 
    where operation is a function reference.

    Use lambda functions to:
    * Add 5 grace marks
    * Double each mark
    * Find whether a mark is greater than 40

    Create a decorator that prints "Processing started" and "Processing completed".'''

'''
def decor1(func):
    def wrapper(*args, **kwargs):
        print("Processing Order")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper


@decor1
def process_marks(marks, operation):
    result = []

    for mark in marks:
        result.append(operation(mark))

    return result

grace = lambda mark: mark + 5
double = lambda mark: mark * 2
greater = lambda mark: mark > 40

marks = [30, 45, 60, 35]

print(process_marks(marks, grace))
print()

print(process_marks(marks, double))
print()

print(process_marks(marks, greater))
'''


#Q3
''' Create a function process_order(price, discount_function).

    Pass different lambda functions to calculate:
    * 10% discount
    * 20% discount
    * ₹100 flat discount
    
    Create two decorators:
    * order_logger → logs the order processing
    * payment_check → prints "Payment verification completed"
    
    Apply both decorators to the function.'''

'''
def order_logger(func):
    def wrapper(*args, **kwargs):
        print("Order Processing")
        result = func(*args, **kwargs)
        return result
    return wrapper

def payment_check(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Payment Verified")
        return result
    return wrapper

@order_logger
@payment_check
def process_order(price, discount_function):
    return discount_function(price)

discount10 = lambda price: price - (price *10/100)
discount20 = lambda price: price-(price * 20/100)
discount100 = lambda price: price-100

print(process_order(290, discount20))
print(process_order(467, discount10))
print(process_order(318, discount100))
'''


#Q4
''' Create a function send_notification(message, formatter).

    Use lambda functions as formatter to:
    * Convert the message to uppercase
    * Convert the message to lowercase
    * Add "!!!" to the message
    
    Create a decorator that prints "Notification started" 
    before execution and "Notification sent" after execution.'''

'''
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Notification started")
        result = func(*args, **kwargs)
        print("Notification executed")
        return result
    return wrapper

@decorator
def send_notification(message, formatter):
    return formatter(message)

uppercase = lambda message: message.upper()
lowercase = lambda message: message.lower()
adding = lambda message: message + "!!!"

print(send_notification("Hello Guys", lowercase))
print()

print(send_notification("I Went to shopping", uppercase))
print()

print(send_notification("Bye", adding))
'''


#Q5
''' Create a function transaction(amount, operation).

    Pass different functions as operation:
    * Deposit
    * Withdrawal
    * Balance update
    
    Use a decorator to log every transaction.
    
    Create another decorator that 
    checks whether the transaction amount is greater than 0.
    
    Use two decorators together.'''

'''
def decor1(func):
    def wrapper(*args, **kwargs):
        print("Log Every Transaction")
        result = func(*args, **kwargs)
        return result
    return wrapper

def decor2(func):
    def wrapper(*args, **kwargs):
        if args[0]>0:
            result = func(*args, **kwargs)
            return result
        else:
            print("Invalid transaction amount")
    return wrapper

@decor1
@decor2
def transaction(amount, operation):
    return operation(amount)

def deposit(amount):
    return amount + 500

def withdrawal(amount):
    return amount-300

def balance_update(amount):
    return amount

print(transaction(530, deposit))
print()

print(transaction(379, balance_update))
print()

print(transaction(460, withdrawal))
'''