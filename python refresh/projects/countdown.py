import time

#start = int(input("Please enter starting point: "))
#end = int(input("Please enter ending point: "))

#for i in reversed(range(end, start+1)):
#    print(i)
#    time.sleep(1)
#print("Count down is over!")

time_input = int(input("Please enter time in seconds: "))

for x in range(time_input, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
