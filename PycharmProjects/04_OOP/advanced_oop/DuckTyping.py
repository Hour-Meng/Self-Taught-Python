# Duck Typing = Another way to achieve polymorphism in python
#               The concept of duck typing is that 
#               "If it looks like a duck and quacks like a duck, it must be a duck"

class Animal():
    alive = True

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Car:
    
    alive = False

    def speak(self):
        return "Vroom!"
    

animals = [Dog(), Cat(), Car()]


for animal in animals:
    print(animal.speak(), animal.alive)