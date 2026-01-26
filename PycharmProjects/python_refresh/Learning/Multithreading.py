# Multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIS
#                  threading. THread(target= my_function)


import threading
import time

def shower():
    time.sleep(4)
    print("Just finish showering")

def eat():
    time.sleep(2)
    print("Just finish eating")


def drive():
    time.sleep(5)
    print("Driving to work now!")


todo1 = threading.Thread(target = shower)
todo2 = threading.Thread(target = eat)
todo3 = threading.Thread(target = drive )

"""todo1.start()
todo2.start()
todo3.start()


print("I have completed all of my tasks")

"""

# By using the code on top, it will print "I have completed all of my tasks" before the tasks are done.
# To fix that, we use the join() method


todo1.start()
todo2.start()
todo3.start()

todo1.join()
todo2.join()
todo3.join()

print("I have completed all of my tasks")

# Note: Multithreading may not speed up CPU bound tasks due to GIL (Global Interpreter Lock)

# But what if my function has arguments?

def wash_dishes(dish_count, size):
    time.sleep(3)
    print(f"I have finished washing {dish_count} {size} dishes")

chore = threading.Thread(target = wash_dishes, args = (10, "large"))  # Note the comma after 10 to make it a tuple

chore.start()
chore.join()