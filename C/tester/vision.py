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

        green_frame_threshold = cv.inRange(frame_HSV, (lh, ls, lv),(hh, hs, hv))

        blue_frame_threshold = cv.inRange(frame_HSV, (lh, ls, lv),(hh, hs, hv))


        cv.imshow('Captured Image', frame)
        frame_threshold = (red_frame_threshold + green_frame_threshold + blue_frame_threshold)
        cv.imshow('Frame Threshhold', frame_threshold)
#----------------
        # ret, red_thresh = cv.threshold(red_frame_threshold, 127, 255, 0)
        # red_contours, red_hierarchy = cv.findContours(red_thresh, 1, 2)
        # red_circles = cv.HoughCircles(red_frame_threshold, cv.HOUGH_GRADIENT, 1.2, 100)
        #
        # for i in range(len(red_contours)):
        #     if red_contours[i].size > 300:
        #         red_cnt = red_contours[i]
        #         red_rect = cv.minAreaRect(red_cnt)
        #         cv.putText(frame, str(red_rect[-1]), (10, 60), font, fontScale, (0, 0, 255),
        #                    lineType)  # print rotation of box
        #
        #         redBox = cv.boxPoints(red_rect)
        #         redBox = np.int0(redBox)
        #
        #         cv.drawContours(frame, [redBox], 0, (0, 0, 255), 1)
        #
        #         cv.putText(frame, str(redBox[0]), (redBox[0][0], redBox[0][1]), red_font, red_fontScale, red_fontColor,
        #                    red_lineType)
        #         cv.putText(frame, str(redBox[1]), (redBox[1][0], redBox[1][1]), red_font, red_fontScale, red_fontColor,
        #                    red_lineType)
        #         cv.putText(frame, str(redBox[2]), (redBox[2][0], redBox[2][1]), red_font, red_fontScale, red_fontColor,
        #                    red_lineType)
        #         cv.putText(frame, str(redBox[3]), (redBox[3][0], redBox[3][1]), red_font, red_fontScale, red_fontColor,
        #                    red_lineType)
        #         M = cv.moments(red_cnt)
        #
        #         # calculate x,y coordinate of center
        #         cX = int(M["m10"] / M["m00"])
        #         cY = int(M["m01"] / M["m00"])
        #         cv.circle(img, (cX, cY), 5, red_fontColor, -1)
        #         cv.putText(img, "center", (cX - 25, cY - 25), red_font, red_fontScale, red_fontColor,
        #                    red_lineType)
        # cv.imshow("vis kasse", frame)

        #print(Color.print_value(blueDefault))  # debugging
        return self, lh, ls, lv, hh, hs, hv

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


redDefault = Hsv(0,18,30,16,255,87)
# greenDefault = Hsv(53,74,66,96,225,185)
# blueDefault = Hsv(89,148,64,166,214,143)
# yellowDefault = Hsv(0,158,109,31,255,255)
#
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


