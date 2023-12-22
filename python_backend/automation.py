#imports
import os
import cv2
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from register_user import register_user
from user_recognition import user_recognition
import RPi.GPIO as GPIO

#setup GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN)
GPIO.setup(9, GPIO.OUT)

#start backend flask server

subprocess.Popen('python server.py', shell=True)

#start react app in full screen

os.chdir(r'../mirror_UI/frontend/')
subprocess.Popen('npm start', shell=True)
os.chdir(r'../../python_backend/')
time.sleep(5)
print('slept')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=chrome_options)
driver.get('http://localhost:3000/')
driver.fullscreen_window()

def detect_face():
    cam = cv2.VideoCapture(0)
    for i in range(10):
        check, frame = cam.read()
        user_name = user_recognition("people.json", frame)
        if(user_name != None):
            return user_name
        else:
            continue
    return None

#detect motion
while True:
    PIR = GPIO.input(11)
    if PIR == 1:
        face = detect_face()
        if (face != None):
            driver.get(f'http://localhost:3000/users/{face}')
            driver.fullscreen_window()
            GPIO.output(9, GPIO.HIGH)
            time.sleep(60)
        elif(face == None):
            driver.get(f'http://localhost:3000/')
            driver.fullscreen_window()
            GPIO.output(9, GPIO.LOW)

#scan faces


