Brand = ["Kawasaki", "Honda", "Indian"]
Car = ["Mustang", "Lambo", "Mini-Cooper"]
Candy = ["Snicker", "Mar", "Skittle"]

Collection = [Brand, Car, Candy]

#   --num pad--
num = ((1, 2, 3),
       (4, 5, 6),
       (7, 8, 9),
       ("*", 0, "#"))

for row in num:
    for digit in row:
        print(digit, end=" ")
    print()