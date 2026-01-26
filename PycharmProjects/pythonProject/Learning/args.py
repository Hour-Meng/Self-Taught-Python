def number(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(number(1,5,4))