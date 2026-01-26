# input  = A function that prompts the user to enter data
#          Returns the entered data as a string

#stripe() remove any accidental spaces that users might enter
name = input("Hello!What is your name?: ").strip()

while not name:
     print("Please enter your name!")
     name = input("Enter your name: ").strip()

print(f"Hello {name}")

