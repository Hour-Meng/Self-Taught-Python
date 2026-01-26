import datetime

date = datetime.date(2026, 1, 1)
current_date = datetime.date.today()

time = datetime.time(12,30,45)
time_now = datetime.datetime.now()

time_now = time_now.strftime("%H:%M:%S")

print(time_now)