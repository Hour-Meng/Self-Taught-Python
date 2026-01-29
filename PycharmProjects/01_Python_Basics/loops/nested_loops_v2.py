 #nested loops = The "Inner loop" will finish all of it's interations before finishing one interation of the "outer loop"

rows = int(input("How many rows do you want?: "))
columns = int(input("How many columns do you want?: "))
symbol = input("What symbol do you want?: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
        print()
