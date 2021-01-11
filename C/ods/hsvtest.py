import numpy as np
import cv2 as cv

# # Color threshold
# image = cv2.imread('image_12.png')
# original = image.copy()
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# lower = np.array([0, 120, 0])
# upper = np.array([179, 255, 255])
# mask = cv2.inRange(hsv, lower, upper)
#
# result = cv2.bitwise_and(original,original,mask=mask)
# result[mask==0] = (255,255,255)
#
# # Make text black and foreground white
# result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
# result = cv2.threshold(result, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
#
# cv2.imshow('mask', mask)
# cv2.imshow('result', result)
# cv2.waitKey()

imageFrame = cv.imread("image_12.png")
#---------------------------------------------------------------------------------------------------------------------
#imageFrame = cv.resize(img, None, fx=0.6, fy=0.6, interpolation=cv.INTER_AREA)
#cv.imshow('Original image Resized', imageFrame)
hsvFrame = cv.cvtColor(imageFrame, cv.COLOR_BGR2HSV)
cv.imshow('hsvFrame', hsvFrame)
#---------------------------------------------------------------------------------------------------------------------
kernel = np.ones((5, 5), "uint8")
#---------------------------------------------------------------------------------------------------------------------
# Set range for red color and define mask
red_lower = np.array([0, 18, 30], np.uint8)
red_upper = np.array([16, 255, 87], np.uint8)
red_mask = cv.inRange(hsvFrame, red_lower, red_upper)
red_mask = cv.dilate(red_mask, kernel)
cv.imshow('1---red_mask 1. gang dilate', red_mask)

res_red = cv.bitwise_and(imageFrame, imageFrame,mask=red_mask)
res_red[red_mask==0] = (255,255,255)
#cv.imshow('2---res_red[red_mask==0]', res_red)

res_red = cv.cvtColor(res_red, cv.COLOR_BGR2GRAY)
cv.imshow('3---res_red[red_mask==0]', res_red)
res_red = cv.threshold(res_red, 0, 255, cv.THRESH_OTSU + cv.THRESH_BINARY)[1]

#cv.imshow('4---red_mask 2. gang', red_mask)     # shows black object on white background
#cv.imshow('5---res_red threshold', res_red)     # shows white object on black background

cv.waitKey()