import cv2
import json
import os

#register new person
def register_user(name, frames, file):

    #reading file
    with open(file) as fp:
        people = json.load(fp)

    #name to lower case
    name = name.lower()

    #dict to append to list of people
    person = {
        "name": name,
        "faces": []
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
        frame_no = frame_no + 1

    people.append(person)

    os.chdir("../../")

    with open(file, 'w') as json_file:
        json.dump(people, json_file, indent=4)

    cam.release()
    cv2.destroyAllWindows()