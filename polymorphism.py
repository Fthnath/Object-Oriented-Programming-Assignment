class Vehicle:
    def move(self):
        pass  # Abstract method

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Test polymorphism
vehicles = [Car(), Plane()]
for vehicle in vehicles:
    vehicle.move()
