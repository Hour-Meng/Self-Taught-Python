# This is a hangman game project

import random

words = ("python", "java", "lua", "bash")

#dictionary to hold hangman stages

hangman_art = { 0: ("   ________     ",
                   "   |      |     ",
                   "   |            ",
                   "   |            ",
                   "   |            ",
                   "___|__________ "),

                1: ("   ________     ",
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
                   
                5: ("   ________     ",
                   "   |      |     ",
                   "   |      O     ",
                   "   |     /|\\   ",
                   "   |     /      ",
                   "___|__________ "),
                6: ("   ________     ",
                   "   |      |     ",
                   "   |      O     ",
                   "   |     /|\\   ",
                   "   |     / \\   ",
                   "___|__________ ")}
#print hangman stage example


def wrong_guess():
    pass

def hint(chosen_word):
    
    display = []
    for _ in chosen_word:
        display += "_"
    print(" ".join(display))



def main():
    print(" Welcome to my Hangman game!")

    #This is the random workd selection
    chosen_word = random.choice(words)

    print("\n") # new line after printing all underscores

    running = True

    while running:

        hint(chosen_word)
        user_input = input("Please enter a letter: ").lower()

        if user_input in chosen_word:
            display = []
            for letter in chosen_word:
                if letter == user_input:
                    display.append(letter)
                else:
                    display.append("_")
            print(" ".join(display))
        else:
            print("Wrong guess!")



        if user_input == "exit":
            break

    print("Thank you for playing my Hangman game!")

if __name__ == "__main__":
    main()
