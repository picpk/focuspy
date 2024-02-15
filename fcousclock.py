import time
import winsound  # For Windows
# import os  # For MacOS and Linux

def sound_alert():
    frequency = 2500  # Set frequency to 2500 Hertz
    duration = 1000  # Set duration to 1000 milliseconds (1 second)
    winsound.Beep(frequency, duration)
    # For MacOS and Linux, you can use the following line instead:
    # os.system('afplay /System/Library/Sounds/Ping.aiff')

def countdown_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

def focus_timer(work_time, rest_time, rounds):
    for i in range(rounds):
        print("Work Time:")
        countdown_timer(work_time)
        print("\nTime's up! Take a break!")
        sound_alert()
        countdown_timer(rest_time)
        print("\nBack to work!")
        sound_alert()

if __name__ == "__main__":
    work_time = 25 * 60  # 25 minutes for work time
    rest_time = 5 * 60  # 5 minutes for rest time
    rounds = 4  # Number of rounds

    focus_timer(work_time, rest_time, rounds)
