# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code resuability and extensibility
#               class Child(Parent)


class mammal():
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating ")
    
    def sleep(self):
        print(f"{self.name} is sleeping ")

class dog_C(mammal):
    def speak(self):
        print("woof woof")

dog1 = dog_C("Dandy")
print(dog1.name)
dog1.eat()
dog1.sleep()
dog1.speak()

