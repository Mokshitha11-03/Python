'''7. Create a module containing two classes where one uses composition
and another uses inheritance to reuse code from a base class. Import
and demonstrate the difference between the two approaches. '''

# Base class
class Vehicle:
    def start(self):
        print("Vehicle is starting")


# Inheritance
class Car(Vehicle):
    def drive(self):
        print("Car is driving")


# Composition
class Engine:
    def start_engine(self):
        print("Engine is starting")


class Bike:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start_engine()
        print("Bike is ready")
