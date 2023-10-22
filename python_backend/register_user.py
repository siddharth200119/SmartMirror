import cv2
import json
import face_recognition
import os

#register new person
def register_user(name, frames, file):

    #check if user exists
    if(os.path.exists(f'people_images/{name}')):
        return "user exists"

    #reading file
    with open(file) as fp:
        people = json.load(fp)

    #name to lower case
    name = name.lower()

    #dict to append to list of people
    person = {
        "name": name,
        "faces": [],
        "face_encodings": []
    }

    #reading camera feed
    cam = cv2.VideoCapture(0)
    frame_no = 0
    os.mkdir('people_images/' + name)
    os.chdir('people_images/' + name)
    while frames > frame_no:

        check, frame = cam.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imwrite(str(frame_no) + ".jpg", rgb_frame)
        person["faces"].append("people_images/" + name + "/" + str(frame_no) + ".jpg")
        face_encoding = face_recognition.face_encodings(rgb_frame)
        try:
            person["face_encodings"].append((face_recognition.face_encodings(rgb_frame)[0]).tolist())
        except:
            print("No face detected")
        frame_no = frame_no + 1
    people.append(person)
        

    os.chdir("../../")

    with open(file, 'w') as json_file:
        json.dump(people, json_file, indent=4)

    cam.release()
    cv2.destroyAllWindows()

    return "new user registered successfully"

register_user("sidd", 10, "people.json")