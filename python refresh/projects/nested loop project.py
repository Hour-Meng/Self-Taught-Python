rows = int(input("How many rows do you want?: "))
columns = int(input("How many columns do you want?: "))
symbol = input("What symbol do you want?: ")

for x in range(rows):
    for y in range(0, columns):
        print(symbol, end="")
    print()