# tester klasser og objekter
# Class names staret med stort
# methods_like_this (alt er småt)
# objectsLikeThis (starter med småt)
from __future__ import print_function
#import defs
import numpy as np
import cv2 as cv
#-------------------------------------------------------
# Vinduesnavn
cv.namedWindow('Tracking', cv.WINDOW_NORMAL)
#cap = cv.VideoCapture(0)
cap = cv.imread("image_0.png")

class Hsv:
    def __init__(self, lh, ls, lv, hh, hs, hv):     # HSV værdier - low/high
        self.lh = lh     # creates atribute called hl and takes in parameter hl
        self.ls = ls
        self.lv = lv
        self.hh = hh
        self.hs = hs
        self.hv = hv


class Color(Hsv):

    def create(self):
        cv.createTrackbar('Low_H', 'Tracking', self.lh,180, Color.on_trackbar)
        cv.createTrackbar("Low_S", "Tracking", self.ls, 255, Color.on_trackbar)
        cv.createTrackbar("Low_V", "Tracking", self.lv, 255, Color.on_trackbar)
        cv.createTrackbar("High_H", "Tracking", self.hh, 180, Color.on_trackbar)
        cv.createTrackbar("High_S", "Tracking", self.hs, 255, Color.on_trackbar)
        cv.createTrackbar("High_V", "Tracking", self.hv, 255, Color.on_trackbar)


    def on_trackbar(self):

        print(self)
        lh = cv.getTrackbarPos("Low_H", "Tracking")
        ls = cv.getTrackbarPos("Low_S", "Tracking")
        lv = cv.getTrackbarPos("Low_V", "Tracking")
        hh = cv.getTrackbarPos("High_H", "Tracking")
        hs = cv.getTrackbarPos("High_S", "Tracking")
        hv = cv.getTrackbarPos("High_V", "Tracking")

        #ret, frame = cap.read()
        frame = cap

        frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        red_frame_threshold = cv.inRange(frame_HSV, (lh, ls, lv), (hh, hs, hv))

        cv.imshow('video feed', frame)
        frame_threshold = red_frame_threshold
        cv.imshow('Frame Threshhold', frame_threshold)

        #print(Color.print_value(blueDefault))  # debugging
        return self

    def print_color(self):
        print('Color is red')

    def print_value(self):    # til debugging
        print('HSV values')
        print(self.lh)
        print(self.ls)
        print(self.lv)
        print(self.hh)
        print(self.hs)
        print(self.hv)

class Red:
    pass




default = Hsv(0,0,0,0,0,0)
redDefault = Hsv(0,18,30,16,255,87)
#greenDefault = Hsv(53,74,66,96,225,185)
#blueDefault = Hsv(0,0,65,171,234,110)

red1 = Color.create(redDefault)
#green1 = Color.create(greenDefault)
#blue1 = Color.create(blueDefault)
#print(Color.print_value(blueDefault))  # debugging
print(Color.print_value(redDefault))  # debugging

#Color.on_trackbar(0)


print('Press q to exit Trackbar')
while True:
    key = cv.waitKey(30)

    # print(Color.print_value(redDefault))  # debugging
    if key == ord('q') or key == 27:

        break

    # if key == ord('q') or key == 27:
    #     break

