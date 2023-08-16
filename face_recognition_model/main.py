import cv2 
import face_recognition
import os
import json
from os import listdir

#to register prople
people = json.load(open('people.json'))

#register new person
def register_user(name, frames):
    cam = cv2.VideoCapture(0)
    frame_no = 0
    while frames > frame_no:

        check, frame = cam.read()
        cv2.imshow('video', frame)
        

    cam.release()
    cv2.destroyAllWindows()