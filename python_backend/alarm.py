from user_recognition import user_recognition
import datetime
from time import sleep
import cv2
from playsound import playsound
import RPi.GPIO as GPIO

alarmsound = "sound.mp3"
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)

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
                playsound(alarmsound)
             
 
