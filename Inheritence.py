#21 SEPTEMBER
'''
class Bank:
    def m1(self, balance):
        self.balance  = balance

    def deposit(self, amount):
        self.amount += balance

    def withdraw(self, amount):
        self.amount -= balance

    def check_balance(self):


obj = Bank()
obj.m1()
obj.deposit(1200)
obj.withdraw()
obj.check_balance()

class User(Bank):
    pass

obj1 = User()
obj1.Bank()
obj1.deposit()
obj1.withdraw()
obj1.check_balance()
'''


'''
class A:
    pass
class B(A):
    pass
class C(B):
    pass
class D(A):
    pass
class E(B, C, D):
    pass
print(E.mro())
print(E.__mro__)
'''

'''
class A:
    def __init__(self, x, y):
        print("A Class Constructor")
        self.x = x
        super().__init__(y)

class B:
    def __init__(self, y):
        self.y = y
        print("B Class Constructor")

class C(A, B):
    def __init__(self, x, y, z):
        print("C Class Constructor")
        self.z = z
        super().__init__(x, y)
c = C(10, 20, 30)
print(c.z)
print(c.y)
print(c.x)
'''

#Multi Level Inheritance
'''
class A:
    def __init__(self):
        print("A Class Constructor")
class B(A):
    def __init__(self):
        print("B Class Constructor")
        super().__init__()
class C(B):
    def __init__(self):
        print("C Class Constructor")
        super().__init__()
c = C()
'''

'''
class A:
    def __init__(self):
        print("A Class Constructor")
class B(A):
    def __init__(self):
        print("B Class Constructor")
        super().__init__()
class C(A):
    def __init__(self):
        print("C Class Constructor")
        super().__init__()

b = B()
c = C()
'''

'''
class A:
    def __init__(self):
        print("A Class Constructor")

class B(A):
    def __init__(self):
        print("B Class Constructor")
        super().__init__()

class C(A):
    def __init__(self):
        print("C Class Constructor")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D Class Constructor")
        super().__init__()

d = D()
print(D.mro())
print(D.__mro__)
'''

'''
class A:
    def m1(self):
        print("m1 = A class")
    @classmethod
    def m2(cls):
        print("A class method")

class B(A):
    def m1(self):
        print("m1 - B class")
        super().m1()
    @classmethod
    def m2(cls):
        print("B class method")
        super().m2()

class C(B):
    def m1(self):
        print("m1 - C class")
        super().m1()
    @classmethod
    def m2(cls):
        print("C class method")
        super().m2()

c = C()
c.m1()
c.m2()
C.m2()
'''

'''
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        self.amount = amount

class UPI(Payment):
    def pay(self, amount):
        print("Payment done through UPI", amount)
upi = UPI()
upi.pay(3000)

class CreditCard(Payment):
    def pay(self, amount):
        print("Payment done through creditcard", amount)
cc = CreditCard()
cc.pay(500)

class Cash(Payment):
    def pay(self, amount):
        print("Payment done through cash", amount)
c = Cash()
c.pay(2200)
'''

'''
from abc import ABC, abstractmethod
class DataStorage(ABC):
    def storage_property(self):
        pass

    @abstractmethod
    def save(self, data):

class 
'''

'''
from abc import ABC, abstractmethod
class Notification(ABC):
    def send(self, message):
        pass

class Email(Notification):
    def send(self, message):
        print("Sent a email message")
'''

#MOCK PREPARATION
#24 OCTOBER
#INHERITANCE
'''
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f'{self.name} makes a sound'

class Dog(Animal):
    def fetch(self):
        return f'{self.name} fetches the ball'

d = Dog('Rex')
print(d.speak())
print(d.fetch())
'''

'''
class Vehicle:
    def start(self):
        return 'Vehicle started'

class Car(Vehicle):
    def drive(self):
        return 'Car is driving'

class ElectricCar(Car):
    def charge(self):
        return 'Charging battery...'


ec = ElectricCar()
print(ec.start())
print(ec.drive())
print(ec.charge())
'''

'''
class Flyable:
    def fly(self):
        return 'I can fly!'

class Swimmable:
    def swim(self):
        return 'I can swim'

class Duck(Flyable, Swimmable):
    def quack(self):
        return 'Quack!'

d = Duck()
print(d.fly())
print(d.swim())
print(d.quack())
'''

'''
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

print(Circle(5).area())
print(Rectangle(4, 6).area())
'''

'''
class A:
    pass
class B:
    pass
class C:
    pass
class D(B, C):
    pass

print(D.__mro__)
print(D.mro())

for c in D.mro():
    print(c.__name__)
'''

#Q1
'''
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def info(self):
        super().info()
        print("Doors:", self.doors)

class ElectricCar(Car):
    def __init__(self, make, model, year, doors, battery_range):
        super().__init__(make, model, year, doors)
        self.battery_range = battery_range

    def info(self):
        super().info()
        print("Battery Range:", self.battery_range, "km")

v = Vehicle("Toyota", "Innova", 2022)
print("Vehicle Details:")
v.info()
print()

c = Car("Honda", "City", 2023, 4)
print("Car Details:")
c.info()
print()

e = ElectricCar("Tesla", "Model 3", 2025, 4, 500)
print("Electric Car Details:")
e.info()
'''

#Q2
'''
class Printable:
    def print_info(self):
        print("Printing document information")

class Saveable:
    def save(self):
        print("Document saved successfully")

class Document(Printable, Saveable):
    pass

d = Document()
d.print_info()
d.save()

print("\nMRO")
print(Document.mro())
'''

#Q3
'''
class A:
    def hello(self):
        return "A"

class B(A):
    def hello(self):
        return "B"

class C(A):
    def hello(self):
        return "C"

class D(B, C):
    def hello(self):
        return "D"

d = D()
print(d.hello())
print(D.mro())
'''

#Q4
'''
class School:
    def __init__(self, school_name):
        self.school_name = school_name
        print("School constructor called")

class Department(School):
    def __init__(self, school_name, department_name):
        super().__init__(school_name)
        self.department_name = department_name
        print("Department constructor called")

class Course(Department):
    def __init__(self, school_name, department_name, course_name):
        super().__init__(school_name, department_name)
        self.course_name = course_name
        print("Course constructor called")

    def display(self):
        print("School:", self.school_name)
        print("Department:", self.department_name)
        print("Course:", self.course_name)

c = Course("ABC School", "Computer Science", "Python")
c.display()
'''

#INHERITANCE PDF QUESTIONS
#Q1
'''
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Balance:", self.balance)

class User(Bank):
    def __init__(self, name, balance):
        super().__init__(balance)
        self.name = name

    def display(self):
        print("User Name:", self.name)

u = User("Mokshitha", 5000)
u.display()
u.deposit(2500)
u.check_balance()
u.withdraw(3700)
u.check_balance()
'''

'''
class Employee:
    def __init__(self, emp_name, salary):
        self.emp_name = emp_name
        self.salary = salary

    def display_details(self):
        print("Employee name:", self.emp_name)
        print("Salary:", self.salary)

class Manager(Employee):
    def __init__(self, emp_name, salary, bonus):
        super().__init__(emp_name, salary)
        self.bonus = bonus

    def display_total_salary(self):
        print("Bonus:", self.bonus)
        print("Total sal:", self.salary + self.bonus)

m = Manager("Rahul", 30000, 5000)
m.display_details()
m.display_total_salary()
'''

#Q3: . Student Result System
'''
Create a Student class with:
• Name 
• marks
• display_marks()
Create a Result class that inherits Student and calculates whether the student has 
passed or failed. '''

'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_marks(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

class Result(Student):
    def __init__(self, name, marks):
        super().__init__(name, marks)

    def result(self):
        if self.marks >= 35:
            print("Result: pass")
        else:
            print("Result: fail")

s = Result("Rahul", 75)
s.display_marks()
s.result()
'''

#Q4. Food Ordering System Using Multilevel Inheritance
'''
Class 1: Restaurant
• Create a method menu(item) that returns the price of the selected food
item.
Class 2: FoodCourt (inherits Restaurant)
Create the following methods:
• display_menu() – Display the available food items.
• order() – Accept the food item from the user and allow multiple orders.
• billing() – Display the total bill and add a packing charge of ₹20.
Class 3: Customer (inherits FoodCourt)
• Create an object of the Customer class.
• Call the order() method. '''

'''
class Restaurant:
    def menu(self, item):
        if item == "Pizza":
            return 180
        elif item == "Burger":
            return 100
        elif item == "Fries":
            return 60
        elif item == "Biryani":
            return 200

class FoodCourt(Restaurant):
    def display_menu(self):
        print("Available Food items: ")
        print("Pizza - 180rs")
        print("Burger - 180rs")
        print("Fries - 180rs")
        print("Biryani - 180rs")

    def order(self):
        self.total = 0
        self.display_menu()

        while True:
            item = input("Enter food item: ")
            price = self.menu(item)

            if price == 0:
                print("Invalid item")
            else:
                self.total += price
                print(item, price, "-rs")

            ch = input("Do yo want to order more? (Y/N):")
            if ch == "N" or ch == "no":
                break
        self.billing()

    def billing(self):
        print("Food Total:", self.total)
        print("Packing charge: rs20")
        print("Total Bill: rs", self.total + 20)

class Customer(FoodCourt):
    pass

c = Customer()
c.order()
'''

#Q5: Movie Ticket Booking System Using Multilevel Inheritance
'''
Class 1: Movie
• Create a method ticket(movie) that returns the ticket price. 
Class 2: Booking (inherits Movie)
Create the following methods:
• movies() – Display the available movies. 
• selection() – Allow the user to book multiple tickets. 
• billing() – Display the total amount and add a booking charge of ₹30. 
Class 3: Customer (inherits Booking)
• Create an object and call the selection() method. '''

'''
class Movie:
    def ticket(self, movie):
        if movie == "Hi Nanna":
            return 250
        elif movie == "Varsham":
            return 180
        elif movie == "Raja Rani":
            return 150
        else:
            return 0

class Booking(Movie):
    def movies(self):
        print("Available movies:")
        print("Hi Nanna - 250rs")
        print("Varsham - 250rs")
        print("Raja Rani - 250rs")

    def selection(self):
        self.total = 0
        self.movies()

        while True:
            movie = input("Enter movie name: ")
            price = self.ticket(movie)

            if price == 0:
                print("Movie unavailable")
            else:
                self.total += price
                print("Ticket price:", price)

            ch = input("Do you want to book more tickets? (Y/N):")
            if ch.upper() == "N":
                break
        self.billing()

    def billing(self):
        print("Movie ticket price:", self.total)
        print("Booking charge: 30rs")
        print("Final ticket price:", self.total + 30)

class Customer(Booking):
    pass

c = Customer()
c.selection()
'''

#6. Online Course Enrollment System Using Multilevel Inheritance
'''
Class 1: Course
• Create a method fee(course) that returns the course fee. 
Class 2: Academy (inherits Course)
Create the following methods:
• courses() – Display available courses. 
• enroll() – Allow the user to enroll in multiple courses. 
• billing() – Display the total fee and add a registration fee of ₹100. 
Class 3: Student (inherits Academy)
• Create an object and call the enroll() method. 
'''

'''
class Course:
    def fee(self, course):
        if course == "Python":
            return 30000
        elif course == "Java":
            return 32000
        elif course == "Data Analytics":
            return 28000
        else:
            return 0

class Academy(Course):
    def courses(self):
        print("Available courses:")
        print("Python - 30000")
        print("Java - 32000")
        print("Data Analytics - 28000")

    def enroll(self):
        self.total = 0
        self.courses()

        while True:
            course = input("Enter course name: ")
            price = self.fee(course)

            if price == 0:
                print("Course unavailable")
            else:
                self.total += price
                print("Course price: ", price)

            ch = input("Do you want to register more courses? (Y/N)")
            if ch.upper() == "N":
                break
        self.billing()

    def billing(self):
        print("Course fee:", self.total)
        print("Registration fee: 100rs")
        print("Total fee:", self.total + 100)

class Student(Academy):
    pass

s = Student()
s.enroll()
'''

#7. Cab Booking System Using Hierarchical Inheritance
'''
Class 1: Cab
• Create methods to calculate the fare for Bike, Auto, and Car rides. 
Class 2: Uber (inherits Cab)
• Create the methods menu(), booking(), and billing(). 
• Add 10% GST and apply a 15% discount if the bill is above ₹1000. 
Class 3: Ola (inherits Cab)
• Create the methods menu(), booking(), and billing(). 
• Add 12% GST and apply a 20% discount if the bill is above ₹1500. 
Driver Code
• Ask the user to choose Uber or Ola and call the booking() method. '''

'''
class Cab:
    def bike(self, distance):
        return distance * 10
    def auto(self, distance):
        return distance * 20
    def car(self, distance):
        return distance * 30

class Uber(Cab):
    def menu(self):
        print("Available Vehicle for Ride:")
        print("1.Bike - Rs.10/km")
        print("2.Auto - Rs.20/km")
        print("3.Car - Rs.30/km")

    def booking(self):
        self.menu()
        choice = input("Choose ride:")
        distance = int(input("Enter distance in km:"))

        if choice == 1:
            self.total = self.bike(distance)
        elif choice == 2:
            self.total = self.auto(distance)
        elif choice == 3:
            self.total == self.car(distance)
        else:
            print("Invalid choice")
            return
        self.billing()

    def billing(self):
        gst = self.total * 10/100
        amount = self.total + gst

        if amount > 1000:
            discount = amount * 15/100
        else:
            discount = 0

        print("Base Fare:", self.total)
        print("GST:", gst)
        print("Discount:", discount)
        print("Final Bill:", amount - discount)

class Ola(Cab):
    def menu(self):
        print("1.Bike - Rs.10/km")
        print("2.Auto - Rs.20/km")
        print("3.Car - Rs.30/km")

    def booking(self):
        self.menu()
        choice = input("Choose ride:")
        distance = int(input("Enter distance in km:"))

        if choice == "1":
            self.total = self.bike(distance)
        elif choice == "2":
            self.total = self.auto(distance)
        elif choice == "3":
            self.total = self.car(distance)
        else:
            print("Invalid choice")
            return
        self.billing()

    def billing(self):
        gst = self.total * 12/100
        amount = self.total + gst

        if amount > 1500:
            discount = amount * 20 / 100
        else:
            discount = 0

        print("Base Fare:", self.total)
        print("GST:", gst)
        print("Discount:", discount)
        print("Final Bill:", amount - discount)


print("Choose Cab Service")
print("1. Uber")
print("2. Ola")

choice = input("Enter your choice: ")

if choice == "1":
    u = Uber()
    u.booking()
elif choice == "2":
    o = Ola()
    o.booking()
else:
    print("Invalid cab service")
'''



#MULTIPLE INHERITANCE
#Q10. ATM System Using Multiple Inheritance
'''
Class 1: SBI
• Create the methods deposit(amount) and check_balance(). 
Class 2: UnionBank
• Create the methods withdraw(amount) and mini_statement(). 
Class 3: ATM (inherits SBI and UnionBank)
• Create the methods menu() and transaction(). 
• Allow the user to perform banking operations. 
Driver Code
• Create an object of the ATM class. 
• Call the transaction() method.'''

'''
class SBI:
    def deposit(self, amount):
        self.balance += amount

    def check_balance(self):
        print("Current balance:", self.balance)

class UnionBank:
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def mini_statement(self):
        print("Available balance:", self.balance)

class ATM(SBI, UnionBank):
    def menu(self):
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Check balance")
        print("4.Mini Statement")
        print("5.Exit")

    def transaction(self):
        self.balance = 1000

        while True:
            self.menu()
            choose = int(input("Enter your choice:"))

            if choose==1:
                amount = int(input("Enter deposit amount:"))
                self.deposit(amount)
            elif choose==2:
                amount = int(input("Enter withdrawal amount:"))
                self.withdraw(amount)
            elif choose==3:
                self.check_balance()
            elif choose==4:
                self.mini_statement()
            elif choose==5:
                print("Thank you, Please visit again")
                break
            else:
                print("Invalid choice")

c = ATM()
c.transaction()
'''

#11. Paytm Application Using Multiple Inheritance
'''
Write a Python program to implement a Paytm Application using multiple 
inheritance.
Class 1: MobileRecharge
• Create the methods recharge_plans() and mobile_recharge(). 
Class 2: BusTicketBooking
• Create the methods display_buses() and book_ticket(). 
Class 3: ElectricityBills
• Create the methods bill_details() and pay_bill(). 
Class 4: Paytm (inherits MobileRecharge, BusTicketBooking, and 
ElectricityBills)
Create the following methods:
• menu() – Display the available services. 
• services() – Allow the user to choose and use any service (Mobile 
Recharge, Bus Ticket Booking, or Electricity Bill Payment). '''

'''
class MobileRecharge:
    def recharge_plans(self):
        print("\nAvailable Recharge Plans:")
        print("1. 199 - 1.5GB/day")
        print("2. 299 - 2GB/day")
        print("3. 399 - 3GB/day")

    def mobile_recharge(self):
        mobile = input("Enter Mobile Number: ")
        self.recharge_plans()
        plan = int(input("Choose a plan (1-3): "))

        if plan == 1:
            print("Recharge of Rs.199 Successful!")
        elif plan == 2:
            print("Recharge of Rs.299 Successful!")
        elif plan == 3:
            print("Recharge of Rs.399 Successful!")
        else:
            print("Invalid Plan")


class BusTicketBooking:
    def display_buses(self):
        print("\nAvailable Buses:")
        print("1. Hyderabad to Bangalore")
        print("2. Hyderabad to Chennai")
        print("3. Hyderabad to Vijayawada")

    def book_ticket(self):
        self.display_buses()
        choice = int(input("Choose a bus (1-3): "))

        if choice == 1:
            print("Ticket booked: Hyderabad to Bangalore")
        elif choice == 2:
            print("Ticket booked: Hyderabad to Chennai")
        elif choice == 3:
            print("Ticket booked: Hyderabad to Vijayawada")
        else:
            print("Invalid Bus Selection")


class ElectricityBills:
    def bill_details(self):
        print("\nElectricity Bill Payment")
        print("1. TSSPDCL")
        print("2. TSNPDCL")

    def pay_bill(self):
        self.bill_details()
        consumer = input("Enter Consumer Number: ")
        amount = float(input("Enter Bill Amount: "))
        print("Bill Paid Successfully!")
        print("Consumer Number:", consumer)
        print("Amount Paid: Rs.", amount)


class Paytm(MobileRecharge, BusTicketBooking, ElectricityBills):
    def menu(self):
        print("\n===== WELCOME TO PAYTM =====")
        print("1. Mobile Recharge")
        print("2. Bus Ticket Booking")
        print("3. Electricity Bill Payment")
        print("4. Exit")

    def services(self):
        while True:
            self.menu()
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.mobile_recharge()

            elif choice == 2:
                self.book_ticket()

            elif choice == 3:
                self.pay_bill()

            elif choice == 4:
                print("Thank you for using Paytm!")
                break

            else:
                print("Invalid Choice! Try Again.")

obj = Paytm()
obj.services()
'''