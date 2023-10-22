from user_recognition import user_recognition
import datetime
from time import sleep
import cv2

def alarm(time, userName):
    alarmTime = [int(n) for n in time.split(":")]
    if 0 <= alarmTime[0] < 24 and 0 <= alarmTime[1] <= 60:
        alarmTimeInSecs = (alarmTime[0] * 3600) + (alarmTime[1] * 60)
        
        #get now time
        now = datetime.datetime.now()
        nowSecs = (now.hour * 3600) + (now.minute * 60) + now.second
        secondsUntillAlarm = alarmTimeInSecs - nowSecs
        if secondsUntillAlarm < 0:
            secondsUntillAlarm += 86400
        sleep(secondsUntillAlarm - 15)
        cam = cv2.VideoCapture(0)
        soundAlarm = True
        while soundAlarm:
            check, frame = cam.read()
            user_name = user_recognition("people.json", frame)
            if(user_name == userName):
                print("recognized")
                soundAlarm = False
            else:
                print("alarm!!!")
                sleep(1)

alarm("12:15:00", "sidd")