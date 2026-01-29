# --- Concession stand program ---

menu = {"Hamburger": 4.1,
        "Coke": 1.2,
        "Fries": 2.1,
        "Pancake": 3.1,
        "Pizza": 5.12}
cart = []
total = 0
for food, price in menu.items(): # this items can be used to replace zip
    print(f"{food:10} : ${price:.2f}")

while True:
    user_order = input("What would you like to have?(q to quit): ")
    if user_order.lower() == "q":
        break
    elif menu.get(user_order) is not None:
        cart.append(user_order)

for i in cart:
    total += menu.get(i)
print("Your total is $", total)
