# timer file to be displayed on the flask app
import time

# 20 min study time
MINS = 20
SECS = 60
study_time = MINS * SECS

def countdown(x):
    while x > 0:
        mins, secs = divmod(x, SECS)
        timer = ('{:02d}:{:02d}', mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        x -= 1
    print("Time's Up!")

