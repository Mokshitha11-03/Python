'''
4.Create a package with a module containing an abstract base class (ABC).
Another module in the same package should define concrete subclasses that implement
all abstract methods.Write a driver program that imports these classes and demonstrates polymorphism.
'''

from abstractPack4.shapes import Rectangle, Circle

r = Rectangle()
c = Circle()

print("Rectangle area:", r.area())
print("Circle area:", c.area())