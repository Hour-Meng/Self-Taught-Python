# Abstract is to prevent other's using a specific method in the parent class.

from abc import ABC, abstractclassmethod
class Vehicle(ABC):
    @abstractclassmethod # with this all  the child class are required to have the same thing as the parent class too
    def go(self):
        print("Hi")
    @abstractclassmethod # since children doesn't has this function it won't run
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("The car is moving")
class Motorcycle(Vehicle):
    def go(self):
        print("The moto is moving")

car = Car()
moto = Motorcycle()
Vehicle.go()
car.go()
moto.go()