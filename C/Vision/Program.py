# CBL
from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np
import defs

# define a video capture object
cam = cv.VideoCapture(0)
# cam.set(10,160)     # 10 for brightness - value 160
# cam.set(3,1920)     # 3 for hight - value 1920
# cam.set(4,1080)     # 4 for width - value 1080
pixToMil = 0.2645833333
scale = 3   # scale to make image bigger
wWorkspace = 200 *scale
hWorkspace = 200 *scale

defs.Capture.takePicture(cam)
img = cv.imread(r'C:\Users\Carin\Documents\UCL_2019\3.Sem\Python\UR\Vision\image_0.png')
defs.Square.getContours(img, show=True)

imgContours, fContours = defs.Square.getContours(img, show= True, minArea=50000, filter=4)
# find the biggest objects 4 corners - unsorted
if len(fContours) != 0:
    biggest = fContours[0][2]   # takes 1. and 3. parameter in finalContours-->([len(approx), area, approx, bbox, i])
    # print (biggest)
    imgWarp = defs.Square.warpImg(img, biggest, wWorkspace, hWorkspace)
    imgContours2, fContours2 = defs.Square.getContours(imgWarp, show=True, minArea=2000, filter=4, cThr=[60, 60], draw=False)

    if len(fContours) !=0:
        for obj in fContours2:
            cv.polylines(imgContours2,[obj[2]], True, (0,255,0),2)  # green full lines
            nPoints = defs.Square.reorder(obj[2])    # reorder points

            # calculate x,y coordinate of center
            M = cv.moments(fContours2)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv.circle(img, (cX, cY), 5, red_fontColor, -1)
            cv.putText(img, str([cX, cY]), (cX - 25, cY - 25), red_font, red_fontScale, red_fontColor, red_lineType)

            print('nPoints reordered: \n ', nPoints)
            nW = round(defs.Square.findDis(nPoints[0][0] // scale, nPoints[1][0] // scale), 1)    # find width of obj, (number of pixels divided by scale-value)
            nH = round(defs.Square.findDis(nPoints[0][0] // scale, nPoints[2][0] // scale), 1)    # find height of obj in millimeters, round to 1 decimal
            cv.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]),
                                 (255, 0, 255), 2, 10, 0, 0.08)
            cv.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),
                                 (255, 0, 255), 2, 10, 0, 0.08)
            x, y, w, h = obj[3]
            cv.putText(imgContours2, '{}mm'.format(nW), (x + 30, y - 10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1,
                             (255,0,255), 1)
            cv.putText(imgContours2, '{}mm'.format(nH), (x - 70, y + h // 2), cv.FONT_HERSHEY_COMPLEX_SMALL, 1,
                             (255, 0, 255), 1)
            print('\nWidth: ', nW, '\nHight: ', nH)
    cv.imshow("Workspace", imgContours2)
# cv.imshow("Last saved image", img)

cv.waitKey(0)
cam.release()
cv.destroyAllWindows()





