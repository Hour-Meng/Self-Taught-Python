# Polymorphism = Green word that means to "have many forms or faces"
#                Poly = Many , Morph = Forms
#               Two ways to archieve polymorphism in python
#               1. Inherirance = When a child class inherits methods and properties from a parent class
#               2. Duck Typing

from abc import ABC, abstractmethod

class Shape():
    @abstractmethod

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radious):
        self.radious = radious

    def area(self):
        return 3.14 * self.radious**2

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2

class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return 0.5 * self.width * self.height
    
class Pizza(Circle):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius)


#circle = Circle()

# Here is what you need to note
# circle is an instance of Circle and also Shape but not Square or Triangle

shapes = [Circle(2), Square(3), Triangle(3, 4), Pizza(5)]
# Now to get the area of all shapes we can just loop through the list and call the area method

for i in shapes:
    print(i.area())
