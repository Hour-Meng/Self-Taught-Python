# In this we will learn how to detect files using python
# Fitstly we will import the os module

# I created a name test.txt in the folder testing_stuff
import os
 
file_path = "testing_stuff/test.txt"

if os.path.exists(file_path):
    print("The file exists")

        # This detects if the path is a file
    if os.path.isfile(file_path):
        print("The path is a file")
else:
    print("The file does not exist")

