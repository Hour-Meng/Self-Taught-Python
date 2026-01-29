# exception = An event that interrupts the flow of a program 
#             (ZeroDivisionError, TypeError, ValueError)
#              1. try, 2.except, 3.finally, 4.raise




try:
    user_input  = int(input("Please enter a number: "))

    result = 1/user_input
    print(result)


# what if the user enters 0?
# This is result in a ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!")

# What if they enter a string instead of a number?
# This will result in a ValueError
except ValueError:
    print("Invalid input! Please enter a valid number.")

# What if they are too smart and enter something else, in result of an error that we never knew existed
except Exception:
    print("Yo bro, something went wrong!")

# If everything goes well
finally:  # This thing always runs, no matter what
    print("Execution completed.")
                    