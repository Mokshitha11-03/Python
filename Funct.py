#Q1
'''
def add(*args):
    print(args)

    sum=0
    for i in args:
        sum += i
    print(sum)

add(10, 20, 30, 40)
add(2, 7, 8)
'''

'''
from functools import reduce
lst = [10,20,30,40]
r = reduce(lambda x, y: x+y, lst)
print(r)
'''

'''
def multiply_all(*args):
    product = 1

    for i in args:
        product *= i
    print(product)

multiply_all(2, 9, 5, 7)
'''

'''
from functools import reduce
lst = [2, 9, 5, 7]
r = reduce(lambda x,y: x*y, lst)
print(r)
'''

'''
def mixed_function(a, b, *args, **kwargs):
    print(a, end = " ")
    print(b, end = " ")

    for i in args:
        print(i, end = " ")

    for k, v in kwargs.items():
        print(k, "=", v, end = " ")

mixed_function(10, 20, 20, 30, 40, name = "Mokshitha", age = 21, city = "Hyderabad")
'''

'''
def positional_def(a, c=2):
    print(a, c)

positional_def(2, 8)
'''

'''
def positional_keyword(a, b):
    print(a, b)

positional_keyword(20, b = "Mokshitha")
'''

