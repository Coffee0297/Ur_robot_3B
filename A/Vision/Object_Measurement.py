# Jeg kan ikke importere customModules. hjææææælp


import cv2 as cv
import numpy as np


import os
import sys


file_dir = os.path.dirname('customModule')
sys.path.append('c:\\Users\\Pc\\PycharmProjects\\Ur_robot_3B\\A\\Vision\\customModule.py')



webcam = False
path = 'c:\\Users\\Pc\\Desktop\\3. Semester\\Vision\\Ressourcer\\Billeder\\a4_klods_1.jpg'
cap = cv.VideoCapture(1)
cap.set(10,160)
cap.set(3,1920)
cap.set(4,1080)
scale = 3
wP = 210 *scale
hP = 279 *scale

def getContours(img, cThr=[100, 100], showCanny=False, cannyResize=False, minArea = 500, filter=0, draw = False): # minArea er standard = 100
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny_Original = cv.Canny(imgBlur, cThr[0], cThr[1])
    # imgCanny_Resized = cv.resize(imgCanny_Original.copy(),(0, 0), None, 0.4, 0.4)
    kernel = np.ones((5,5))
    imgDial = cv.dilate(imgCanny_Original, kernel, iterations=3)
    imgThres = cv.erode(imgDial, kernel, iterations=2)



    if showCanny: cv.imshow('Canny', imgCanny_Original)
    if cannyResize: cv.imshow('Resized Canny', imgThres)

    contours, hierarchy = cv.findContours(imgThres,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    finalContours = []
    for i in contours:
        area = cv.contourArea(i)
        if area > minArea:
            peri = cv.arcLength(i,True)
            approx = cv.approxPolyDP(i,0.02*peri,True)
            bbox = cv.boundingRect(approx)
            if filter > 0:
                if len(approx) == filter:
                    finalContours.append([len(approx),area,approx,bbox,i])
            else:
                finalContours.append([len(approx),area,approx,bbox,i])
    finalContours = sorted(finalContours,key= lambda x:x[1], reverse=True)

    if draw:
        for con in finalContours:
            cv.drawContours(img,con[4],-1,(0,0,255),3)

    return img, finalContours

def reorder(myPoints):
    print(myPoints.shape)
    myPointsNew = np.zeros_like(myPoints)
    myPoints = myPoints.reshape((4,2))
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    return myPointsNew

def warpImg(img, points, w, h, pad = 20):
    # print("Points: ", points)
    points = reorder(points)
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    matrix = cv.getPerspectiveTransform(pts1,pts2)
    imgWarp = cv.warpPerspective(img, matrix, (w,h))
    imgWarp = imgWarp[pad:imgWarp.shape[0]-pad, pad:imgWarp.shape[1]-pad]

    return imgWarp

def findDis(pts1, pts2):
    return ((pts2[0]-pts1[0])**2 + (pts2[1]-pts1[1])**2)**0.5


while True:

    if webcam: success,img = cap.read()
    else: img = cv.imread(path)

    img, conts = getContours(img, minArea=50000, showCanny= True, filter=4)

    if len(conts) != 0:
        biggest = conts[0][2]
        print("Biggest: ", biggest)
        imgWarp = warpImg(img, biggest, wP, hP)
        img2, conts2 = getContours(imgWarp, minArea=2000, filter=4, cThr=[50,50], draw=False)
        if len(conts2) != 0:
            for obj in conts2:
                cv.polylines(img2, [obj[2]], True,(0,255,0), 2)
                nPoints = reorder(obj[2])
                nW = round((findDis(nPoints[0][0]//scale,nPoints[1][0]//scale)/10),1)
                nH = round((findDis(nPoints[0][0]//scale,nPoints[2][0]//scale)/10),1)
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