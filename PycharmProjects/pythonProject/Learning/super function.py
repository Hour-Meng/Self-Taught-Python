class max:
    def __init__(self, length, width ):
        self.length = length
        self.width = width


class Square(max):
    def __init__(self, lengt, width):
        super().__init__(lengt, width)  # can use max instead of super()

    def area(self):
        area_formula = self.length*self.width
        return area_formula


class Cube(max):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        volume_formula = self.length*self.width*self.height
        return volume_formula


square = Square(3, 3)

cube = Cube(3, 2, 5)

print(square.area())
print(cube.volume())
