'''
# elif

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a>b and a>c:
    print(a, "is gratest")
elif b>a and b>c:
    print(b, "is greatest")
else:
    print(c, "is greatest")
'''

#elif-ladder
'''
m = int(input("Enter m: "))

if m>=85 and m<=100:
    print("O+")
elif m>=70 and m<=84:
    print("A")
elif m>=55 and m<=67:
    print("B")
elif m>=40 and m<=54:
    print("C")
else:
    print("F")
'''

#nested-if
'''
n = int(input("Enter n: "))

if n%5==0:
    print(n, "is a multiple of 5")
    if n%3==0:
        print(n, "is mul of 3")
    else:
        print(n, "is not a mul of 5")
    print(5, "is a factor of ", n)
else:
    print(n, "is not a mul of 5")
    if n%7==0:
        print(n, "is a mul of 7")
    elif n%3==0:
        print(n, "is a mul of 3")
    else:
        print("nothing")
    print("tata")
print("bye")
'''