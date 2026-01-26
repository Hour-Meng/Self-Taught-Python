# object = A "bundle" of related variables and functions
#   Ex: Phone, Book, Mouse, Car, Motorcycle

#class = a blueprint for creating objects

from carOOP import car
    
car1 = car("Mustang", "Red", True, 20000)
car2 = car("Nissan R35", "Black", False, 100000)

print(car1.model)
print(car2.price)


car1.drive()
car2.stop()
car1.description()
car.description(car2)