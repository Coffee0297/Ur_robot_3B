import vision
import cv2 as cv

testingColor=True

greenDefault = vision.Hsv(53,74,66,96,225,185)
redDefault = vision.Hsv(0,18,30,16,255,87)
yellowDefault = vision.Hsv(0,158,109,31,255,255)
blueDefault = vision.Hsv(89, 148, 64, 166, 214, 143)


color = vision.Colordetect.detect_color(redDefault)
while testingColor==True:

    if color[0][2] == 0:
        color = vision.Colordetect.detect_color(blueDefault)
    elif color[0][2] == 255:
        vision.Color.yellow_color(color)
        break

    if color[0][2] == 0:
        color = vision.Colordetect.detect_color(greenDefault)
    elif color[0][2] == 255:
        vision.Color.green_color(color)
        break

    if color[0][2]==0:      #('move on')
        color = vision.Colordetect.detect_color(yellowDefault)
    elif color[0][2]==255:
        vision.Color.yellow_color(color)
        break

    if color[0][2] != True:
        testingColor = False
        vision.Color.no_color_detected(color)






print('Press q to exit')
while True:
    key = cv.waitKey(30)

    if key == ord('q') or key == 27:
        break