#15 SEPTEMBER

#Q1
'''
class PasswordUtils:
    @staticmethod
    def is_strong(password):
        digit_check = False
        upper_check = False
        for i in password:
            if i.isdigit():
                digit_check = True
            if i.isupper():
                upper_check = True
        return len(password)>=8 and digit_check and upper_check

    @staticmethod
    def generate_hint(password):
        print(password[0:2] + "***")

    @staticmethod
    def validate_email(email):
        return '@' in email and '.' in email
pwd = "ABXYZ@123"
PasswordUtils.generate_hint(pwd)
print(PasswordUtils.validate_email("mokshithasadula11@email.com"))
print(PasswordUtils.is_strong(pwd))
'''

#Q2
'''
class Library:
    library_name = "PY21 Library"
    def __init__(self, books_list, member_name):
        if member_name == "":
            raise ValueError("Name cannot be empty.")
        else:
            self.books_list = books_list
            self.member_name = member_name

    def add_book(self, title):
        if Library.is_valid_title(self, title):
            self.books_list.append(title)
            print("New Book Added Successfully!!")
        else:
            print("Enter a valid title:")

    @classmethod
    def create_guest(cls):
        return Library([], "Guest")

    def is_valid_title(self,title):
        return title != "" and title != "None"

user1 = Library(["ABC", "DEF"], "User1")
user1.add_book("PQL")
print(user1.books_list)
print(user1.member_name)
print(type(user1.books_list))
print(type("guest"))
print(user1.__dict__)
print()

user2 = Library(['LMN', "OPQ"], "User2")
print(user2.__dict__)

guest = Library.create_guest()
print(guest.member_name)
print(type(guest))
# guest = Library.create_guest()
# print(guest.member_name)
# print(type(guest))
'''

#Q1
'''
class Student:
    count = 0
    def __init__(self, student_name, rollno, marks):
        self.student_name = student_name
        self.rollno = rollno
        self.marks = marks
        Student.count += 1

    def display(self):
        print("Student Name:", self.student_name)
        print("Student Rollno:", self.rollno)
        print("Student Marks:", self.marks)
        print("Student Percentage:", self.calculate_percentage())
        print("Student Result:", Student.result(self.marks))

    def calculate_percentage(self):
        per = sum(self.marks)/len(self.marks)
        return per

    @classmethod
    def total(cls):
        print("Total student count:", cls.count)

    @staticmethod
    def result(marks):
        if sum(marks) >= 40:
            return "pass"
        else:
            return "fail"

s1 = Student("S1", 1, [50, 60, 70])
s1.display()
Student.total()

s2 = Student("S2", 2, [53, 80, 60])
s3 = Student("S3", 3, [79, 57, 85])
'''

#18 SEPTEMBER
#Multiples of Two using next()
'''
def m1():
    val = 2
    while True:
        yield val
        val += 2
x = m1()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
'''

'''
def fib():
    a,b = 0, 1
    while True:
        yield a
        a, b = b, a+b

obj = fib()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
'''

'''
l = [x*x for x in range(1, 11)]
print(l)
print(type(l))
'''

'''
s = {x*x for x in range(1, 11)}
print(s)
print(type(s))
'''

'''
d = {x:x*x for x in range(1, 11)}
#d = {x*x for x in range(1, 11)}
print(d)
print(type(d))
'''

'''
t = tuple(x for x in range(1, 11))
print(t)
print(type(t))
'''

'''
g = (x for x in range(1, 11) if x%2==0)
for i in g:
    print(i)
'''

'''
g = (x for x in range(1, 11) if x%2==0)
print(max(x for x in range(1, 11) if x%2==0))
'''

'''
g = (x for x in range(1, 11) if x%2==0)
print(min(x for x in range(1, 11) if x%2==0))
'''

'''
g = (x for x in range(1, 11) if x%2==0)
print(sum(x for x in range(1, 11) if x%2==0))
'''

'''
class Student:
    def __init__(self, name, age, marks, subjects):
        self.name = name
        self.age = age
        self.marks = marks
        self.subjects = subjects
    def __str__(self):
        return f"Hi! This is {self.name}"
    def __repr__(self):
        return f"Student ({self.name}, {self.marks}, {self.age}, {self.subjects}"
    def __contains__(self, item):
        return item in self.subjects
    def __len__(self):
        return len(self.subjects)
    def __add__(self, other):
        return self.age + other.age
    def __sub__(self, other):
        return self.marks - other.marks
    def __le__(self, other):
        return self.marks < other.marks
    def __hash__(self):
        return self.marks

mohana = Student("Mohana", 20, 90, ['Python Coding', 'Core Python'])
akhila = Student("Akhila", 21, 92, ['Python Coding'])
nikhith = Student("Nikhith", 22, 80, ['Python Coding', 'Core Python', 'SQL'])


print(str(mohana))
print(repr(mohana))
print("Python Coding" in mohana)
print(len(mohana))
print(len(akhila))
print(len(nikhith))
print(akhila + mohana)
print(mohana - nikhith)
print(akhila <= mohana)
print(hash(mohana))
'''


'''
class Number:
    def __init__(self, n):
        self.n = n
    def __add__(self, other):
        x = self.n + other.n
    def __sub__(self, other):
        return Number(self.n - other.n)
    def __mul__(self, other):
        return self.n / other.n
    def __truediv__(self, other):
        return self.n / other.n
    def __floordiv__(self, other):
        return self.n // other.n
    def __mod__(self, other):
        return self.n % other.n
    def __pow__(self, power, modulo=None):
        return self.n ** power
    def __lt__(self, other):
        return self.n < other.n
    def __gt__(self, other):
        return self.n > other.n
    def __le__(self, other):
        return self.n <= other.n
    def __ge__(self, other):
        return self.n >= other.n
    def __eq__(self, other):
        return self.n == other.n
    def __ne__(self, other):
        return self.n != other.n
    def __str__(self):
        return f"{self.n}"
    def __hash__(self):
        return self.n
n1 = Number(10)
n2 = Number(20)

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1//n2)
print(n1/n2)
print(n1%n2)
print(n1**n2)
print(n1>n2)
print(n1<n2)
print(n1>=n2)
print(n1<=n2)
print(n1==n2)
print(n1!=n2)
print(hash(n1))
'''