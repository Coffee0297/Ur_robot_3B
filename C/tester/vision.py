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
# Her defineres tekst størrelse til den skrevet rotation i hjørnet
font = cv.FONT_HERSHEY_SIMPLEX
fontScale = .5
lineType = 1
# Her defineres tekst størrelse til den røde klods
red_font = cv.FONT_HERSHEY_SIMPLEX
red_fontColor = (0, 0, 255)
red_fontScale = .5
red_lineType = 2

class Hsv:
    print('Object Created...')
    def __init__(self, lh, ls, lv, hh, hs, hv):     # HSV værdier - low/high
        self.lh = lh     # creates atribute called hl and takes in parameter hl
        self.ls = ls
        self.lv = lv
        self.hh = hh
        self.hs = hs
        self.hv = hv


class Color(Hsv):

    def create(self):
        print('Creating Trackbar...')
        print('Move trackbar to adjust HSV values...')
        cv.createTrackbar('Low_H', 'Tracking', self.lh,180, Color.on_trackbar)
        cv.createTrackbar("Low_S", "Tracking", self.ls, 255, Color.on_trackbar)
        cv.createTrackbar("Low_V", "Tracking", self.lv, 255, Color.on_trackbar)
        cv.createTrackbar("High_H", "Tracking", self.hh, 180, Color.on_trackbar)
        cv.createTrackbar("High_S", "Tracking", self.hs, 255, Color.on_trackbar)
        cv.createTrackbar("High_V", "Tracking", self.hv, 255, Color.on_trackbar)
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

    def detect_color(self):
        print('Detecting color...')
        # detect color
        frame = cap
        frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        red_frame_threshold = cv.inRange(frame_HSV, (self.lh, self.ls, self.lv), (self.hh, self.hs, self.hv))
        green_frame_threshold = cv.inRange(frame_HSV, (lh, ls, lv), (hh, hs, hv))

        ret, red_thresh = cv.threshold(red_frame_threshold, 127, 255, 0)
        red_contours, red_hierarchy = cv.findContours(red_thresh, 1, 2)

        ret, green_thresh = cv.threshold(green_frame_threshold, 127, 255, 0)
        green_contours, green_hierarchy = cv.findContours(green_thresh, 1, 2)

        for i in range(len(red_contours)):
            if red_contours[i].size > 300:
                Color.red_color(self)

        for j in range(len(blue_contours)):
            if blue_contours[j].size > 300:
                pass


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


redDefault = Hsv(0,18,30,16,255,87)
# greenDefault = Hsv(53,74,66,96,225,185)
# blueDefault = Hsv(89,148,64,166,214,143)
# yellowDefault = Hsv(0,158,109,31,255,255)
#q
red1 = Color.red_color(redDefault)
red1 = Color.create(redDefault)
# green1 = Color.create(greenDefault)
# blue1 = Color.create(blueDefault)
# yellow11 = Color.create(yellowDefault)

# default = Hsv(0,0,0,0,0,0)
# default1 = Color.create(default)
# print(Color.print_value(default))       # debugging

print(Color.print_value(redDefault))       # debugging
#print(Color.print_value(greenDefault))     # debugging
#print(Color.print_value(blueDefault))      # debugging
#print(Color.print_value(yellowDefault))    # debugging

#Color.on_trackbar(0)

print('Press q to exit Trackbar')
while True:
    key = cv.waitKey(30)

    # print(Color.print_value(redDefault))  # debugging
    if key == ord('q') or key == 27:

        break

print(Color.print_value(redDefault))  # debugging


