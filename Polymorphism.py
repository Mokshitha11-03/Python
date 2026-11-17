        #POLYMORPHISM
#Practice Questions
#Q1: Method Overriding
'''
Build a payment system with a base class Payment(amount) and three subclasses: 
CreditCard, UPI, and NetBanking. Each overrides a method process() with its own 
logic. Write a function checkout(payment) that calls process() on any payment object 
and demonstrate polymorphism.'''

'''
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        print("Actual amount:", self.amount)
        print("Payment processing")

class CreditCard(Payment):
    def process(self):
        print("Paid using CreditCard", self.amount)

class UPI(Payment):
    def process(self):
        print("Paid using UPI", self.amount)

class NetBanking(Payment):
    def process(self):
        print("Paid using NetBanking", self.amount)

def checkout(payment):
    payment.process()

p = Payment(50000)
checkout(p)

c = CreditCard(4800)
checkout(c)

u = UPI(6000)
checkout(u)

n = NetBanking(8000)
checkout(n)
'''


#Q2: Duck Typing
'''
Create three completely unrelated classes: PDFReport, ExcelSheet, and 
EmailMessage. Each has a method send(). Write a function dispatch(item) that calls 
send() using duck typing. Prove that no inheritance is needed. '''

'''
class PDFReport:
    def send(self):
        print("Sending PDF Report")
class ExcelSheet:
    def send(self):
        print("Sending ExcelSheet")
class EmailMessage:
    def send(self):
        print("Sending Email Message")

def dispatch(item):
    item.send()

p = PDFReport()
dispatch(p)

e = ExcelSheet()
dispatch(e)

m = EmailMessage()
dispatch(m)
'''
#else you can call like this when you have same method names
'''
def dispatch():
    items = [PDFReport(), ExcelSheet(), EmailMessage()]

    for i in items:
        i.send()
dispatch()
'''

#Q3:Polymorphism + Duck Typing
'''
Write a function total_area(shapes) that takes a list of any shape objects and returns 
their combined area. Use duck typing — any object with an area() method should 
work. Test with Circle, Rectangle, Triangle, and a custom class Hexagon. '''

'''
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Hexagon:
    def __init__(self, side):
        self.side = side

    def area(self):
        return (3*1.732/2)*self.side*self.side

def total_area(shapes):
    total=0

    for i in shapes:
        total += i.area()
    return total

c = Circle(5)
r = Rectangle(30, 40)
t = Triangle(3, 6)
h = Hexagon(4)

shapes = [c, r, t, h]

result = total_area(shapes)
print("Total Area:", result)
'''
