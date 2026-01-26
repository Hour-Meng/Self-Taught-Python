# static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usally used for general utility functions

# INstance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def position_info(position):
        valid_positions = ["Manager", "Staff", "Intern"]

        return position in valid_positions

# Instead of calling through an instance, we can call through the class itself
#emp1 = Employee("John", "Manager")

# Here is how
# This is a static method
print(Employee.position_info("Manager") ) # True
print(Employee.position_info("CEO") ) # False

# This is an instance method
emp1 = Employee("John", "Manager")
print(emp1.get_info() ) # John = Manager