import cv2 as cv
import numpy as np


def getContours(img, cThr=[100, 100], showCanny=False, cannyResize=False, minArea = 1000, filter=0, draw = False):
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

webcam = False
path = 'c:\\Users\\Pc\\Desktop\\3. Semester\\Vision\\Ressourcer\\Billeder\\a4.jpg'
cap = cv.VideoCapture(0)
cap.set(10,160)
cap.set(3,480)
cap.set(4,640)

while True:
    if webcam:success,img = cap.read()
    else: img = cv.imread(path)

    img, conts = getContours(img,cannyResize=True,
                                     minArea=50000,filter=4) #SPOL TILBAGE OG FIND UD AF HVORFOR DEN IKKE VISER EDGES CA. 26 MINUTTER INDE
    # if len(conts) != 0:
    #     biggest = conts[0][2]
    #     print(biggest)

    img = cv.resize(img,(0,0),None, 0.4, 0.4)

    cv.imshow("Original", img)
    if cv.waitKey(0) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()