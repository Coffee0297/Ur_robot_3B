import cv2 as cv
import numpy as np

def getContours(img,cThr=[100,100],showCanny=False,cannyResize=False):
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray,(5,5),1)
    imgCanny_Original = cv.Canny(imgBlur,cThr[0],cThr[1])

    if showCanny: cv.imshow('Canny',imgCanny_Original)
    if cannyResize: cv.resize(imgCanny_Original(0,0),None, 0.3, 0.3)
