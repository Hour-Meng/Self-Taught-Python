#class variables = Shared among all instane of a class
#                  Defined outside the constructor
#                  Allow you to share data among all objects created from that class

class students:
    total_students = 0
    batch = 14
    depatment = "SE"

    def __init__(self, name, age):
        self.name = name
        self.age = age

        students.total_students += 1

student1 = students("George", 21)
student2 = students("Alice", 22)

print(students.total_students)


print(f"My class is in batch {students.batch} of department {students.depatment} with a total of {students.total_students} students.")

# How do I loop through class variables?
for key, value in students.__dict__.items(): # dont's unsdertand this line, but maybe some day I will
    if not key.startswith("__"):
        print(f"{key}: {value}")