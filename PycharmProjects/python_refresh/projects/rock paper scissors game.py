import random

option = ("rock", "paper", "scissors")

bot_value = 0
player_value = 0

print("Welcome to our rock paper and scissors game!")

while True:
    bot = random.choice(option)
    player = input("Please pick rock paper or scissors(q to quit): ")
    if player == "q":
        break
    if player not in option:
        print("Invalid option")
        continue

    if player == "rock":
        player_value = 1
    elif player == "paper":
        player_value = 2
    else:
        player_value = 3

    if bot == "rock":
        bot_value = 1
    elif bot == "paper":
        bot_value = 2
    else:
        bot_value = 3

    if player_value - bot_value in (-2, 2):
        if player_value - bot_value == -2:
            print(f"You are the winner! you pick {player} bot pick {bot}")
        elif player_value - bot_value == 2:
            print(f"You lost! you pick! {player} bot pick {bot}")
    if player_value - bot_value in (-1, 1):
        if player_value - bot_value == 1:
            print(f"You are the winner! you pick {player} bot pick {bot}")
        elif player_value - bot_value == -1:
            print(f"You lost! you pick! {player} bot pick {bot}")

    if player_value - bot_value == 0:
        print(f"It's a tie!! you pick! {player} bot pick {bot}")

#other simple logic
# 1 beats 3, 2 beats 1, 3 beats 2
#    print("It's a tie!")
#elif (player_value - bot_value) % 3 == 1:
#    print("You win!")
#else:
#    print("You lose!")
