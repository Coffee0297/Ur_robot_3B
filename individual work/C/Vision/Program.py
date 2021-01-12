# CBL
from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np
import defs
import vision

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
img = cv.imread('image_0.png')
#frame_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

defs.Square.getContours(img, show=True)
imgContours, fContours = defs.Square.getContours(img, show= True, minArea=50000, filter=4)

# find the biggest objects 4 corners - unsorted
if len(fContours) != 0:
    biggestContour = fContours[0][2]   # takes 1. and 3. parameter in finalContours-->([len(approx), area, approx, bbox, i])
    imgWarp = defs.Square.warpImg(img, biggestContour, wWorkspace, hWorkspace)
    #worspaceImg = imgWarp.copy()
    #print(imgWarp.size/3)
    imgContours2, fContours2 = defs.Square.getContours(imgWarp, show=True, showCenterWS=True, findAngle=True, minArea=2000, filter=4, cThr=[60, 60], draw=False)

    # warped image
    if len(fContours) !=0:
        for obj in fContours2:
            cv.polylines(imgContours2,[obj[2]], True, (0,255,0),2)  # green full lines
            nPoints = defs.Square.reorder(obj[2])    # reorder points
            print('nPoints reordered: \n ', nPoints)

            # function call to find distance (hight and width of object)
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
            ContourImg1 = imgContours2.copy()

    cv.imshow("Workspace2", imgContours2)
    cv.imshow("Original", imgContours)
cv.waitKey(0)
cam.release()
cv.destroyAllWindows()





