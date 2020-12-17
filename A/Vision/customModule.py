import cv2 as cv
import numpy as np

def getContours(img,cThr=[100,100],showCanny=False):
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv.Canny(imgBlur,cThr[0],cThr[1])
    if showCanny: cv.imshow('Canny',imgCanny)
