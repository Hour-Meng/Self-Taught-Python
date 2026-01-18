import random

low = int(input("Please enter a low number: "))
high = int(input("Please enter a high number: "))

ran = random.randint(low, high)

while True:
    guess = int(input(f"Please enter a random number from {low} to {high}: "))
    if guess < low or guess > high:
        print("You are going too far from the range!")
        continue

    if guess == ran:
        print("You got it right!")
        break

    elif guess > ran:
        print("Too high")
    else:
        print("Too low")
