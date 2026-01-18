class prey:
    def run(self):
        print("The animal is running")

class preditor:
    def hunt(self):
        print("The animal is hunting")

class dog(preditor):
    def bark(self):
        print("The dog is barking")
class worm(prey):
    def hide(self):
        print("The worm is hiding")
class fish(prey, preditor):
    def swim(self):
        print("The fish is swimming")
dog = dog()
worm = worm()
fish = fish()

dog.hunt()
worm.run()
fish.run()