#18-JULY

#Q1
'''
product_prices = [250, 300, 550, 400, 680]
mapping = list(map(lambda x: x*0.1, product_prices))
print(mapping)
'''

#Q2
'''
usernames = ["mokshitha", "rishitha", "ruthika", 'john', 'bob', 'david']
mapping = list(map(lambda x: x.title(), usernames))
print(mapping)
'''

#Q3
'''
products = [560, 380, 938, 847, 253, 851, 241, 390, 389]
filtering = list(filter(lambda x: x>500, products))
print(filtering)
'''

#Q4
'''
lst = [10, 28, 37, 49, 59]
mapping = list(map(lambda x: x*5, lst))
print(mapping)
'''

#Q5
'''
strings = ["Alice", "Bob", "Carol", "David", "Elvin", "Steeven"]
mapping = list(map(lambda x: len(x), strings))
print(mapping)
'''

#Q6
'''
integers = [28, 38, 49, 27, 50, 69, 38, 17, 83, 93]
filtering = list(filter(lambda x: x>50, integers))
print(filtering)
'''


#18-JULY
#Q1
'''
numbers = [2, 4, 8, 10, 12, 15, 16, 18, 10, 22]
filtering = list(filter(lambda x: x%4==0, numbers))
print(filtering)
'''
#Q2
'''
integers = [6, 2, 3, 4, 7, 9]
mf = list(map(lambda x: x*3, list(filter(lambda x: x%2==0, integers))))
print(mf)
'''
#Q3
'''
numbers = [29, 71, 15, 3, 9, 75, 14]
mf = list(map(lambda x: x*x, list(filter(lambda x: x>20, numbers))))
print(mf)
'''

#Q3
'''
words = ['Alice', 'Bob', 'Jhon', 'Mam', 'Sir', 'Teacher']
mf = list(map(lambda x: x.upper(), list(filter(lambda x: len(x)>4, words))))
print(mf)
'''

#Q4
'''
integers = [12, 87, 15, 36, 72, 90]
mf = list(map(lambda x: x+10, list(filter(lambda x: x%5==0, integers))))
print(mf)
'''

#Q5
'''
student_marks = [38, 49, 72, 94, 50, 66]
mf = list(map(lambda x: x+5, list(filter(lambda x: x>40, student_marks))))
print(mf)
'''

#Q6
'''
from functools import reduce
strings = ['Alice', 'Bob', 'Carol', 'Marley']
mf = reduce(lambda x, y: x + y, strings)
print(mf)
'''

#Q7
'''
from functools import reduce
digits = [1, 2, 3, 4]
r = reduce(lambda x, y: x*10+y, digits)
print(r)
'''

#Q8
'''
from functools import reduce
numbers = [93, 74, 39, 85, 19]
r = reduce(lambda x, y: x-y, numbers)
print(r)
'''

#Q9
'''
from functools import reduce
student_marks = [50, 93, 85, 49, 75]
total_marks = reduce(lambda x, y: x+y, student_marks)
print(total_marks)
print(total_marks/len(student_marks))
'''

#Q10
'''
product_prices = [480, 950, 690, 740, 370]
f = list(filter(lambda x: x>500, product_prices))
m = list(map(lambda x: x*0.9, f))
print(m)
'''


#JULY-23
#Q1
'''
from functools import reduce
product_prices = [380, 850, 280, 840, 547]
total_bill = reduce(lambda x,y: x+y, list(map(lambda x: x*0.1, list(filter(lambda x: x>500, product_prices)))))
print(total_bill)
'''

#Q2
'''
from functools import reduce
numbers = [-28, 94, 38, -92, 48]
f = list(filter(lambda x: x<0, numbers))
print(f)
m = list(map(lambda x: abs(x), f))
print(m)
r = reduce(lambda x,y: x if x>y else y, m)
print(r)
'''

#Q3
'''
from functools import reduce
integers = [28, 93, 79, 54, 12]
f = list(filter(lambda x: x>50, integers))
m = list(map(lambda x: x*3, f))
r = reduce(lambda x, y: x if x>y else y, m)
print(r)
'''

#Q4
'''
from functools import reduce
words = ['Alice', 'Bob', 'Carol', 'Marley', 'Jhon']
f = list(filter(lambda x: len(x)>3, words))
m = list(map(lambda x: x.upper(), f))
r = reduce(lambda x,y: x+y, m)
print(r)
'''

#Q5
'''
from functools import reduce
salaries = [25000, 38000, 17000, 500000, 45000]
f = list(filter(lambda x: x>30000, salaries))
m = list(map(lambda x: x*0.15, f))
total_salary = reduce(lambda x, y: x+y, m)
print(total_salary)
'''

#Q6
'''
from functools import reduce
integers = [28, 91, 16, 53, 63]
f = list(filter(lambda x: x%2==0, integers))
m = list(map(lambda x: x*x, f))
r = reduce(lambda x, y: x+y, m)
print(r)
'''

#Q7
'''
from functools import reduce
product_prices =[240, 950, 470, 678, 369, 481, 600]
f = list(filter(lambda x: x>500, product_prices))
m = list(map(lambda x: x*0.1, f))
total_bill_amount = reduce(lambda x,y: x+y, m)
print(total_bill_amount)
'''

#Q8
'''
from functools import reduce
amounts = [-250, 987, -478, -780, 582, 140]
f = list(filter(lambda x: x>0, amounts))
m = list(map(lambda x: x+10, f))
total_credited_amount = reduce(lambda x, y: x+y, m)
print(total_credited_amount)
'''


#JULY-25
#Q1
'''
lst = [('Alice', 85), ('Bob', 45), ("Carol", 97), ("David", 80), ('Marley', 95)]
lst.sort(key=lambda x: x[1], reverse=True)
print(lst)
lst.sort(key=lambda x: x[0])
print(lst)
'''

#Q2
'''
strings = ['Alice', 'Marley', 'Bob', 'Carol', 'Davidson']
strings.sort(key = lambda x: len(x))
print(strings)
strings.sort(key = lambda x: x[0])
print(strings)
'''

#Q3
'''
from functools import reduce
integers = [15, 28, 90, 78, 84, 10]
f = list(filter(lambda x: x%2==0 and x%5==0, integers))
print(f)
r = reduce(lambda x,y: x*y, f)
print(r)
'''

#Q4 (****)
'''
from functools import reduce
words = ['Level', 'Madam', 'Apple', 'Radar', 'Python', 'Anna', 'Malayalam']
f = list(filter(lambda x: x[0].lower()==x[-1].lower(), words))
print(f)
m = list(map(lambda x: x.lower(), f))
print(m)
m.sort(key = lambda x: (x[-1], len(x)))
print(m)
r = reduce(lambda x, y: x + " " + y, m)
print(r)
'''

#Q5 (****)(DOUBT)
'''
from functools import reduce
transactions = [
                {"type": "credit", "amount": 1000},
                {"type": "debit", "amount": 500},
                {"type": "credit", "amount": 2000}
]

f = list(filter(lambda x: x["type"]=="credit", transactions))
#print("Filter: ", f)
print(f)
m = list(map(lambda x: x['amount']+0.05, f))
print(m)
#print("Map: ", m)
sort = m.sort(key = lambda x: x["amount"], reverse = True)
#print("Sorted: ", m)
print(m)
total = reduce(lambda x,y: x+y, map(lambda x: x["amount"], f))
#print("Reduce: ", total)
print(total)
'''


#Mixed Concept Challenges
#Q1
'''
def apply_function(a, b, op):
    return op(a, b)

print(apply_function(10, 5, lambda x, y: x+y)) #add
print(apply_function(10, 5, lambda x, y: x-y)) #sub
print(apply_function(10, 5, lambda x, y: x*y)) #mul
'''

#Q2 (Recursion)

#Q3
'''
def make_greeting(name, prefix = "Hello", formatter = lambda x: x):
    greeting = f"{prefix} {name}"
    return formatter(greeting)

print(make_greeting("Mokshitha"))
print(make_greeting("Mokshitha", formatter=str.upper))
print(make_greeting("Mokshitha", "Hi", formatter=str.upper))
'''

#Q4
'''
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
f = list(filter(lambda x: x%3==0, integers))
m = list(map(lambda x: x*x, f))
print(m)
'''

#Q5
'''
double = lambda x: x*2
triple = lambda x: x*3
quadraple = lambda x: x*4

funcs = [(double), (triple), (quadraple)]

def apply_all(funcs, value):
    for func in funcs:
        value = func(value)
    return value

result = apply_all(funcs, 5)
print(result)
'''

#Q6 (RECURSION)

#Q7 (DOUBT)
'''
from functools import reduce

def weighted_average(**scores):
    marks = scores.values()

    total = reduce(lambda x, y: x+y, marks)

    count=0
    for subject in scores:
        count += 1

    average = total/count
    return average

result = weighted_average(
    Math = 90,
    English = 80,
    Science = 85
)

print(result)
'''

#Q8
'''
students = [
            {"name": "Ram", "score": 75},
            {"name": "Sita", "score": 55},
            {"name": "John", "score": 90},
            {"name": "Anu", "score": 60},
            {"name": "Raj", "score": 45}
]

f = list(filter(lambda x: x["score"] >= 60, students))
m = list(map(lambda x: {**x, "grade": "Pass"}, f))
m.sort(key = lambda x: x["score"], reverse = True)
print(m)
'''

#Q9
'''
students ={
    ("Ram", 75),
    ("Sita", 55),
    ("John", 90),
    ("Anu", 60),
    ("Raj", 45)
}

strategies = {
                "by_score": lambda x: x[1],
                "by_name": lambda x: x[0],
                "by_length": lambda x: len(x[0])
}

choice = input("Enter (by_score/by_name/by_length): ")

result = sorted(students, key = strategies[choice])
print(result)
'''

#Q10 (DOUBT)