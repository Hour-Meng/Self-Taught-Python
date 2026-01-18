# Python compound interest calculator

# A = P(1 + r/n)^t
import math

P = float(input("Please enter principle: "))
t = int(input("Please enter amount of years: "))
r = float(input("Please enter interest rate: "))
while P <= 0 or t <= 0 or r <= 0:

    if P <= 0:
        print("Principle can't be under or equal to 0")
        P = float(input("Please enter principle: "))
    elif t <= 0:
        print("Amount of years can't be under or equal to 0")
        t = int(input("Please enter amount of years: "))
    elif r <= 0:
        print("Interest rate can't be under or equal 0")
        r = float(input("Please enter interest rate: "))


result = P*pow((1 + r/100), t)

print(f"Balance after {t} year(s): ${result:.2f}")