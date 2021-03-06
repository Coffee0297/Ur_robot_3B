from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np


def nothing(x):
    pass


# Vinduesnavn
cv.namedWindow('Tracking')

# Opretter en trackbar og attaches
# vedhæfter det til vindue
cv.createTrackbar("green_low_H", "Tracking", 0, 180, nothing)
cv.createTrackbar("green_low_S", "Tracking", 0, 255, nothing)
cv.createTrackbar("green_low_V", "Tracking", 0, 255, nothing)
cv.createTrackbar("green_high_H", "Tracking", 0, 180, nothing)
cv.createTrackbar("green_high_S", "Tracking", 0, 255, nothing)
cv.createTrackbar("green_high_V", "Tracking", 0, 255, nothing)

cv.createTrackbar("blue_low_H", "Tracking", 0, 180, nothing)
cv.createTrackbar("blue_low_S", "Tracking", 0, 255, nothing)
cv.createTrackbar("blue_low_V", "Tracking", 0, 255, nothing)
cv.createTrackbar("blue_high_H", "Tracking", 0, 180, nothing)
cv.createTrackbar("blue_high_S", "Tracking", 0, 255, nothing)
cv.createTrackbar("blue_high_V", "Tracking", 0, 255, nothing)

cv.createTrackbar("red_low_H", "Tracking", 0, 180, nothing)
cv.createTrackbar("red_low_S", "Tracking", 0, 255, nothing)
cv.createTrackbar("red_low_V", "Tracking", 0, 255, nothing)
cv.createTrackbar("red_high_H", "Tracking", 0, 180, nothing)
cv.createTrackbar("red_high_S", "Tracking", 0, 255, nothing)
cv.createTrackbar("red_high_V", "Tracking", 0, 255, nothing)


max_value = 255
max_value_H = 360//2

# Her defineres tekst størrelse til den skrevet rotation i hjørnet
font = cv.FONT_HERSHEY_SIMPLEX
fontScale = .5
lineType = 1

window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'

parser = argparse.ArgumentParser(description='Code for Thresholding Operations using inRange tutorial.')
parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)
args = parser.parse_args()
cap = cv.VideoCapture(args.camera)

while True:

    # Grønt filter trehshold
    # Her defineres tekst farve og størrelse for de grønne punkter
    green_font = cv.FONT_HERSHEY_SIMPLEX
    green_fontScale = .5
    green_fontColor = (0, 255, 0)
    green_lineType = 2
    # Her defineres farvefiltret for den grønne nuance
    green_low_H = cv.getTrackbarPos("green_low_H", "Tracking")
    green_low_S = cv.getTrackbarPos("green_low_S", "Tracking")
    green_low_V = cv.getTrackbarPos("green_low_V", "Tracking")
    green_high_H = cv.getTrackbarPos("green_high_H", "Tracking")
    green_high_S = cv.getTrackbarPos("green_high_S", "Tracking")
    green_high_V = cv.getTrackbarPos("green_high_V", "Tracking")

    # Blå filter trehshold
    # Her defineres tekst farve og størrelse for de blå punkter
    blue_font = cv.FONT_HERSHEY_SIMPLEX
    blue_fontColor = (255, 0, 0)
    blue_fontScale = .3
    blue_lineType = 2
    # Her defineres farvefiltret for den blå nuance
    blue_low_H = cv.getTrackbarPos("blue_low_V", "Tracking")
    blue_low_S = cv.getTrackbarPos("blue_low_V", "Tracking")
    blue_low_V = cv.getTrackbarPos("blue_low_V", "Tracking")
    blue_high_H = cv.getTrackbarPos("blue_high_H", "Tracking")
    blue_high_S = cv.getTrackbarPos("blue_high_S", "Tracking")
    blue_high_V = cv.getTrackbarPos("blue_high_V", "Tracking")

    # Rødt filter treshold
    # Her defineres tekst farve og størrelse for de røde punkter
    red_font = cv.FONT_HERSHEY_SIMPLEX
    red_fontColor = (0, 0, 255)
    red_fontScale = .3
    red_lineType = 2
    # Her defineres farvefiltret for den røde nuance
    red_low_H = cv.getTrackbarPos("red_low_V", "Tracking")
    red_low_S = cv.getTrackbarPos("red_low_V", "Tracking")
    red_low_V = cv.getTrackbarPos("red_low_V", "Tracking")
    red_high_H = cv.getTrackbarPos("red_high_H", "Tracking")
    red_high_S = cv.getTrackbarPos("red_high_S", "Tracking")
    red_high_V = cv.getTrackbarPos("red_high_V", "Tracking")


    ret, frame = cap.read()
    if frame is None:
        break

    # Her oprettes farvefiltre til grøn, blå og rød
    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    blue_frame_threshold = cv.inRange(frame_HSV, (blue_low_H,blue_low_S,blue_low_V),(blue_high_H,blue_high_S,blue_high_V))
    red_frame_threshold = cv.inRange(frame_HSV, (red_low_H,red_low_S,red_low_V),(red_high_H,red_high_S,red_high_V))
    green_frame_threshold = cv.inRange(frame_HSV, (green_low_H,green_low_S,green_low_V),(green_high_H,green_high_S,green_high_V))
    frame_threshold=(blue_frame_threshold+red_frame_threshold+green_frame_threshold)
    cv.imshow(window_capture_name, frame)

    cv.imshow(window_detection_name, frame_threshold)

    
    # minAreaRect

    img = frame.copy()
    
    #Her bliver det grønne filter lagt over alle lagene
    ret,green_thresh = cv.threshold(green_frame_threshold,127,255,0)
    #Her findes konjukturen i billedet med det grønne filter
    green_contours,green_hierarchy = cv.findContours(green_thresh, 1, 2)
    
    #Her bliver det blå filter lagt over alle lagene    
    ret,blue_thresh = cv.threshold(blue_frame_threshold,127,255,0)
    #Her findes konjukturen i billedet med det blå filter
    blue_contours,blue_hierarchy = cv.findContours(blue_thresh, 1, 2)
    
    #Her bliver det røde filter lagt over alle lagene
    ret,red_thresh = cv.threshold(red_frame_threshold,127,255,0)
    #Her findes konjukturen i billedet med det røde filter
    red_contours,red_hierarchy = cv.findContours(red_thresh, 1, 2)

    boxFound = False
   # Grøn klods
    for x in range(len(green_contours)):
      if green_contours[x].size > 100: #for loop der tæller pixels indenfor farvefiltret
        green_cnt = green_contours[x]
        green_rect = cv.minAreaRect(green_cnt)
        cv.putText(img, str(green_rect[-1]), (10,20), font, fontScale,(0,255,0),lineType) # print rotation of box

        greenBox = cv.boxPoints(green_rect)# Her findes klodsens hjørner
        greenBox = np.int0(greenBox) # Her laves klodsens hjærner om til en liste

        cv.drawContours(img,[greenBox],0,(0,255,0),1) # her tegnes konjukturen af firkanten

        # her skrives koordinatet på alle 4 punkter
        cv.putText(img, str(greenBox[0]), (greenBox[0][0],greenBox[0][1]), green_font, green_fontScale,green_fontColor,green_lineType)
        cv.putText(img, str(greenBox[1]), (greenBox[1][0],greenBox[1][1]), green_font, green_fontScale,green_fontColor,green_lineType)
        cv.putText(img, str(greenBox[2]), (greenBox[2][0],greenBox[2][1]), green_font, green_fontScale,green_fontColor,green_lineType)
        cv.putText(img, str(greenBox[3]), (greenBox[3][0],greenBox[3][1]), green_font, green_fontScale,green_fontColor,green_lineType)

        #blå klods
    for j in range(len(blue_contours)):
         if blue_contours[j].size > 100: #for loop der tæller pixels indenfor farvefiltret 
            blue_cnt = blue_contours[j]
            blue_rect = cv.minAreaRect(blue_cnt)
            cv.putText(img, str(blue_rect[-1]), (10,20), font, fontScale,(255,0,0),lineType) # print rotation of box
                                
            blueBox = cv.boxPoints(blue_rect)# Her findes klodsens hjørner
            blueBox = np.int0(blueBox) # Her laves klodsens hjærner om til en liste

            cv.drawContours(img,[blueBox],0,(255,0,0),1) # her tegnes konjukturen af firkanten

            # her skrives koordinatet på alle 4 punkter
            cv.putText(img, str(blueBox[0]), (blueBox[0][0],blueBox[0][1]),blue_font, blue_fontScale,blue_fontColor,blue_lineType) 
            cv.putText(img, str(blueBox[1]), (blueBox[1][0],blueBox[1][1]), blue_font, blue_fontScale,blue_fontColor,blue_lineType) 
            cv.putText(img, str(blueBox[2]), (blueBox[2][0],blueBox[2][1]), blue_font, blue_fontScale,blue_fontColor,blue_lineType) 
            cv.putText(img, str(blueBox[3]), (blueBox[3][0],blueBox[3][1]), blue_font, blue_fontScale,blue_fontColor,blue_lineType) 

    #Rød kasse
    for i in range(len(red_contours)):
         if red_contours[i].size > 100: #for loop der tæller pixels indenfor farvefiltret
            red_cnt = red_contours[i]
            red_rect = cv.minAreaRect(red_cnt)
            cv.putText(img, str(red_rect[-1]), (10,20), font, fontScale,(0,0,255),lineType) # print rotation of box
            
            redBox = cv.boxPoints(red_rect) # Her findes klodsens hjørner
            redBox = np.int0(redBox) # Her laves klodsens hjærner om til en liste

            cv.drawContours(img,[redBox],0,(0,0,255),1) # her tegnes konjukturen af firkanten

            # her skrives koordinatet på alle 4 punkter
            cv.putText(img, str(redBox[0]), (redBox[0][0],redBox[0][1]), red_font, red_fontScale,red_fontColor,red_lineType)
            cv.putText(img, str(redBox[1]), (redBox[1][0],redBox[1][1]), red_font, red_fontScale,red_fontColor,red_lineType)
            cv.putText(img, str(redBox[2]), (redBox[2][0],redBox[2][1]), red_font, red_fontScale,red_fontColor,red_lineType)
            cv.putText(img, str(redBox[3]), (redBox[3][0],redBox[3][1]), red_font, red_fontScale,red_fontColor,red_lineType)
            
        
    cv.imshow("Box fit", img)


    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break
