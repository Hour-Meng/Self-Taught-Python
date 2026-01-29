import os
sorce = "name.txt"
destination = "C:\\Users\\Borin\\OneDrive\\Desktop\\newfile.txt"

try:
    if os.path.exists(destination):
        print(sorce+" was already existed")
    elif os.replace(sorce,destination):
        print(sorce+" was moved")
except ValueError:
    print(sorce+ " got a value error maybe try checking the name again? ")