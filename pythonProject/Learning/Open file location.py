import os

with open("name.txt") as file:
    print(file.read())

print(file.closed)