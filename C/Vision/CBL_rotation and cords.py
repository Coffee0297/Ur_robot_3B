from __future__ import print_function

import cv2 as cv
import numpy as np

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

# Her defineres tekst størrelse til den skrevet rotation i hjørnet
font = cv.FONT_HERSHEY_SIMPLEX
fontScale = .5
lineType = 1

window_capture_name = 'Video Feed'
window_detection_name = 'Object Detection'

# cap = cv.VideoCapture(0)
cap = cv.imread("image_0.png")
while True:

    green_font = cv.FONT_HERSHEY_SIMPLEX
    green_fontScale = .5
    green_fontColor = (0, 255, 0)
    green_lineType = 2

    green_low_H = cv.getTrackbarPos("green_low_H", "Tracking")
    green_low_S = cv.getTrackbarPos("green_low_S", "Tracking")
    green_low_V = cv.getTrackbarPos("green_low_V", "Tracking")
    green_high_H = cv.getTrackbarPos("green_high_H", "Tracking")
    green_high_S = cv.getTrackbarPos("green_high_S", "Tracking")
    green_high_V = cv.getTrackbarPos("green_high_V", "Tracking")

    blue_font = cv.FONT_HERSHEY_SIMPLEX
    blue_fontColor = (255, 0, 0)
    blue_fontScale = .5
    blue_lineType = 2

    blue_low_H = cv.getTrackbarPos("blue_low_V", "Tracking")
    blue_low_S = cv.getTrackbarPos("blue_low_V", "Tracking")
    blue_low_V = cv.getTrackbarPos("blue_low_V", "Tracking")
    blue_high_H = cv.getTrackbarPos("blue_high_H", "Tracking")
    blue_high_S = cv.getTrackbarPos("blue_high_S", "Tracking")
    blue_high_V = cv.getTrackbarPos("blue_high_V", "Tracking")

    red_font = cv.FONT_HERSHEY_SIMPLEX
    red_fontColor = (0, 0, 255)
    red_fontScale = .5
    red_lineType = 2

    red_low_H = cv.getTrackbarPos("red_low_V", "Tracking")
    red_low_S = cv.getTrackbarPos("red_low_V", "Tracking")
    red_low_V = cv.getTrackbarPos("red_low_V", "Tracking")
    red_high_H = cv.getTrackbarPos("red_high_H", "Tracking")
    red_high_S = cv.getTrackbarPos("red_high_S", "Tracking")
    red_high_V = cv.getTrackbarPos("red_high_V", "Tracking")

    # ret, frame = cap.read()
    frame = cap
    if frame is None:
        break

    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    blue_frame_threshold = cv.inRange(frame_HSV, (blue_low_H, blue_low_S, blue_low_V),
                                      (blue_high_H, blue_high_S, blue_high_V))
    red_frame_threshold = cv.inRange(frame_HSV, (red_low_H, red_low_S, red_low_V), (red_high_H, red_high_S, red_high_V))
    green_frame_threshold = cv.inRange(frame_HSV, (green_low_H, green_low_S, green_low_V),
                                       (green_high_H, green_high_S, green_high_V))
    frame_threshold = (blue_frame_threshold + red_frame_threshold + green_frame_threshold)
    cv.imshow(window_capture_name, frame)

    cv.imshow(window_detection_name, frame_threshold)
    cv.imshow("blue detection", blue_frame_threshold)
    cv.imshow("red detection", red_frame_threshold)
    cv.imshow("green detection", green_frame_threshold)

    img = frame.copy()

    ret, green_thresh = cv.threshold(green_frame_threshold, 127, 255, 0)
    green_contours, green_hierarchy = cv.findContours(green_thresh, 1, 2)

    ret, blue_thresh = cv.threshold(blue_frame_threshold, 127, 255, 0)
    blue_contours, blue_hierarchy = cv.findContours(blue_thresh, 1, 2)

    ret, red_thresh = cv.threshold(red_frame_threshold, 127, 255, 0)
    red_contours, red_hierarchy = cv.findContours(red_thresh, 1, 2)

    boxFound = False
    # Grøn klods
    for x in range(len(green_contours)):
        if green_contours[x].size > 300:
            green_cnt = green_contours[x]
            green_rect = cv.minAreaRect(green_cnt)
            cv.putText(img, str(green_rect[-1]), (10, 20), font, fontScale, (0, 255, 0),
                       lineType)  # print rotation of box

            greenBox = cv.boxPoints(green_rect)
            greenBox = np.int0(greenBox)

            cv.drawContours(img, [greenBox], 0, (0, 255, 0), 1)

            cv.putText(img, str(greenBox[0]), (greenBox[0][0], greenBox[0][1]), green_font, green_fontScale,
                       green_fontColor, green_lineType)
            cv.putText(img, str(greenBox[1]), (greenBox[1][0], greenBox[1][1]), green_font, green_fontScale,
                       green_fontColor, green_lineType)
            cv.putText(img, str(greenBox[2]), (greenBox[2][0], greenBox[2][1]), green_font, green_fontScale,
                       green_fontColor, green_lineType)
            cv.putText(img, str(greenBox[3]), (greenBox[3][0], greenBox[3][1]), green_font, green_fontScale,
                       green_fontColor, green_lineType)

            M = cv.moments(green_cnt)

            # calculate x,y coordinate of center
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv.circle(img, (cX, cY), 5, green_fontColor, -1)
            cv.putText(img, "center", (cX - 25, cY - 25), green_font, green_fontScale,
                       green_fontColor, green_lineType)

            # blå klods
    for j in range(len(blue_contours)):
        if blue_contours[j].size > 300:
            blue_cnt = blue_contours[j]

            blue_rect = cv.minAreaRect(blue_cnt)
            cv.putText(img, str(blue_rect[-1]), (10, 40), font, fontScale, (255, 0, 0),
                       lineType)

            blueBox = cv.boxPoints(blue_rect)
            blueBox = np.int0(blueBox)

            cv.drawContours(img, [blueBox], 0, (255, 0, 0), 1)

            cv.putText(img, str(blueBox[0]), (blueBox[0][0], blueBox[0][1]), blue_font, blue_fontScale, blue_fontColor,
                       blue_lineType)
            cv.putText(img, str(blueBox[1]), (blueBox[1][0], blueBox[1][1]), blue_font, blue_fontScale, blue_fontColor,
                       blue_lineType)
            cv.putText(img, str(blueBox[2]), (blueBox[2][0], blueBox[2][1]), blue_font, blue_fontScale, blue_fontColor,
                       blue_lineType)
            cv.putText(img, str(blueBox[3]), (blueBox[3][0], blueBox[3][1]), blue_font, blue_fontScale, blue_fontColor,
                       blue_lineType)

            M = cv.moments(blue_cnt)
            # calculate x,y coordinate of center
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv.circle(img, (cX, cY), 5, blue_fontColor, -1)
            cv.putText(img, "center", (cX - 25, cY - 25), blue_font, blue_fontScale, blue_fontColor,
                       blue_lineType)

            # Rød kasse
    for i in range(len(red_contours)):
        if red_contours[i].size > 300:
            red_cnt = red_contours[i]
            red_rect = cv.minAreaRect(red_cnt)
            cv.putText(img, str(red_rect[-1]), (10, 60), font, fontScale, (0, 0, 255),
                       lineType)  # print rotation of box

            redBox = cv.boxPoints(red_rect)
            redBox = np.int0(redBox)

            cv.drawContours(img, [redBox], 0, (0, 0, 255), 1)

            cv.putText(img, str(redBox[0]), (redBox[0][0], redBox[0][1]), red_font, red_fontScale, red_fontColor,
                       red_lineType)
            cv.putText(img, str(redBox[1]), (redBox[1][0], redBox[1][1]), red_font, red_fontScale, red_fontColor,
                       red_lineType)
            cv.putText(img, str(redBox[2]), (redBox[2][0], redBox[2][1]), red_font, red_fontScale, red_fontColor,
                       red_lineType)
            cv.putText(img, str(redBox[3]), (redBox[3][0], redBox[3][1]), red_font, red_fontScale, red_fontColor,
                       red_lineType)
            M = cv.moments(red_cnt)

            # calculate x,y coordinate of center
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv.circle(img, (cX, cY), 5, red_fontColor, -1)
            cv.putText(img, "center", (cX - 25, cY - 25), red_font, red_fontScale, red_fontColor,
                       red_lineType)
    cv.imshow("vis kasse", img)

    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break
