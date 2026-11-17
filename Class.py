# 24 - AUGUST
'''
class A:
    pass
obj1 = A()
print(type(obj1))
print(id(obj1))

obj2 = A()
print(type(obj2))
print(id(obj2))
'''
from multiprocessing import process

'''class A:
    x = 10
    def __init__(self, y):
        self.age = y
        self.grade = 7'''


# 25 - AUGUST
'''
class Employee:
    org = 'CV CORP'
    count = 0
    def __init__(self, name, eno):
        self.name = name  #self.name = mokshitha
        self.eno = eno    #self.eno = 267867897
        self.exp = 'Fresher'
#obj1 = Employee()
#print(obj1.name)
#obj1.name = "mokshi"
#obj1.exp = 10
#print(obj1.name)
#print(obj1.__dict__)
#obj2 = Employee()
#print(obj2.__dict__)

#obj3 = Employee()
#obj3.salary = 10000
        Employee.count += 1

emp_details = Employee("Mokshitha", 1011171372)
print(emp_details.name)
print(emp_details.eno)
print(emp_details.org)

emp1 = Employee("Someone", 2839102279)
print(emp1.eno)
print(emp1.name)
print(emp1.org)

emp_details.org = "Microsoft"
print(emp_details.org)

#Class Dictionary

print(Employee.__dict__)
print(emp_details.__dict__)
print(emp1.__dict__)

emp_details.__dict__['salary'] = 100000
print(emp_details.__dict__)
print(emp1.__dict__)

emp1.org = "Meta"
print(emp1.__dict__)
print(Employee.count)


#print(obj1.__dict__)
#print(obj2.__dict__)
#print(obj3.__dict__)
print(Employee.__dict__)
'''


# 26 - AUGUST
'''
class Student:

    def __init__(self, age):
        if age>=18:
            self.age = age
        else:
            #print(ValueError)
            raise ValueError("Age is less than 18")
        self.age = age
s = Student(19)
print(s.age)
'''


# 26-AUGUST
#Q1
'''
class BankAccount:
    bank_name = "ABC Bank"
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number

        if balance<0:
            self.balance = 0
        else:
            self.balance = balance

print("Person1 Details: ")
obj1 = BankAccount("Mokshitha Sadula", 2345678567, -12)
print(obj1.account_holder_name)
print(obj1.account_number)
print(obj1.balance)

obj1.balance = 8
print(obj1.balance)

print("Person2 Details: ")
obj2 = BankAccount("Mahendra", 2345678989, 126)
print(obj2.account_holder_name)
print(obj2.account_number)
print(obj2.balance)
'''


#Q2
'''
class Student:
    college = "ABC College"
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.marks = marks
        self.roll_no = roll_no

        if 0<=marks<=100:
            self.marks = marks
        else:
            self.marks = 0

print("Object1 Details: ", end = "")
obj1 = Student("Mokshitha", 22810550, 81)
print(obj1.roll_no, end = ", ")
print(obj1.name, end = ", ")
print(obj1.marks)

print("Object2 Details: ", end = "")
obj2 = Student("Rashmi", 23456789, -32)
print(obj2.name, end = ", ")
print(obj2.roll_no, end = ", ")
print(obj2.marks)

print("Object3 Details: ", end = "")
obj3 = Student("Meena", 45678234, 258)
print(obj3.name, end = ", ")
print(obj3.roll_no, end = ", ")
print(obj3.marks)
'''


#Q3
'''
products = []
class Product:
    store_name = "ABC Store"

    def __init__(self, name, price, quantity):
        self.name = name

        if price>0 or quantity>0:
            self.price = price
            self.quantity = quantity

        else:
            # print("Invalid quantity or price")
            raise ValueError("Invalid quantity or price")
        products.append(name)


p1 = Product("Mars Lip Liner", 79, 5)
p2 = Product("Dior Lip Gloss ", 5000, -4)
p4 = Product("PS5", 50000, 4)
p3 = Product("Kay Beauty Lip Oil", 799, 1)
print(p1.__dict__)
print(p2.__dict__)
print(products)
'''


# 28 - AUGUST
#Q1
'''
class Employee:
    company = "TechCorp"
    employee_count = 0

    def __init__(self, name, department, salary, experience):
        self.name = name
        self.department = department
        self.salary = salary
        self.experience = experience

        if salary<0 or experience<0:
            raise ValueError("Invalid salary or experience")


        if experience > 5:
            bonus = salary * 15/100

        elif experience >= 3 and experience <= 5:
            bonus = salary * 10/100

        elif experience < 3:
            bonus = salary * 5/100
        final_salary = salary + bonus

        Employee.employee_count += 1
        self.employee_id = Employee.employee_count

        self.pay_details = {
            "name" : name,
            "salary" : salary,
            "experience" : experience,
            "bonus" : bonus,
            "final salary": final_salary
        }

emp1 = Employee("Mokshitha", "CSE", 50000, 3)
emp2 = Employee("Mahendra", "HR", 40000, 5)
emp3 = Employee("Rashmi", "IT", 36700, 2)

print(emp1.__dict__)
print(emp2.__dict__)
print(emp3.__dict__)
'''

#Q2
'''
class MobilePurchase:
    store_name = "Smart Mobiles"
    purchase_count = 0
    
    def __init__(self, customer, brand, price, storage, quantity):
        self.customer = customer
        self.brand = brand
        self.price = price
        self.storage = storage
        self.quantity = quantity
        
        if price<=0 or quantity<=0 or storage not in (64, 128, 256, 512):
            raise ValueError("Invalid price, storage or quantity")

        total_price = price + quantity

        if total_price > 50000:
            discount = total_price * 10/100
        else:
            discount = total_price * 5/100

        final_price = total_price - discount

        MobilePurchase.purchase_count += 1

        self.purchase_details = {
            "customer" : customer,
            "brand" : brand,
            "price" : price,
            "storage" : storage,
            "quantity" : quantity
        }

customer1 = MobilePurchase("Mokshitha", "GooglePixel", 100000, 128, 1)
customer2 = MobilePurchase("Mahendra", "Iphone", 80000, 256, 3)
customer3 = MobilePurchase("Rashmi", "Samsung", 38000, 64, 5)

print(customer1.__dict__)
print(customer1.purchase_details)
print(customer2.__dict__)
print(customer3.__dict__)
'''


#Q3
'''
class Product:
    store = "ShopEasy"
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        self.product_details = {
            "product name" : name,
            "price" : price,
            "quantity" : quantity,
            #"total price" : total_price
        }

prod1 = Product("Lip Liner" , 250, 7)
prod2 = Product("Nail Polish" , 200, 4)

print(prod1.__dict__)
print(prod1.product_details)

prod1.price = 300               #change price using instance variable
print(prod1.__dict__)

prod1.product_details['price'] = 480      #change price inside the dictionary
print(prod1.__dict__)
print(prod2.__dict__)
'''


'''
class Phone:
    os = "Android"

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


phn1 = Phone('OnePlus', 5000)
print(phn1.brand)
print(phn1.os)
print(phn1.__dict__)
print()

phn2 = Phone('Vivo', 30000)
print(phn2.price)
print(phn2.os)
print(phn2.brand)
print(phn2.__dict__)
'''


'''
class A:
    def __init__(self, y, z):
        self.y = y
        self.z = z

obj1 = A(30, 40)
print(obj1.z)
print(obj1.y)
print(obj1.__dict__)
print()

obj2 = A(800, 350)
print(obj2.y)
print(obj2.z)
print(obj2.__dict__)
'''


# *******
'''
class Student:
    def __init__(self, age):
        if age >= 18:
            self.age = age
        else:
            print("Error: Student is not Eligible to vote")

def display_age(obj):
    print("Age:", obj.age)

age = int(input("Enter age: "))

obj1 = Student(age)
print(obj1.age)
print(obj1.__dict__)

if age >= 18:
    display_age(obj1)
'''


'''
class A:
    pass

obj = A()
print(obj.__class__)
print(obj.__class__.__name__)
print(isinstance(obj, A))   #isinstance(object, class)
print(type(obj) is A)
print(obj.__class__ is A)
'''


'''
class A:
    pass
obj = A()
print(obj.__class__)
#print(obj.A())     #class A has no attribute error
'''




'''
class A:
    def m1(self):
        print("hi")
        print(self)
obj1 = A()
print(obj1)
obj1.m1()

obj2 = A()
print(obj2)
obj2.m1()
'''


'''
class Account:
    def checkbalance(self, balance, deposit, withdraw):
        self.balance = balance
        self.deposit = balance+deposit
        self.withdraw = balance-withdraw

        print("Final balance: ", self.balance)
        print("Deposit Amount: ", self.deposit)
        print("Withdraw Amount: ", self.withdraw)

obj1 = Account()
obj1.checkbalance(1000, 200, 150)
'''


'''
class Account:
    def check_balance(self, balance, deposit, withdraw):
        self.balance = balance
        self.deposit = balance+deposit
        self.withdraw = balance-withdraw

        print("Final Balance: ", self.balance)
        print("Amount Deposited: ", self.deposit)
        print("Amount Withdrawn: ", self.withdraw)

obj1 = Account()
obj1.check_balance(1000, 200, 150)
'''


'''
class Bank:
    def __init__(self, accno, pin, balance):
        self.accno = accno
        self.pin = pin
        self.balance = balance
        print("Account Creation Successful!")
        
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Your account has been debited with Rs.", amount)
            else:
                print("You have insufficient Funds!")
        else:
            print("You've entered an invalid amount.")
            
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Your account has been credited with Rs.", amount)
        else:
            print("You've entered an invalid amount.")
            
    def check_balance(self):
        print("Your current available balance is Rs.", self.balance)

mokshitha = Bank(123456, 1110, 100000)
yesmitha = Bank(111111, 2704, 200000)
akhila = Bank(934774,1406, 5)

user = input("Please enter your name:")
if user == 'mokshitha':
    ac = int(input('Enter Your Account Number:'))
    if ac == mokshitha.accno:
        pin = int(input("Enter Your Pin :"))
        if pin == mokshitha.pin:
            print("Hey !", user)
            while True:
                print("1.Withdraw\n2.Deposit\n3.Check Balance")
                choice = int(input("Enter the operation you want to perform:"))
                if choice == 1:
                    mokshitha.withdraw(int(input("Enter the amount you want to withdraw :")))
                elif choice == 2:
                    mokshitha.deposit(int(input("Enter the amount you want to deposit :")))
                elif choice == 3:
                    mokshitha.check_balance()
                else:
                    break
        else:
            print("Incorrect Pin.")
    else:
        print("Incorrect Account Number.")
elif user == 'yesmitha':
    ac = int(input('Enter Your Account Number:'))
    if ac == yesmitha.accno:
        pin = int(input("Enter Your Pin :"))
        if pin == yesmitha.pin:
            print("Hey !", user)
            while True:
                print("1.Withdraw\n2.Deposit\n3.Check Balance")
                choice = int(input("Enter the operation you want to perform:"))
                if choice == 1:
                    yesmitha.withdraw(int(input("Enter the amount you want to withdraw :")))
                elif choice == 2:
                    yesmitha.deposit(int(input("Enter the amount you want to deposit :")))
                elif choice == 3:
                    yesmitha.check_balance()
                else:
                    break
        else:
            print("Incorrect Pin.")
    else:
        print("Incorrect Account Number.")
elif user == 'akhila':
    ac = int(input('Enter Your Account Number:'))
    if ac == akhila.accno:
        pin = int(input("Enter Your Pin :"))
        if pin == akhila.pin:
            print("Hey !", user)
            while True:
                print("1.Withdraw\n2.Deposit\n3.Check Balance")
                choice = int(input("Enter the operation you want to perform:"))
                if choice == 1:
                    akhila.withdraw(int(input("Enter the amount you want to withdraw :")))
                elif choice == 2:
                    akhila.deposit(int(input("Enter the amount you want to deposit :")))
                elif choice == 3:
                    akhila.check_balance()
                else:
                    break
        else:
            print("Incorrect Pin.")
    else:
        print("Incorrect Account Number.")
else:
    print("Invalid User.")
Bank.check_balance(akhila)
Bank.deposit(akhila, 2000)
'''


'''
class Zomato:
    restaurant_no = 0
    restaurants = []
    discount = 0.2
    coupon_Code = "PY21"
    def __init__(self, restaurant_name, restaurant_menu):
        self.restaurant_name = restaurant_name
        self.restaurant_menu = restaurant_menu
        
        Zomato.restaurant_no += 1
        Zomato.restaurants.append(restaurant_name)
        
        self.restaurant_id = Zomato.restaurant_no
Pista_House = Zomato("Pista House",
                     {"Chicken Biryani" : 220,
                                    "Mutton Biryani" : 300,
                                    "Shawarma" : 100
                                     })
Paradise = Zomato("Paradise",
                     {"Chicken Biryani" : 250,
                                    "Mutton Biryani" : 350,
                                    "Coke" : 70,
                                    "Apricot Delight" : 120
                                     })
McDonalds = Zomato("McDonalds",
                     {"Chicken Burger" : 120,
                                    "Veg Burger" : 100,
                                    "Coke" : 70,
                                    "Fries" : 120
                                     })
def take_order(restaurant, item_no):
    items = list(restaurant.restaurant_menu.items())
    price = items[item_no - 1][1]
    
    print("Your Cart Value is :", price )
    uc = input("Do you want to checkout? Y/N")
    code = input("Do you have a coupon code ? Y/N")
    
    if code == 'Y' or code == 'y':
        couponcode = input("Enter the Coupon Code:")
        if couponcode == Zomato.coupon_Code:
            price = price - (price * Zomato.discount)
        else:
            print("Invalid Coupon Code.")
    print("Your Final Price Rs.", price)
c = 0
for restaurant in Zomato.restaurants:
    c += 1
    print(c , restaurant)

choice = int(input("Enter your choice of restaurant :"))

if choice ==  1:
    c = 0
    for item in Pista_House.restaurant_menu:
        c += 1
        print(c, item, "Rs. ", Pista_House.restaurant_menu[item])
    order =  int(input("Enter Your Item No: "))
    take_order(Pista_House, order)
elif choice == 2:
    c = 0
    for item in Paradise.restaurant_menu:
        c += 1
        print(c, item, "Rs.",Paradise.restaurant_menu[item])
    order =  int(input("Enter Your Item No: "))
    take_order(Paradise, order)
elif choice == 3:
    c = 0
    for item in McDonalds.restaurant_menu:
        c += 1
        print(c ,item,"Rs.", McDonalds.restaurant_menu[item])
    order =  int(input("Enter Your Item No: "))
    take_order(McDonalds, order)
else:
    print("Invalid Choice")
#'''


#Perfect Code
'''
class Zomato:
    restaurant_no = 0
    restaurants = []
    discount = 0.2
    coupon_code = "PY21"

    def __init__(self, restaurant_name, restaurant_menu):
        self.restaurant_name = restaurant_name
        self.restaurant_menu = restaurant_menu

        Zomato.restaurant_no += 1
        Zomato.restaurants.append(restaurant_name)

        self.restaurant_id = Zomato.restaurant_no

PistaHouse = Zomato("Pista House", {"chicken biryani" : 220, "mutton biryani" : 300, "shawarma" : 100})
Paradise = Zomato("Paradise", {"chicken biryani" : 220, "mutton birtyani" : 300, "coke" : 70, "Apricot Delight" : 120})
McDonalds = Zomato("Mc Donalds", {"chicken biryani" : 120, "veg burger" : 100, "coke" : 70, "fries" : 120})

def take_order(restaurant, item_no):
    items = list(restaurant.restaurant_menu.items())
    price = items[item_no - 1][1]
    print("Your cart value is: ", price)
    co = input("Do you want to checkout ? Y/N")
    code = input("Do you have a coupon ? Y/N")
    
    if code == "Y" or code == "y":
        couponcode = input("enter the coupon code: ")
        if couponcode == Zomato.coupon_code:
            price = price - (price*Zomato.discount)
        else:
            print("Invalid Coupon Code")
    print("Your final price rs.", price)
    
c = 0
for restaurant in Zomato.restaurants:
    c += 1
    print(c, restaurant)
choice = int(input("Enter your choice of restaurant: "))

if choice == 1:
    c = 0
    for item in PistaHouse.restaurant_menu:
        c += 1
        print(c, item, "Rs.", PistaHouse.restaurant_menu[item])
    order = int(input("Enter your item no: "))
    take_order(PistaHouse, order)
elif choice == 2:
    c = 0
    for item in Paradise.restaurant_menu:
        c += 1
        print(c, item, "Rs.", Paradise.restaurant_menu[item])
    order = int(input("Enter your item_no: "))
    take_order(Paradise, order)
elif choice == 3:
    c = 0
    for item in McDonalds.restaurant_menu:
        c += 1
        print(c, item, "Rs.", McDonalds.restaurant_menu[item])
    order = int(input("Enter your item_no: "))
    take_order(McDonalds, order)
else:
    print("Invalid choice")
'''

'''
class Employee:
    company = "TechCorp"
    employee_count = 0

    def __init__(self, name, department, salary, experience):
        self.name = name
        self.department = department
        self.salary = salary
        self.experience = experience

        if salary<0 or experience<0:
            print("Invalid salary or experience")

        if experience>5:
            bonus = salary*15/100
        elif 3>=experience<=5:
            bonus = salary*10/100
        elif experience<3:
            bonus = salary*5/100
    final_salary = salary + bonus

        Employee.employee_count += 1
        self.employee_id = Employee.employee_count

        self.pay_details = {"name": name,
                            "department": department,
                            "salary": salary,
                            "experience": experience,
                            "bonus": bonus,
                            "final salary": final_salary
        }

Emp1 = Employee("Mokshitha", "CSE", 234500, 3)
Emp2 = Employee("Rakshmi", "IT", 456456, 4)
Emp3 = Employee("Nayani", "CSE", 560450, 2)
print(Emp1.__dict__)
print(Emp2.__dict__)
print(Emp3.__dict__)
'''


'''
class Employee:
    company = "TechCorp"
    employee_count = 0

    def __init__(self, name, department, salary, experience):
        self.name = name
        self.department = department
        self.salary = salary
        self.experience = experience

        if salary<0 or experience<0:
            raise ValueError("Invalid salary or experience")


        if experience > 5:
            bonus = salary * 15/100

        elif experience >= 3 and experience <= 5:
            bonus = salary * 10/100

        elif experience < 3:
            bonus = salary * 5/100
        final_salary = salary + bonus

        Employee.employee_count += 1
        self.employee_id = Employee.employee_count

        self.pay_details = {
            "name" : name,
            "salary" : salary,
            "experience" : experience,
            "bonus" : bonus,
            "final salary": final_salary
        }

emp1 = Employee("Mokshitha", "CSE", 50000, 3)
emp2 = Employee("Mahendra", "HR", 40000, 5)
emp3 = Employee("Rashmi", "IT", 36700, 2)

print(emp1.__dict__)
print(emp2.__dict__)
print(emp3.__dict__)
'''

'''
class MobilePurchase:
    store_name = "Smart Mobiles"
    purchase_count = 0

    def __init__(self, customer, brand, price, storage, quantity):
        self.customer = customer
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.storage = storage

        if price<=0 or quantity<=0 or storage not in(64, 128, 256, 512):
            print("Invalid price or quantity or storage")

        total_price = price*quantity
        if total_price > 50000:
            discount = price * 10/100
        else:
            discount = price * 5/100

        final_amount = total_price - discount

        MobilePurchase.purchase_count += 1
        self.purchase_details = {
            'customer': customer, 'brand': brand,
            'price': price, 'storage': storage,
            'quantity': quantity, 'discount': discount,
            'final_amount': final_amount
        }

Purchase1 = MobilePurchase("M", "OnePlus", 3700, 64, 2)
Purchase2 = MobilePurchase("N", "GPixel", 58800, 128, -3)
Purchase3 = MobilePurchase("O", "Iphone", 79000, 115, 3)

print(Purchase1.__dict__)
print(Purchase2.__dict__)
print(Purchase3.__dict__)

print(Purchase1.purchase_details)
print(Purchase2.purchase_details)
print(Purchase3.purchase_details)
print(MobilePurchase.purchase_count)
'''

'''
class Product:
    store = "ShopEasy"

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        total_price = price * quantity

        self.product_details = {
            'name': name, 'price': price,
            'quantity': quantity, 'total_price': total_price
        }

Prod1 = Product("OnePlus", 4500, 2)
print(Prod1.__dict__)
Prod1.price = 7800
print(Prod1.__dict__)
Prod1.product_details['price'] = 6700
print(Prod1.__dict__)
print(Prod1.product_details)
print()

Prod2 = Product("Iphone", 6000, 5)
print(Prod2.__dict__)
'''


'''
_username = "mokshitha"
_password = "12345"

successful_attempts = 0
unsuccessful_un_attempts = 0
unsuccessful_pw_attempts = 0

def dec1(func):
    def wrap1(*args, **kwargs):
        print("Welcome to our application! Please log in to continue")
        func(*args, **kwargs)
    return wrap1

@dec1
def login(username, password):
    global successful_attempts, unsuccessful_un_attempts, unsuccessful_pw_attempts

    if username == _username and password == _password:
        print("Login successful")
        successful_attempts += 1
        return

    elif username != _username:
        unsuccessful_un_attempts += 1
        if unsuccessful_un_attempts <= 3:
            username = input("This un not exists. Enter again: ")
            login(username, password)
        else:
            print("Youre out of attempts. Try again later.")
            return

    else:
        unsuccessful_pw_attempts += 1
        if unsuccessful_pw_attempts <= 3:
            password = input("Wrong pw. Enter your pw again: ")
            login(username, password)
        else:
            print("Youre out of attempts. Try again later.")
            return

login(input("Enter Username: "), input("Enter Password: "))

print("Unsuccessful Password attempts: ", unsuccessful_pw_attempts)
print("Unsuccessful Username attempts: ", unsuccessful_un_attempts)
print("Successful attempts: ", successful_attempts)
'''


'''
class Zomato:
    restaurant_no = 0
    restaurants = []
    discount = 0.2
    coupon_code = "PY21"

    def __init(self, restaurant_name, restaurant_menu):
        self.restaurant_name = restaurant_name
        self.restaurant_menu = restaurant_menu

        Zomato.restaurant_no += 1
        Zomato.restaurants.append(restaurant_name)

        self.restaurant_id = Zomato.restaurant_no

PistaHouse = Zomato("Pista House", {"chicken biryani": 220,
                                     "mutton biryani": 300,
                                     "shawarma": 100})

Paradise = Zomato("Paradise", {"chicken biryani": 220,
                                "mutton biryaani": 300,
                                "coke": 50,
                                "Apricot delight": 120})

McDonalds = Zomato("Mc Donalds", {"chicken biryani": 120,
                                  "veg burger": 100,
                                   "coke": 70,
                                   "fries": 120})

def take_order(restaurant, item_no):
    items = list(restaurant.restaurant_menu.items())
    price = items[item_no-1][1]

    print("Your cart value is:", price)
    co = input("Do you want to checkout? (Y/N)")
    code = input("Do you have any couponcode? (Y?N)")

    if code == "Y" or code == "y":
        couponcode = input("Enter your couponcode: ")
        if couponcode == Zomato.coupon_code:
            price = price - (price*Zomato.discount)
        else:
            print("Invalid coupon code")
    print("Your final price rs.", price)

c = 0
for restaurant in Zomato.restaurants:
    c += 1
    print(c, restaurant)
choice = int(input("Enter your choice of restaurant: "))

if choice == 1:
    c=0
    for item in PistaHouse.restaurant_menu:
        c += 1
        print(c, item, PistaHouse.restaurant_menu[item])
    order = int(input("Enter your item no: "))
    take_order(PistaHouse, order)

elif choice == 2:
    c=0
    for item in Paradise.restaurant_menu:
        c+=1
        print(c, item, Paradise.restaurant_menu[item])
    order = int(input("Enter your item no: "))
    take_order(Paradise, order)

elif choice == 3:
    c=0
    for item in McDonalds.restaurant_menu:
        c += 1
        print(c, item, McDonalds.restaurant_menu[item])
    order = int(input("Enter your item no: "))
    take_order(McDonalds, order)

else:
    print("Invalid choice")
'''


'''
class Bank:
    def __init__(self, accno, pin, balance):
        self.accno = accno
        self.pin = pin
        self.balance = balance
        print("Account creation successful")

    def withdraw(self, amount):
        if amount>0:
            if amount <= self.balance:
                self.balance = -amount
                print("Your account has debited with Rs.", amount)
            else:
                print("You have insufficient funds")
        else:
            print("You've entered invalid amount")

    def deposit(self, amount):
        if amount>0:
            self.balance = self.balance+amount
            print("Your account has credited with Rs.", amount)
        else:
            print("You've entered invalid amount")


    def check_balance(self):
        print("Your final balance is Rs.", self.balance)

mokshitha = Bank(123456, 1110, 10000)
yesmitha = Bank(111111, 2704, 200000)
akhila = Bank(00000, 1406, 5)

user = input("Please enter your name: ")
if user == "mokshitha":
    ac = int(input("Enter your accno: "))
    if ac == mokshitha.accno:
        pin = int(input("Enter your pin: "))
        if pin == mokshitha.pin:
            print("Hey!", user)
            while True:
                print("1.Withdraw\n 2.Deposit\n 3.CheckBalance")
                choice = int(input("Enter your chocie to perform : "))
                if choice == 1:
                    mokshitha.withdraw(int(input("Enter amount to WD: ")))
                    break
                elif choice == 2:
                    mokshitha.deposit(int(input("Enter amount to D: ")))
                    break
                elif choice == 3:
                    mokshitha.check_balance()
                    break
        else:
            print("Wrong pin")
    else:
        print("Invalid accno")
else:
    print("Invalid user")

Bank.check_balance(mokshitha)
Bank.deposit(mokshitha, 350)
'''