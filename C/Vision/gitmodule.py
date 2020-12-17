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

    # Do some processing
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    canny = cv.Canny(gray, cThr[0], cThr[1])
    blur = cv.medianBlur(gray, 5)
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv.filter2D(blur, -1, sharpen_kernel)
    edges = cv.Canny(sharpen, 150, 175)
    outImg = cv.dilate(edges, None)

    if show:
        # Do some debugging
        cv.imshow('Webcam', gray)
        cv.imshow('Canny', canny)
        cv.imshow('Blur', blur)
        cv.imshow('Sharpen', sharpen)
        cv.imshow("Webcam", frame)
        cv.imshow("Webcam edges", edges)
        cv.imshow("Output", outImg)

    cv.imshow('Original', frame)
    cv.imshow('Canny', canny)
