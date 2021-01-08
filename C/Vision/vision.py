# tester klasser og objekter
# Class names staret med stort
# methods_like_this (alt er småt)
# objectsLikeThis (starter med småt)
from __future__ import print_function
from __future__ import division         # virker sammen med 'Alpha x %d' for at
import defs
import cv2 as cv
#-------------------------------------------------------
# Vinduesnavn
cv.namedWindow('Tracking', cv.WINDOW_NORMAL)
#cap = cv.VideoCapture(0)
img = cv.imread("image_0.png")

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
        self.lh = cv.createTrackbar('Low_H', 'Tracking', self.lh,180, Color.on_trackbar)
        cv.createTrackbar("Low_S", "Tracking", self.ls, 255, Color.on_trackbar)
        cv.createTrackbar("Low_V", "Tracking", self.lv, 255, Color.on_trackbar)
        # cv.createTrackbar("High_H", "Tracking", self.hh, 180, Color.on_trackbar)
        # cv.createTrackbar("High_S", "Tracking", self.hs, 255, Color.on_trackbar)
        # cv.createTrackbar("High_V", "Tracking", self.hv, 255, Color.on_trackbar)
        print(Color.print_value(redDefault))  # debugging

    def on_trackbar(self):

        print(self)
        lh = cv.getTrackbarPos("Low_H", "Tracking")
        # self.ls = cv.getTrackbarPos("Low_S", "Tracking")
        # lv = cv.getTrackbarPos("Low_V", "Tracking")
        # hh = cv.getTrackbarPos("High_H", "Tracking")
        # hs = cv.getTrackbarPos("High_S", "Tracking")
        # hv = cv.getTrackbarPos("High_V", "Tracking")
        return self

    def print_value(self):    # til debugging
        print('HSV values')
        print(self.lh)
        print(self.ls)
        print(self.lv)
        print(self.hh)
        print(self.hs)
        print(self.hv)

class Red:
    print('Color is red')

# frame_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#
# red_frame_threshold = cv.inRange(frame_HSV, (lh, lS, lv), (hh, hs, hv))
#
# green_frame_threshold = cv.inRange(frame_HSV, (green_low_H, green_low_S, green_low_V),(green_high_H, green_high_S, green_high_V))
#
# blue_frame_threshold = cv.inRange(frame_HSV, (blue_low_H, blue_low_S, blue_low_V),(blue_high_H, blue_high_S, blue_high_V))
#
# frame_threshold = (blue_frame_threshold + red_frame_threshold + green_frame_threshold)
# cv.imshow('video feed', frame)
#
# cv.imshow('Frame Threshhold', frame_threshold)
#
# cv.imshow("red detection", red_frame_threshold)
# cv.imshow("green detection", green_frame_threshold)
# cv.imshow("blue detection", blue_frame_threshold)


default = Hsv(0,0,0,0,0,0)
redDefault = Hsv(0,0,0,24,255,88)
greenDefault = Hsv(53,74,66,96,225,185)
blueDefault = Hsv(0,0,65,171,234,110)

green1 = Color.create(greenDefault)
print(Color.print_value(redDefault))  # debugging
Color.on_trackbar(0)

print('Press q to exit Trackbar')
while True:
    key = cv.waitKey(30)

    # print(Color.print_value(redDefault))  # debugging
    if key == ord('q') or key == 27:

        break

    # if key == ord('q') or key == 27:
    #     break

