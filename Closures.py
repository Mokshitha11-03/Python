'''
def greet(name):
    print("hi!", name)
say_hi = greet
say_hi("greet")
'''

'''
def m1():
    print("This is m1")
    def m2():
        print("hi")
    return m2
func = m1()
func()
func()
'''

'''
def m1():
    print("This is m1")
    def m2():
        print("hi")
    return m2
func = m1
func()
func()
'''

def m1():
    msg = "This is m1"
    def m2():
        print(msg)
    m2()
m1()