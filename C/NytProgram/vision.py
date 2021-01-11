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
img = cv.imread("image_11.png")
#---------------------------------------------------------------------------------------------------------------------
imageFrame = cv.resize(img, None, fx=0.6, fy=0.6, interpolation=cv.INTER_AREA)
cv.imshow('Original image Resized', imageFrame)
hsvFrame = cv.cvtColor(imageFrame, cv.COLOR_BGR2HSV)
cv.imshow('hsvFrame', hsvFrame)
#---------------------------------------------------------------------------------------------------------------------
kernel = np.ones((5, 5), "uint8")
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
        print('Creating Trackbar...')
        print('Move trackbar to adjust HSV values...')
        cv.createTrackbar('Low_H', 'Tracking', self.lh, 180, Trackbar.on_trackbar)
        cv.createTrackbar("Low_S", "Tracking", self.ls, 255, Trackbar.on_trackbar)
        cv.createTrackbar("Low_V", "Tracking", self.lv, 255, Trackbar.on_trackbar)
        cv.createTrackbar("High_H", "Tracking", self.hh, 180, Trackbar.on_trackbar)
        cv.createTrackbar("High_S", "Tracking", self.hs, 255, Trackbar.on_trackbar)
        cv.createTrackbar("High_V", "Tracking", self.hv, 255, Trackbar.on_trackbar)
        return self

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
        green_frame_threshold = cv.inRange(frame_HSV, (lh, ls, lv),(hh, hs, hv))
        blue_frame_threshold = cv.inRange(frame_HSV, (lh, ls, lv),(hh, hs, hv))

        # # detect color
        # ret, red_thresh = cv.threshold(red_frame_threshold, 127, 255, 0)
        # red_contours, red_hierarchy = cv.findContours(red_thresh, 1, 2)
        #
        # for i in range(len(red_contours)):
        #     if red_contours[i].size > 300:
        #         Color.print_color(self)
        # #-----
        cv.imshow('Captured Image', frame)
        frame_threshold = (red_frame_threshold + green_frame_threshold + blue_frame_threshold)
        cv.imshow('Frame Threshhold', frame_threshold)
        return self, lh, ls, lv, hh, hs, hv

class Colordetect:
    def detect_color(self):
        print('Detecting color...')
        imageFrame = cv.resize(img, None, fx=0.6, fy=0.6, interpolation=cv.INTER_AREA)
        cv.imshow('Original image Resized', imageFrame)
        hsvFrame = cv.cvtColor(imageFrame, cv.COLOR_BGR2HSV)

        threshold = cv.inRange(hsvFrame, (self.lh, self.ls, self.lv), (self.hh, self.hs, self.hv))

        threshold = cv.dilate(threshold, kernel)
        cv.imshow('1---mask dilate', threshold)

        return threshold

class Color:
    def red_color(self):
        print('Color is red')

    def green_color(self):
        print('Color is green')

    def blue_color(self):
        print('Color is blue')

    def yellow_color(self):
        print('Color is yellow')

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

testingColor=True
greenDefault = Hsv(53,74,66,96,225,185)
redDefault = Hsv(0,18,30,16,255,87)
yellowDefault = Hsv(0,158,109,31,255,255)
blueDefault = Hsv(89, 148, 64, 166, 214, 143)


color = Colordetect.detect_color(redDefault)
while testingColor==True:

    if color[0][2]==0:      #('move on')
        color = Colordetect.detect_color(yellowDefault)
    elif color[0][2]==255:
        Color.yellow_color(color)
        break

    if color[0][2] == 0:
        color = Colordetect.detect_color(blueDefault)
    elif color[0][2] == 255:
        Color.yellow_color(color)
        break

    if color[0][2] == 0:
        color = Colordetect.detect_color(greenDefault)
    elif color[0][2] == 255:
        Color.green_color(color)
        break

print('Press q to exit Trackbar')
while True:
    key = cv.waitKey(30)

    # print(Color.print_value(redDefault))  # debugging
    if key == ord('q') or key == 27:

        break


# red1 = Trackbar.create(redDefault)
# red1 = Color.red_color(redDefault)

# green1 = Color.create(greenDefault)
# blue1 = Trackbar.create(blueDefault)
# yellow11 = Color.create(yellowDefault)

# default = Hsv(0,0,0,0,0,0)
# default1 = Color.create(default)
# print(Color.print_value(default))        # debugging

#print(Color.print_value(redDefault))       # debugging
#print(Color.print_value(greenDefault))     # debugging
#print(Color.print_value(blueDefault))      # debugging
#print(Color.print_value(yellowDefault))    # debugging

#Color.on_trackbar(0)



#print(Trackbar.print_value(redDefault))  # debugging


