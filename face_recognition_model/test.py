import cv2
from user_recognition import user_recognition

cam = cv2.VideoCapture(0)
while True:
    check, frame = cam.read()
    result = user_recognition("people.json", frame)
    print(result)