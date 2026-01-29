# walrus operator :=

# happy = "hi"
# print(happy + " yay")

# print(happy := "Hi" + " Yay")
foods = list()
while (food := input("What is your favorite food?: ")) != "quit":
    foods.append(food)
print("These are your favorite foods: ")
for items in foods:
    print(items)

