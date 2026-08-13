from functools import reduce

'''
prices = [280, 52, 850, 980, 370, 650]

total = reduce(lambda x,y: x+y, 
               map(lambda x: x**0.9, 
                   filter(lambda x: x>500, prices)))
print(int(total))
'''

'''
numbers = [-280, 52, -850, 980, -370, 650]
total = reduce(lambda x,y:x+y, map(abs, filter(lambda x: x<0, numbers)))

print(total)
'''

'''
integers = [56, 76, 34, 76, 87]

total =list(map(lambda x: x*3, list(filter(lambda x: x<50, integers))))
print(reduce(lambda a, b: a if a>b else b, total))
'''

#27JULY
'''
def calculator(*args, operation='add', **options):
    op={'add': lambda x,y: x+y,
        'mul': lambda x,y: x*y,
        'min': lambda x,y: x if x<y else y,
        'max': lambda x,y: x if x>y else y}
    func = op['operation']
    res = args[0]
    for i in range(1, len(args)):
        res = func(res, args[i])
        if options.get('show_steps'):   #if True:
            print(res, i, operation, func(res, i))
        res = func(res, i)
    return res
'''

'''
from functools import reduce
lst = ['maDAm', 'Cat', 'beLlb', 'radaR']
print(reduce(lambda x,y: x+ ' ' + y,
             sorted(list(map(lambda x: x.lower(), 
             list(filter(lambda x: x[0] == x[-1], lst)))), 
             key = lambda x: (x[-1], len(x)))))
'''


students = [{'Alice', 85}, {'Bob', 74}, {'David', 88}]

#final = list(filter(lambda x: x['score'] >= 65, students))
final = list(filter(lambda x: x[1] >= 65, students))
results = list(map(lambda x: {**x, 'grade' : 'Pass'}, final))
print(results)
