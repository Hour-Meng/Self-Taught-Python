# In this we will learn on how to write and edit file using python

text = "Hello world "

file_path = "sample.txt"

# w mean write mode, r means read mode, a means append mode, x means create mode
# open(file, mode)

with open(file_path, "w") as file:
    file.write(text)

# to read the file we can do the following

with open(file_path, "r") as file:
    content = file.read()
    print(content)

