puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def valid(puzz, pos, num):
    #check row
    for column in range(len(puzz[0])): # loop through each column in that row
        if puzz[pos[0]][column] == num and pos[1] != column:
            return False
        
    #check column
    for row in range(len(puzz)): # loop through each row
        if puzz[row][pos[1]] == num and pos[0] != row:
            return False

    #Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for row in range(box_y*3, box_y*3 +3):
        for column in range(box_x*3 , box_x*3 + 3):
            if puzz[row][column] == num and (row, column) != pos:
                return False
    
    return True

def puzzle_map(puzz):
    for row in range(len(puzz)):
        if row % 3 == 0 and row != 0:
            print(" -" * len(puzz))
        
        for column in range(len(puzz[0])):
            if column % 3 == 0 and column != 0:
                print("| ", end = "")
        
            if column == 8:
                print(puzz[row][column])
            else:
                print(str(puzz[row][column] ) + " ", end = "")

def empty_box(puzz):
    for row in range(len(puzz)):
        for column in range(len(puzz[0])):
            if puzz[row][column] == 0:
                return (row, column)

    return None       

def solver(puzz):
    finder = empty_box(puzz)

    if not finder:
        return True
    else:
        row, column = finder

    for i in range(1, 10):
        if valid(puzz, (row, column), i):
            puzz[row][column] = i

            if solver(puzz):
                return True

            puzz[row][column] = 0
    
    return False
    

puzzle_map(puzzle)

solver(puzzle)
print("____________________________________________________")
puzzle_map(puzzle)