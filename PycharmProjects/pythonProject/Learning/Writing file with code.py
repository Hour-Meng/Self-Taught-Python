# the "r" stand for read , "w" stand for write, "a" stand for append it just to write over a file without deleting the existing one
# for Ex: with open("your file name" , "w" or "r")
# in code if you want to write a new line then use \n

text = ("Hello guy\nline1\nline2\nline3\nline4")
with open("test", "w") as file:
    file.write(text)
