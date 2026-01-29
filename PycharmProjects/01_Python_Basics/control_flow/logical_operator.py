# Logical operator: "and", "or", "not"
# Use "and" = both condition must be true
# Use "or" = at least one condition must be true
# Use "not" = Inverts the condition ( not False , not True)

tempt = input("Hello please enter the Temperature: ")
is_sunny = input("Is it sunny outside?(Y/N): ")

if "30" > tempt > "20" and is_sunny == "Y":
    print("Pretty cold lol")
elif tempt > "30" or is_sunny == "Y":
    print("Maybe hot?")
elif tempt < "0" and not is_sunny == "Y":
    print("It is cold then")
else: print("You are a Clown")