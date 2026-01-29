# This code will tell you about a file location

import os

location = "C:\\Users\\Borin\\Downloads\\New folder"
if os.path.exists(location):
    print("The file exist ")
    if os.path.isdir(location):
        print("It is a directory")
    else:
        print("It is not a directory")
else:
    print("It doesn't exist! ")