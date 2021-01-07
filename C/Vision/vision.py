# tester klasser og objekter
# Class names staret med stort
# methods_like_this (alt er småt)
# objectsLikeThis (starter med småt)
from __future__ import print_function
import cv2 as cv
#-------------------------------------------------------
# Vinduesnavn
cv.namedWindow('Tracking', cv.WINDOW_NORMAL)

class Trackbar:
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

class Color(Trackbar):
    def create(self):
        cv.createTrackbar("Low_H", "Tracking", self.lh, 180, Color.nothing)
        cv.createTrackbar("Low_S", "Tracking", self.ls, 255, Color.nothing)
        cv.createTrackbar("Low_V", "Tracking", self.lv, 255, Color.nothing)
        cv.createTrackbar("High_H", "Tracking", self.hh, 180, Color.nothing)
        cv.createTrackbar("High_S", "Tracking", self.hs, 255, Color.nothing)
        cv.createTrackbar("High_V", "Tracking", self.hv, 255, Color.nothing)

    def printValue(self):    # til debugging
        print('HSV values')
        print(self.lh)
        print(self.ls)
        print(self.lv)
        print(self.hh)
        print(self.hs)
        print(self.hv)


default = Trackbar(0,0,0,0,0,0)
redDefault = Trackbar(0,0,0,24,255,88)
greenDefault = Trackbar(53,74,66,96,225,185)
blueDefault = Trackbar(0,0,65,171,234,110)

red1 = Color.create(redDefault)
#green1 = Color.create(greenDefault)

print(Color.printValue(redDefault))           # debugging

# greenDefault = Trackbar(53,74,66,96,225,185)
# print(greenDefault.printValue())    # debugging

# cv.createTrackbar("Low_H", "Tracking", greenDefault.lh, 180, Color.nothing)
# cv.createTrackbar("Low_S", "Tracking", default.ls, 255, Color.nothing)
# cv.createTrackbar("Low_V", "Tracking", default.lv, 255, Color.nothing)
# cv.createTrackbar("High_H", "Tracking", default.hh, 180, Color.nothing)
# cv.createTrackbar("High_S", "Tracking", default.hs, 255, Color.nothing)
# cv.createTrackbar("High_V", "Tracking", default.hv, 255, Color.nothing)



# blueDefault.printValue()          # debugging

while True:
    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break

