import cv2 
import face_recognition
import os
from os import listdir
import json


with open("people.json") as fp:
    people = json.load(fp)

cam = cv2.VideoCapture(0)
while True:
    check, frame = cam.read()
    rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cpm_img_encoding = face_recognition.face_encodings(rgb_img)[0]
    result = face_recognition.compare_faces([people[0]["face_encoding"]], cpm_img_encoding)
    print(result)