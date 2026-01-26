# multiple inheritance = inherit from more than one parent class, C(A, B)

# multilevel inheritance = inherit from a parent which inhenits from another parent C(B) <- B(A) <- A

class animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} eats")

    def sleep(self):
        print(f"{self.name} sleeps")

class prey(animal):
    def flee(self):
        print(f"{self.name} flees")

class predator(animal):
    def hunt(self):
        print(f"{self.name} hunts")

class Rabbit(prey):
    pass

class Lion(predator):
    pass

class Fish(predator, prey):
    pass

rabbit = Rabbit("John")
lion = Lion("Leo")
fish = Fish("Nemo")

rabbit.flee()
lion.hunt()
fish.flee()
fish.hunt()


rabbit.eat()