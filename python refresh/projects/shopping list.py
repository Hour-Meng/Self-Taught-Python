fruits = []
prices = []
quantities = []

while True:
    fruit = input("What fruit do you want to buy?(q to quit): ")
    if fruit.lower() == "q":
        break
    else:
        fruits.append(fruit)
        price = float(input("What is the price?: "))
        prices.append(price)
        quantity = int(input(f"How many {fruit} do you want?: "))
        quantities.append(quantity)
print("---Your cart---")

x = 0
for fruit in fruits:
    print(f"{fruit} qnt = {quantities[x]} total ${prices[x]*quantities[x]}")
    x += 1

total = 0
y = 0
for price in prices:
    total += price*quantities[y]
    y += 1
print("---Total---")
print("$", total)
