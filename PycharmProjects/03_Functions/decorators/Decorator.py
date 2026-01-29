# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_scream("Chocolate")


def add_sprinkles(func): # The word func here is to pass in (order_ice_cream) function in

    def wrapper(*args, **kwargs): # wrapper is a nested function
        print("You added a sprinkles topping")
        func(*args, **kwargs) # This is calling the order_ice_cream function

    return wrapper

# to add order_ice_cream function to add_sprinkles you need to use @(name of decorator)
# in this case the decorator is add_sprinkles

#You can add multiple decorators
#@decorator_2
def decorator_2(func):
    def wrapper(*args, **kwargs):
        print("You added a chocolate syrup topping")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@decorator_2

# if this accept arguments you need to add *args and **kwargs in both wrapper and func
def order_ice_cream(flavor):

    print(f"Your Ice Cream flavor is {flavor}")


order_ice_cream("Vanilla")
