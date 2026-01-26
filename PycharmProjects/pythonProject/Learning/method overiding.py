class Animal:
    def jump(self):
        print("The animal is jumping")

class kangkaroo(Animal):
    def jump(self):
        print("The kangkaroo is jumping over a wall")
class dog(Animal):
    pass
Dog = dog()

Kangkaroo = kangkaroo()


Kangkaroo.jump()

Dog.jump()


# with this method instead of printing "The animal is jumping"
# It will print "The kangaroo is jumping over a wall" specially just for the kangaroo