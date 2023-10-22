#imports
import os
import cv2
import subprocess
from selenium import webdriver
import time
from register_user import register_user
from user_recognition import user_recognition

#start backend flask server

subprocess.Popen('python server.py', shell=True)

#start react app in full screen

os.chdir(r'../mirror_UI/frontend/')
subprocess.Popen('npm start', shell=True)
os.chdir(r'../../python_backend/')
time.sleep(5)
print('slept')

driver = webdriver.Firefox()
driver.get('http://localhost:3000/')
driver.fullscreen_window()

#detect motion

#scan faces

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

face = detect_face()
if (face != None):
    driver.get(f'http://localhost:3000/users/{face}')