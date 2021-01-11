# tester klasser og objekter
# Class names staret med stort
# methods_like_this (alt er småt)
# objectsLikeThis (starter med småt)
from __future__ import print_function
#import defs
import numpy as np
import cv2 as cv
#---------------------------------------------------------------------------------------------------------------------
#cv.namedWindow('Tracking', cv.WINDOW_NORMAL)
#cap = cv.VideoCapture(0)
#---------------------------------------------------------------------------------------------------------------------
#cap = cv.imread("image_0.png")
#---------------------------------------------------------------------------------------------------------------------

class Hsv:
    print('Object Created...')
    def __init__(self, lh, ls, lv, hh, hs, hv):     # HSV værdier - low/high
        self.lh = lh     # creates atribute called hl and takes in parameter hl
        self.ls = ls
        self.lv = lv
        self.hh = hh
        self.hs = hs
        self.hv = hv

class Trackbar(Hsv):

    def create(self):
        cv.namedWindow('Tracking', cv.WINDOW_NORMAL)
        print('Creating Trackbar...')
        print('Move trackbar to adjust HSV values...')
        cv.createTrackbar('Low_H', 'Tracking', self.lh, 180, Trackbar.on_trackbar)
        cv.createTrackbar("Low_S", "Tracking", self.ls, 255, Trackbar.on_trackbar)
        cv.createTrackbar("Low_V", "Tracking", self.lv, 255, Trackbar.on_trackbar)
        cv.createTrackbar("High_H", "Tracking", self.hh, 180, Trackbar.on_trackbar)
        cv.createTrackbar("High_S", "Tracking", self.hs, 255, Trackbar.on_trackbar)
        cv.createTrackbar("High_V", "Tracking", self.hv, 255, Trackbar.on_trackbar)
        print('Press q to exit')

        cv.waitKey(0)

        return self

    def on_trackbar(self):
        print(self)
        lh = cv.getTrackbarPos("Low_H", "Tracking")
        ls = cv.getTrackbarPos("Low_S", "Tracking")
        lv = cv.getTrackbarPos("Low_V", "Tracking")
        hh = cv.getTrackbarPos("High_H", "Tracking")
        hs = cv.getTrackbarPos("High_S", "Tracking")
        hv = cv.getTrackbarPos("High_V", "Tracking")

        cap = cv.imread("image_100.png")
        #ret, frame = cap.read()
        frame = cap
        frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        red_frame_threshold = cv.inRange(frame_HSV, (lh, ls, lv), (hh, hs, hv))
        green_frame_threshold = cv.inRange(frame_HSV, (lh, ls, lv),(hh, hs, hv))
        blue_frame_threshold = cv.inRange(frame_HSV, (lh, ls, lv),(hh, hs, hv))

        cv.imshow('Captured Image', frame)
        frame_threshold = (red_frame_threshold + green_frame_threshold + blue_frame_threshold)
        cv.imshow('Frame Threshhold', frame_threshold)

        print('Press q to exit')

        cv.waitKey(0)

        return self, lh, ls, lv, hh, hs, hv

class Colordetect:
    def detect_color(self, hsvFrame):
        print('Detecting color...')
        kernel = np.ones((5, 5), "uint8")
        threshold = cv.inRange(hsvFrame, (self.lh, self.ls, self.lv), (self.hh, self.hs, self.hv))
        threshold = cv.dilate(threshold, kernel)

        cv.imshow('1---mask dilate', threshold)
        return threshold

class Color:

    def red_color():
        print('\n*** Color is red ***')
        col = 1
        print('print rød fra vision', col,'\n')
        return col

    def green_color():
        print('\n*** Color is green ***')
        col = 2
        print('print grøn fra vision', col,'\n')
        return col

    def blue_color():
        print('\n*** Color is blue ***')
        col = 3
        print('print blå fra vision',col,'\n')
        return col

    def yellow_color():
        print('\n*** Color is yellow ***')
        col = 4
        print('print gul fra vision',col,'\n')
        return col

    def no_color_detected(self):
        print('NO COLOR DETECTED')


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


# default = Hsv(0, 0, 0, 0, 0, 0)
#greenDefault = Hsv(53, 74, 66, 96, 225, 185)
# redDefault = Hsv(0, 18, 30, 16, 255, 87)
# yellowDefault = Hsv(0, 158, 109, 31, 255, 255)
# blueDefault = Hsv(89, 148, 64, 166, 214, 143)
#track = Trackbar.create(greenDefault)

# while True:
#     key = cv.waitKey(30)
#
#     if key == ord('q') or key == 27:
#         break



