# Jeg kan ikke importere customModules. hjææææælp


import cv2 as cv
import numpy as np
import custommodule as cm

import os
import sys


file_dir = os.path.dirname('customModule')
sys.path.append('/A/Vision/custommodule.py')



webcam = True
path = 'c:\\Users\\Pc\\Desktop\\3. Semester\\Vision\\Ressourcer\\Billeder\\a4_klods_1.jpg'
cap = cv.VideoCapture(1)
cap.set(10,160)
cap.set(3,1920)
cap.set(4,1080)
scale = 3
wP = 210 *scale
hP = 148.5 *scale




while True:

    if webcam: success,img = cap.read()
    else: img = cv.imread(path)

    img, conts = cm.getContours(img, minArea=5000, showCanny= True, filter=4)

    if len(conts) != 0:
        biggest = conts[0][2]
        print("Biggest: ", biggest)
        imgWarp = cm.warpImg(img, biggest, wP, hP)
        img2, conts2 = cm.getContours(imgWarp, minArea=200, filter=4, cThr=[50,50], draw=False) # minArea er standard 2000
        if len(conts2) != 0:
            for obj in conts2:
                cv.polylines(img2, [obj[2]], True,(0,255,0), 2)
                nPoints = cm.reorder(obj[2])
                nW = round((cm.findDis(nPoints[0][0]//scale,nPoints[1][0]//scale)/10),1)
                nH = round((cm.findDis(nPoints[0][0]//scale,nPoints[2][0]//scale)/10),1)
                cv.arrowedLine(img2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]),
                               (255, 0, 255), 3, 8, 0, 0.05)
                cv.arrowedLine(img2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),
                               (255, 0, 255), 3, 8, 0, 0.05)
                x, y, w, h = obj[3]
                cv.putText(img2, '{}cm'.format(nW), (x + 30, y - 10), cv.FONT_HERSHEY_COMPLEX_SMALL, 2,
                           (255, 0, 255), 2)
                cv.putText(img2, '{}cm'.format(nH), (x - 70, y + h // 2), cv.FONT_HERSHEY_COMPLEX_SMALL, 2,
                           (255, 0, 255), 2)
        cv.imshow("A4", img2)


    img = cv.resize(img,(0,0),None, 0.4, 0.4)


    cv.imshow("Original", img)

    cv.waitKey(1)
cap.release()
cv.destroyAllWindows()