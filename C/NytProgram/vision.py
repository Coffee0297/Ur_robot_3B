# tester klasser og objekter
# Class names staret med stort
# methods_like_this (alt er småt)
# objectsLikeThis (starter med småt)
from __future__ import print_function
#import defs
import numpy as np
import cv2 as cv
#-------------------------------------------------------
# Her defineres tekst størrelse til den skrevet rotation i hjørnet
font = cv.FONT_HERSHEY_SIMPLEX
fontScale = .5
lineType = 1
# Her defineres tekst størrelse til den røde firkant
red_font = cv.FONT_HERSHEY_SIMPLEX
red_fontColor = (0, 0, 255)
red_fontScale = .5
red_lineType = 2

#cv.namedWindow('Tracking', cv.WINDOW_NORMAL)
#cap = cv.VideoCapture(0)

imageFrame = cv.imread("image_0.png")

hsvFrame = cv.cvtColor(imageFrame, cv.COLOR_BGR2HSV)
cv.imshow('hsvFrame', hsvFrame)

kernal = np.ones((5, 5), "uint8")

# Set range for red color and define mask
red_lower = np.array([0, 18, 30], np.uint8)
red_upper = np.array([16, 255, 87], np.uint8)
red_mask = cv.inRange(hsvFrame, red_lower, red_upper)
red_mask = cv.dilate(red_mask, kernal)
res_red = cv.bitwise_and(imageFrame, imageFrame,mask=red_mask)
cv.imshow('res_red', res_red)

# Set range for green color and define mask
green_lower = np.array([25, 52, 72], np.uint8)
green_upper = np.array([102, 255, 255], np.uint8)
green_mask = cv.inRange(hsvFrame, green_lower, green_upper)
green_mask = cv.dilate(green_mask, kernal)
res_green = cv.bitwise_and(imageFrame, imageFrame, mask=green_mask)
cv.imshow('res_green', res_green)

# Set range for blue color and define mask
blue_lower = np.array([94, 80, 2], np.uint8)
blue_upper = np.array([120, 255, 255], np.uint8)
blue_mask = cv.inRange(hsvFrame, blue_lower, blue_upper)
blue_mask = cv.dilate(blue_mask, kernal)
res_blue = cv.bitwise_and(imageFrame, imageFrame,mask=blue_mask)
cv.imshow('res_blue', res_blue)


yellow_lower = np.array([0, 158, 109], np.uint8)
yellow_upper = np.array([31, 255, 255], np.uint8)
yellow_mask = cv.inRange(hsvFrame, yellow_lower, yellow_upper)
yellow_mask = cv.dilate(yellow_mask, kernal)
res_yellow = cv.bitwise_and(imageFrame, imageFrame,mask=yellow_mask)
cv.imshow('res_yellow', res_yellow)

# Creating contour to track red color
contours, hierarchy = cv.findContours(red_mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv.findContours(green_mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv.findContours(blue_mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):
    area = cv.contourArea(contour)
    if (area > 300):
        cv.putText(imageFrame, "Red Colour", (10, 30),cv.FONT_HERSHEY_SIMPLEX, 1.0,(0, 0, 0),2)
        cv.putText(imageFrame, "Green Colour", (10, 60), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)
        cv.putText(imageFrame, "Blue Colour", (10, 90), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)
        cv.putText(imageFrame, "Gul Colour", (10, 120), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)

    else:
        print('nope')

cv.imshow('imageFrame', imageFrame)

# red_lower = np.array([136, 87, 111], np.uint8)
# red_upper = np.array([180, 255, 255], np.uint8)

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
                Color.blue_color(self)

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


#redDefault = Hsv(0,18,30,16,255,87)
# greenDefault = Hsv(53,74,66,96,225,185)
#blueDefault = Hsv(89,148,64,166,214,143)
# yellowDefault = Hsv(0,158,109,31,255,255)
#red1 = Trackbar.create(redDefault)
#red1 = Color.red_color(redDefault)

# green1 = Color.create(greenDefault)
#blue1 = Trackbar.create(blueDefault)
# yellow11 = Color.create(yellowDefault)

# default = Hsv(0,0,0,0,0,0)
# default1 = Color.create(default)
# print(Color.print_value(default))       # debugging

#print(Color.print_value(redDefault))       # debugging
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

print(Trackbar.print_value(redDefault))  # debugging


