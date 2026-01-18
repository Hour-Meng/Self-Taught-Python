questions = ("What does 4+4 equal to?: ",
             "What is the square root of 4?: ",
             "What is 2 to the power of 3 equal to?: ",
             "Who is the current president of USA?: ")
options = (("A.4", "B.2", "C.8", "D.0"),
           ("A.2", "B.5", "C.3", "D.16"),
           ("A.4", "B.8", "C.16", "D.2"),
           ("A.Obama", "B.Abraham Lincoln", "C.Joe Biden", "D.Donald Trump"))
answers = ("C", "A", "B", "D")

score = 0
for question, option, answer in zip(questions, options, answers):
    print(question, option)
    user_input = input("Type your answer here: ")
    if user_input.lower() == answer.lower():
        print("You are correct!")
        score += 1
    else:
        print(f"You are wrong! the correct answer was {answer}")

print(f"Congrats! you have complete the game and you got a score of {score}/{len(questions)}")
