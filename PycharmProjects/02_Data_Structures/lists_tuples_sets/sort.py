# sort() method = used with list
# sorted() function = used with iterables

#students = [("Pork", 2, "A"),("Park", 5 , "D"), ("Bark", 4, "B"), ("Bin", 3, "E")]

#student_rank = lambda rank:rank[2]
#lat = sorted(students,key=student_rank)

#print(lat)


student = []

while True:
    ask_student_name = input("Please enter your student name: ")

    ask_student_grade = input("Please enter your student's grade: ").upper()

    ask_student_age = input("Please enter your student age: ")

    student_info = (ask_student_name, int(ask_student_age), ask_student_grade)
    #Add a tuple to the list
    student.append(student_info)
    #Ask whether it's all or not
    ask_to_continue = input("Is it all? if it is enter yes: ")
    #Break if it's yes
    if ask_to_continue == "yes":
        break

print("Student= ", student)
