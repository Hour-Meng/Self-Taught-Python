

class Organism:
    status = True

class Animal(Organism):

    def eat(self):
        print("The animal is eating")

class Dog(Animal):

    def bark(self):
        print("The dog is barking")
dog = Dog()

print(dog.status)
dog.bark()
dog.eat()
