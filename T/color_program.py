import vision ##########
import cv2 as cv

def colors(run=False):
    img = cv.imread("image_100.png")
    imageFrame = cv.resize(img, None, fx=0.6, fy=0.6, interpolation=cv.INTER_AREA)
    #cv.imshow('Original image Resized', imageFrame)
    hsvFrame = cv.cvtColor(imageFrame, cv.COLOR_BGR2HSV)

    default = vision.Hsv(0, 0, 0, 0, 0, 0)
    greenDefault = vision.Hsv(53,74,66,96,225,185)
    redDefault = vision.Hsv(0,18,30,16,255,87)
    yellowDefault = vision.Hsv(0,158,109,31,255,255)
    blueDefault = vision.Hsv(89, 148, 64, 166, 214, 143)

    thresh = vision.Colordetect.detect_color(redDefault,hsvFrame)
    #print('...Default color(hvid)')
    while run:

        if thresh[0][2]==0:
            #print('...ikke rød')
            thresh = vision.Colordetect.detect_color(blueDefault, hsvFrame)
        else:
            col = vision.Color.red_color()
            break
#-----------------------------------------------------------------------------------
        if thresh[0][2] == 0:
            #print('...ikke blå')
            thresh = vision.Colordetect.detect_color(yellowDefault,hsvFrame)
        else:
            col = vision.Color.blue_color()
            break
# -----------------------------------------------------------------------------------
        if thresh[0][2] == 0:
            #print('...ikke gul')
            thresh = vision.Colordetect.detect_color(greenDefault, hsvFrame)

        else:
            col = vision.Color.yellow_color()
            break
# -----------------------------------------------------------------------------------
        if thresh[0][2]==0:
            #print('...ikke grøn')
            thresh = vision.Colordetect.detect_color(yellowDefault,hsvFrame)
        else:
            col =vision.Color.green_color()
            break
# -----------------------------------------------------------------------------------

        if thresh[0][2] != 0:
            testingColor = False
            vision.Color.no_color_detected()
    return col

# print('Press q to exit')
# while True:
#     key = cv.waitKey(30)
#
#     if key == ord('q') or key == 27:
#         break