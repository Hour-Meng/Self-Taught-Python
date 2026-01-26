import random

while True:
    #Choices for the player
    Choices = ["rock","paper","scissors"]

    #Computer pick
    Computer = random.choice(Choices)

    #The player's value before they enter the game
    Player = None
    while Player not in Choices:
        Player = input("rock , paper , or scissors?: ").lower()
        if Player not in Choices:
            print("Please enter a valid choice")

    # Print both the player and computer choice
    print("Computer:",Computer)
    print("Player:",Player)

    #Determine who's the winner
    if Player == Computer:
        print("Tie!!")
    elif (Player == "rock" and Computer == "scissors") or \
            (Player == "scissors" and Computer == "paper") or \
            (Player == "paper" and Computer == "rock"):
        print("Congrats! You win")
    else:
        print("You loose!")
    # Player's choice on whether they want to continue or stop
    Play_again = ["yes","no"]

    Play_again_input = None

    while Play_again_input not in Play_again:
        Play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if Play_again_input not in Play_again:
            print("invalid choice please type either Yes or No")
    if Play_again_input == "no":
         break
#end message
print("Goodbye")

#The if Play_again == "No":
# can also replace with
# if Player_again != "Yes":
#   break


# != mean does not equal to. So basically the code mean if Play_agin does not equal to yes then break(end) it