# Class Methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter instead of (self), which represents the instance of the class

class Student:
    count = 0
    total_gpa = 0.0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #Instance method
    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"
        
    @classmethod
    def get_count(cls): #cls stands for the class itself
        return f"There are currently {cls.count} students enrolled."
    
    @classmethod
    def average_gpa(cls):
        if cls.count == 0:
            return 0
        else:

            return cls.total_gpa/cls.count

student1 = Student("Alice", 3.8)
student2 = Student("Bob", 3.5)
student3 = Student("Charlie", 3.9)

print(Student.get_count())
print(f"The average GPA is {Student.average_gpa():.2f}")


"""Instance methods (self) → work with individual object data (student1.name)
Class methods (cls) → work with shared class data (Student.count)
Static methods (no self or cls) → utility functions, no access to class/instance data"""