# timer file to be displayed on the flask app
import time
from itertools import count

def countdown():
    study_time = 20 * 60
    while study_time > 0:
        mins, secs = divmod(study_time, 60)
        timer = ('{:02d}:{:02d}', mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        study_time -= 1
    print("Time's Up!")
