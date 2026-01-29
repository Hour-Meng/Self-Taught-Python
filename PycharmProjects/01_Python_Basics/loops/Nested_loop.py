#Nested loop = a loop within a loop ( outer, inner)
#               outerloop:
#                 innerloop:

for x in range(3):      #outer loop:
    for y in range(1, 11):  #inner loop:
        print(y, end="")
    print(end=" ")