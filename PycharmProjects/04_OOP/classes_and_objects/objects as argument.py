class Car:
    colour = None


def change_color(car, color):
    car.colour = color


car_1 = Car()
car_2 = Car()
change_color(car_1, "Blue")
change_color(car_2, "Black")

print(car_1.colour)
print(car_2.colour)
