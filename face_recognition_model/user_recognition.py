import cv2 
import face_recognition
import os
from os import listdir
import json

def user_recognition(file, image_cv2):
    with open(file) as fp:
        people = json.load(fp)

    rgb_img = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)
    try:  
        cpm_img_encoding = face_recognition.face_encodings(rgb_img)[0]
        for person in people:
            if face_recognition.compare_faces([person["face_encodings"][0]], cpm_img_encoding)[0]:
                return(person['name'])
    except:
        return("no face detected")
        
