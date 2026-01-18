# With os function you can delete file or empty folder
# to delete a file use this code: os.remove("the file")
# to delete an empty folder use this code: os.rmdir("the folder") rmdir stands for remove directory

# lastly to remove a folder/directory that contain a file(s) you need to use the shutil function
# use this following code to delete it: shutil.rmtree("the file")  rmtree stand for remove tree
# carefully use the rmtree because it will delete all files that contain in the folder as well as the folder