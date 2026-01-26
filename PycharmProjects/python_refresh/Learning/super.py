# super() = Function used in a child class to call methods from a parent class ( super class)
#           Allows you to extend the functionality of the inherited methods

class Shape():
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"This shape is {self.color} and {"filled" if self.filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color, filled, radious):

        super().__init__(color, filled)

        self.radious = radious

    def describe(self):
        print(f"The total area of this circle is {3.14 * self.radious**2}")  # here is what to note
                                                                             # we are overriding the describe method of the parent class
        super().describe()  # but we can still call the parent method using super()


class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height
    
circle = Circle("Red", True, 5)
square = Square("Blue", False, 4)
triangle = Triangle("Green", True, 3, 6)



print(circle.color)

circle.describe()

square.describe()
triangle.describe()
