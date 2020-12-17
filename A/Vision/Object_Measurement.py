import cv2 as cv
import numpy as np
import utlis

webcam = False
path = 'c:\\Users\\Pc\\Desktop\\3. Semester\\Vision\\Ressourcer\\Billeder\\a4.jpg'
cap = cv.VideoCapture(0)
cap.set(10,160)
cap.set(3,480)
cap.set(4,640)

while True:
    if webcam:success,img = cap.read()
    else: img = cv.imread(path)



    img = cv.resize(img,(0,0),None, 0.5, 0.5)

    cv.imshow("Original", img)
    if cv.waitKey(0) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()