import cv2 
import face_recognition
import json

def user_recognition(file, image_cv2):
    with open(file) as fp:
        people = json.load(fp)

    rgb_img = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)
    try:  
        cpm_img_encodings = face_recognition.face_encodings(rgb_img)
        for person in people:
            for encoding in cpm_img_encodings:
                if face_recognition.compare_faces([person["face_encodings"][0]], encoding)[0]:
                    return(person['name'])
                else:
                    continue
    except:
        return("no face detected")