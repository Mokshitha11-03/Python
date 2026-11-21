''' 5. Create three modules: Module A: class Animal Module B: class Walkable
Module C: class Dog that inherits from both Animal and Walkable.
Demonstrate method resolution order (MRO) by calling overridden methods and
printing the MRO.'''

from animal import Animal
from walkable import Walkable

class Dog(Animal, Walkable):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()
d.walk()

print(Dog.__mro__)