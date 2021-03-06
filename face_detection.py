import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(r'C:\Users\vanminh1\OneDrive - Intel Corporation\Desktop\Cody\Minhne\Python Tutorial\OpenCV\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray) #detect face base on support tools

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow("Detecting face", frame)

    key = cv2.waitKey(1)
    if key==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
