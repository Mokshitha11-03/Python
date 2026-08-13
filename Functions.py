#DATE: 16 July

#Q1: Write a function simple_interest(principal, rate=5, time=1) to calculate simple interest. Demonstrate different function calls by passing only required arguments and then overriding default values.
'''
def simple_interest(principal, rate=5, time=1):
    si = principal*rate*time/100
    return si
print(simple_interest(24))
print(simple_interest(12, 20, 7))
print(simple_interest(18, time=2))
'''


#Q2: 2. Create a function student_info(name, *subjects, **details) that prints a student’s name, subjects enrolled, and additional details like grade and school.
'''
def student_info(name, *subjects, **details):
    print("Student's Name =", name)

    print("Subjects enrolled --", end = " ")
    print(subjects)
    
    for detail,value in details.items():
        print(detail, ":", value)

student_info("Mokshitha", "Python", "Excel", "SQL", "Power BI", grade = 'A', school = "SR Digi School", city = "Nizamabad")
'''


#Q3: Write a function order_food(*items, **preferences) that accepts multiple food items and optional preferences like spice level or delivery time. Display the order summary.
'''
def order_food(*items, **preferences):
    
    print("Items available=", end = " ")
    for item in items:
        print(item)
    
    for prefering, value in preferences.items():
        print(prefering, ":", value)
    
order_food("Biryani", "Butter Naan", "Panner", "Raita", spice_level = "avg", estimated_delivery_time =  "35 mins", delivery_time = "25 mins")
'''


#Q4: Write a function shopping_cart(discount=0, *prices) that calculates the total price after applying a discount. Demonstrate calling the function with and without the discount argument.
'''
def shopping_cart(*prices, discount=0):
    total = sum(prices)
    final = total - (total*discount/100)

    print("Total Price:", total)
    print("Final Price:", final)
    #return total, final
#print(shopping_cart(29, 387, 27, 50))
shopping_cart(10, 100, 250, 496, 360)
shopping_cart(100, 250, 496, 360, discount=10)
'''


#Q5: Design a function register_user(username, role="user", *permissions, **details) that stores user information, including optional permissions and additional attributes.
'''
def register_user(username, role="Data Analyst", *permissions, **details):
    print("Username=", username)
    print("Role:", role)
    
    print("User permissions are:", end = " ")
    for i in permissions:
        print(i)
    
    print("User Details:")
    for detail, about in details.items():
        print(detail, ":", about)

register_user("Mokshitha Sadula", "Data Analyst", 'Access Database', 'Control OS', qualification = "BTech", experience = "8+ Years", city = "Hyderabd")
'''


#Q6: Write a program to create a list containing dictionaries. Perform a shallow copy and a deep copy of the list. Modify a value inside one of the dictionaries in the original list and display all lists. Explain the observed behavior.
'''
import copy

lsts = [
        {
            "FirstName": "Mokshitha",
            "LastName": "Sadula",
            "Role": "Data Analyst",
            "Qualification": "BTech",
            "Experience": "Fresher"
        }
    ]
print("Original list:", lsts)

shallow_copy = copy.copy(lsts)
lsts[0]["Role"] = "Software Engineer"
print("Final list:", lsts)
print("shallow copy:", shallow_copy)


deep_copy = copy.deepcopy(lsts)
lsts[0]["Experience"] = "2+ Years"
print("Final list:", lsts)
print("Deep copy:", deep_copy)
'''

#Q7: ⁠Define a function login(username, password="1234"). Demonstrate how default arguments work and explain a potential issue with using default passwords.
'''
def login(username, password = "1234"):
    print("Username:", username)
    print("Password:", password)

login("Mokshitha Sadula")
login("Mokshitha Sadula", "mokshitha11")
'''


#Q8: Write a function area(length, breadth=None) that calculates the area of a rectangle. If breadth is not provided, assume it is a square and compute accordingly.
'''
def area(length, breadth=None):
    if breadth is None:
        breadth = length
    
    return length * breadth

print(area(12, 20))
print(area(10))   #tell what it prints
'''

#Q9: Write a function calculate_score(base_score=0, *bonus_points, **penalties) that computes a final score after adding bonuses and subtracting penalties.
'''
def calculate_score(base_score=0, *bonus_points, **penalities):
    score = base_score

    for bonus in bonus_points:
        score += bonus
    
    for value in penalities.values():
        score -= value
    
    print("Final score:", score)

calculate_score(10, 203, 500, 8, 12, ball_gone = 200, broken_wickets = 38)
'''



#Q10: Design a function send_email(sender, receiver, subject="No Subject", *attachments, **options) that simulates sending an email with optional attachments and settings.
'''
def send_email(sender, receiver, subject="No Subject", *attachments, **options):
    print("Sender: ", sender)
    print("Receiver:", receiver)
    print("Subject:", subject)

    print("Attachments: ", end = "")
    for i in attachments:
        print(i)
    
    print("Options available = ", end = " ")
    for option, value in options.items():
        print(option, ":", value)

send_email("Mokshitha", "XXXCotiviti", "Requesting a Job offer", "Resume Shortlisting", joining_date = '21/09/2026', onboarding_data = "01/10/2026")
'''


'''
prices = [100, 250, 500, 550, 300, 118]
def add_tax(price):
    return price * 1.1
final_price = list(map(add_tax, prices))
final_prices = list(map(lambda x: x * 1.1, prices))
print(final_price)
print(final_prices)
'''


'''
usernames = ["jude", "harry", "alice", "vini"]
print(list(map(lambda x: x.upper(), usernames)))
print(list(map(lambda x: x.title(), usernames)))
'''


'''
prices = [100, 250, 500, 670, 345, 977]
print(list(filter(lambda x: x > 500, prices)))
print(list(map(lambda x: x * 5, prices)))
print(list(map(lambbda x: len(x), prices)))
'''


'''
numbers = [28, 45, 89, 56, 34, 67]
print(list(filter(lambda x: x > 50, numbers)))
'''


'''
multiples = [38, 27, 4, 12, 24, 68, 44]
print(list(filter(lambda x: x % 4 == 0, multiples)))
'''



from functools import reduce
'''
l = [1, 2, 3, 4]
print(reduce(lambda x, y: x+y, l))
'''

'''
l1 = [2, 4, 6, 8]
print(reduce(lambda x, y: x*y, l1))
'''

'''
l =[14, 16, 2, 32, 9, 6]
print(reduce(lambda x,y: x if x>y else y, l))
'''

'''
l = [1, 7, 14, 22, 19, 6, 8, 25]
u = list(map(lambda x: x//2, l))
print(list(filter(lambda x: x%2==1, l)))
print(list(filter(lambda x: x%2==1, u)))

print(list(filter(lambda x: x%2==1, list(map(lambda x: x//2, l)))))     #*******SinglePipeline Solution
'''

'''
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: x*3, list(filter(lambda x: x%2==0, l)))))
'''

'''
l = [23, 45, 67, 89, 97, 630]
print(list(filter()))
'''

#Syntax: lambda input: expression (Anonymous Func= func without name)
'''
s=lambda n: n*n
print(s(4))
'''

'''
s = lambda x: x*x
print(s(3))
print(lambda x: x*x)
'''

#20 JULY H/W
'''
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: x*3, list(filter(lambda x: x%2==0, l)))))
'''

'''
l=[12, 67, 34, 85, 42]
print(list(map(lambda x: x**2, list(filter(lambda x: x>20, l)))))
'''

'''
l = ["alice", "bob", "charlie", "david", "eve"]
print(list(map(lambda x: x.upper(),list(filter(lambda x: len(x) > 4, l)))))
'''

'''
l=[23, 54, 98, 23, 46, 71]
print(list(map(lambda x: sum+x, sum = list(filter(lambda x: x%5==0, l)))))
'''

'''
l = [45, 87, 98, 36, 76, 85]
print(list(map(lambda x: x+5, list(filter(lambda x: x>40, l)))))
'''

'''
l = ["apple", "banana", "cherry", "date"]
print(list(reduce(lambda x, y: x+y, l)))
'''

'''
l = [2, 5, 7, 4, 8, 9]
print(list(reduce(lambda x,y: x,y, l)))
'''

'''
l = [3, 6, 2, 7, 8, 4, 10, 80, 45]
print(list(map(lambda x: x+10, list(filter(lambda x: x%5==0, l)))))
'''



'''
l = [200, 530, 870, 580, 350]
print(list(map(lambda x: x*0.1, list(filter(lambda x: x>500, l)))))
print(list(map(lambda x: int(x*0.1), list(filter(lambda x: x>500, l)))))
'''