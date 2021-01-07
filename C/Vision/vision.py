# tester klasser og objekter
# Class names staret med stort
# methods_like_this (alt er småt)
# objectsLikeThis (starter med småt)
from __future__ import print_function
import cv2 as cv
#-------------------------------------------------------
# Vinduesnavn
cv.namedWindow('Tracking', cv.WINDOW_NORMAL)

class Color:
    def __init__(self, lh, ls, lv, hh, hs, hv):     # HSV værdier - low/high
        self.lh = lh     # creates atribute called hl and takes in parameter hl
        self.ls = ls
        self.lv = lv
        self.hh = hh
        self.hs = hs
        self.hv = hv


    def nothing(self):  # definere nothing for at den kan blive ignoreret i cv.createTrackbar
        lh = cv.getTrackbarPos("Low_H", "Tracking")
        ls = cv.getTrackbarPos("Low_S", "Tracking")
        lv = cv.getTrackbarPos("Low_V", "Tracking")
        hh = cv.getTrackbarPos("High_H", "Tracking")
        hs = cv.getTrackbarPos("High_S", "Tracking")
        vh = cv.getTrackbarPos("High_V", "Tracking")
        return lh, ls, lv, hh, hs, hv

    def printValue(self):    # til debugging
        print('HSV values')
        print(self.lh)
        print(self.ls)
        print(self.lv)
        print(self.hh)
        print(self.hs)
        print(self.hv)

default = Color(0,0,0,0,0,0)
print(default.printValue())         # debugging

greenDefault = Color(53,74,66,96,225,185)
print(greenDefault.printValue())    # debugging

cv.createTrackbar("Low_H", "Tracking", default.lh, 180, Color.nothing)
cv.createTrackbar("Low_S", "Tracking", default.ls, 255, Color.nothing)
cv.createTrackbar("Low_V", "Tracking", default.lv, 255, Color.nothing)
cv.createTrackbar("High_H", "Tracking", default.hh, 180, Color.nothing)
cv.createTrackbar("High_S", "Tracking", default.hs, 255, Color.nothing)
cv.createTrackbar("High_V", "Tracking", default.hv, 255, Color.nothing)


# blueDefault = Color(0,0,65,171,234,110)
# blueDefault.printValue()          # debugging

# redDefault = Color(0,0,0,24,255,88)
# redDefault.printValue()           # debugging



