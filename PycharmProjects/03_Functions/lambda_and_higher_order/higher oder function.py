# Higher order function: a function that either:
#                          1: accepts a function as an argument
#                          2: returns a function ( In python, functions are also treated as objects)


def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def talk(func):
    tex = func("Stop it")
    print(tex)


talk(loud)
