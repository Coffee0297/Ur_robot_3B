import cv2 as cv
import numpy as np

def trackbar():

    def nothing(x):
        pass
    # Vinduesnavn
    cv.namedWindow('Tracking', cv.WINDOW_NORMAL)

    # Opretter en trackbar og attaches
    # vedhæfter det til vindue
    cv.createTrackbar("green_low_H", "Tracking", 53, 180, nothing)
    cv.createTrackbar("green_low_S", "Tracking", 74, 255, nothing)
    cv.createTrackbar("green_low_V", "Tracking", 66, 255, nothing)
    cv.createTrackbar("green_high_H", "Tracking", 96, 180, nothing)
    cv.createTrackbar("green_high_S", "Tracking", 225, 255, nothing)
    cv.createTrackbar("green_high_V", "Tracking", 185, 255, nothing)

    cv.createTrackbar("blue_low_H", "Tracking", 0, 180, nothing)
    cv.createTrackbar("blue_low_S", "Tracking", 0, 255, nothing)
    cv.createTrackbar("blue_low_V", "Tracking", 65, 255, nothing)
    cv.createTrackbar("blue_high_H", "Tracking", 171, 180, nothing)
    cv.createTrackbar("blue_high_S", "Tracking", 234, 255, nothing)
    cv.createTrackbar("blue_high_V", "Tracking", 110, 255, nothing)

    cv.createTrackbar("red_low_H", "Tracking", 0, 180, nothing)
    cv.createTrackbar("red_low_S", "Tracking", 0, 255, nothing)
    cv.createTrackbar("red_low_V", "Tracking", 0, 255, nothing)
    cv.createTrackbar("red_high_H", "Tracking", 24, 180, nothing)
    cv.createTrackbar("red_high_S", "Tracking", 255, 255, nothing)
    cv.createTrackbar("red_high_V", "Tracking", 88, 255, nothing)

    max_value = 255
    max_value_H = 360 // 2