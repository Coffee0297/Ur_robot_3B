import vision
import cv2 as cv

img = cv.imread("image_13.png")
imageFrame = cv.resize(img, None, fx=0.6, fy=0.6, interpolation=cv.INTER_AREA)
cv.imshow('Original image Resized', imageFrame)
hsvFrame = cv.cvtColor(imageFrame, cv.COLOR_BGR2HSV)

testingColor=False

greenDefault = vision.Hsv(53,74,66,96,225,185)
redDefault = vision.Hsv(0,18,30,16,255,87)
yellowDefault = vision.Hsv(0,158,109,31,255,255)
blueDefault = vision.Hsv(89, 148, 64, 166, 214, 143)

def colors():
    color= vision.Colordetect.detect_color(redDefault,hsvFrame)
    while testingColor==True:

        if color[0][2] == 0:
            color = vision.Colordetect.detect_color(blueDefault,hsvFrame)
        elif color[0][2] == 255:
            vision.Color.yellow_color(color)
            break

        if color[0][2] == 0:
            color = vision.Colordetect.detect_color(greenDefault,hsvFrame)
        elif color[0][2] == 255:
            vision.Color.green_color(color)
            break

        if color[0][2]==0:      #('move on')
            color = vision.Colordetect.detect_color(yellowDefault,hsvFrame)
        elif color[0][2]==255:
            vision.Color.yellow_color(color)
            break

        if color[0][2] != True:
            testingColor = False
            vision.Color.no_color_detected(color)

    return


print('Press q to exit')
while True:
    key = cv.waitKey(30)

    if key == ord('q') or key == 27:
        break