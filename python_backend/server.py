from flask import Flask, request
import cv2
from register_user import register_user
from user_recognition import user_recognition

app = Flask(__name__)

@app.route('/api/register_face/<name>', methods=['GET'])
def register_face(name):
    register_user(name, 7, "people.json")
    return 'registered'

@app.route('/api/detect_face', methods=['GET'])
def detect_face():
    cam = cv2.VideoCapture(0)
    for i in range(int(request.args.get("frames"))):
        check, frame = cam.read()
        user_name = user_recognition("people.json", frame)
        if(user_name != None):
            return user_name
        else:
            continue
    return "user not recognised"

if __name__ =='__main__':  
    app.run()  