#collection = single variable used to store multiple values
# List = [] order and changeable. can duplicate
# Set = {} unordered and immutable, can add/remove. can't duplicate
# Tuple = () ordered and changeable. can duplicate. Faster
#           --List--
Fruits = ["Mango", "Coconut", "Orange", "Banana"]

#print(f"Here is a list of fruits {Fruits}")
#qna = int(input("What is your favorite fruit?: "))

#print(f"Your favorite fruit is {Fruits[qna-1]}")

#Fruits[0] = "Berry"  #It will replace
#Fruits.append("Berry")
#Fruits.remove("1.Mango")
#Fruits.sort()   #Place it in alphabet or number order

#print(Fruits.index("Coconut")) --count which position coconut is in. In this case coconut is in position 1(stared from 0)
#Print("Mango" in Fruits) -- find if there's mango in the list, if there is then it'll return true
#print(Fruits.count("Mango")) #Count how many Mango(s) are there in the list because list is ok with duplicate

#print(Fruits)

#       --Set--
set = {"Banana", "Mango", "Apple", "Coconut"}
set.pop() # randomly remove one value out

print(set)

#       --Tuple--
Tuple = ("Mango", "Banana", "Coconut", "Berry")
