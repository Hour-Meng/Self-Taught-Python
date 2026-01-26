# This is a hangman game project
from hangman_words import words
import random
import time

#dictionary to hold hangman stages

hangman_art = { 0: ("   ________    ",
                   "   |      |     ",
                   "   |            ",
                   "   |            ",
                   "   |            ",
                   "___|__________ "),

                1: ("   ________    ",
                   "   |      |     ",
                   "   |      O     ",
                   "   |            ",
                   "   |            ",
                   "___|__________ "),
                   
                2:("   ________     ",
                   "   |      |     ",
                   "   |      O     ",
                   "   |      |     ",
                   "   |            ",
                   "___|__________ "),
                   
                3:("   ________     ",
                   "   |      |     ",
                   "   |      O     ",
                   "   |     /|     ",
                   "   |            ",
                   "___|__________ "),
                   
                4:("   ________     ",
                   "   |      |     ",
                   "   |      O     ",
                   "   |     /|\\   ",
                   "   |            ",
                   "___|__________ "),
                   
                5: ("   ________    ",
                   "   |      |     ",
                   "   |      O     ",
                   "   |     /|\\   ",
                   "   |     /      ",
                   "___|__________ "),
                6: ("   ________    ",
                   "   |      |     ",
                   "   |      O     ",
                   "   |     /|\\   ",
                   "   |     / \\   ",
                   "___|__________ ")}
#print hangman stage example


def wrong_guess(guesses):
    print("**********************")

    for line in hangman_art[guesses]:
        print(line)
    print("\n")
    print("**********************")

def hint_fnc(hint):
    
    print(" ".join(hint))

def main():
    print(" Welcome to my Hangman game!")

    #This is the random workd selection
    chosen_word = random.choice(words)
    guesses = 0
    hint = ["_"]*len(chosen_word)
    guessed_letters = set()

    running = True

    while running:

        wrong_guess(guesses)
        hint_fnc(hint)

        print("\n")
        user_input = input("Please enter a letter: ").lower()

        if not user_input.isalpha() or len(user_input) != 1:
            print("Invalid input. Please enter a single letter.")
            time.sleep(1)
            continue



        if user_input in guessed_letters:
            print("You already guessed that letter. Try again.")
            time.sleep(1)
            continue

        guessed_letters.add(user_input)            

        if user_input in chosen_word:
            for i in range(len(chosen_word)):
               if user_input == chosen_word[i]:
                    hint[i] = user_input
        else:
            guesses += 1

        # Win Condition
        if "_" not in hint:
            wrong_guess(guesses)
            hint_fnc(hint)
            print("Congratulations! You guessed the word correctly!")
   
        # Lose Condition

        if guesses == 6:
            wrong_guess(guesses)
            hint_fnc(hint)
            print(f"Sorry, you've been hanged! The word was '{chosen_word}'.")
            break


        if user_input == "exit":
            break

    print("Thank you for playing my Hangman game!")




if __name__ == "__main__":

    while True:

        main()

        replay = input("Do you want to play again? (yes/no): ")

        while replay not in ["yes", "no"]:
            replay = input("Do you want to play again? (yes/no): ")
            continue
        if replay == "no":
            print("Goodbye!")
            break
            