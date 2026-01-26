# @property = Decorator used to define a method as a property ( it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write or delete attributes
#             Gives you getter, setter and deleter functionality

class Rectangle:
    def __init__(self, width, height):
        self._width = width    # This one is the raw data
        self._height = height  # We can still print it out by using rectangle._width but it's not recommended

    @property
    def width(self):
        return f"{self._width:.1f} cm "
    
    @property
    def height(self):
        return f"{self._height:.1f} cm "
    
    @width.setter  # call the name of the attribute you want to set
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            return print("Width must be positive")
            
    @height.deleter
    def height(self):
        del self._height
        print("Height attribute deleted")
    


rectangle = Rectangle(10, 5)
rectangle.width = 0  # when I try to set width to 0, it will call the setter me
    #but will not change the value since it's not positive

print(rectangle.width)
print(rectangle.height)

del rectangle.height  # This will call the deleter method