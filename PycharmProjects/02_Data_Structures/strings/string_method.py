# use

#print(help(str))

#Validate user's input
#1. Username is no more than 12 characters
#2. Username must not contain spaces
#3. Username must not contain digits

username = input("Please enter your name: ")

if len(username) > 12:
    print("Keep it under 12 characters")
elif not username.find(" ") == -1:
    print("No space is allowed")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:print(f"Welcome {username}")