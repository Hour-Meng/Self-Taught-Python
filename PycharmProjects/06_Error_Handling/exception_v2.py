try:
    up = int(input("Please enter number: "))
    down = int(input("Please enter number: "))
    Value = up/down

except ValueError as e:
    print(e)
    print("Please enter number!")
except ZeroDivisionError:
    print("You cannot devide it with a zero! ")
except Exception:
    print("There was an error sorry! :( ")
else:
    print(Value)