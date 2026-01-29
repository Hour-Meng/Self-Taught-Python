# Higher order function: a function that either:
#                          1: accepts a function as an argument
#                          2: returns a function ( In python, functions are also treated as objects)


def divisor(x):
    def dividend(y):
        def plus_max(z):
            return y/x + z
        return plus_max
    return dividend


result = divisor(4)  # or result = divisor(4)(20)
result = result(20)
print(int(result(20)
          )
      )
