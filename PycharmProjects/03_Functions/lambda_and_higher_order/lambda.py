# lambda use for maybe something of a getaway or one use

multiplier = lambda x:x * 5


ask_user = input("What is your name? ")
name = lambda ask_user, last_name: ask_user+" "+last_name
age_checker = lambda age: True if age > 18 else False

print(name("John", "Pig") + " " + ask_user)
ask_age = (input("How old are you?: "))
print(age_checker(int(ask_age)))
