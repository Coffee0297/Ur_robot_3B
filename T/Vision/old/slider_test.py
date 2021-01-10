from __future__ import print_function
from __future__ import division
import cv2 as cv



alpha_slider_max = 100
title_window = 'Linear Blend'
src1 = cv.imread("image_20.png")

def on_trackbar(val):
    print(val)
    cv.imshow(title_window, src1)



cv.namedWindow(title_window)
trackbar_name = 'Alpha x %d' % alpha_slider_max
cv.createTrackbar(trackbar_name, title_window, 0, alpha_slider_max, on_trackbar)
# Show some stuff
on_trackbar(0)
# Wait until user press some key







cv.waitKey()
