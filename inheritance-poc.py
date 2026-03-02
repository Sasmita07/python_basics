class Vehicle:
    def general_usage(self):
        print("General usage of Vehicle")

class Car(Vehicle):
    def __init__(self):
        print("Inside Car class")
        self.wheel = 4;
        self.has_roof = True
    
    def specific_usage(self):
        self.general_usage()
        print("Car Usage")

class MotorCycle(Vehicle):
    def __init__(self):
        print("Inside MotorCycle class")
        self.wheel = 2;
        self.has_roof = False
    
    def specific_usage(self):
        self.general_usage()
        print("MotorCycle Usage")

c = Car()
c.specific_usage()

m = MotorCycle()
m.specific_usage()

print(isinstance(c, Car))
print(isinstance(c, MotorCycle))

print(issubclass(Car, Vehicle))
print(issubclass(Car, MotorCycle))