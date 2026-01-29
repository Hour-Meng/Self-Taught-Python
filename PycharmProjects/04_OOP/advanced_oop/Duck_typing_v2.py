# Duck typing : if it walks like a duck it quacks like a duck then it must be a duck.


class Duck:

    def walk(self):
        print("The duck is walking. ")


    def quack(self):
        print("The duck is qwacking. ")
        print("You caught a duck")

class Chicken:
    def walk(self):
        print("The chicken is walking. ")


    def quack(self):
        print("Umm Chicken can't quack. ")
        print("Not a duck but you caught it anyway. ")

class Person:
    def catch(self, man):
        man.walk()
        man.quack()


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
if person.catch(man=duck):
    print("You caught a chicken")
else:
    print("You caught a duck")