# Base class
class Car:
    def fuel_type(self):
        pass

    def max_speed(self):
        pass


# First subclass
class BMW(Car):
    def fuel_type(self):
        return "Diesel"

    def max_speed(self):
        return "250 km/h"


# Second subclass
class Ferrari(Car):
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "340 km/h"


# Polymorphism in action
cars = [BMW(), Ferrari()]

for car in cars:
    print("Car Type:", car.__class__.__name__)
    print("Fuel Type:", car.fuel_type())
    print("Max Speed:", car.max_speed())
    print("------")
