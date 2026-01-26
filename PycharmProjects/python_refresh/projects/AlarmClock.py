import time
import datetime
import pygame

alarm_sound = "kumalala.mp3"


def timer(alarm_clock):
    print(f"Alarm set for {alarm_clock}")

    current_time = datetime.datetime.now().strftime("%H:%M:%S")    
    is_running = True
    while is_running and alarm_clock > current_time:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_clock:
            pygame.mixer.init()
            pygame.mixer.music.load(alarm_sound)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
            
        time.sleep(1)

    

user_input = input("Please enter a timer (HH:MM:SS): ")

timer(user_input)