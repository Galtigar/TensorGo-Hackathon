import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('data\haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)

while 1:

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    try:
        human_count = faces.shape[0]
    except:
        human_count = 0

    if human_count == 0:
        cv2.rectangle(img, (5, 20), (260, 90), (0,0,255), 2)
        cv2.putText(img, "Status:", (10, 50), 0, 1,(255,255,255), 2)
        cv2.putText(img,"No Person",(12,75),0,1,(0,0,255),2)
    else:
        cv2.rectangle(img, (5, 20), (260, 90), (0, 255, 0), 2)
        cv2.putText(img, "Status:", (10, 50), 0, 1, (255,255,255), 2)
        cv2.putText(img,"Person Present",(12,75),0,1,(0,255,9),2)

    if len(faces) > 1 :
        cv2.rectangle(img, (5, 140), (420, 100), (255, 255, 255), 2)
        #cv2.putText(img, "Status:", (10, 50), 0, 1, (255, 255, 255), 2)
        cv2.putText(img, "Another Person Detected", (12, 130), 0, 1, (0, 255, 9), 2)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()