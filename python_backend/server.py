from flask import Flask, request, render_template
import requests
import cv2
from register_user import register_user
from user_recognition import user_recognition
from alarm import alarm
import threading

app = Flask(__name__)

#API

@app.route('/api/register_face/<name>', methods=['GET'])
def register_face(name):
    register_user(name, 7, "people.json")
    return 'registered'

@app.route('/api/detect_face', methods=['GET'])
def detect_face():
    cam = cv2.VideoCapture(0)
    for i in range(int(request.args.get("frames", default = 10, type = int))):
        check, frame = cam.read()
        user_name = user_recognition("people.json", frame)
        if(user_name != None):
            return user_name
        else:
            continue
    return "user not recognised"

@app.route('/api/set_alarm', methods=['GET'])
def set_alarm():
    alarmThread = threading.Thread(target=alarm, args=(request.args.get("time"), request.args.get("userName")))
    alarmThread.start()
    return("received")

if __name__ =='__main__':  
    app.run(port = 8080, host="0.0.0.0")  
