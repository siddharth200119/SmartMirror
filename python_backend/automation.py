#imports
import os
import cv2
import subprocess
from selenium import webdriver
import time
from flask import Flask, jsonify, request  #for backend server
from register_user import register_user
from user_recognition import user_recognition

#start backend flask server

subprocess.Popen('python server.py', shell=True)

##########################################################################################################################################################

#start react app in full screen

os.chdir('..\\mirror_UI\\frontend\\')
subprocess.Popen('npm start', shell=True)

time.sleep(5)
print('slept')

driver = webdriver.Firefox()
driver.get('http://localhost:3000/')
driver.fullscreen_window()