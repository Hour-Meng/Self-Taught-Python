def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1
    for key in Questions:
        print("#---------------------------")
        print(key)
        for i in Choices[question_number-1]:
            print(i)
        guess = None
        while guess not in [choice.split()[0] for choice in Choices[question_number-1]]:
            #choice.split()[0] mean in the current question which is question 1 or 0 for python which has a choice
            # of 4("A = 4" ,"B = 21" , "C = 22" , "D = 5")
            # with choice.split()[0] it will split "A = 4"to ["A", "=" , "4"] and [0] it take the first one which is A
            # so if split()[1] then it will choose = , and if [2] then it will choose 4
            # and for choice in Choices[question_number-1] it just take the current option for that question


            guess = input("Enter your answer here: ").strip().upper() #Wait for user input
            #.strip() is to remove any of whitespace,tap...
            # for example in the user input if the user type "a " with space without strip() it will ask you to type again as it is invalid


            if guess not in [choice.split()[0] for choice in Choices[question_number-1]]:
                print("Please enter a valid choice!")
        guesses.append(guess)
        #append is used to store all user input

        correct_guesses += check_answer(Questions.get(key), guess)  #score if the player is right

        question_number += 1  # Move to the next question
    score_system(correct_guesses, guesses)

def check_answer(answer , guess):
    if answer == guess:
        print("You are correct")
        return 1
    else:
        print("You are wrong")
        return 0

def score_system(correct_guesses, guesses):
    print("Result: ")
    print("--------------------------")

    print("Correct answers: ", end=" ")
    for i in Questions:
        print(Questions.get(i), end=" ")
    print()
    print("Your guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    player_score = int((correct_guesses/len(Questions))*100)
    print("you got: "+str(player_score)+"%")
def play_again():
    Player_input = ["yes", "no"]
    Play = None
    while Play not in Player_input:
        Play = input("Do you want to play again?(yes/no): ").strip().lower()
        if Play not in Player_input:
            print("Please enter a valid choice ")
        if Play == "yes":
            return True
        elif Play == "no":
            return False
Questions = {"What is the answer of 2+2?: ":"A",
             "What is the answer of 7*3?: ":"C",
             "What is the answer of 90/3?: ":"D",
             "what is the answer of 2 square?: ":"B"}

Choices = [["A = 4" ,"B = 21" , "C = 22" , "D = 5"],
           ["A = 23", "B = 10", "C = 21", "D = 15"],
           ["A = 270", "B = 93", "C = 12", "D = 30"],
           ["A = 8", "B = 4", "C = 12", "D = 0"]]
new_game()
while play_again():
    new_game()
print("Bye!!")