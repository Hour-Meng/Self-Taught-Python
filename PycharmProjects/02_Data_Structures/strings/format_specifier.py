# format specifiers = {value:flag} format a value based on what flags are interested

price1 = 2312.1231
price2 = 131.151
price3 = 5236.1241

users_choice = input("How many last digits do you want?: ")

#print(f"This is the price {price1:.2f}")
print(f"Here is the price {price1:^}") # "^" will make it centered
print(f"Here is the price {price2:<}")
print(f"Here is the price {price3:>}")
print(f"Here is the price {price1:10}") #This will add 10 spaces total
print(f"Here is the price {price1:+}") # Will make it positive if it is
print(f"Here is the price {price1:,}")
