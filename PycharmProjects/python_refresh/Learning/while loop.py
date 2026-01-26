# while loop = will run the code forever if it remains true

user_name = input("Please enter your name: ")
user_age = int(input("Please enter your age: "))

while user_name == "" or user_age < 0:
    if user_name == "" :
        print("Your username is invalid")
    elif user_age < 0 :
        print("Your age is invalid")
    elif user_name == "" and user_age < 0:
        print("Both are invalid")
        
    print("Please re enter")
    user_name = input("Please enter your name: ")
    user_age = int(input("Please enter your age: "))
print(f"Hello {user_name} and you are {user_age} years old")