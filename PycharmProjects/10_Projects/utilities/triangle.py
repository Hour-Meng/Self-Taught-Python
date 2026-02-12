def pyramid(height):
    if height < 3:
        return print("invalid height need to be bigger than 2")

    width = height * 2 -1
    
    star = 1
    for i in range(1, height + 1):
        print(("*"* star).center(width))
        star += 2
    for i in range(2):
        print(("*").center(width))
    
    print("*" * width)