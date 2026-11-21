#SYNTAX TO IMPORT FROM MUL FILES: from pack_name.module_name import class_name

'''2. Create a Python package that contains two or more modules. Each module
should define classes with attributes and methods. Then create another module
outside the package, import the package modules, and create a subclass that
inherits from at least one of the classes. Finally, create objects of both
parent and child classes.'''


from Package.Animal2 import Animal
from Package.Vehicle2 import Vehicle

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

a = Animal("Lion")
a.display()

v = Vehicle("BMW")
v.show()

d = Dog("Tommy")
d.display()
d.bark()