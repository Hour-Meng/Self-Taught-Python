#copyfile() = copies contents of a file
#copy() =  copyfile() + permission mode + destination can be a directory
#copy2() = copy() + copies metadata (file's creation and modification times)
# When using this you need to write import shutil

import shutil
shutil.copyfile("name.txt",'C:\\Users\\Borin\\OneDrive\\Desktop\\program.txt')  #src(sorce) , dst(destination)