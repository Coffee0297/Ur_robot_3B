# CBL
# Masking functions

import cv2 as cv
import numpy as np

# cThr=[150, 175]: user can define threshold later (these are default values)
# show=False: set true when calling function (if you wish to see images on screen)
'''
def getContours(img,cThr=[100, 100],showCanny=False):
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (5,5), 1)
    imgCanny = cv.Canny(imgBlur, cThr[0], cThr[1])
    kernel = np.ones((5,5))
    imgDial = cv.dilate(imgCanny, kernel, iterations=3)
    imgThres = cv.erode(imgDial,kernel, iterations=2)
    if showCanny:cv.imshow('Canny', imgThres)
'''

# cThr=[150, 175]: user can define threshold later (these are default values)
# show=False: set true when calling function (if you wish to see images on screen)
def getContours(frame, cThr=[150, 175], show=False):

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    canny = cv.Canny(gray, cThr[0], cThr[1])

    lap = cv.Laplacian(gray, cv.CV_64F)
    lap = np.uint8(np.absolute(lap))

    if show:
        cv.imshow('Webcam', gray)
        cv.imshow('Canny', canny)
        cv.imshow('Laplacian', lap)