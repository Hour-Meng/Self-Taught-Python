# map() : applies a function to each item in an iterable ( list , tuple , etc...)
#
# map(function, iterable)

store = [("Mustang", "$", 12000), ("Dodge Hellcat", "$", 21000), ("Nissan R35", "$", 100000)]  #iterable

print("Welcome to my car shop this is a list of our car in USD ")

#for loop to print the store items
for i in store:
    print(i)

# Ask the user for exchange rate
user_currency = input("Please enter your currency symbol (e.g EUR, JPY, GBP): ")
ask_user = float(input("Please enter your exchange rate: "))

# lamda function to convert the prices
to_user_exchange = lambda data: (data[0], user_currency, data[2] * ask_user)

store_user_exchange = map(to_user_exchange, store)  # function


for i in store_user_exchange:
    print(i)
