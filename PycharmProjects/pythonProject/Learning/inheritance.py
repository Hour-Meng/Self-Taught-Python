#Inheritance to pass to its ancestor.

class Animal:
    status = True

    def sleep(self):

        print("The animal is sleeping")

    def eat(self):

        print("The animal is eating")

    def rest(self):
        print("The animal is resting")

class Dog(Animal):

    def bark(self):
        print("The dog is barking ")

class Cat(Animal):
    pass
class Mouse(Animal):
    pass

dog = Dog()
cat = Cat()
mouse = Mouse()

dog.bark()