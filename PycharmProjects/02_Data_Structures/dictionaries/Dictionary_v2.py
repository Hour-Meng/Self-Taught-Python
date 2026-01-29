Capital = {"Cambodia":"Phnom Pehn",
            "USA":"Washinton",
            "Russia":"Moscow"}
User = input("What's your country?: ")

if User in Capital:
    print("The Capital city of "+ User + " is " + Capital.get(User))
else:
    print("Sorry but your country isn't in our list yet 1")