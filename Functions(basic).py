'''
def say_hello():
    print("Welcome to Python!")
say_hello()
'''

'''
def add(a, b):
    return a + b
print(add(5, 4))
'''

'''
def say_hi():
    print("hi")
print(say_hi())

#it takes the return stmnt automatically when return is not in the block of code.
'''

'''
def area_of_rectangle(length, width):
    return length * width
print(area_of_rectangle(7, 4))
'''

'''
def area_of_rectangle(lenght, width):
    return length * width
print(area_of_rectangle(2))
'''

#We use functions to remove code redundancy and reuse the code to perform a specific task.

'''
def add(a, b):
    print(a+b)
add(5, 4)
'''

'''
def multiply(a, b, c):
    c = a * b * c
    return c
print(multiply(3, 4, 2))
'''

'''
def describe_pet(animal, name):
    print("My", animal, "is named as", name)
describe_pet("[lion]", "[king]")
'''

'''
def des():
    print("hello")
des("lion", 10)  #TypeError: des() takes 0 positional arguments but 2 were given
'''

'''
def power(base, exponent):
    return base ** exponent
print(power(3, 12))
'''

'''
def full_name(first, middle, last):
    c = first + middle + last
    return c
print(full_name("mokshitha ", "sadula ", "nizamabad"))
'''

'''
#Scenario Question: Create an applicatn of a simple ATM sys, where a user attempts to withdraw(or) deposit money.The progrm should verify if sufficient balance is available, then perform implement this using multiple functions. 
balance = int(input("Enter balance: "))
withdraw_amount = int(input("Enter amount: "))

if(balance >= withdraw_amount):
    print("Sufficient balance available, You can able to withdraw your", withdraw_amount, "rs.")
    print("Your", withdraw_amount, "has deposited from your TGB account")
elif(balance <= withdraw_amount):
    print("Unable to withdraw your money")
else:
    print("Bye")
'''

'''
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a//b
print(div(mul(add(40, 20), sub(40, 20)), 10))
'''

'''
def discount(price):
    return price*0.1

def final_price(price, discount_amount):
    return price -discount_amount

amount = 10000
discount = discount(amount)
final_price = final_price(amount, discount)
print("Your  final amount is", final_price)
print("Your final amount is:", final_price(amount, discount(amount)))
'''
'''
total_fare = int(input("Enter total_fare: "))
driver_name = input("Driver name: "))
pickup = input("Enter pickup location: ")
drop = input("Enter drop location: ")
'''

'''
def trip_Details(total_fare, driver_name, pickup, drop):
    print("Trip Details: ", total_fare, driver_name, pickup, drop)
    return driver_name
trip_Details(pickup = "KPHB", drop = "Kompally", total_fare = 500, driver_name = "Raju")
'''

'''
def trip_Details(total_fare, driver_name, pickup, drop):
    print("Total fare of drive:", total_fare)
    print("Driver name:", driver_name)
    print("Pickup location: ", pickup)
    print("Drop location: ", drop)
    return driver_name, total_fare, pickup, drop
x = trip_Details(500, "Raju", "KPHB", "Kompally")
print(trip_Details)
'''

'''
def send_email(to, subject, body):
    return to, subject, body
print(send_email(subject = "Asking for 1 day leave.", to = "To CV corp", body = "Requesting for a leave"))
'''


'''
def m1():           #method/function is a object
    print("hi")
print(type(m1))

hi = m1
hi()
'''


'''
def m1(name, age):           #method/function is a object
    print("hi")
print(type(m1))

hi = m1
hi("Mokshitha", 21)
'''


'''
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b

calculate = [add,sub,mul]
print(calculate[0] (10,20))
operations = {'+':add, '-':sub, '*':mul}

op = input("Enter a and b:")
print(operations[op](20,30))
'''


'''
def add(a,b):
    print("Addition:",a,b)
def sub(a,b):
    print("Subtraction:", a,b)
def mul(a,b):
    print("Multiplication:", a,b)
def div(a,b):
    print("Division:", a,b)

result(a,b) = add, sub, mul, div
print(result(a, b))
'''


'''
def square(a):
    return a**2
    
val = square(2)
print(square(val))
'''


'''
def square(a):
    return a**2
    
val = square(2)
print(square(square(2)))
'''


'''
def twice(func, val):
    return func(func(value))
print(twice())

def cube(a):
    return a**3
    print(twice(cube, 10))
    print(twice(square, 2))
'''

#We can do in 3-ways: store in var, store in list/tuple store in func
'''
#Length of List
def lists(lst):   
    print(len(lst))
lists([10,20,30,20,60])


#Length of List using count var
'''

'''
def lsts(lst):
    count=0
    for i in lst:
        print(i)
        count += 1
    print(count)
lists =[3,7,9,5,7,8,6]

print("Length of list:",len(lists))
lsts(lists)
'''

#Assign the built in function sum to a variable and use it to calculate total of a list of numbers.
'''
def lsts(lst):
    val = sum(lst)
    return val
result = lsts([3,5,3,7,8])
print(result)
'''

#Store functions min, max, sum in a dictionary allow the user to choose which operation to perform.
'''
def func():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    operations = {
        "min": min,
        "max": max,
        "sum": sum
    }

    choice = input("Choose operation (min/max/sum): ")

    if choice == "min":
        print("Result:", operations[choice](a, b))
    elif choice == "max":
        print("Result:", operations[choice](a, b))
    elif choice == "sum":
        print("Result:", operations[choice]([a, b]))
    else:
        print("Invalid choice")

func()
'''

#Write a function repeat with parameters function, n, value.
'''
def repeat(func, n, value):
    for i in range n:
        func *= n
        return func

repeat(12, 3, 7)
'''

'''
def square(a):
    return a**2

def cube(a):
    return a**3

def twice(func, val):
    return func(val)

print(twice(cube, 2))
print(twice(square, 3))
'''